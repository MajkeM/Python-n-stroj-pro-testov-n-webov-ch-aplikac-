import argparse
from pathlib import Path

import yaml

from .config import load_config, validate_config


def main():
    parser = argparse.ArgumentParser(
        description="This is a command line interface for the injection framework"
    )

    #adding arguments to the parser

    parser.add_argument(
        "--config", help="Path to the config file", type=Path
    )

    parser.add_argument(
        "--target", dest="target_url", help="Target URL"
    )

    parser.add_argument(
        "--parameter", help="Parameter to inject"
    )

    parser.add_argument(    
        "--modules", nargs="+", help="Modules to use"
    )



    args = parser.parse_args()

   

    try:

        config = {}

        #if config yaml file is exist this block will load the yaml file

        if args.config is not None:
            if not args.config.is_file():
                parser.error("Config file does not exist")

            config = load_config(args.config)


        #if config yaml file in uncompleted, this block will add the missing values from cli

        if args.target_url is not None:
            config["target_url"] = args.target_url

        if args.parameter is not None:
            config["parameter"] = args.parameter

        if args.modules is not None:
            config["modules"] = args.modules

        config = validate_config(config)





    except (ValueError, yaml.YAMLError, OSError) as error:
        parser.error(str(error))

    print(config)
