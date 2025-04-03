# File: dispatcher.py
import json
def dispatch_function_call(json_response):
    """
    Parses the JSON response and executes the corresponding function.
    """
    data = json.loads(json_response)
    if "function" in data:
        func_name = data["function"]
        params = data.get("parameters", {})
        if func_name in function_map:
            return function_map[func_name](**params)
        else:
            return f"Error: Function '{func_name}' is not defined."
    return "No actionable function call identified."
