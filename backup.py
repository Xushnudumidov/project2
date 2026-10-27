while True:
    b = {"qalam": "200", "daftar": "500", "ruchka": "100"}
    ism = input("element zakaz qiling(toxtash uchun 'stop' yozing) ")
    if ism == 'stop':
        break
    if ism in b:
        print(f"Sizning zakazingiz: {ism} narxi: {b[ism]}")
    else:
        print("Bunday element mavjud emas")