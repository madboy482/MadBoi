# COPYRIGHT (C) BY LEGENDX22, PROBOYX AND MADBOY

"""
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
                 MADE BY LEGENDX AND PROBOY
                PLEASE DON'T REMOVE CREDITS
"""
#    Don't dare to remove the credits, else be ready for DMCA.
#    Changed some texts for ROMEO-3.0

#    Credits to :-
#    ➥ LEGENDX
#    ➥ PROBOY
#    ➥ MADBOY

# +-+ +-+ +-+ +-+    +-+ +-+ +-+ +-+    +-+ +-+ +-+ +-+ +-+ +-+ +-+
# |K| |A| |N| |G|    |W| |I| |T| |H|    |C| |R| |E| |D| |I| |T| |S|
# +-+ +-+ +-+ +-+    +-+ +-+ +-+ +-+    +-+ +-+ +-+ +-+ +-+ +-+ +-+

from telethon import events, Button, custom
import re, os
from MadBoi.events import register
from MadBoi import telethn as tbot
from MadBoi import telethn as tgbot
PHOTO = "https://telegra.ph/file/90e0bceeaf40b4a16f672.jpg"
@register(pattern=("/alive"))
async def awake(event):
  madboy = event.sender.first_name
  MadBoy = f"✧✧ ROMEO-3.0 IS UP AND RUNNING SUCCESSFULLY ✧✧\n\n"
  MadBoy += f"➥ DATABASE : `ALL DATABASES FUNCTIONING PROPERLY`\n"
  MadBoy += f"➥ ROMEO OS : `3.0` [LATEST]\n"
  MadBoy += f"➥ USER : {madboy}\n"
  MadBoy += f"➥ FULLY UPDATED\n"
  MadBoy += f"➥ TELETHON : `1.19.5` [LATEST]\n\n"
  MadBoy += "THANKS FOR USING ME!!"
  BUTTON = [[Button.url("🧑‍💻 DEVELOPER 🧑‍💻", "https://t.me/Warning_MadBoy_is_Here"), Button.url("DEVs", "https://t.me/Wanacoins")]]
  BUTTON += [[custom.Button.inline("REPOSITORYS", data="MadBoi")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=MadBoy,  buttons=BUTTON)




@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"MadBoi")))
async def callback_query_handler(event):

  MBoy = [[Button.url("REPO » ROMEO ", "https://github.com/madboy482/Romeo"), Button.url("REPO » ROMEO-3.0", "https://github.com/madboy482/MadBoi")]]
  MBoy +=[[Button.url("DEPLOY » ROMEO", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Fmadboy482%2FRomeo&template=https%3A%2F%2Fgithub.com%2Fmadboy482%2FRomeoP%2FLE"), Button.url("DEPLOY » ROMEO-3.0", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Fmadboy482%2FMadBoi&template=https%3A%2F%2Fgithub.com%2Fmadboy482%2FMadBoi")]]
  MBoy +=[[Button.url("REPO » JOIN CAPTCHA", "https://github.com/madboy482/Join-Captcha"), Button.url("REPO » POKEDEX BOT", "https://github.com/madboy482/Rotom-2.0")]]
  MBoy +=[[Button.url("REPO » TELEGRAPH UPLOADER", "https://github.com/madboy482/Telegraph-Uploader"), Button.url("REDIS", "https://redislabs.com")]]
  MBoy +=[[Button.url("SUPPORT CHANNEL", "https://t.me/LEGENDBOT_OFFICIAL"), Button.url("SUPPORT GROUP", "https://t.me/LEGEND_USERBOT_SUPPORT")]]
  MBoy +=[[custom.Button.inline("«« ALIVE", data="PROBOY")]]
  await event.edit(text=f"ALL DETAILS OF REPOS", buttons=MBoy)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"PROBOY")))
async def callback_query_handler(event):
  global PHOTO
  madboy = event.sender.first_name

  LEGENDX = "HELLO THIS IS GRAND OFFICIAL \n\n"
  LEGENDX += "ALL SYSTEM WORKING PROPERLY\n\n"
  LEGENDX += "GRAND OS : 3.8 LATEST\n\n"
  LEGENDX += f"MY MASTER {legendx} ☺️\n\n"
  LEGENDX += "FULLY UPDATED BOT\n\n"
  LEGENDX += "TELETHON : 1.19.5 LATEST\n\n"
  LEGENDX += "THANKS FOR ADD ME HERE"
  BUTTONS = [[Button.url("MASTER", "https://t.me/LEGENDX22"), Button.url("DEVLOPER", "https://t.me/proboyx")]]
  BUTTONS += [[custom.Button.inline("REPOSITORYS", data="LEGENDX")]]
  await event.edit(text=LEGENDX, buttons=BUTTONS)


@register(pattern=("/repo|#repo"))
async def repo(event):
  await tbot.send_message(event.chat, "REPO OF GRAND OFFICIAL", buttons=[[Button.url("⚜️REPO⚜️", "https://github.com/LEGENDXOP/LEGEND-X")]])


__help__ = """
 - /alive check bot alive or die
 - /repo for this bot repo
"""
__mod_name__ = "Alive⚜️"
