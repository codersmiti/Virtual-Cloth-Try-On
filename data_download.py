import os
import tarfile
import shutil

tarfile.open("/content/Virtual-Cloth-Try-On/data/viton_resize.tar.gz").extractall(path='/content/Virtual-Cloth-Try-On/data/')

shutil.move('/content/Virtual-Cloth-Try-On/data/viton_resize/test/', '/content/Virtual-Cloth-Try-On/data/test/')
shutil.move('/content/Virtual-Cloth-Try-On/data/viton_resize/train/','/content/Virtual-Cloth-Try-On/data/train/')
