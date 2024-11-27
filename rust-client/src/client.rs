use grpc_demo::grpc_demo_client::GrpcDemoClient;
use grpc_demo::String;

pub mod grpc_demo {
    tonic::include_proto!("grpc_demo");
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut client = GrpcDemoClient::connect("http://[::1]:50052").await?;

    let request = tonic::Request::new(String {
        str: "promt from rust grpc client".into(),
    });

    let response = client.generate_seq(request).await?;

    println!("RESPONSE={:?}", response);

    let request = tonic::Request::new(String {
        str: "promt from rust grpc client".into(),
    });

    let mut stream_response = client.generate_seq_stream(request).await?
        .into_inner();

    while let Some(txt) = stream_response.message().await? {
        println!("{}", txt.str)
    }
    Ok(())
}