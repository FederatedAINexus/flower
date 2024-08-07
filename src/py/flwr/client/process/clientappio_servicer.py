# Copyright 2024 Flower Labs GmbH. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""ClientAppIo API servicer."""


from logging import DEBUG, INFO
from typing import Optional

import grpc

from flwr.common import Context, Message, typing
from flwr.common.logger import log
from flwr.common.serde import (
    context_from_proto,
    context_to_proto,
    message_from_proto,
    message_to_proto,
    run_to_proto,
    status_to_proto,
)
from flwr.common.typing import Run

# pylint: disable=E0611
from flwr.proto import appio_pb2_grpc
from flwr.proto.appio_pb2 import (
    PullClientAppInputsRequest,
    PullClientAppInputsResponse,
    PushClientAppOutputsRequest,
    PushClientAppOutputsResponse,
)
from flwr.proto.run_pb2 import Run as ProtoRun
from flwr.proto.transport_pb2 import Context as ProtoContext
from flwr.proto.transport_pb2 import Message as ProtoMessage


class ClientAppIoServicer(appio_pb2_grpc.ClientAppIoServicer):
    """ClientAppIo API servicer."""

    def __init__(self) -> None:
        self.message: Optional[Message] = None
        self.context: Optional[Context] = None
        self.proto_message: Optional[ProtoMessage] = None
        self.proto_context: Optional[ProtoContext] = None
        self.proto_run: Optional[ProtoRun] = None
        self.token: Optional[int] = None

    def PullClientAppInputs(
        self, request: PullClientAppInputsRequest, context: grpc.ServicerContext
    ) -> PullClientAppInputsResponse:
        log(INFO, "ClientAppIo.PullInputs")
        assert request.token == self.token
        return PullClientAppInputsResponse(
            message=self.proto_message,
            context=self.proto_context,
            # fab=self.fab,
            run=self.proto_run,
        )

    def PushClientAppOutputs(
        self, request: PushClientAppOutputsRequest, context: grpc.ServicerContext
    ) -> PushClientAppOutputsResponse:
        log(INFO, "ClientAppIo.PushOutputs")
        assert request.token == self.token
        self.proto_message = request.message
        self.proto_context = request.context
        # Update Message and Context
        self._update_object()
        # Set status
        code = typing.Code.OK
        status = typing.Status(code=code, message="Success")
        proto_status = status_to_proto(status=status)
        return PushClientAppOutputsResponse(status=proto_status)

    def set_object(
        self,
        message: Message,
        context: Context,
        run: Run,
        token: int,
    ) -> None:
        """Set client app objects."""
        log(DEBUG, "ClientAppIo.SetObject")
        # Serialize Message, Context, and Run
        self.proto_message = message_to_proto(message)
        self.proto_context = context_to_proto(context)
        # self.fab = fab
        self.proto_run = run_to_proto(run)
        self.token = token

    def get_object(self) -> tuple[Message, Context]:
        """Get client app objects."""
        log(DEBUG, "ClientAppIo.GetObject")
        return self.message, self.context

    def _update_object(self) -> None:
        """Update client app objects."""
        log(DEBUG, "ClientAppIo.UpdateObject")
        # Deserialize Message and Context
        self.message = message_from_proto(self.proto_message)
        self.context = context_from_proto(self.proto_context)
