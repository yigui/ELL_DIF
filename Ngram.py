#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 12:25:41 2020

@author: yigui
"""


with open('/Users/yigui/Downloads/w3.txt', 'r') as file:
    n3gram=  file.readlines()

n3gram=[p.replace("\n", "").split('\t') for p in n3gram]

N3gramDIct={}



for e in n3gram:
    N3gramDIct[' '.join(e[1:3])]=e[0]
    
    
with open('/Users/yigui/Downloads/w2.txt', 'r',encoding = "ISO-8859-1") as file:
    n2gram=  file.readlines()

n2gram=[p.replace("\n", "").split('\t') for p in n2gram]

N2gramDIct={}



for e in n2gram:
    N2gramDIct[' '.join(e[1:2])]=e[0]
    
with open('/Users/yigui/Downloads/w4.txt', 'r',encoding = "ISO-8859-1") as file:
    n4gram=  file.readlines()

n4gram=[p.replace("\n", "").split('\t') for p in n4gram]

N4gramDIct={}

for e in n4gram:
    N4gramDIct[' '.join(e[1:4])]=e[0]
    

with open('/Users/yigui/Downloads/w5.txt', 'r',encoding = "ISO-8859-1") as file:
    n5gram=  file.readlines()

n5gram=[p.replace("\n", "").split('\t') for p in n5gram]

N5gramDIct={}

for e in n5gram:
    N5gramDIct[' '.join(e[1:4])]=e[0]
    
k='I makes it'

