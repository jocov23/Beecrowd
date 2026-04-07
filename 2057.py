Hsaida, dura, fuso = map(int, input().split())

HBruto = Hsaida + dura + fuso

if HBruto > 24:
    Hliquido = HBruto - 24
    print(Hliquido)
elif HBruto < 0:
    Hliquido = HBruto + 24
    print(Hliquido)
elif HBruto == 24:
    print("0")
else:
    print(HBruto)