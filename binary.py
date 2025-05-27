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

