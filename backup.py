while True:
    menyu = {"osh": "10000", "shurva": "5000", "lagmon": "8000", "somsa": "6000", "manti": "7000"}
    zakaz = input("Nima zakaz qilasiz? (Chiqish uchun 'stop' deb yozing): ")
    
    if zakaz == 'stop':
        print("Dastur tugatildi. Rahmat!")
        break

    if zakaz in menyu:
        print(f"Siz {zakaz} zakaz qildingiz. Narxi: {menyu[zakaz]} so'm")
    else:
        print("Bunday taom yo'q. Iltimos, menyudagi taomlardan birini tanlang.")
