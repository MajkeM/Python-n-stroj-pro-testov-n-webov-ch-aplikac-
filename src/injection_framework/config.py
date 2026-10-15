from pathlib import Path

import yaml
from urllib.parse import urlsplit 

def load_config(path: Path):
    
    data = yaml.safe_load(path.read_text(encoding="utf-8"))

    if not isinstance(data, dict):
        raise ValueError("Config file must contain key: value pairs")

    return data


def validate_config(data):

    if not isinstance(data, dict):
        raise ValueError("Configuration must be a dictionary")

    required_keys = ["target_url", "parameter", "modules"]



    
    # Check all required keys before reading their values.
    for key in required_keys:
        if key not in data:
            raise ValueError(f"Configuration must include key: {key}")




    # Text values must not be empty or contain only whitespace.
    for key in ("target_url", "parameter"):
        value = data[key]
        if not isinstance(value, str):
            raise ValueError(f"{key} must be a string")
        if not value.strip():
            raise ValueError(f"{key} must not be empty")


    """ validating url link"""
    
    # checking if url contain http or https
    parsed_url = urlsplit(data["target_url"])
    if parsed_url.scheme not in ("http", "https"):
        raise ValueError("url link does not contain http/https protocol")

    # checking hostname
    if not parsed_url.hostname:
        raise ValueError("missing server, hostname")


    
    modules = data["modules"]



    if not isinstance(modules, list):
        raise ValueError("modules must be a list")
    if not modules:
        raise ValueError("modules must not be empty")

    for module in modules:
        if not isinstance(module, str):
            raise ValueError("Each module name must be a string")
        if not module.strip():
            raise ValueError("Module names must not be empty")

    return data
