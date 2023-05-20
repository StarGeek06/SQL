import sqlite3

"""
Ici etant donné qu'on veut les informations de chaque utilisateur il est important
de commencer par creer une base de données prenant en parametre le nom,prenom
et les mots de passe.
"""

# Nous devons d'abord commencer par creer les bases de donnees.

Bd = sqlite3.connect('GesMDP.bd')

TBd = Bd.cursor()

Bd.execute('''CREATE TABLE Users(id INT,Nom VARCHAR(20), Password TEXT NOT NULL)''')

Bd.execute('''CREATE TABLE Account(id INT, service TEXT NOT NULL, Mdp TEXT NOT NULL)''')

# Enregistrer les utilisateurs

def AddUsers(nom, mot_de_passe):
    Bd.execute("INSERT INTO TABLE Users(nom,mot_de_passe) VALUES (?,?)",(nom,mot_de_passe))
    Bd.commit()

# Enregistrer les comptes

def AddAccount(id, service, Password):
    Bd.execute("INSERT INTO TABLE Account(id, service, Password) VALUES (?,?,?)",(id, service,Password))
    Bd.commit()

# Modifier les informations de leur compte

def UpdateAccount(nservice, nPassword, id):
    Bd.execute("UPDATE Account SET service = ?, Password = ? WHERE id = ?",(nservice,nPassword,id))
    Bd.commit()

# Supprimer les informations d'un compte

def Delete(C_Id):
    Bd.execute("DELETE FROM Account WHERE id = ?",(C_Id))
    Bd.commit()


AddUsers('ADISSO','Oneldan78')
