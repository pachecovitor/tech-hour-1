from pydantic import BaseModel, EmailStr

class EmailSchema(BaseModel):
    email_to: EmailStr
    subject: str
    body: str
