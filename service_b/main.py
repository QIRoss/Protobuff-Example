# service_b/main.py
from fastapi import FastAPI, Request
import message_pb2
from fastapi.responses import Response

app = FastAPI()

@app.post("/receive-message/")
async def receive_message(request: Request):
    request_data = await request.body()
    received_message = message_pb2.RequestMessage()
    received_message.ParseFromString(request_data)

    response_message = message_pb2.ResponseMessage(reply=f"Received: {received_message.message}")
    serialized_response = response_message.SerializeToString()

    return Response(content=serialized_response, media_type="application/octet-stream")