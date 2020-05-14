from jsoimport json

print("Le module JSON est prêts!")

x = {
    "name": "root",
    "password": "root",
    "new_account": False,
    "google account": True,
    "discord account": None,
    "youtube account": True,
    
}

print(json.dumps(x, indent=4))
 #ici c'est du JSON
