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

'Test_VVLX_Bot'
'6541851084:AAFIsmRzvzndK-x2vZxyFra-P40yZtPkbnw'