# 消費税素数の検索
[京大の素数ものさし](https://rcpt.kyoto-bauc.or.jp/goods/kyodai_goods/indicate.php?mode=detail&id=375&category=4)が税抜き売価が577円で、税込みだと売価が素数にならないことに端を発して、税抜きでも税込みでも素数になる価格を探すことにしました。とりあえず税抜き100万円までのリストです。

```py
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
```
