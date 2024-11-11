# -*- coding: utf-8 -*-
"""
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
Copyright 2021 | Nghiên Cứu Thuốc | RD Pharma Plus

Email: nghiencuuthuoc@gmail.com | info@nghiencuuthuoc.com

Web: http://www.nghiencuuthuoc.com

See more: https://twitter.com/nghiencuuthuoc | https://facebook.com/nghiencuuthuoc

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
DEVELOPMENT NOTES

+ 20210828:

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
"""


#
bioactive_compounds = ["carotenoids", "flavonoids", "carnitine", "choline", "coenzyme", "dithiolthiones", "phytosterols", "phytoestrogens", "glucosinolates", "polyphenols", "taurine"]

bioactive_compounds =['Fisetin']



import pharmapp as pa

for bioactive_compound in bioactive_compounds:
    print(bioactive_compound)
    pa.get_inactive_ingredient(name_drug=bioactive_compound)
    print(f'{bioactive_compound} done!')

# passs error


#