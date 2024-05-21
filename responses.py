from random import choice, randint
from discord import Message
from pokemon import pokemon_name
from anime_ref import jojo_ref
"""
0.0.2a - Pokemon, and Anime Ref added

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
    
    # elif "temp" in lowered:
    #     return "https://tenor.com/view/ora-star-platinum-jo-jos-bizarre-adventure-jojo-gif-5505650"
    
    elif "pokemon help" in lowered:
        return pokemon_name(lowered[17:])
    
    elif "jojo reference" in lowered or "jojo's reference" in lowered:
        return jojo_ref()
    
    elif "command list" in lowered: # Keep up to date!!!!
        return f"# [ COMMANDS FOR SPINBOT ] \n **-hi** \n **-dice**\n **-what's my name** \n **-what's the channel** \n **-what's my msg**"
    
    elif "quit" in lowered:
        return 
    else:
        return choice (['Idk','what','try again'])