kontaktlar = {"Ali": "+998901234567", "Vali": "+998919876543"}

while True:
    ism = input("Ism kiriting (chiqish uchun 'stop'): ")
    
    if ism == 'stop':
        break
        
    if ism in kontaktlar:
        print("Raqami:", kontaktlar[ism])
    else:
        print("Bu ism topilmadi!")
        yangi_raqam = input(ism + " uchun yangi raqam kiriting: ")
        kontaktlar[ism] = yangi_raqam
        print("Kontakt qo'shildi!")