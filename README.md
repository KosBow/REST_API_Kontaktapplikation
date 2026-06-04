# REST API Kontaktapplikation

## API-beskrivning

Detta projekt är ett REST API för hantering av kontakter, utvecklat med FastAPI och Pydantic. API:et gör det möjligt att skapa, hämta, uppdatera, ta bort och söka efter kontakter.

Varje kontakt kan innehålla förnamn, efternamn, flera kontaktvägar, flera adresser, övrig information samt datum för när kontakten skapades och senast uppdaterades.

Projektet använder separata Pydantic-modeller för att skapa, uppdatera och visa data, vilket ger tydlig validering och en flexibel struktur som är enkel att bygga vidare på. Data lagras i minnet under programmets körning.

Som bonusfunktion har validering av e-postadresser implementerats.

## Exempel på API-anrop

### Skapa kontakt
POST /contacts

### Hämta alla kontakter
GET /contacts

### Uppdatera kontakt
PUT /contacts/{contact_id}

### Ta bort kontakt
DELETE /contacts/{contact_id}
