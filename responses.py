from random import choice, randint
from discord import Message
"""
0.0.1a - Basic Commands Added

Need to add command list, and more commands
"""
def get_response(user_input:str, message: Message) -> str:
    lowered: str = user_input.lower()
    
    username: str = str(message.author.display_name)
    user_msg: str = message.content
    channel: str = str(message.channel)

    #Put in own logic !!!
    if lowered == '':
        return "Say something"
    elif 'hi' in lowered:
        return "hi"
    elif 'roll dice' in lowered:
        return f'you rolled: {randint(1,6)}'
    elif "what's my name" in lowered:
        return f'{username}'
    elif "what's the channel" in lowered:
        return f'{channel}'
    elif "what's my msg" in lowered:
        return f'{user_msg}'
    
    elif "quit" in lowered:
        return 
    else:
        return choice (['Idk','what','try again'])