import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import gdown






def get_x(row,col,nmb):
    return sheet.cell(row, col+nmb+1).value

def get_y(row,col,nmb):
    return sheet.cell(row, col+nmb+2).value

def trouver_nom(sheet, nom):
    try :
        cell = sheet.find(nom)
        return cell.row,cell.col
    except :
        print("Le nom n'est pas dans la base de donnee")
        return None,None

def get_BDD():
    # Connect to Google Sheets
    scope = ['https://www.googleapis.com/auth/spreadsheets',
            "https://www.googleapis.com/auth/drive"]

    credentials = ServiceAccountCredentials.from_json_keyfile_name("Appli_BDD/projet.json", scope)
    client = gspread.authorize(credentials)
    sheet = client.open("BDD_nom_id_projet").worksheet("Sheet2")
    return sheet

def trouver_nmb(nmb):
    try :
        cell = sheet.find(str(nmb))
        return cell.row,cell.col
    except :
        #print("Le nombre n'est pas dans la base de donnee")
        return None,None


def get_user_pwd(sheet, row, col):
    return sheet.cell(row, col+1).value

def check_utilisateur(name, pwd):
    # We get our Data Base
    sheet = get_BDD()
    row, col =trouver_nom(sheet, name)
    #print(row, col)
    #if we got a result
    if ( row !=None and col!=None ):
        # checking for the password
        if ( pwd == get_user_pwd(sheet,row, col) ):
            #print("mot de passe trouvé")
            return True
        return False 

check_utilisateur("gaellou", "azer")