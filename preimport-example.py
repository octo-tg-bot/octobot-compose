import logging
logging.basicConfig(level=logging.DEBUG)
logging.getLogger("telegram.bot").setLevel(logging.INFO)
logging.getLogger("telegram.vendor.ptb_urllib3.urllib3.connectionpool").setLevel(logging.WARNING)
logging.info("Python-Telegram-Bot is quiet now")
