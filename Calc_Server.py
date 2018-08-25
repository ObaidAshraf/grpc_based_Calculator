from concurrent import futures
import time

import grpc

import Calc_pb2
import Calc_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Calculator(Calc_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        return Calc_pb2.AddReply(n1 = request.n1 + request.n2)

    def Subtract(self, request, context):
        return Calc_pb2.AddReply(n1 = request.n1 - request.n2)

    def Multiple(self, request, context):
        return Calc_pb2.AddReply(n1 = request.n1 * request.n2)

    def Divide(self, request, context):
        return Calc_pb2.AddReply(n1 = request.n1 / request.n2)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Calc_pb2_grpc.add_CalculatorServicer_to_server(Calculator(), server)
    server.add_insecure_port('[::]:50051')