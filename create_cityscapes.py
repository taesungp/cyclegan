import os
import glob
import argparse
import numpy as np
from scipy import misc

dir_name = 'cityscapes-comparison'
# backward  bigan  cogan  content_gan  forward  l1_gan  no_cycle  no_gan  pix2pix

def comparison():

  methods = ['bigan', 'cogan', 'content_gan', 'l1_gan', 'cycle', 'pix2pix']
  subdirs = ['photo2label', 'label2photo']

  for filename in glob.glob('images/%s/%s/target/images/*.jpg' % (dir_name,subdirs[1])):
    nameonly = os.path.basename(filename)
    
    direction = 0
    subdir = subdirs[direction]
    theotherdir = subdirs[1-direction]
    
    print(("| ![]({{site.baseurl}}/images/%s/%s/%s/images/%s) " +
           "| ![]({{site.baseurl}}/images/%s/%s/%s/images/%s) " +
           "| ![]({{site.baseurl}}/images/%s/%s/%s/images/%s) " +
           "| ![]({{site.baseurl}}/images/%s/%s/%s/images/%s) " +
           "| ![]({{site.baseurl}}/images/%s/%s/%s/images/%s) " +
           "| ![]({{site.baseurl}}/images/%s/%s/%s/images/%s) " +
           "| ![]({{site.baseurl}}/images/%s/%s/%s/images/%s) " +
           "| ![]({{site.baseurl}}/images/%s/%s/%s/images/%s) |") %
          (dir_name,theotherdir,'target',nameonly,
           dir_name,subdir,methods[0],nameonly,
           dir_name,subdir,methods[1],nameonly,
           dir_name,subdir,methods[2],nameonly,
           dir_name,subdir,methods[3],nameonly,
           dir_name,subdir,methods[4],nameonly,
           dir_name,subdir,methods[5],nameonly,
           dir_name,subdir,'target',nameonly,
         ))
    
    direction = 1
    subdir = subdirs[direction]
    theotherdir = subdirs[1-direction]
    
    print(("| ![]({{site.baseurl}}/images/%s/%s/%s/images/%s) " +
           "| ![]({{site.baseurl}}/images/%s/%s/%s/images/%s) " +
           "| ![]({{site.baseurl}}/images/%s/%s/%s/images/%s) " +
           "| ![]({{site.baseurl}}/images/%s/%s/%s/images/%s) " +
           "| ![]({{site.baseurl}}/images/%s/%s/%s/images/%s) " +
           "| ![]({{site.baseurl}}/images/%s/%s/%s/images/%s) " +
           "| ![]({{site.baseurl}}/images/%s/%s/%s/images/%s) " +
           "| ![]({{site.baseurl}}/images/%s/%s/%s/images/%s) |") %
          (dir_name,theotherdir,'target',nameonly,
           dir_name,subdir,methods[0],nameonly,
           dir_name,subdir,methods[1],nameonly,
           dir_name,subdir,methods[2],nameonly,
           dir_name,subdir,methods[3],nameonly,
           dir_name,subdir,methods[4],nameonly,
           dir_name,subdir,methods[5],nameonly,
           dir_name,subdir,'target',nameonly,
         ))

def ablation():
  methods = ['no_gan', 'no_cycle', 'forward', 'backward', 'CycleGAN']
  subdirs = ['photo2label', 'label2photo']

  for filename in glob.glob('images/%s/%s/target/images/*.jpg' % (dir_name,subdirs[1])):
    nameonly = os.path.basename(filename)
    
    direction = 0
    subdir = subdirs[direction]
    theotherdir = subdirs[1-direction]
    
    print(("| ![]({{site.baseurl}}/images/%s/%s/%s/images/%s) " +
           "| ![]({{site.baseurl}}/images/%s/%s/%s/images/%s) " +
           "| ![]({{site.baseurl}}/images/%s/%s/%s/images/%s) " +
           "| ![]({{site.baseurl}}/images/%s/%s/%s/images/%s) " +
           "| ![]({{site.baseurl}}/images/%s/%s/%s/images/%s) " +
           "| ![]({{site.baseurl}}/images/%s/%s/%s/images/%s) " +
           "| ![]({{site.baseurl}}/images/%s/%s/%s/images/%s) |") %
          (dir_name,theotherdir,'target',nameonly,
           dir_name,subdir,methods[0],nameonly,
           dir_name,subdir,methods[1],nameonly,
           dir_name,subdir,methods[2],nameonly,
           dir_name,subdir,methods[3],nameonly,
           dir_name,subdir,methods[4],nameonly,
           dir_name,subdir,'target',nameonly,
         ))
    
    direction = 1
    subdir = subdirs[direction]
    theotherdir = subdirs[1-direction]
    
    print(("| ![]({{site.baseurl}}/images/%s/%s/%s/images/%s) " +
           "| ![]({{site.baseurl}}/images/%s/%s/%s/images/%s) " +
           "| ![]({{site.baseurl}}/images/%s/%s/%s/images/%s) " +
           "| ![]({{site.baseurl}}/images/%s/%s/%s/images/%s) " +
           "| ![]({{site.baseurl}}/images/%s/%s/%s/images/%s) " +
           "| ![]({{site.baseurl}}/images/%s/%s/%s/images/%s) " +
           "| ![]({{site.baseurl}}/images/%s/%s/%s/images/%s) |") %
          (dir_name,theotherdir,'target',nameonly,
           dir_name,subdir,methods[0],nameonly,
           dir_name,subdir,methods[1],nameonly,
           dir_name,subdir,methods[2],nameonly,
           dir_name,subdir,methods[3],nameonly,
           dir_name,subdir,methods[4],nameonly,
           dir_name,subdir,'target',nameonly,
         ))


        
comparison()
#ablation()
