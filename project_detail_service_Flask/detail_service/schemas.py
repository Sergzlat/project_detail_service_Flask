from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DetailBase(BaseModel):
    first_name: str
    last_name: str
    birth_date: datetime
    
class Nextdetail(BaseModel):
    id: int
    first_name: str
    last_name: str
    birth_date: Optional[datetime]

    class Config:
        orm_mode = True

class DetailCreate(DetailBase):
    pass

class DetailUpdate(DetailBase):
    pass

class DetailInDBBase(DetailBase):
    id: int
    card_id: str
    is_deleted: bool

    class Config:
        orm_mode = True

class Detail(DetailInDBBase):
    pass

class IdentityCardBase(BaseModel):
    serial: str
    number: str
    issuer: str
    issue_date: datetime
    issue_place: str
    code: str

class IdentityCardCreate(IdentityCardBase):
    pass

class IdentityCardUpdate(IdentityCardBase):
    pass

class IdentityCardInDBBase(IdentityCardBase):
    id: int

    class Config:
        orm_mode = True

class IdentityCard(IdentityCardInDBBase):
    pass

class NextdetailCreate(BaseModel):
    first_name: str
    last_name: str
    birth_date: datetime
    card_id: str

class NextdetailUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    birth_date: Optional[datetime] = None
    card_id: Optional[str] = None
