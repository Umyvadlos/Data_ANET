s = int(input("Napiš začáteční číslo: "))
e = int(input("Napiš konečné číslo: "))

num = s

while num <= e:
    if num > 1:
        delit = 2

        while delit != num:
            if num % delit != 0:
                delit = delit +1
            else:
                break
        else:
            print(num)
    num = num + 1

#while num <= e:
#smycka pro range

#whilewhile delit != num:
           # if num % delit != 0:
            #    delit = delit +1
            #else:
             #   break
        #else:
         #   print(num)
         #smycka pro prvocislo
         #dddddddddd