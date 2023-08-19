import logging
from tgbot.bot_app.app import bot
from .handlers import commands
from .handlers import navigation
from .keybords.kb_avia_rain import keybords_avia_rain
from tgbot.bot_app.keybords import keyboards_menu
from tgbot.bot_app.handlers import text_erly_help
from tgbot.bot_app.keybords import early_help


logging.basicConfig(level=logging.INFO)


