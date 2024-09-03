from pydantic import BaseModel

class Details(BaseModel):
    name: str
    age: int
    phone_no: str
    marital_status: bool
    shopping_zone: list
    address: dict