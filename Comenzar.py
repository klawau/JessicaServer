# -*- coding: cp1254 -*-
import time
import os

def main():
    data = os.system("Forum.py")
    if data == 1:
        print("[ERROR] Reiniciando en 20 segundos...")
        time.sleep(20)
        os.system("cls")
        main()
    elif data in [5,1280]:
        print("[INFO] Server Parado!")
        raw_input("")
    elif data in [11,2816]:
        print("[ERROR] Reiniciando...")
        time.sleep(1)
        os.system("cls")
        main()
    else:
        print("[ERROR] Servidor caido, reiniciando...")
        time.sleep(20)
        os.system("cls")
        main()

if __name__=="__main__":
    main()
