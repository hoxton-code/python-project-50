import json


def format_json(data):
    """
     Render a diff dictionary into a JSON string with 4-space indentation.

     Parameters:
     data: Data structure to convert.

     Returns:
     JSON-formatted string.
     """

    return json.dumps(data, indent=4)
