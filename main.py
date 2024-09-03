from fastapi import FastAPI, HTTPException
from models import Details
from connections import collections
from schema import serielaize_data

app = FastAPI()

@app.post('/add_data')
async def save_data(payload: Details):
    if isinstance(payload, list):
        for data in payload:
            await save_data(data)
    else:
        try:
            resp = collections.insert_one(dict(payload))
            return {"status": 200, "message": "data saved successfully", "id": str(resp.inserted_id)}
        except Exception as e:
            raise HTTPException("unable to save data in db {e}")

@app.get('/get_data')
async def get_data():
    try:
        resp = collections.find()
        return serielaize_data(resp)
    except Exception as e:
        raise HTTPException("unable to fetch the data {e}")

@app.put('/edit_data/{name}')
async def edit_data(name: str, payload: Details):
    try:
        result = collections.update_one(filter={"name":name}, update={"$set": payload.__dict__})
        if result.matched_count == 0:
            return {"status": 404, "message": "Data not found"}
        return {"status":200, "message": "data updated successfully"}
    except Exception as e:
        raise HTTPException("unable to update the data {e}")

@app.delete('/delete/{name}')
async def delete_data(name: str):
    try:
        result = collections.delete_one(filter={"name": name})
        if result.deleted_count == 0:
            return {"message": "no data got deleted"}
        return {"status": 200, "message": "data got deleted"}
    except Exception as e:
        raise HTTPException("unable to delete the data {e}")







# data = dict(payload)
# resp = collections.find({"name":name})
# for each in resp:
#     each["name"] = data["name"]
#     each["age"] = data["age"]
#     each["phone_no"] = data["phone_no"]
#     each["marital_status"] = data["marital_status"]
#     each["shopping_zone"] = data["shopping_zone"]
#     each["address"] = data["address"]

