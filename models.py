from pydantic import BaseModel, field_validator
from typing import List, Optional
from datetime import datetime
import re


class ContactMethod(BaseModel):
    typ: str
    varde: str

    @field_validator("varde")
    @classmethod
    def validate_email(cls, value, info):

        if info.data.get("typ") == "email":

            email_pattern = r"^[^@]+@[^@]+\.[^@]+$"

            if not re.match(email_pattern, value):
                raise ValueError("Ogiltig e-postadress")

        return value


class Address(BaseModel):
    typ: str
    gata: str
    stad: str
    postnummer: str


class ContactCreate(BaseModel):
    fornamn: str
    efternamn: str
    kontaktvagar: List[ContactMethod] = []
    adresser: List[Address] = []
    ovrig_information: Optional[str] = None


class ContactUpdate(BaseModel):
    fornamn: Optional[str] = None
    efternamn: Optional[str] = None
    kontaktvagar: Optional[List[ContactMethod]] = None
    adresser: Optional[List[Address]] = None
    ovrig_information: Optional[str] = None


class ContactResponse(BaseModel):
    id: int
    fornamn: str
    efternamn: str
    kontaktvagar: List[ContactMethod]
    adresser: List[Address]
    ovrig_information: Optional[str]
    skapad_datum: datetime
    uppdaterad_datum: datetime