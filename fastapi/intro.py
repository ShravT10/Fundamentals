from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'message':'ok boss'}


@app.post('/greet')
async def name(name):
    return {"Message":f"Hello {name} what's up !"}

