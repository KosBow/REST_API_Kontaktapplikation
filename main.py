from fastapi import FastAPI, HTTPException

from models import *
from datetime import datetime

app = FastAPI()

contacts_db = []
next_id = 1

@app.post("/contacts", response_model=ContactResponse)
def create_contact(contact: ContactCreate):
    global next_id

    new_contact = {
        "id": next_id,
        "fornamn": contact.fornamn,
        "efternamn": contact.efternamn,
        "kontaktvagar": contact.kontaktvagar,
        "adresser": contact.adresser,
        "ovrig_information": contact.ovrig_information,
        "skapad_datum": datetime.now(),
        "uppdaterad_datum": datetime.now(),
    }

    contacts_db.append(new_contact)

    next_id += 1

    return new_contact

@app.get("/contacts", response_model=List[ContactResponse])
def read_contact():
    return contacts_db

@app.get("/contacts/{contact_id}", response_model=ContactResponse)
def read_contact(contact_id: int):
    for contact in contacts_db:
        if contact["id"] == contact_id:
            return contact

    raise HTTPException(status_code=404, detail="Kontakt hittades inte")

@app.put("/contacts/{contact_id}", response_model=ContactResponse)
def update_contact(contact_id: int, contact: ContactUpdate):

    for existing_contact in contacts_db:

        if existing_contact["id"] == contact_id:

            if contact.fornamn is not None:
                existing_contact["fornamn"] = contact.fornamn

            if contact.efternamn is not None:
                existing_contact["efternamn"] = contact.efternamn

            if contact.kontaktvagar is not None:
                existing_contact["kontaktvagar"] = contact.kontaktvagar

            if contact.adresser is not None:
                existing_contact["adresser"] = contact.adresser

            if contact.ovrig_information is not None:
                existing_contact["ovrig_information"] = contact.ovrig_information

            existing_contact["uppdaterad_datum"] = datetime.now()

            return existing_contact

    raise HTTPException(
        status_code=404,
        detail="Kontakt hittades inte"
    )

@app.delete("/contacts/{contact_id}")
def delete_contact(contact_id: int):
    for existing_contact in contacts_db:
        if existing_contact["id"] == contact_id:
            contacts_db.remove(existing_contact)
            return {
                "message": "Kontakt borttagen",
                "contact": existing_contact
            }

    raise HTTPException(status_code=404, detail="Kontakt hittades inte")