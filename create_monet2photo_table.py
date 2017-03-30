import os
import glob
import argparse
import numpy as np
from scipy import misc
import random
#from skimage import io, color


dir_name = 'monet-to-photo-512-small-idt-testset'

def show_one_direction():
  idx = 0
  for filename in glob.glob(os.path.join("images/" + dir_name + "/real_A/", "*.png")):
    nameonly = os.path.basename(filename)
    idx += 1
    
    ## Style transfer
    print("| %s | ![]({{site.baseurl}}/images/%s/real_A/%s) | ![]({{site.baseurl}}/images/%s/fake_B/%s) | " % 
          (nameonly, dir_name,nameonly, 
           dir_name,nameonly))

def show_both_directions():
  dir_name = 'facades'
  idx = 0  
  for filename in glob.glob(os.path.join("images/" + dir_name + "/real_A/", "*.jpg")):
    nameonly = os.path.basename(filename)
    idx += 1
    
    ## Style transfer
    print("| ![]({{site.baseurl}}/images/%s/real_A/%s) | ![]({{site.baseurl}}/images/%s/fake_B/%s) | ![]({{site.baseurl}}/images/%s/real_B/%s) | ![]({{site.baseurl}}/images/%s/fake_A/%s) |" % 
          (dir_name,nameonly, 
           dir_name,nameonly,
           dir_name,nameonly,
           dir_name,nameonly,
         ))
  

  
def show_cherrypick():
  # cherrypick list
  filenumbers= [719,1288,755,933,1262,1122,312,911,367,939,718,946,952,986,1016,556,1105,889,685,1259,989,743,
                 414,94,261,221,257,791,978,873,758,141,775,336,1031,1082,364,
                 32,887,348,1129,35,711,634,857,92,968,385,712,1017,548,981,1303,973,272,
                 157,113,26,777,194,1159,195,809,706,1146,736,269,745,284,748,938]

  dir_name = 'monet-to-photo-512-small-idt'
  filenumbers2= [933,
                 26,
                 18,
                 719,
                 173,
                 704,
                 1288,
                 755,
                 735,
                 735,
                 895,
                 1009,
                 855,
                 809,
                 1041,
                 711,
                 34,
                 398,
                 745,
                 312,
                 414 ,
                 911,
                 791,
                 239,
                 1232,
                 685]

  filenumbers.extend(f for f in filenumbers2 if f not in filenumbers)
  
  for filenumber in filenumbers:
    nameonly = '%05d.png' % filenumber
    print("| %s | ![]({{site.baseurl}}/images/%s/real_A/%s) | ![]({{site.baseurl}}/images/%s/fake_B/%s) | " % 
          (nameonly, dir_name,nameonly, 
           dir_name,nameonly))

def show_idt_comparison():
  dir_name = 'monet-to-photo-360-idt-comparison'
  idx=0
  #for filename in glob.glob(os.path.join("images/" + dir_name + "/no_idt/", "*.jpg")):
  #  nameonly = os.path.splitext(os.path.basename(filename))[0]
  #  idx += 1

  #filenumbers = [1259, 169,34,644,524,809,966,1159,592,985]
  filenumbers = [755,911,367,719,385,272,809,414,775,1122,939,556,1288,548,1159,1016]
  for filenumber in filenumbers:
    nameonly = '%05d' % filenumber    

    square_im = misc.imread('./images/%s/no_idt/%s.png' % (dir_name,nameonly))
    big_im = misc.imread('./images/%s/small_idt/real_A/%s.png' % (dir_name,nameonly))
    fake_im = misc.imread('./images/%s/small_idt/fake_B/%s.png' % (dir_name,nameonly))
    big_im = misc.imresize(big_im, (int(360*big_im.shape[0]/big_im.shape[1]),360))
    square_im = misc.imresize(square_im, (big_im.shape[0],big_im.shape[1]))
    fake_im = misc.imresize(fake_im, (big_im.shape[0],big_im.shape[1]))
    misc.imsave('./images/%s/no_idt/%s_aspectratio.png' % (dir_name,nameonly), square_im)
    misc.imsave('./images/%s/small_idt/real_A/%s_360.png' % (dir_name,nameonly), big_im)
    misc.imsave('./images/%s/small_idt/fake_B/%s_360.png' % (dir_name,nameonly), fake_im)

    print("| %s.png | ![]({{site.baseurl}}/images/%s/small_idt/real_A/%s_360.png) | ![]({{site.baseurl}}/images/%s/no_idt/%s_aspectratio.png) | ![]({{site.baseurl}}/images/%s/small_idt/fake_B/%s_360.png) |" % 
          (nameonly, dir_name,nameonly, dir_name,nameonly, 
           dir_name,nameonly))

def show_gatys_comparison():
  dir_name = 'gatys-comparison/resized'
  indices = [110, 112, 116, 117, 119, 11, 121, 131, 134, 136, 143, 146, 150, 151, 152,
             160, 164, 168, 170, 171, 178, 17, 183, 185, 189, 18, 192, 194, 195, 197,
             203, 204, 205,33, 39, 3, 44, 45, 55, 52, 56, 65, 6, 73, 75, 7, 85, 87, 89,
             96, 98]
  random.shuffle(indices)
  artists = ['vangogh', 'ukiyoe','cezanne','monet']  
  for index in indices[:30]:
    for artist in artists:
      print("| %s | ![]({{site.baseurl}}/images/%s/%d_content.jpg) | ![]({{site.baseurl}}/images/%s/resized_128/%d_style_%s_0.jpg) | ![]({{site.baseurl}}/images/%s/%d_result_%s_0.jpg) |![]({{site.baseurl}}/images/%s/resized_128/%d_style_%s_1.jpg) | ![]({{site.baseurl}}/images/%s/%d_result_%s_1.jpg) | ![]({{site.baseurl}}/images/%s/%d_result_%s_total.jpg) | ![]({{site.baseurl}}/images/%s/%s/%d.jpg) |" % 
            (artist, dir_name, index, 
             dir_name, index, artist,
             dir_name, index, artist,
             dir_name, index, artist,
             dir_name, index, artist,
             dir_name, index, artist,
             dir_name, artist, index, # our result
           ))

def show_facades():
  dir_name = 'facades_everything/test'
  idx = 0  
  for filename in glob.glob(os.path.join("images/" + dir_name + "/real_A/", "*.jpg")):
    nameonly = os.path.basename(filename)
    idx += 1
    
    ## Style transfer
    print("| ![]({{site.baseurl}}/images/%s/real_A/%s) | ![]({{site.baseurl}}/images/%s/fake_B/%s) | ![]({{site.baseurl}}/images/%s/real_B/%s) | ![]({{site.baseurl}}/images/%s/fake_A/%s) |" % 
          (dir_name,nameonly, 
           dir_name,nameonly,
           dir_name,nameonly,
           dir_name,nameonly,
         ))
  


#show_idt_comparison()
#show_both_directions()
#show_facades()
show_cherrypick()
