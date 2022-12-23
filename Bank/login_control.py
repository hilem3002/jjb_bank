

def login_control(process):
    continue_situation = "E"
    while continue_situation == "E":
        password_correction = False
        email_correction = False
        email = input("Lütfen e-postanızı giriniz:")
        email_txt = open("email.txt", "r")
        email_list = [0] * 4
        email_counter = -1
        email_opened = email_txt.readline()
        correct_password_index = 0
        while email_opened != "":
            email_counter += 1
            email_list[email_counter] = email_opened[:-1:]
            email_opened = email_txt.readline()
        for x in email_list:
            if email == x:
                correct_password_index = email_list.index(x)
                email_correction = True
                break
        password = input("Lütfen şifrenizi giriniz:")
        password_txt = open("password.txt", "r")
        password_list = [0] * 4
        password_counter = 0
        password_opened = password_txt.readline()
        while password_opened != "":
            password_list[password_counter] = password_opened[:-1:]
            password_counter += 1
            password_opened = password_txt.readline()
        for y in password_list:
            if password == y:
                if correct_password_index == password_list.index(y):
                    password_correction = True
        if password_correction == True and email_correction == True:
            print("Jorje Tarkan Melih Bankasına Hoşgeldiniz Değerli Üyemiz!")
            print("JTM'li olmak bir ayrıcalıktır!")
            continue_situation = "h"
        else:
            print("şifre veya Epostanız Yanlış!")
            continue_situation = input("Tekrar Denemek İster Misiniz?(E/H)")

