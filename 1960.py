# -*- coding: utf-8 -*-

n = int(input())
#---------------CENTENAS
centena = int(n/100)
if centena == 9:
    x="CM"
elif centena == 8:
    x = "DCCC"
elif centena == 7:
    x = "DCC"
elif centena == 6:
    x="DC"
elif centena == 5:
    x ="D"
elif centena ==4:
    x= "CD"   
elif centena == 3:
    x = "CCC"
elif centena == 2:
    x ="CC"
elif centena == 1:
    x ="C"
else:
    x = ""
#-------------------------DEZENAS
dezena = int((n%100)/10)
if dezena == 9:
    y="XC"
elif dezena == 8:
    y = "LXXX"
elif dezena == 7:
    y = "LXX"
elif dezena == 6:
    y="LX"
elif dezena == 5:
    y ="L"
elif dezena ==4:
    y= "XL"   
elif dezena == 3:
    y = "XXX"
elif dezena == 2:
    y ="XX"
elif dezena == 1:
    y ="X"
else:
    y = ""
#--------UNIDADES
unidade = int((n%100)%10)
if unidade == 9:
    z="IX"
elif unidade == 8:
    z = "VIII"
elif unidade == 7:
    z = "VII"
elif unidade == 6:
    z="VI"
elif unidade == 5:
    z ="V"
elif unidade == 4:
    z= "IV"   
elif unidade == 3:
    z = "III"
elif unidade == 2:
    z ="II"
elif unidade == 1:
    z ="I"
else:
    z = ""

romano = x + y + z
print(romano)






