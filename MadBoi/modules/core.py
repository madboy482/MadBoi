from MadBoi import telethn as tbot, OWNER_ID, DEV_USERS, MadBoi
from MadBoi.events import register
import os
import asyncio
import os
import time
from datetime import datetime
from MadBoi import TEMP_DOWNLOAD_DIRECTORY as path
from MadBoi import TEMP_DOWNLOAD_DIRECTORY
from datetime import datetime
import asyncio
from MadBoi.events import register
import os
import time
from datetime import datetime as dt
# from MadBoi import MadBoi, telethn as client
opn = []

@register(pattern="/open")
async def _(event):
    xx = await event.reply("Processing...")
    if event.reply_to_msg_id:
        a = await event.get_reply_message()
        if a.media:
            b = await a.download_media()
            c = open(b, "r")
            d = c.read()
            c.close()
            n = 4096
            for bkl in range(0, len(d), n):
                opn.append(d[bkl : bkl + n])
            for bc in opn:
                await event.client.send_message(
                    event.chat_id,
                    f"{bc}",
                    reply_to=event.reply_to_msg_id,
                )
            await event.delete()
            opn.clear()
            os.remove(b)
            await xx.delete()
        else:
            return await event.reply("Reply to a readable file")
    else:
        return await event.reply("Reply to a readable file")
client = tbot
import time
from io import BytesIO
from pathlib import Path
from MadBoi import telethn as borg
from telethon import functions, types
from telethon.errors import PhotoInvalidDimensionsError
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.messages import SendMediaRequest
@register(pattern="^/dox ?(.*)")
async def get(event):
    name = event.text[5:]
    if name is None:
        await event.reply("Reply to text message as `/dox <file name>`")
        return
    m = await event.get_reply_message()
    if m.text:
        with open(name, "w") as f:
            f.write(m.message)
        await event.delete()
        await event.client.send_file(event.chat_id, name, force_document=True)
        os.remove(name)
    else:
        await event.reply("Reply to text message as `/dox <file name>`")

from MadBoi.events import load_module
import asyncio
import os
from datetime import datetime
from pathlib import Path

@register(pattern="^/install")
async def install(event):
    if event.fwd_from:
        return
    if event.sender_id == OWNER_ID or event.sender_id in DEV_USERS or event.sender_id == MadBoi:
        pass
    else:
        return
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = (
                await event.client.download_media(  # pylint:disable=E0602
                    await event.get_reply_message(),
                    "MadBoi/modules/",  # pylint:disable=E0602
                )
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await event.reply("Installed, the given plug....\n😉😏 `{}`".format(
                        os.path.basename(downloaded_file_name)
                    ),
                )
            else:
                os.remove(downloaded_file_name)
                await event.reply("**Error!**\nCan't Install!\n Or Pre-Installed Maybe..",
                )
        except Exception as e:  # pylint:disable=C0103,W0703
            j = await event.reply(str(e))
            await asyncio.sleep(3)
            await j.delete()
            os.remove(downloaded_file_name)
    await asyncio.sleep(3)
    await event.delete()
__help__ = """
 *You can make a file 
  name. *

 ✪ /install for devs only 🙄
 ✪ /dox tag a message <file name> example /dox example.py
 ✪ /open tag a file <÷>
"""

__mod_name__ = "Core 🙄"

