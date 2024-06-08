import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("/Users/isabelkamphaus/Documents/CRM/crm-project-eb2d8-firebase-adminsdk-ppqq9-89298d2e78.json")
firebase_admin.initialize_app(cred)
