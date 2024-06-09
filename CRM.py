# 

import firebase_admin
from firebase_admin import credentials, firestore
import time
from google.api_core.exceptions import ServiceUnavailable

cred = credentials.Certificate("/Users/isabelkamphaus/Documents/CRM/crm-project-eb2d8-firebase-adminsdk-ppqq9-89298d2e78.json")
firebase_admin.initialize_app(cred)

# Access Firestore database
db = firestore.client()

def get_info():
    kind_of_client = input("Is the client buying or selling? buy/sell ").lower()
    id = input("What is the name of the Client? Please add their first and last name: ")
    name = id.split(" ")
    fname = name[0]
    lname = name[1]
    address = input("What is the address? ")
    phone = input("What is the phone number? ")
    interested = input("Is the client interested? yes/no ").lower()

    interested = True if interested == "yes" else False

    if kind_of_client == "buy":
        kind_of_client = "Buying"
        selling_price = int(input("What price range are they looking at? "))
        client_data = {
            "id": id,
            "fname": fname,
            "lname": lname,
            "address": address,
            "phone": phone,
            "interested": interested,
            "kind_of_client": kind_of_client,
            "selling_price": selling_price,
            "notes": ""
        }
    elif kind_of_client == "sell":
        kind_of_client = "Selling"
        selling_price = int(input("What price are they wanting to sell for? "))
        buying = input("Is the client using you to buy another house? yes/no ").lower()

        buying_price = int(input("What price range are they looking at? ")) if buying == "yes" else None

        client_data = {
            "id": id,
            "fname": fname,
            "lname": lname,
            "address": address,
            "phone": phone,
            "interested": interested,
            "kind_of_client": kind_of_client,
            "selling_price": selling_price,
            "buying": buying == "yes",
            "buying_price": buying_price,
            "notes": ""
        }
    else:
        print("Invalid input for kind of client.")
        return None
    
    return client_data

def main():
    client = get_info()
    if client:
        doc_ref = db.collection("CRM").document(client["id"])
        retry_count = 5
        for attempt in range(retry_count):
            try:
                doc_ref.set(client)
                print(f"Document for {client['id']} added successfully.")
                break
            except ServiceUnavailable as e:
                print(f"Attempt {attempt + 1} failed with error: {e}")
                if attempt < retry_count - 1:
                    time.sleep(2 ** attempt)  # Exponential backoff
                else:
                    print("Failed to add document after several attempts.")
                    raise

if __name__ == "__main__":
    main()
