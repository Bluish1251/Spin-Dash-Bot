from discord import Intents, Client, Message
from dotenv import load_dotenv
import os
from typing import Final
from responses import get_response

"""
To Setup on other devices, run 'pip3 install discord', then run 'pip install python-dotenv'

Replace the Token with your token, and change responses for your own logic

                                    /####################(                                      
                                 /############################(                 
                           ,########################################.           
                       ,###############################################%        
                    #######################################################     
                 %####################################################.         
 ###########%,,#################################################                
############################################################(                   
 #########################################################,                     
 .##########################*. ./################################%*             
  ,####################*           /##################################%.        
   .#################                #####################################      
    ###, (#########%                  ######################################.   
   /##    ########%                   %#######################################  
   ##%     #######           #####    *########################################.
   ##%     .#####(           #####%   .#################################%%%#(//(
   *##     ######.           %#####.  *##########################               
    %#,   *####              ,#####/  %######################                   
     %#    #####              /####. .##########################%.              
      ##   .####                    #################################           
      ,########,.                 #####################################/        
    #####################%%%%############################################       
      ,(%%%%##############################################################.     
             ,#############################################################     
                 ##########################%*                       .%######    
                     ,%############%(                                                               

"""

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
#Create a '.env' file, and paste your discord token after you put in 'DISCORD_TOKEN='

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

async def send_msg(message: Message, user_message: str) -> None:
    if not user_message:
        print("(Msg was empty because intents weren't enabled)")
        return

    try:
        # Pass the message object to get_response
        response: str = get_response(user_message, message)
        await message.channel.send(response)
    except Exception as e:
        print(e)

@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user or not message.content.startswith('spin'): #checks if it starts with spin
        return
    
    username: str = str(message.author)
    user_msg: str = message.content
    channel: str = str(message.channel)
    print(f'[{channel}] {username}: "{user_msg}"')
    await send_msg(message, user_msg)

def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()