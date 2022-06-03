import torch
import time
import argparse


parser = argparse.ArgumentParser(description='PyTorch MNIST Example')

parser.add_argument('--batch_size', type=int, default=64, metavar='N',
                    help='input batch size for training (default: 64)')
args = parser.parse_args()


time.sleep(30)
print(args.batch_size)