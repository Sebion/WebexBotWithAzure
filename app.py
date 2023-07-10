from webex_bot.webex_bot import WebexBot
from gpt import gpt

bot = WebexBot("ZGU5MjEwZjctNGEwYi00MzlmLWJlZDAtODJiOTAyZTdlNGI0YTFlMmZjZWItNjNi_PE93_b6c69aac-d199-4628-980a-d750015d67a5")
bot.commands.clear()
bot.add_command(gpt())
bot.help_command = gpt()
bot.run()
