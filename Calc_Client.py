from __future__ import print_function

import grpc

import Calc_pb2
import Calc_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = Calc_pb2_grpc.CalculatorStub(channel)
        response = stub.Add(Calc_pb2.AddRequest(n1 = 20, n2 = 10))
        print(response.n1)


if __name__ == '__main__':
    run()