from fastapi import Depends

@router.get("/contacts/", response_model=List[schemas.Contact])
async def read_contacts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return db.query(models.Contact).filter(models.Contact.owner_id == current_user.id).offset(skip).limit(limit).all()

from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

@app.route("/contacts", methods=["POST"])
@limiter.limit("5 per minute")
async def create_contact():

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def add_contact(name: str, phone: str) -> None:

