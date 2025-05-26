def desitkovadodvojkove(n):
    if n == 0:
        return "0"
    binarni = ""
    while n > 0:
        binarni = str(n % 2) + binarni
        n = n // 2
    return binarni


cislo = int(input("Zadej cislo: "))
print(f"Binární tvar čísla {cislo} je {desitkovadodvojkove(cislo)}")



def dvojkovadodesitkove(binarni):
    desitkove = 0
    for bit in binarni:
        desitkove = desitkove * 2 + int(bit)
    return desitkove


binarni_cislo = input("Zadej číslo v binární soustavě: ")
print(f"Desítkový tvar čísla {binarni_cislo} je {dvojkovadodesitkove(binarni_cislo)}")