from json2 import *



id =  "root"
print("Les identifiant sont: ", id)
password = "root"
print("les mdp sont: ", password)

new_account = json.dumps(x["name"])
print(new_account)


if new_account == True:

    new_account = input('voulez vous faire un nouveau compte? ')

    if new_account != oui:
        id2 = input("Veuillez entrer votre identifiant: ")

        if id2 != id:
            print("L'identifient rentré n'es pas le bon!")

        elif id2 == id:    
            inputpassword2 = input("Veuiller rentrer votre Mots De Passe: ")
        
            if inputpassword2 == password:
                print("Bonjour " + id)
        
            elif inputpassword2 != password:
                print("Le mots de passe n'est pas le bon!")

    else:
        new_id = input("Veuillez rentrez un nom d'utilisateur ")
        if new_id == id:
            print("Cette identifient est déja utilisé!")
            
        
        elif new_id != id:
            new_password = input("Veuillez rentrez un Mots De Passe ")
            check = input("Etes vous sur de vote chois? ")
            if check == 'oui':
                print("Veuillez patienter!")
            elif check != 'oui':
                check2 = input("que voulez vous modifier? ")
                if check2 == 'le mot de passe':
                    print("Votre mots de passe va être modifier! Veuillez patienter!")
                    new_new_password = input("Rentrer votre nouveau mot de passe ")
                    check3 = input("Voulez vous changez autre chose? ")
                    if check3 == "non":
                        print("Bonjour " + new_id)
                    if check == "oui":
                        print("Votre identifient va être modifier! Veuillez patienter!")
                elif check2 == "L'identifient":
                    print("Votre identifient va être modifier! Veuillez patienter!")

elif new_account == False:
    print(json.dumps(x["new_account"]))