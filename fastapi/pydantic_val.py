from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

array = []

class Detail(BaseModel):
    name: str
    age: int
    place: str

@app.post('/info')
async def info(detail: Detail):
    return {f'hi {detail.name}, of age {detail.age} from {detail.place}'}

@app.post('/insert')
async def insert_into_array(item: str):
    array.append(item)
    return {'message':f"item {item} added at index {len(array)-1}"}

@app.get('/get_items')
async def get_from_array():
    return {'message':f'array : {array}'}

@app.put('/put_item/{item}')
async def put_into_array(item):
    if item in array:
        return {"message":f"Item {item} already in array"}
    else:
        array.append(item)
        return {"message":f"item {item} added into array"}

@app.delete('/delete_item')
async def delete_from_array(item):
    if item in array:
        array.remove(item)
        return {"message":f"item {item} is removed from array"}
    else:
        
        return {"message":f"item {item} not in array , {array}"}