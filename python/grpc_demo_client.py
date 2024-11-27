import grpc
import grpc_demo_pb2_grpc
import grpc_demo_pb2

channel = grpc.insecure_channel('localhost:50052')
print(channel)

stub = grpc_demo_pb2_grpc.GrpcDemoStub(channel)

respanse = stub.generate_seq(grpc_demo_pb2.String(str="message from python rpc clinet: generate_seq"))
print(respanse)

for respanse in stub.generate_seq_stream(grpc_demo_pb2.String(str="message from python rpc clinet: generate_seq")):
    print(respanse)