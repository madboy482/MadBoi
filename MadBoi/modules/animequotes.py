# Made By @Madepranav On Telegram & Github Id Superboyfan
import random

from telegram import Update
from telegram.ext import CallbackContext, run_async

import MadBoi.modules.animequotesstring as animequotesstring
from MadBoi import dispatcher
from MadBoi.modules.disable import DisableAbleCommandHandler


@run_async
def animequotes(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(animequotesstring.ANIMEQUOTES))


ANIMEQUOTES_HANDLER = DisableAbleCommandHandler("animequotes", animequotes)

dispatcher.add_handler(ANIMEQUOTES_HANDLER)
