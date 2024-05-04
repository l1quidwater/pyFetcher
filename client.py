import discord
import json
import os
import sys
import asyncio
import shutil
from pystyle import Colors, Colorate, Center, Box
from discord.ext import commands

os.system('cls' if os.name == 'nt' else 'clear')

def header():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    def read_log_file():
        with open("var/log.txt", 'r') as file:
            file_text = file.read()
            return file_text
    
    print(Colorate.Color(Colors.purple, Center.XCenter(read_log_file()), True))
    print(Colorate.Color(Colors.purple, Center.XCenter(Box.DoubleCube("v.0.0.1 | created by adam93 | github.com/adaminit")), True))
    print("\n\n")

def respond(text, state):
    color = {
        "Good": Colors.purple,
        "Error": Colors.red,
    }.get(state, Colors.white)
    
    center = Center.XCenter(text)
    te = Colorate.Color(color, center)

    print(te)

config = json.load(open("./var/config.json"))

async def main(user_ids):
    client = discord.Client()

    @client.event
    async def on_ready():
        for user_id in user_ids:
            try:
                user = await client.fetch_user(int(user_id))
                
                def if_banner(user):
                    try:
                        if user.banner.url:
                            return True
                        else:
                            return False
                    except:
                        return False
                        
                if if_banner(user):
                    ta = Center.XCenter("Scrape Results")
                    print(Colors.purple, ta)
                    respond(f"\nUsername: {user.global_name}\nUser Id: {user.id}\nCreation: {user.created_at}\nAvatar URL: {user.avatar.url}\nBanner URL: {user.banner.url}", "Good")
                else:
                    ta = Center.XCenter("Scrape Results")
                    print(Colors.purple, ta)
                    respond(f"\nUsername: {user.global_name}\nUser Id: {user.id}\nCreation: {user.created_at}\nAvatar URL: {user.avatar.url}", "Good")
            except:
                respond("Error, please make sure all provided IDs are valid.", "Good")

        await asyncio.sleep(1)
        respond("Exiting..", "Good")
        await client.close()
        await asyncio.sleep(0.5)
        sys.exit()

    await client.start(config["TOKEN"])


if __name__ == '__main__':
    header()
    respond("Enter User IDs to scrape (separated by commas):\n", "Good")
    user_ids_input = input().split(',')
    user_ids = [uid.strip() for uid in user_ids_input]
    asyncio.run(main(user_ids))
