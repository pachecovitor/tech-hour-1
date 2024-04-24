from fastapi import FastAPI, HTTPException
from .schemas import EmailSchema
from worker.celery_worker import send_email_task

app = FastAPI()

@app.post("/send-email/")
def send_email(email: EmailSchema):
    try:
        send_email_task.delay(email.dict())
        return {"message": "Email is being sent"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
