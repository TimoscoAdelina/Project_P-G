
from fastapi.testclient import TestClient
from main import app
client = TestClient(app)


# verifica daca endpointul "/" functioneaza corect 
def test_root():
    response = client.get("/") #like e echivalent cu deschiderea manuala in browser
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {"message": "FastApi -> proiect"}  # daca imi arata 200 atunci it works



def test_get_all_identifiers():  #dă-mi toate identificatoarele din sistem
    response = client.get("/identifiers/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
   #isinstance -> x e de tip lista?


#Pot să iau un identifier specific după nume și API-ul îmi returnează corect acel obiect.
def test_get_identifier_by_name():
    response = client.get("/identifiers/99999999")
    assert response.status_code == 200
    assert response.json()["identifier_name"] == "99999999"


def test_create_country():
    response = client.post("/countries/", json={
        "name": "Spain",
        "iso_code": "ES",
        "short_code": "724"
    })

    assert response.status_code == 200
    assert response.json()["name"] == "Spain"
    assert response.json()["iso_code"] == "ES"
    assert response.json()["short_code"] == "724"




def test_get_country_by_name():
    response = client.get("/countries/Spain")
    assert response.status_code == 200
    assert response.json()["name"] == "Spain"




def test_get_missing_country():
    response = client.get("/countries/UnknownCountry")
    assert response.status_code == 404
    assert response.json() == {"detail": "Country not found"}