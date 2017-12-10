#!/usr/bin/env python
# -*- coding: utf-8 -*-
adict = {
    "sf":{
        "max":51,
        "maxRateList": [2.5,3.0,3.5,4.0,4.5],
        "min":48.80,
        "minRateList": [0.5,0.8,1.0]
    },
    "gf":{
        "max":74.87,
        "maxRateList": [2.5,3.0,3.5,4.0,4.5],
        "min":68.0,
        "minRateList": [0.5,0.8,1.0]
    },
}

for key in adict:
    print key+":"
    print "max:",
    for rate in adict[key]["maxRateList"]:
        print rate,adict[key]["min"]*(1+rate/100),
    print ""
    print "min:",
    for rate in adict[key]["minRateList"]:
        print rate,adict[key]["min"]*(1+rate/100),
    print ""
