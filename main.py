from fastapi import Depends, FastAPI
from dependencies import get_token_header,get_query_token

from routers import users, items

app = FastAPI(dependencies=[Depends(get_query_token)])

app.include_router(users)
app.include_router(items)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications"}