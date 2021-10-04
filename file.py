import time
from PIL import Image

with open('/tmp/tempfile.txt', 'w') as fp:
    fp.write('This is from /tmp/tempfile.txt')

with open('sample.log', 'w') as fp:
    fp.write('This is from sample.log')

# time.sleep(10)

im = Image.new(mode="RGB", size=(200, 200))
im.save('test.jpg')
print('Finished')
