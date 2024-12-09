import logging.config, yaml

with open('app/logging_config/config_logging.yaml', "tr") as file:
    config = yaml.safe_load(file.read())
    logging.config.dictConfig(config)



if __name__ == '__main__':
    pass