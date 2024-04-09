from dataclasses import dataclass
from environs import Env

@dataclass
class TgBot:
    token: str
    admin_ids: list[int] # Токен для доступа к телеграм-боту

@dataclass
class Config:
    tg_bot: TgBot

def load_config(path: str | None) -> Config:

    env: Env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),
            admin_ids = list(map(int, env.list('ADMIN_IDS')))))

class GlobalVars:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GlobalVars, cls).__new__(cls)
            cls._instance.page = None
        return cls._instance