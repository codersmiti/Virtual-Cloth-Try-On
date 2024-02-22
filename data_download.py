import os
import tarfile
import shutil

tarfile.open("/content/Virtual-Cloth-Try-On/data/viton_resize.tar.gz").extractall(path='/content/Virtual-Cloth-Try-On/data/')

shutil.move('data/viton_resize/test/', 'data/test/')
shutil.move('data/viton_resize/train/', 'data/train/')
