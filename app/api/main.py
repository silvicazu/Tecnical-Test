from fastapi import FastAPI
import requests

app = FastAPI()
url = "https://swapi.dev/api/"

@app.get("/")
async def root():
    return {"message": "LLA DevOps test"}

@app.get("/people")
async def get_people(search: str | None = None, page: int | None = None):
    base_url = url+"people/?"
    if search:
        base_url= f"{base_url}search={search}&"
    if page:
        base_url= f"{base_url}page={page}"
    response = requests.request("GET", base_url)
    return(response.json())

@app.get("/people/{person_id}")
async def get_person(person_id):
    response = requests.request("GET", url+"people/"+person_id)
    return(response.json())