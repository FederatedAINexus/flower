import flwr as fl

# Start Flower server
fl.server.start_server(
    server_address="0.0.0.0:8080",  # TODO revert
    config={"num_rounds": 3},
    use_rest=True,
)
