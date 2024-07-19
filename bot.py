# Credit @TheBlackXYZ.
# Please Don't remove credit.
# TheBlackXYZBotz Forever !
# Thanks You For Help Us In This Amazing Creativity 
# Thanks You For Giving Me Credit @TheBlackXYZBotz
# For Any ERROR Please Contact Me -> Telegram ->@TheBlackXYZBotz & Insta @TheBlackXYZ
# Please Love & Support 💗💗🙏

import sys
from aiohttp import web
from plugins import web_server
import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
from datetime import datetime
from info import *
#from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, #TG_BOT_WORKERS, FORCE_CHANNEL, #CHANNEL_ID, PORT

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={"root": "plugins"},
            workers=BOT_WORKERS,
            bot_token=BOT_TOKEN)
            self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        if FORCE_CHANNEL:
            try:
                link = (await self.get_chat(FORCE_CHANNEL)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_CHANNEL)
                    link = (await self.get_chat(FORCE_CHANNEL)).invite_link
                self.invitelink = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Please Double check the FORCE_CHANNEL value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCE_CHANNEL}")
                self.LOGGER(__name__).info("\Sweety Bot Is Stopped 🤔🛠️. Developerr https://t.me/Itz_rohan_24")
                sys.exit()
        try:
            db_channel = await self.get_chat(CHANNEL)
            self.db_channel = db_channel
            test = await self.send_message(chat_id = db_channel.id, text = "Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(f"Make Sure bot is Admin in DB Channel, and Double check the CHANNEL_ID Value, Current Value {CHANNEL}")
            self.LOGGER(__name__).info("\nBot Stopped. Developerr https://t.me/Itz_rohan_24")
            sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(f"Bot Started Sweetie ❤️\n\nDeveloperr\nhttps://t.me/TheBlackXYZBotz")
        self.LOGGER(__name__).info(f""" \n\n THE BLACK XYZ FILE SHARING BOT READY """)
        self.username = usr_bot_me.username
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Sweety Bot Is Stopped 🤔🛠️")



Bot().run()