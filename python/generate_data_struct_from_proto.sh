# pip install grpcio-tools
python -m grpc_tools.protoc   -I ../proto --python_out=. --pyi_out=. --grpc_python_out=. grpc_demo.proto