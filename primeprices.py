#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import sympy
for i in range(1,1000000):
    fi=math.floor(i*1.08)
    ci=math.ceil(i*1.08)
    if(sympy.isprime(i) and sympy.isprime(fi)):
        print(i,fi,end=" ")
        if(i*1.08-fi<0.5):
            print("切り捨て・四捨五入")
        else:
            print("切り捨て")
    if(sympy.isprime(i) and sympy.isprime(ci)):
        print(i,ci,end=" ")
        if(ci-i*1.08<=0.5):
            print("切り上げ・四捨五入")
        else:
            print("切り上げ")
