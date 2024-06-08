import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("/Users/isabelkamphaus/Documents/CRM/crm-project-eb2d8-firebase-adminsdk-ppqq9-89298d2e78.json")
firebase_admin.initialize_app(cred)

# Access Firestore database
db = firestore.client()

# Define data for two people
people_data = [
    {
        "id": "alice_smith",
        "fname": "Alice",
        "lname": "Smith",
        "address": "456 Elm St",
        "phone": "555-5678",
        "interested": True,
        "notes": "Interested in our services."
    },
    {
        "id": "bob_johnson",
        "fname": "Bob",
        "lname": "Johnson",
        "address": "789 Oak Ave",
        "phone": "555-6789",
        "interested": False,
        "notes": "Not currently interested."
    }
]

# Add each person's data to the CRM collection
for person in people_data:
    doc_ref = db.collection("CRM").document(person["id"])
    doc_ref.set(person)

print("Two people added to the CRM collection.")