
def login_control(process):
    continue_situation = "E"
    while continue_situation == "E":
        password_correction = False
        email_correction = False
        email = input("Lütfen e-postanızı giriniz:")
        email_txt = open("email.txt", "r")
        email_list = [0] * 4
        counter = -1
        email_opened = email_txt.readline()
        correct_password_index = 0
        while email_opened != "":
            counter += 1
            email_list[counter] = email_opened[:-1:]
            email_opened = email_txt.readline()
        for x in email_list:
            if email == x:
                correct_password_index = email_list.index(x)
                email_correction = True
                break
        sifre = input("Lütfen şifrenizi giriniz:")
        sifre_txt = open("password.txt", "r")
        sifre_listesi = [0] * 4
        sifre_sayaci = 0
        sifre_okunmus = sifre_txt.readline()
        while sifre_okunmus != "":
            sifre_listesi[sifre_sayaci] = sifre_okunmus[:-1:]
            sifre_sayaci += 1
            sifre_okunmus = sifre_txt.readline()
        for y in sifre_listesi:
            if sifre == y:
                if correct_password_index == sifre_listesi.index(y):
                    password_correction = True
        if password_correction == True and email_correction == True:
            print("Sisteme başarılya girdiniz")
            continue_situation = "h"
        else:
            print("Sisteme giremediniz, şifre veya epostanız yanlış!")
            continue_situation = input("Tekrar denemek ister misiniz?(E/H)")
