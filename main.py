import discord
import importlib
import os
import sys

bot = discord.Client()
commands = {}
__message_times = {}

@bot.event
async def on_ready():
  bot.loop.create_task()


@bot.event 
async def on_message(message: discord.Message):
  if message.author.id == bot.user.id:
    return
  
  if len(message.attachments) > 0:
    [author, description] = message.content.split('\n')
    embed = discord.Embed(color=discord.Color.blue(), title=message.attachments[0].filename.split('.')[0].replace('_', ' '), description=description)
    embed.set_footer(text='Art contest 1 - 2021/04/02')
    embed.set_image(url=message.attachments[0].url)
    embed.set_author(name=author)
    await message.channel.send(embed=embed)
    await message.delete()

  # if message.content.startswith(os.getenv('CMD_SYMBOL')) and len(message.content) > len(os.getenv('CMD_SYMBOL')):
  #   # test for time
  #   if not sent_too_soon(message):
  #     await run_command(message)


async def run_command(message: discord.Message):
  # ".ping hey" -> "ping hey" -> ["ping", "hey"]
  keywords = message.content[1:].split()
  # ["ping", "hey"] -> "ping"
  module = commands.get(keywords[0])

  if module:
    # get function to run the command
    command_func = getattr(module, 'on_command', None)
    if command_func:
      requirements = getattr(module, 'main_globals', [])
      kwargs = {r: globals()[r] for r in requirements}
      await command_func(message, **kwargs)


def prep_commands():
  for file_name in os.listdir(os.getcwd() + '/commands'):
    if not file_name.endswith('.py'):
      continue
    trimmed_name = file_name[:-3]  # ping.py -> ping
    
    # import
    module = importlib.import_module('commands.' + trimmed_name)
    commands[getattr(module, 'alias', trimmed_name)] = module
    
if __name__ == '__main__':
  prep_commands()
  bot.run(os.environ.get('DISCORD_TOKEN'))
