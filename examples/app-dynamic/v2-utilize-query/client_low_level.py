from flwr.client import ClientApp
from flwr.common import Context
from flwr.common import Message
from flwr.common.constant import ErrorCode
from flwr.common.message import Error

# Flower ClientApp
app = ClientApp()

@app.query()
def query(msg: Message, ctx: Context):
    try:
        raise ValueError()
        # load the model/dataset
        print(f"In Client msg.content.configs_records: {msg.content.configs_records}")
        return msg.create_reply(msg.content)
    except:
        msg.create_error_reply(
            error=Error(code=ErrorCode.UNKNOWN, reason="Unknown")
        )
