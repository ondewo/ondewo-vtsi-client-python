import argparse

from ondewo.utils.base_client_config import BaseClientConfig

from ondewo.vtsi.client.client import Client
from ondewo.vtsi.client.client_config import ClientConfig
from ondewo.vtsi.projects_pb2 import GetVtsiProjectRequest


def main() -> None:
    parser = argparse.ArgumentParser(description="File transcription example.")
    parser.add_argument(
        "--config",
        type=str,
        help="The GRPC configuration file path. "
             "See examples/configs in the ondewo-s2t-client-python repository.",
    )
    parser.add_argument(
        "--secure",
        default=False,
        action="store_true",
        help="Use secure GRPC connection (default is insecure).",
    )
    args = parser.parse_args()

    config: BaseClientConfig
    if args.config:
        with open(args.config) as f:
            config = ClientConfig.from_json(f.read())
    else:
        config = BaseClientConfig(
            host="localhost",
            port="50200",
        )

    client: Client = Client(config=config, use_secure_channel=False)
    client.services.projects.get_vtsi_project(request=GetVtsiProjectRequest(name="test"))


if __name__ == "__main__":
    main()
