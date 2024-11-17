from fastapi import FastAPI

from src.contacts.routers import router as contacts_router
from src.auth.routers import router as auth_router


app = FastAPI()


app.include_router(contacts_router, prefix="/contacts", tags=["contacts"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])