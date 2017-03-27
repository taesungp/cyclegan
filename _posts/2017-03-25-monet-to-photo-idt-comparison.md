---
layout: post
title: Effect of adding the identity mapping loss on Monet to Photo
---
{{ page.title }}
================

| id | Input | Without Identity Loss | With Identity Loss |
|---:|:---------:|:----------:|:----------:|
| 1 | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/small_idt/real_A/00755_360.png) | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/no_idt/00755_aspectratio.png) | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/small_idt/fake_B/00755_360.png) |
| 2 | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/small_idt/real_A/00911_360.png) | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/no_idt/00911_aspectratio.png) | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/small_idt/fake_B/00911_360.png) |
| 3 | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/small_idt/real_A/00367_360.png) | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/no_idt/00367_aspectratio.png) | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/small_idt/fake_B/00367_360.png) |
| 3 | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/small_idt/real_A/00719_360.png) | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/no_idt/00719_aspectratio.png) | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/small_idt/fake_B/00719_360.png) |
| 4 | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/small_idt/real_A/00385_360.png) | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/no_idt/00385_aspectratio.png) | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/small_idt/fake_B/00385_360.png) |
| 5 | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/small_idt/real_A/00272_360.png) | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/no_idt/00272_aspectratio.png) | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/small_idt/fake_B/00272_360.png) |
| 6 | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/small_idt/real_A/00809_360.png) | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/no_idt/00809_aspectratio.png) | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/small_idt/fake_B/00809_360.png) |
| 7 | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/small_idt/real_A/00414_360.png) | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/no_idt/00414_aspectratio.png) | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/small_idt/fake_B/00414_360.png) |
| 8 | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/small_idt/real_A/00775_360.png) | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/no_idt/00775_aspectratio.png) | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/small_idt/fake_B/00775_360.png) |
| 9 | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/small_idt/real_A/01122_360.png) | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/no_idt/01122_aspectratio.png) | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/small_idt/fake_B/01122_360.png) |
| 10 | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/small_idt/real_A/00939_360.png) | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/no_idt/00939_aspectratio.png) | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/small_idt/fake_B/00939_360.png) |
| 11 | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/small_idt/real_A/00556_360.png) | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/no_idt/00556_aspectratio.png) | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/small_idt/fake_B/00556_360.png) |
| 12 | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/small_idt/real_A/01288_360.png) | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/no_idt/01288_aspectratio.png) | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/small_idt/fake_B/01288_360.png) |
| 13 | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/small_idt/real_A/00548_360.png) | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/no_idt/00548_aspectratio.png) | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/small_idt/fake_B/00548_360.png) |
| 14 | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/small_idt/real_A/01159_360.png) | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/no_idt/01159_aspectratio.png) | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/small_idt/fake_B/01159_360.png) |
| 15 | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/small_idt/real_A/01016_360.png) | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/no_idt/01016_aspectratio.png) | ![]({{site.baseurl}}/images/monet-to-photo-360-idt-comparison/small_idt/fake_B/01016_360.png) |
