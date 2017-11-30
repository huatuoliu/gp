#!/usr/bin/env python
# -*- coding: utf-8 -*-
adict = {
    "ht":{
        "max":20.3,
        "min":19.0
    },
    "sh":{
        "max":24.4,
        "min":22.50
    },
    "gf":{
        "max":75,
        "min":69.0
    },
}

for key in adict:
    print key+":"
    maxV = adict[key]["max"]
    minV = adict[key]["min"]
    print "max:",maxV*(1-0.2/100),maxV*(1-0.5/100),maxV*(1-1.0/100)
    print "min:",minV*(1+0.2/100),minV*(1+0.5/100),minV*(1+1.0/100)
