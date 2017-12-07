#!/usr/bin/env python
# -*- coding: utf-8 -*-
adict = {
    "zg":{
        "max":6.5,
        "min":6.0
    },
    "sh":{
        "max":24.5,
        "min":22.46
    },
    "gf":{
        "max":74.87,
        "min":68.0
    },
}

for key in adict:
    print key+":"
    maxV = adict[key]["max"]
    minV = adict[key]["min"]
    print "max:",maxV*(1-0.5/100),maxV*(1-0.8/100),maxV*(1-1.0/100)
    print "min:",minV*(1+0.5/100),minV*(1+0.8/100),minV*(1+1.0/100)
    print "mid:",minV*(1+4.0/100)
