# gRPC Calculator

A simplest (Python based) calculator program using gRPC architecture. The Calculator supports Add, Subtract, Multiplication and division operation. 

## Getting Started with gRPC
gRPC consists of following steps:

* Create the service definition and payload structure in the Protocol Buffer (.proto) file.
* Generate the gRPC code from the .proto file.
* Implement the server in one of the supported languages.
* Create the client that invokes the service through the Stub.
* Run the server and client(s).

### Proto file

The proto file is placed in "Proto" folder. It is based on "proto3" syntax.
Use below command (inside Proto directory) to compile the .proto file:

```
python -m grpc.tools.protoc  --python_out=. --grpc_python_out=. --proto_path=. Calc.proto
```

After compiling, use the following command:
```
cp Calc_pb2* ../
```
### Server and Client

Use the following command to run Server and Client:

For Server:

```
python Calc_Server.py
```

And for Client:

```
python Calc_Client.py
```

## References

* [gRPC Quickstart with Python](https://grpc.io/docs/quickstart/python.html)
