#    Copyright (C) 2020-2021 by @LEGENDX22 AND PROBOYX

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

#    Don't dare to remove the credits, else be ready for DMCA.
#    Changed some texts for ROMEO-3.0

#    Credits to :-
#    ➥ LEGENDX
#    ➥ PROBOY
#    ➥ MADBOY

# +-+ +-+ +-+ +-+    +-+ +-+ +-+ +-+    +-+ +-+ +-+ +-+ +-+ +-+ +-+
# |K| |A| |N| |G|    |W| |I| |T| |H|    |C| |R| |E| |D| |I| |T| |S|
# +-+ +-+ +-+ +-+    +-+ +-+ +-+ +-+    +-+ +-+ +-+ +-+ +-+ +-+ +-+


from MadBoi import telethn as bot
import os
import re
import urllib
from math import ceil

import requests
from telethon import Button, custom, events, functions
from youtubesearchpython import SearchVideos

@bot.on(events.InlineQuery(pattern=r"yt (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    k = event.pattern_match.group(1)
    if ";" in k:
         testinput,legendx = event.pattern_match.group(1).split(";")
    else:
         testinput = event.pattern_match.group(1)
         legendx = 5
    urllib.parse.quote_plus(testinput)
    lund = event.sender_id
    if lund == lund:
        results = []
        search = SearchVideos(f"{testinput}", offset=1, mode="dict", max_results=int(legendx))
        mi = search.result()
        moi = mi["search_result"]
        if search == None:
            resultm = builder.article(
                title="No Results...",
                description="Try Again with Correct Spelling...",
                text="**No Matching Found...**",
                buttons=[
                    [Button.switch_inline("Search Again", query="yt ", same_peer=True)],
                ],
            )
            await event.answer([resultm])
            return
        for mio in moi:
            mo = mio["link"]
            thum = mio["title"]
            mboy = mio["id"]
            thums = mio["channel"]
            td = mio["duration"]
            tw = mio["views"]
            kekme = f"https://img.youtube.com/vi/{mboy}/hqdefault.jpg"
            okayz = f"**➥ Title :** `{thum}` \n**➥ Link :** {mo} \n**➥ Channel :** `{thums}` \n**➥ Views :** `{tw}` \n**➥ Duration :** `{td}`"
            hmmkek = f"➥ Channel : {thums} \n➥ Duration : {td} \n➥ Views : {tw}"
            results.append(
                await event.builder.article(
                    title=thum,
                    description=hmmkek,
                    text=okayz,
                    buttons=Button.switch_inline(
                        "Search Again...", query="yt ", same_peer=True
                    ),
                )
            )
        await event.answer(results)

__mod_name__="YouTube ▶️"
__help__ = """
 - `@Romeov3Bot yt <search your query> ;8`
    Use ; this as result stopper
"""
