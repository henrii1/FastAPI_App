from fastapi import Header, HTTPException


async def get_token_header(x_token: str = Header("fake-user-secret-token")):
    if x_token != "fake-user-secret-token":
        raise HTTPException(status_code= 400, detail="Token Header Invalid")

async def get_query_token(token: str = 'jessica'):
    if token != "jessica":
        raise HTTPException(status_code=400, detail="No Jessica token provided")
    
    
    