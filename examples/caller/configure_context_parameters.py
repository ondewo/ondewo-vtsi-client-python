import uuid
from typing import Dict, Optional

from ondewo.nlu import context_pb2

PROJECT_ID: str = "example_project_id"
call_id = str(uuid.uuid4())
input_context_name = "c-input"
input_context_parameters = {
    "test": "test_value"
}


def create_parameter_dict(my_dict: Dict) -> Optional[Dict[str, context_pb2.Context.Parameter]]:
    assert isinstance(my_dict, dict) or my_dict is None, "parameter must be a dict or None"
    if my_dict is not None:
        return {
            key: context_pb2.Context.Parameter(
                display_name=key,
                value=my_dict[key]
            )
            for key in my_dict
        }
    return None


context = context_pb2.Context(
    name=f"projects/{PROJECT_ID}/agent/sessions/{call_id}/contexts/{input_context_name}",
    lifespan_count=10000,
    parameters=create_parameter_dict(input_context_parameters),
)

contexts_to_pass = [context]

# Context list can be passed during CaiConfiguration initialization (global) OR
# VtsiClient.start_caller() function call (local)
