class StringScheme:
    scheme_get_string = {
        "type": "object",
        "properties": {
            "result": {"type": "string"},
        },
        "required": ["result"]
    }
    scheme_post_string = {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "result": {"type": "string"},
        },
        "required": ["result", "id"],
    }