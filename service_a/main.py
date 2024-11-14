from fastapi import FastAPI
from pydantic import BaseModel
import message_pb2
import httpx

app = FastAPI()

class MessageRequest(BaseModel):
    message: str

@app.post("/send-message/")
async def send_message(request: MessageRequest):
    request_message = message_pb2.RequestMessage(message=request.message)
    serialized_message = request_message.SerializeToString()

    async with httpx.AsyncClient() as client:
        response = await client.post("http://service_b:8001/receive-message/", content=serialized_message)

    response_message = message_pb2.ResponseMessage()
    response_message.ParseFromString(response.content)
    return {"reply": response_message.reply}
