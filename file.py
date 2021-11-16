import time
from PIL import Image

with open('/tmp/tempfile.txt', 'w') as fp:
    print('Writing to tempfile')
    fp.write('This is from /tmp/tempfile.txt')

fp = open('sample', 'a')
for _ in range(1000000):
    print('Writing to sample.log')
    fp.write('This is from sample.log')

    time.sleep(0.5)

fp.close()

im = Image.new(mode="RGB", size=(200, 200))
im.save('test.jpg')
print('Finished')
