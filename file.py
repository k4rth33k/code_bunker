import time
from PIL import Image

with open('/tmp/tempfile.txt', 'w') as fp:
    print('Writing to tempfile')
    fp.write('This is from /tmp/tempfile.txt')

for _ in range(1000000):
	with open('sample', 'a') as fp:
	    print('Writing to sample.log')
	    fp.write('This is from sample.log')

	time.sleep(0.5)

im = Image.new(mode="RGB", size=(200, 200))
im.save('test.jpg')
print('Finished')
