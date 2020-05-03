#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import yaml
from telegram.ext import Updater, MessageHandler, Filters

with open('credential') as f:
	credential = yaml.load(f, Loader=yaml.FullLoader)

tele = Updater(credential['bot_token'], use_context=True) # @contribute_bot
debug_group = tele.bot.get_chat(-1001198682178)

@log_on_fail(debug_group)
def command(update, context):
	msg = update.effective_message
	file = msg.document
	file = file.get_file().download('tmp/')
	cuts = list(pic_cut.cut(file))
	os.system('rm %s' % file)
	
tele.dispatcher.add_handler(MessageHandler(Filters.document, command))
tele.start_polling()
tele.idle()