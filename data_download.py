import os
import tarfile
import shutil

tarfile.open("data/viton_resize.tar.gz").extractall(path='data/')

shutil.move('data/viton_resize/test/', 'data/test/')
shutil.move('data/viton_resize/train/', 'data/train/')

os.rmdir('data/viton_resize/')
os.remove('data/viton_resize.tar.gz')
