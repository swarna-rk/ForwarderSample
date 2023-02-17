from telethon import TelegramClient, events, sync
from telethon.tl.types import InputChannel
import yaml
import sys

client = TelegramClient("Any name here - this will be ur session name", 
                        "api_id - from Telegram Web API registration", 
                        "api_hash  - from Telegram Web API registration")
client.start()


input_channels_entities = []
input_channels_entities.append(InputChannel("Group ID in number", "Group Access Hash")) ## eg : TechJobs 

## How to get group id and access hash - use the below code
## user_input_channel = "https://t.me/techjobboard"
## my_channel = client.get_entity(user_input_channel)
## print(my_channel) - this will print all details about the group 
## The same cannot be done for MPA->Jobs as MPA is a mega group and Jobs is a subgroup within MPA. 
## MPA->Jobs group id was 1898564780_187 and this threw error when used to get entity details.
## MPA Telegram Group id is -1001898564780

output_channel_entities = []
output_channel_entities.append(InputChannel("Group ID in number", "Group Access Hash"))  ## eg: MPA Jobs

@client.on(events.NewMessage(chats=input_channels_entities))
async def handler(event):
    for output_channel in output_channel_entities:
        await client.forward_messages(output_channel, event.message)

client.run_until_disconnected()