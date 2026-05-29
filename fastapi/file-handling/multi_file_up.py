from fastapi import FastAPI, UploadFile, File
from typing import Annotated, List

app = FastAPI()

@app.post('/upload/')
async def up_file(files: Annotated[List[UploadFile],File(description="Upload Files")]):
    result = []
    for file in files:
        with open(file.filename,'wb') as f:
            content = await file.read()
            f.write(content)
            result.append({'filemame':file.filename,'size':len(content)})
    
    return {"Message":"Files uploaded successfully","Storage":result}