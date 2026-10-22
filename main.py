count = 0
while True:
    parol = input("parol kiriting")
    if parol == "1234":
        print("parol to`g`ri")
        break
    elif count == 3:
        print("siz 3 marta xato kiritdingiz")
        break
    else:
        print("parol xato qayta urinib ko`ring")