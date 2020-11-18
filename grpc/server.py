import grpc
import time
from concurrent import futures
import calculator_grpc_pb2
import calculator_grpc_pb2_grpc


def serve():
    grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_grpc_pb2_grpc.add_apiServicer_to_server(CalculatorServicer(), grpc_server)
    grpc_server.add_insecure_port('[::]:9999')
    grpc_server.start()
    while True:
        time.sleep(860000)


class CalculatorServicer(calculator_grpc_pb2_grpc.apiServicer):

    def add(self, request, context):
        return calculator_grpc_pb2.num(num=(request.numOne+request .numTwo))

    def sub(self, request, context):
        return calculator_grpc_pb2.num(num=(request.numOne-request .numTwo))

    def mul(self, request, context):
        return calculator_grpc_pb2.num(num=(request.numOne*request .numTwo))

    def div(self, request, context):
        return calculator_grpc_pb2.num(num=(request.numOne/request .numTwo))

    def sq(self, request, context):
        return calculator_grpc_pb2.num(num=(request.num ** 0.5))

if __name__ == '__main__':
    serve()
