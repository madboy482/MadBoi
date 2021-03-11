# COPYRIGHT (C) 2021 BY LEGENDX22, PROBOYX AND MADBOY

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

# ALIVE AND REPOSITORYS TEXT :-
# COPYRIGHT (C) 2021 BY MADBOY, DON'T TRY TO USE IT WITHOUT GETTING PERMISSION FROM @Warning_MadBoy_is_Here (Telegram Acc.) 
# {STILL GOING TO USE WITHOUT PERMISSION, BE READY FOR DMCA}

from telethon import events, Button, custom
import re, os
from MadBoi.events import register
from MadBoi import telethn as tbot
from MadBoi import telethn as tgbot
ROMEOv3 = "https://telegra.ph/file/90e0bceeaf40b4a16f672.jpg"
@register(pattern=("/alive|#alive"))
async def awake(event):
  madboy = event.sender.first_name
  MadBoy = f"✧✧ ROMEO-3.0 IS UP AND RUNNING SUCCESSFULLY ✧✧\n\n"
  MadBoy += f"➥ DATABASE : `ALL DATABASES FUNCTIONING PROPERLY`\n"
  MadBoy += f"➥ ROMEO OS : `3.0` [LATEST]\n"
  MadBoy += f"➥ USER : `{madboy}`\n"
  MadBoy += f"➥ FULLY UPDATED\n"
  MadBoy += f"➥ TELETHON : `1.19.5` [LATEST]\n\n"
  MadBoy += "THANKS FOR USING ME!!"
  BUTTON = [[Button.url("🧑‍💻 DEVELOPER 🧑‍💻", "https://t.me/Warning_MadBoy_is_Here"), Button.url("DEVs", "https://t.me/Wanacoins")]]
  BUTTON += [[custom.Button.inline("REPOSITORYS »»", data="MadBoi")]]
  await tbot.send_file(event.chat_id, ROMEOv3, caption=MadBoy,  buttons=BUTTON)

# ALIVE AND REPOSITORYS TEXT :-
# COPYRIGHT (C) 2021 BY MADBOY, DON'T TRY TO USE IT WITHOUT GETTING PERMISSION FROM @Warning_MadBoy_is_Here (Telegram Acc.) 
# {STILL GOING TO USE WITHOUT PERMISSION, BE READY FOR DMCA}


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"MadBoi")))
async def callback_query_handler(event):

  MBoy = [[Button.url("REPO » ROMEO", "https://github.com/madboy482/Romeo"), Button.url("REPO » ROMEO-3.0", "https://github.com/madboy482/MadBoi")]]
  MBoy +=[[Button.url("DEPLOY » ROMEO", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Fmadboy482%2FRomeo&template=https%3A%2F%2Fgithub.com%2Fmadboy482%2FRomeoP%2FLE"), Button.url("DEPLOY » ROMEO-3.0", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Fmadboy482%2FMadBoi&template=https%3A%2F%2Fgithub.com%2Fmadboy482%2FMadBoi")]]
  MBoy +=[[Button.url("REPO » JOIN CAPTCHA", "https://github.com/madboy482/Join-Captcha"), Button.url("REPO » POKEDEX BOT", "https://github.com/madboy482/Rotom-2.0")]]
  MBoy +=[[Button.url("DEPLOY » POKEDEX BOT", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Fmadboy482%2FRotom-2.0&template=https%3A%2F%2Fgithub.com%2Fmadboy482%2FRotom-2.0P%2FLE"), Button.url("REPO » TELEGRAPH UPLOADER", "https://github.com/madboy482/Telegraph-Uploader")]]
  MBoy +=[[Button.url("BOT » ROMEO", "https://t.me/Romeo1Bot"), Button.url("BOT » ROMEO-3.0", "https://t.me/Romeov3Bot")]]
  MBoy +=[[Button.url("BOT » POKEDEX BOT", "https://t.me/MadBoy_Rotomgram2_Bot"), Button.url("BOT » TELEGRAPH ULOADER", "https://t.me/Romeo1_TelegraphBot")]]
  MBoy +=[[Button.url("BOT » JOIN CAPTCHA", "https://t.me/Romeo1_CaptchaBot"), Button.url("MY ASSISTANT", "https://t.me/MadBoy07Bot")]]
  MBoy +=[[custom.Button.inline("«« ALIVE", data="MadB")]]
  await event.edit(text=f"ALL DETAILS OF REPOS", buttons=MBoy)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"MadB")))
async def callback_query_handler(event):
  global ROMEOv3
  madboy = event.sender.first_name

  MadBy = f"✧✧ ROMEO-3.0 IS UP AND RUNNING SUCCESSFULLY ✧✧\n\n"
  MadBy += f"➥ DATABASE : `ALL DATABASES FUNCTIONING PROPERLY`\n"
  MadBy += f"➥ ROMEO OS : `3.0` [LATEST]\n"
  MadBy += f"➥ USER : `{madboy}`\n"
  MadBy += f"➥ FULLY UPDATED\n"
  MadBy += f"➥ TELETHON : `1.19.5` [LATEST]\n\n"
  MadBy += "THANKS FOR USING ME!!"
  BUTTONS = [[Button.url("🧑‍💻 DEVELOPER 🧑‍💻", "https://t.me/Warning_MadBoy_is_Here"), Button.url("DEVs", "https://t.me/Wanacoins")]]
  BUTTONS += [[custom.Button.inline("REPOSITORYS »»", data="MadBoi")]]
  await event.edit(text=MadBy, buttons=BUTTONS)


@register(pattern=("/repo|#repo"))
async def repo(event):
  await tbot.send_message(event.chat, "REPO FOR ROMEO-3.0 :", buttons=[[Button.url("⚜️REPO⚜️", "https://github.com/madboy482/MadBoi"), Button.url("🔰DEPLOY🔰", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Fmadboy482%2FMadBoi&template=https%3A%2F%2Fgithub.com%2Fmadboy482%2FMadBoi")]])


__help__ = """
 - /alive check bot alive or dead
 - /repo for this bot's repo and deploy option
"""
__mod_name__ = "Alive⚜️"

# ALIVE AND REPOSITORYS TEXT :-
# COPYRIGHT (C) 2021 BY MADBOY, DON'T TRY TO USE IT WITHOUT GETTING PERMISSION FROM @Warning_MadBoy_is_Here (Telegram Acc.) 
# {STILL GOING TO USE WITHOUT PERMISSION, BE READY FOR DMCA}
