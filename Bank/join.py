def join(process):
    # the list of email adresses already exist
    email_list = []
    try:
        email_txt = open("email.txt", "r")
        current_email = email_txt.readline()
        while current_email == "":
            email_list.append(current_email[:len(current_email)-1])
            current_email = email_txt.readline()
        email_txt.close()
    except FileNotFoundError:
    email_list = []

    # key word that are gotta be in an email adress
    print("you could use these extension: (@gmail.com, @outlook.com, @hotmail.com, @yahoo.com)")
    print()
    print("       e-mail examples      ")
    print("----------------------------")
    print("   tarkanishere@gmail.com   ")
    print("    hilem3002@hotmail.com   ")
    print("  tarkanishere@outlook.com  ")
    print("     hilem3002@yahoo.com    ")
    print()

    valid_e_mail_keys = ["@gmail.com", "@outlook.com", "@hotmail.com", "@yahoo.com"]
    email = input("please enter a e-mail adress")

    # if email does not have the email keys ask for email again
    is_it_acceptable_email = False
    while is_it_acceptable_email == False:
        for e_mail_keys in valid_e_mail_keys:
            if e_mail_keys in email:
                is_it_acceptable_email = True
                break
            else:
                is_it_acceptable_email = False
        if is_it_acceptable_email == False:
            email = input("this e-mail adress is not valid please select another e-mail adress")

    # if email adress has already used by another user ask for email adress again
    while email in email_list:
        email = input("this e-mail adress has already used by another user please select another e-mail adress")

    # requirements that are gotta be in a password
    print("   your password has to contain these requirements:   ")
    print("------------------------------------------------------")
    print("-> lower and upper cases")
    print("-> at least 6 characters")
    print("-> at least 1 digit")
    print()
    password = input("please enter a password")

    # if password does not have the requirements ask for password again
    is_it_acceptable_password = False
    MIN_PASSWORD_LEN = 6
    while len(password) < MIN_PASSWORD_LEN:
        password = input("password has to contain at least 6 characters please enter another password")
    while password.isalpha() == True:
        password = input("password could not consist of only letters please enter another password")
    while password.isdigit() == True:
        password = input("password could not consist of only digits please enter another password")
    while password.upper() == password:
        password = input("password could not consist of only upper cases please enter another password")
    while password.lower() == password:
        password = input("password could not consist of only lowe cases please enter another password")

    # we wrote the email adress to the e-mail.txt
    email_txt = open("email.txt", "a")
    email_txt.write(f"{email}\n")
    email_txt.close()
    
    # we append the password to the password.txt
    password_txt = open("password.txt", "a")
    password_txt.write(password)
    password_txt.close()

    print("WELCOME!")
    print("you joined the jjb bank succesfuly")

