from pyrogram import Client
import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config  # pylint:disable=import-error


if __name__ == "__main__":
    plugins = dict(root="plugins")

    app = Client(
        "master",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        updates_ch=Config.UPDATES_CH,
        support_grp=Config.SUPPORT_GRP,
        plugins=plugins,
        workers=300,
    )
    app.run()
