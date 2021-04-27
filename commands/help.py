from discord import Color, Embed, Message
from os import getenv

main_globals = frozenset(['commands'])
help_message = "Displays this message"
presence = '%shelp' % getenv('CMD_SYMBOL')

_messages = []
_description = '\
Here\'s a list of commands and what they do. \
'

async def on_command(message: Message, **kwargs):
  if len(_messages) == 0:
    assert kwargs.get('commands') is not None

    for command, module in sorted(kwargs.get('commands').items(), key=lambda item: item[0]):
      # add as a tuple: ('command', 'help message')
      _messages.append(('%s%s' % (getenv('CMD_SYMBOL'), command), getattr(module, 'help_message', 'No help found!')))

  embed = Embed(title='Help', color=Color.blue(), description=_description)
  embed.add_field(name='Command', value='\n'.join(message[0] for message in _messages))
  embed.add_field(name='Message', value='\n'.join(message[1] for message in _messages))
  
  await message.reply(embed=embed)
