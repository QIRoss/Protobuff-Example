# Protobuff Example

## Overview

In this example, we're using Protocol Buffers (protobufs) to facilitate communication between two microservices, ```service_a``` and ```service_b```, both implemented using FastAPI and containerized using Docker. 

The example demonstrates how protobufs provide a structured and efficient way to serialize and deserialize messages exchanged between these services, which makes data communication more efficient compared to text-based formats like JSON.

### Key Components

1. Protocol Buffer Schema (```message.proto```):

* This file defines the structure of the messages that ```service_a``` and ```service_b``` exchange.

* It specifies two message types:

```
syntax = "proto3";

message RequestMessage {
  string message = 1;
}

message ResponseMessage {
  string reply = 1;
}
```

* ```RequestMessage``` includes a single field ```message``` of type string, identified by the tag ```1```.

* ```ResponseMessage``` includes a single field ```reply``` of type string, also identified by the tag ```1```.

2. Serialization and Deserialization:

* Protobufs serialize structured data into a compact binary format. This makes data transmission between ```service_a``` and ```service_b``` efficient and fast.

When a message is received, it is deserialized from its binary format back into a usable object.
Services and Communication Flow:

* ```service_a```:

* Accepts a POST request at the ```/send-message/``` endpoint, containing a JSON payload with a ```message```.

* Converts the ```message``` into a protobuf ```RequestMessage```, serializes it, and sends it to ```service_b``` via an HTTP POST request.

* Receives the response from ```service_b```, deserializes the protobuf ```ResponseMessage```, and returns the response to the client.

```service_b```:

* Listens for requests at the ```/receive-message/``` endpoint.
* Deserializes the incoming ```RequestMessage``` protobuf from ```service_a```.
* Constructs a ```ResponseMessage``` protobuf, serializes it, and sends it back as the response.

### Benefits of Using Protobufs in This Example

1. Efficient Data Transfer: Data is transmitted in a compact binary format, making it faster and more efficient than text-based formats like JSON or XML.

2. Strong Typing: Protobuf enforces strict typing and schema validation, reducing potential errors.

3. Cross-Language Compatibility: Protobuf messages can be easily used in various languages and platforms, making it ideal for distributed systems.

4. Versioning: Fields can be added or modified in a backward-compatible way, minimizing the impact on existing clients and services.

### Example Communication Flow

1. A client sends a POST request to ```service_a``` with a message: ```{"message": "Hello from service_a"}```.

2. ```service_a``` serializes this message using the protobuf ```RequestMessage``` format and sends it to ```service_b```.

3. ```service_b``` deserializes the incoming message, processes it, and creates a ```ResponseMessage``` protobuf.

4. ```service_b``` serializes the response and sends it back to ```service_a```.

5. ```service_a``` deserializes the response and returns it to the client.

This example highlights how Protocol Buffers enable structured, efficient communication between microservices, making them an excellent choice for high-performance, cross-platform data exchange.

## How to Use

### Prerequisites

* Ensure you have Docker and Docker Compose installed on your system.

* You should have your project directory set up with the docker-compose.yml, message.proto, generated message_pb2.py files, and the necessary service directories (```service_a``` and ```service_b```).

### Steps to Run the Services

1. Generate the Protobuf Code (if not already generated): Make sure you have generated the message_pb2.py files for both ```service_a``` and ```service_b``` by running:

```
protoc --python_out=./```service_a``` message.proto
protoc --python_out=./```service_b``` message.proto
```

This will generate the Python code needed to use the protobuf messages.

2. Build and Run the Services using Docker Compose: In your project root directory (where docker-compose.yml is located), run the following command:

```
docker-compose up --build
```

This command:

* Builds the Docker images for ```service_a``` and ```service_b```.

* Starts the containers for both services.

* You should see logs indicating that the FastAPI servers for both services are running.

3. Test the Communication between Services using curl: In another terminal window, send a POST request to ```service_a``` using the following curl command:

```
curl -X POST "http://localhost:8000/send-message/" -H "Content-Type: application/json" -d '{"message": "Hello from service_a"}'
```

This will:

* Send a JSON payload with the message ```"Hello from service_a"``` to ```service_a```.

* ```service_a``` will serialize the message using protobuf, send it to ```service_b```, and handle the response.

* ```service_b``` will deserialize the message, create a response using protobuf, and send it back to ```service_a```.

* ```service_a``` will deserialize the response and return the result.

Expected Output

You should see a response from ```service_a``` similar to the following:

```
{"reply":"Received: Hello from service_a"}
```

### Notes

* If you encounter any issues, check the container logs for ```service_a``` and ```service_b``` to debug.

* Ensure that the ```message_pb2.py``` files are correctly generated and located in the ```service_a``` and ```service_b``` directories.