"""Create global evaluation function.

Optionally, also define a new Server class (please note this is not
needed in most settings).
"""

from collections import OrderedDict
from typing import Callable, Dict, Optional, Tuple

import torch
from moon.dataset_preparation import get_data_transforms, get_transforms_apply_fn
from moon.models import init_net, test
from torch.utils.data import DataLoader

from datasets import load_dataset
from flwr.common import Context
from flwr.common.typing import NDArrays, Scalar
from flwr.server import ServerApp, ServerAppComponents, ServerConfig
from flwr.server.strategy import FedAvg


def gen_evaluate_fn(
    testloader: DataLoader,
    device: torch.device,
    dataset_name: str,
    model_name: str,
    model_output_dim: int,
) -> Callable[
    [int, NDArrays, Dict[str, Scalar]], Optional[Tuple[float, Dict[str, Scalar]]]
]:
    """Generate the function for centralized evaluation."""

    def evaluate(
        server_round: int, parameters_ndarrays: NDArrays, config: Dict[str, Scalar]
    ) -> Optional[Tuple[float, Dict[str, Scalar]]]:
        # pylint: disable=unused-argument
        net = init_net(dataset_name, model_name, model_output_dim)
        params_dict = zip(net.state_dict().keys(), parameters_ndarrays)
        state_dict = OrderedDict({k: torch.from_numpy(v) for k, v in params_dict})
        net.load_state_dict(state_dict, strict=True)
        net.to(device)
        accuracy, loss = test(net, testloader, device=device)
        return loss, {"accuracy": accuracy}

    return evaluate


def server_fn(context: Context) -> ServerAppComponents:
    """Construct ServerAppComponents object to create a ServerApp."""
    dataset_name = context.run_config["dataset-name"]
    # This is the exact same dataset as the one donwloaded by the clients via
    # FlowerDatasets.However, we don't use FlowerDatasets for the server since
    # partitioning it is not needed.
    # We make use of the "test" split only
    global_test_set = load_dataset(dataset_name)["test"]
    _, test_transforms = get_data_transforms(dataset_name=dataset_name)

    transforms_fn = get_transforms_apply_fn(test_transforms)
    testloader = DataLoader(
        global_test_set.with_transform(transforms_fn),
        batch_size=context.run_config["batch-size"],
    )

    evaluate_fn = gen_evaluate_fn(
        testloader,
        device=context.run_config["server-device"],
        dataset_name=dataset_name,
        model_name=context.run_config["model-name"],
        model_output_dim=context.run_config["model-output-dim"],
    )

    strategy = FedAvg(
        # Clients in MOON do not perform federated evaluation
        # (see the client's evaluate())
        fraction_fit=context.run_config["fraction-fit"],
        fraction_evaluate=0.0,
        evaluate_fn=evaluate_fn,
    )

    config = ServerConfig(num_rounds=context.run_config["num-server-rounds"])

    return ServerAppComponents(strategy=strategy, config=config)


app = ServerApp(server_fn=server_fn)
