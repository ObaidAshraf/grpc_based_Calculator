from __future__ import print_function

import grpc

import Calc_pb2
import Calc_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = Calc_pb2_grpc.CalculatorStub(channel)
        response = stub.Add(Calc_pb2.AddRequest(n1 = 20, n2 = 10))
        print(response.n1)
        response = stub.Subtract(Calc_pb2.SubtractRequest(n1 = 50, n2 = 20))
        print(response.n1)
        response = stub.Multiply(Calc_pb2.MultiplyRequest(n1 = 10, n2 = 5))
        print(response.n1)
        response = stub.Divide(Calc_pb2.DivideRequest(n1 = 100, n2 = 2))
        print(response.f1)


if __name__ == '__main__':
    run()