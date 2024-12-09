import logging

from dataclasses import dataclass


@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tg_bot: TgBot


logger = logging.getLogger(__name__)


def load_config() -> Config:
    import os
    from dotenv import load_dotenv, find_dotenv
    logger.info('load .env')
    load_dotenv(find_dotenv())
    logger.info('return Config')
    return Config(tg_bot=TgBot(token=os.getenv('TOKEN')))
