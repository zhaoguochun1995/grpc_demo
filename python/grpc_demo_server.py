from concurrent import futures
import grpc
import grpc_demo_pb2
import grpc_demo_pb2_grpc

class GrpcDemoServer(grpc_demo_pb2_grpc.GrpcDemoServicer):
    def generate_seq(self, request, context):
        print(request)
        return grpc_demo_pb2.String(str="message from python server: generate_seq: " + request.str.upper())

    def generate_seq_stream(self, request, context):

        print(request)
        for word in request.str.split(" "):
            yield grpc_demo_pb2.String(str="message from python server: generate_seq_stream:" + word.upper() )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_demo_pb2_grpc.add_GrpcDemoServicer_to_server(GrpcDemoServer(), server)
    server.add_insecure_port("[::]:50052")
    server.start()
    print(server)
    server.wait_for_termination()


if __name__ == "__main__":
    serve()