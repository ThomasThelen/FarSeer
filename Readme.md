# Far Seer

FastAPI server for detecting official and hacked Warcraft III maps

## Running

The API can be run locally through Docker or by calling uvicorn directly,

`uvicorn src.main:app --host 0.0.0.0 --port 8080 --reload`

or

`docker compose up`

## Using

There are two endpoints:

 - `/map/{map_md5}`: GET request for a single map
 - `/maps/`: POST request with an ordered body of map md5 checksums