from fastapi import FastAPI, Request, Form
from pydantic import BaseModel

from src.hash_store import HashStore

app = FastAPI()

hash_store = HashStore('src/data/maps.csv')


# Define the /map/{hash} endpoint
@app.get("/map/{hash}")
def get_map(hash: str):
    """
    Endpoint to retrieve information for a given hash.

    Args:
        hash (str): The hash string provided by the user.

    Returns:
        dict: A response containing the hash and a message.
    """
    return hash_store.map_status(hash)


class Item(BaseModel):
    name: str = None


@app.post("/maps/")
async def maps(name: str = Form(...)):
    hashes = name.split(',')
    results = []
    for hash in hashes:
        results.append(hash_store.map_status(hash))
    return results

# To run this app, save the file and use the command:
# uvicorn filename:app --reload
