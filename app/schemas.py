from pydantic import BaseModel
from typing import Optional

class IdentifierBase(BaseModel):
    identifier_name: str
    description: Optional[str] = None
    identifier_type: Optional[str] = None

class IdentifierCreate(IdentifierBase):
    pass

class IdentifierResponse(IdentifierBase):
    class Config:
        from_attributes = True