import os
import glob
import argparse
import numpy as np
from scipy import misc
import random
#from skimage import io, color


dir_name = 'monet-to-photo-512-small-idt'

def show_one_direction():
  idx = 0
  for filename in glob.glob(os.path.join("images/" + dir_name + "/real_A/", "*.png")):
    nameonly = os.path.basename(filename)
    idx += 1
    
    ## Style transfer
    print("| %d | ![]({{site.baseurl}}/images/%s/real_A/%s) | ![]({{site.baseurl}}/images/%s/fake_B/%s) | " % 
          (idx, dir_name,nameonly, 
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
  
  for i,filenumber in enumerate(filenumbers):
    nameonly = '%05d.png' % filenumber
    print("| %d | ![]({{site.baseurl}}/images/%s/real_A/%s) | ![]({{site.baseurl}}/images/%s/fake_B/%s) | " % 
          (i, dir_name,nameonly, 
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
  
def show_flower():
  dir_name = 'iphone-to-dslr-flower'
  idx = 0  
  for filename in glob.glob(os.path.join("images/" + dir_name + "/test/real_A/", "*.jpg")):
    nameonly = os.path.basename(filename)
    idx += 1
    
    ## Style transfer
    print("| %d | ![]({{site.baseurl}}/images/%s/test/real_A/%s) | ![]({{site.baseurl}}/images/%s/test/fake_B/%s) |" % 
          (idx, dir_name,nameonly, 
           dir_name,nameonly,
         ))
    

def show_flower_cherrypicked():
  dir_name = 'iphone-to-dslr-flower'
  
  cherrypick = ['c1.staticflickr.com-1-763-32581865124_8e80b0e0f2.jpg',
  'c1.staticflickr.com-3-2887-33395034491_d9f2338994.jpg',
  'c1.staticflickr.com-3-2910-33041518530_d28ea76c05.jpg',
  'c1.staticflickr.com-3-2822-33504455386_52a3077ac8.jpg',
  'c1.staticflickr.com-3-2806-33098149442_354c2f26ed.jpg',
  'c1.staticflickr.com-9-8073-29656831652_ba1c9e40a9.jpg',
  'c1.staticflickr.com-4-3907-33269048062_d22145a93d.jpg',
  'c1.staticflickr.com-9-8432-29733300036_74077df80a.jpg',
  'c1.staticflickr.com-1-435-32277849120_ae4c5dc9be.jpg',
  'c1.staticflickr.com-1-753-33276302616_cc1682b670.jpg',
  'c1.staticflickr.com-3-2812-33098149612_0b603e20c8.jpg',
  'c1.staticflickr.com-4-3760-32581867154_d66ff72bdd.jpg',
  'c1.staticflickr.com-3-2946-33041850440_346b2a568e.jpg',
  'c1.staticflickr.com-6-5577-30372820443_a48d38ee90.jpg',
  'c1.staticflickr.com-9-8061-29141610564_80301ff470.jpg',
  'c1.staticflickr.com-1-588-33298041911_b43a06fb00.jpg',
  'c1.staticflickr.com-1-627-33424927725_d559895993.jpg',
  'c1.staticflickr.com-4-3896-33384295846_382ccbfd37.jpg',
  'c1.staticflickr.com-1-350-32620121711_e5b48f89a5.jpg',
  'c1.staticflickr.com-4-3923-33296488541_a6366e1af6.jpg',
  'c1.staticflickr.com-4-3928-33149660990_268b66a8a0.jpg',
  'c1.staticflickr.com-9-8873-29852080865_d4f1761f21.jpg',
  'c1.staticflickr.com-1-647-33098150682_6a1c4b8e9d.jpg',
  'c1.staticflickr.com-1-506-31771014510_567b1581fe.jpg',
  'c1.staticflickr.com-3-2877-33416588201_ab951ca071.jpg',
  'c1.staticflickr.com-9-8111-29143645603_a9d118f0a3.jpg',
  'c1.staticflickr.com-4-3782-33041455650_2b1aedf661.jpg',
  'c1.staticflickr.com-4-3757-33296421411_7385d9063b.jpg',
  'c1.staticflickr.com-1-596-32659816223_e5a9dbdca0.jpg',
  'c1.staticflickr.com-1-345-32680547201_16b60bd597.jpg',
  'c1.staticflickr.com-3-2652-32091691024_4034098c2b.jpg',
  'c1.staticflickr.com-9-8475-29733268536_a7bbae527c.jpg',
  'c1.staticflickr.com-3-2669-32085879344_4535ae7aa0.jpg',
  'c1.staticflickr.com-1-335-32713052756_5a4c6a03e4.jpg',
  'c1.staticflickr.com-6-5330-31003476500_5012545c29.jpg',
  'c1.staticflickr.com-1-767-33203467565_28d203b4c3.jpg',
  'c1.staticflickr.com-6-5485-30656115043_b4145b7ae5.jpg',
  'c1.staticflickr.com-1-772-33179156506_dfe5527bd2.jpg',
  'c1.staticflickr.com-3-2290-32680551861_b231003bb4.jpg',
  'c1.staticflickr.com-1-630-33384375666_cc66287eba.jpg',
  'c1.staticflickr.com-4-3711-33275026566_160ee9b340.jpg',
  'c1.staticflickr.com-4-3806-33296066071_cd05c989a2.jpg',]

  for i, filename in enumerate(cherrypick):    
    ## Style transfer
    print("| %d | ![]({{site.baseurl}}/images/%s/test/real_A/%s) | ![]({{site.baseurl}}/images/%s/test/fake_B/%s) | " % 
          (i,dir_name,filename, 
           dir_name,filename,
         ))      
 
    
def show_vividcolor():
  dir_name = 'aadb-vividcolor'
  cherrypick = ['farm1_299_19537238303_8d204921a1_b.jpg',
                'farm1_310_19977833649_f2a2457720_b.jpg',
                'farm1_353_20053224236_bde4dfffa1_b.jpg',
                'farm1_275_19535031503_7438172860_b.jpg',
                'farm1_336_19587650813_7c1cc8a6f1_b.jpg',
                'farm1_355_20014009989_85d953a610_b.jpg',
                'farm1_372_20318295352_72abc2fe51_b.jpg',
                'farm1_394_19711782103_d7f9abcb81_b.jpg',
                'farm1_388_19997930278_72270995e1_b.jpg',
                'farm1_318_20078179365_75033b4640_b.jpg',
                'farm1_327_19912866098_cb6b810541_b.jpg',
                'farm1_263_19945255328_f73611bc41_b.jpg',
                'farm1_286_19947256768_41e190f330_b.jpg',
                'farm1_371_20176622541_b3a26b45c0_b.jpg',
                'farm1_452_19903923450_7250a06dc1_b.jpg',
                'farm4_3781_19998809411_2c2ec830c0_b.jpg',
                'farm1_389_19569916923_30d868e921_b.jpg',
                'farm1_388_20093874910_fe1eba4201_b.jpg',
                'farm1_500_20003473999_4ff7c6dda0_b.jpg',
                'farm1_350_20143152590_4324ae0081_b.jpg',
                'farm1_255_20119251251_cfdc54b210_b.jpg',
                'farm1_302_19661089764_3e4de758a0_b.jpg',
                'farm1_277_20142519801_cd79dab9a0_b.jpg',
                'farm1_286_19519973493_d9830efca1_b.jpg',
                'farm1_327_20184643242_91b8ee2910_b.jpg',
                'farm1_381_19585724843_02da34cc31_b.jpg',
                'farm1_290_20072499396_92b7701a00_b.jpg',
                'farm1_427_20116530331_df5410ab01_b.jpg',
                'farm1_259_19569093863_d783d6f2b1_b.jpg',
                'farm1_451_20102962032_7b05438e00_b.jpg',
                'farm1_307_20183873096_2bb45458a1_b.jpg',
                'farm1_312_20147998816_472a4fb670_b.jpg',
                'farm1_305_20071330075_bfe06cff00_b.jpg',
                'farm1_306_19540524024_b0f4b7af10_b.jpg',
                'farm1_300_20010456750_b03d4b5a60_b.jpg',
                'farm1_360_19921057100_4dd6ce7fe0_b.jpg',
                'farm1_361_19372722474_77b8a21770_b.jpg',]

  for i, filename in enumerate(cherrypick):    
    ## Style transfer
    print("| %d | ![]({{site.baseurl}}/images/%s/test/real_A/%s) | ![]({{site.baseurl}}/images/%s/test/fake_B/%s) | " % 
          (i,dir_name,filename, 
          dir_name,filename,
          ))      
 
  


#show_idt_comparison()
#show_both_directions()
#show_facades()
#show_flower()

#show_vividcolor()
#show_cherrypick()
show_one_direction()
