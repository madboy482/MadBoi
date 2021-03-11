import requests
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, run_async

from MadBoi import dispatcher
from MadBoi.modules.disable import DisableAbleCommandHandler


@run_async
def covid(update: Update, context: CallbackContext):
    message = update.effective_message
    text = message.text.split(" ", 1)
    if len(text) == 1:
        r = requests.get("https://corona.lmao.ninja/v2/all").json()
        reply_text = f"**Global Totals** 🦠\n\n__Cases:__ {r['cases']:,}\n__Cases Today:__ {r['todayCases']:,}\n__Deaths:__ {r['deaths']:,}\n__Deaths Today:__ {r['todayDeaths']:,}\n__Recovered:__ {r['recovered']:,}\n__Active:__ {r['active']:,}\n__Critical:__ {r['critical']:,}\n__Cases/Mil:__ {r['casesPerOneMillion']}\n__Deaths/Mil:__ {r['deathsPerOneMillion']}"
    else:
        variabla = text[1]
        r = requests.get(f"https://corona.lmao.ninja/v2/countries/{variabla}").json()
        reply_text = f"**Cases for {r['country']} 🦠**\n\n__Cases:__ {r['cases']:,}\n__Cases Today:__ {r['todayCases']:,}\n__Deaths:__ {r['deaths']:,}\n__Deaths Today:__ {r['todayDeaths']:,}\n__Recovered:__ {r['recovered']:,}\n__Active:__ {r['active']:,}\n__Critical:__ {r['critical']:,}\n__Cases/Mil:__ {r['casesPerOneMillion']}\n__Deaths/Mil:__ {r['deathsPerOneMillion']}"
    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN)


COVID_HANDLER = DisableAbleCommandHandler(["covid", "corona"], covid)
dispatcher.add_handler(COVID_HANDLER)
