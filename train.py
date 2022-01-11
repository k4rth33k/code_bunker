import io
import time

import numpy as np
import torch
import torch.nn as nn
import torchvision.transforms as t
from PIL import Image
from torch.utils.data import Dataset, DataLoader
from torchvision.models import resnet50
import glob


def get_train_transform():
    return t.Compose([
        t.RandomHorizontalFlip(p=0.5),
        t.RandomRotation(15),
        t.RandomCrop(204),
        t.ToTensor(),
        t.Normalize((0, 0, 0), (1, 1, 1))
    ])


def accuracy(preds, trues):
    preds = [1 if preds[i] >= 0.5 else 0 for i in range(len(preds))]
    acc = [1 if preds[i] == trues[i] else 0 for i in range(len(preds))]
    acc = np.sum(acc) / len(preds)

    return acc * 100


class ImageDataset(Dataset):
    def __init__(self, transforms=None):
        super().__init__()
        self.transforms = transforms
        self.imgs = glob.glob('./data/**')

    def __getitem__(self, idx):
        
        image_name = self.imgs[idx]
        
        with open(image_name, 'rb') as file:
            img = Image.open(io.BytesIO(file.read()))
        img = img.resize((224, 224)).convert('RGB')

        # Preparing class label
        _, __, label_name, image = image_name.split('/')
        label = 1 if label_name == 'NORMAL' else 0
        label = torch.tensor(label, dtype=torch.float32)

        # Apply Transforms on image
        img = self.transforms(img)
        return img, label

    def __len__(self):
        return len(self.imgs)


def main():
    train_dataset = ImageDataset(transforms=get_train_transform())

    train_data_loader = DataLoader(
        dataset=train_dataset,
        num_workers=4,
        batch_size=16,
        shuffle=True
    )

    device = torch.device('cuda')

    model = resnet50(pretrained=True)

    model.fc = nn.Sequential(
        nn.Linear(2048, 1, bias=True),
        nn.Sigmoid()
    )

    optimizer = torch.optim.Adam(model.parameters(), lr=0.0001)
    lr_scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=5, gamma=0.5)
    criterion = nn.BCELoss()
    epochs = 1
    model.to(device)

    print('Training has begun...')
    for epoch in range(epochs):

        epoch_loss = []
        epoch_acc = []
        start_time = time.time()

        for images, labels in train_data_loader:
            images = images.to(device)
            labels = labels.to(device)
            labels = labels.reshape((labels.shape[0], 1))  # [N, 1] - to match with preds shape

            # Reseting Gradients
            optimizer.zero_grad()

            # Forward
            preds = model(images)

            # Calculating Loss
            _loss = criterion(preds, labels)
            loss = _loss.item()
            epoch_loss.append(loss)

            # Calculating Accuracy
            acc = accuracy(preds, labels)
            epoch_acc.append(acc)

            # Backward
            _loss.backward()
            optimizer.step()

        end_time = time.time()
        total_time = end_time - start_time

        loss = np.mean(epoch_loss)
        acc = np.mean(epoch_acc)

        if epoch % 3 == 0:
            torch.save(model.state_dict(), f'Epoch_{epoch}.pth')

        print(f"Epoch: {epoch + 1} | Loss: {loss} | Acc: {acc} | Time: {total_time} ")


if __name__ == '__main__':
    main()
