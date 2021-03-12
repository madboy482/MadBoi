# COPYRIGHT (C) 2021 BY LEGENDX22, PROBOYX AND MADBOY

"""
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
            MADE BY LEGENDX, PROBOY AND MADBOY
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

# MYINFO TEXT :-
# COPYRIGHT (C) 2021 BY MADBOY, DON'T TRY TO USE IT WITHOUT GETTING PERMISSION FROM @Warning_MadBoy_is_Here (Telegram Acc.) 
# {STILL GOING TO USE WITHOUT PERMISSION, BE READY FOR DMCA}

from telethon import custom, events, Button
import os,re
from MadBoi import telethn as bot
from MadBoi import telethn as tgbot
from MadBoi.events import register 
@register(pattern="/myinfo|#myinfo")
async def mboy(event):
  button = [[custom.Button.inline("CHECK 👀",data="info")]]
  await bot.send_message(event.chat, "YOUR INFO",buttons=button)

# MYINFO TEXT :-
# COPYRIGHT (C) 2021 BY MADBOY, DON'T TRY TO USE IT WITHOUT GETTING PERMISSION FROM @Warning_MadBoy_is_Here (Telegram Acc.) 
# {STILL GOING TO USE WITHOUT PERMISSION, BE READY FOR DMCA}

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"info")))
async def callback_query_handler(event):
  try:
    BOI = event.sender_id
    MAD = await bot.get_entity(BOI)
    MadBoy = "✧✧ YOUR DETAILS BY ROMEO-3.0 ✧✧\n\n"
    MadBoy += f"➥ FIRST NAME : {MAD.first_name} \n"
    MadBoy += f"➥ LAST NAME : {MAD.last_name}\n"
    MadBoy += f"➥ BOT? : {MAD.bot} \n"
    MadBoy += f"➥ RESTRICTED? : {MAD.restricted} \n"
    MadBoy += f"➥ USER ID : {BOI}\n"
    MadBoy += f"➥ USERNAME : {MAD.username}\n"
    await event.answer(MadBoy, alert=True)
  except Exception as e:
    await event.reply(f"{e}")
    
# MYINFO TEXT :-
# COPYRIGHT (C) 2021 BY MADBOY, DON'T TRY TO USE IT WITHOUT GETTING PERMISSION FROM @Warning_MadBoy_is_Here (Telegram Acc.) 
# {STILL GOING TO USE WITHOUT PERMISSION, BE READY FOR DMCA}
