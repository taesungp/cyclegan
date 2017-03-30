import os
import glob
import argparse
import numpy as np
from scipy import misc
#from skimage import io, color
import random


def create_style_transfer():
  idx = 0
  dir_name = 'style-transfer-train'
  for filename in glob.glob(os.path.join("images/" + dir_name + "/original/", "*.jpg")):
    nameonly = os.path.basename(filename)
    idx += 1

    if random.random() < 0.0:
      os.system('rm images/%s/original/%s' % (dir_name,nameonly))
      os.system('rm images/%s/%s/%s' % (dir_name, 'ukiyoe', nameonly))
      os.system('rm images/%s/%s/%s' % (dir_name, 'vangogh', nameonly))
      os.system('rm images/%s/%s/%s' % (dir_name, 'cezanne', nameonly))
      os.system('rm images/%s/%s/%s' % (dir_name, 'monet', nameonly))
    else:

      ## Style transfer
      print(("| %d | ![]({{site.baseurl}}/images/%s/original/%s) | ![]({{site.baseurl}}/images/%s/%s/%s) | ![]({{site.baseurl}}/images/%s/%s/%s) " + 
             "| ![]({{site.baseurl}}/images/%s/%s/%s) | ![]({{site.baseurl}}/images/%s/%s/%s) |") % 
            (idx, dir_name,nameonly, 
             dir_name, 'monet', nameonly,
             dir_name, 'vangogh', nameonly,
             dir_name, 'cezanne', nameonly, 
             dir_name, 'ukiyoe', nameonly,
           ))

def create_renoir2selfie():
  idx = 0
  dir_name = 'movie-to-renoir'
  search_dir = os.path.join("images/" + dir_name + "/original/", "*.jpg")
  print(search_dir)
  for filename in glob.glob(search_dir):
    nameonly = os.path.basename(filename)
    idx += 1

    ## Style transfer
    print(("| %d | ![]({{site.baseurl}}/images/%s/original/%s) | ![]({{site.baseurl}}/images/%s/%s/%s) | )" % 
           (idx, dir_name,nameonly, 
            dir_name, 'renoir', nameonly,
          )))

#create_renoir2selfie()
create_style_transfer()
  
