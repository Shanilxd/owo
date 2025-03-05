import os as brutality_ghosty

brutality_ghosty.system("pip install discord.py==1.7.3")
brutality_ghosty.system("pip install colorama")
brutality_ghosty.system(
    "sleep 2 && clear >/dev/null 2>&1 &"
    if brutality_ghosty.name == "posix"
    else "timeout /t 2 >nul 2>&1 && cls"
)
import json as ghostop
import random as ghostyjija
from colorama import Fore, Style, init
import discord
from discord.ext import commands, tasks
import time
import sys
import re
import asyncio as made_by_ghosty
import winsound


ghostyop = discord.Intents.all()
GhoStyyy = "."
ghosty = commands.Bot(
    command_prefix=GhoStyyy, case_insensitive=True, self_bot=True, intents=ghostyop
)
ghosty.remove_command("help")

running = True
pray_loop_running = True
last_gem_check = 0

print(
    f"""{Fore.BLUE}

           ▒▒                    ▒▒            ▒▒       ▒▒▒
        ▒▒▒▒▒▒▒   ▒▒▒     ▒▒▒▒ ▒▒▒▒▒▒▒▒        ▒▒▒▒     ▒▒▒▒  ░░░░░░░░
      ▒▒▒▒████▒▒ ▒▒█▒▒  ▒▒▒█▒▒▒▒░█████▒        ▒█▒▒   ▒▒▒██▒ ░░██████░
     ▒▒▒▒██░░██▒▒▒██▒▒ ▒▒░██▒░▒██░░░░█▒        ▒██▒▒ ▒▒██░▒▒ ░█░░░░░█░
     ▒▒██░░░░██▒▒██▒▒▒ ▒░██▒▒██░░░░░░█▒        ▒▒█▒▒▒▒██▒▒▒  ░█░░░░░█░
    ▒▒██░░█░░█▒▒▒█▒▒▒▒▒▒░█▒▒▒█░░░█░░██▒         ▒█▒▒▒██▒▒    ░░░█████░
    ▒▒█░░░░░░█▒▒█░░██░▒░█▒▒ ▒█░░░░░█▒▒▒         ▒░█▒██▒▒     ░░░░░░██░
    ▒▒█░░░░██▒▒▒████████▒▒  ▒██░░███▒▒          ▒▒██░▒       ░█░░░░░█░
     ▒██████▒▒▒███▒▒▒██▒▒   ▒▒████▒▒▒            ▒█▒▒        ░░██████░
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒     ▒▒▒▒▒▒              ▒▒▒          ░░░░░░░
     ▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒      ▒▒▒▒▒               ▒▒▒
               ▒▒   ▒▒        ▒▒                 ▒▒
                                                             BETA VERSION{Style.RESET_ALL}"""
)

init(autoreset=True)
print(f"{Fore.LIGHTRED_EX}\n\n > Made By GhoSty{Style.RESET_ALL}")

@ghosty.event
async def on_ready():
    print(
        f"{Fore.LIGHTRED_EX} > OwO Farm v3 Connected To:{Style.RESET_ALL}",
        f"{Fore.LIGHTGREEN_EX}{ghosty.user}{Style.BRIGHT}{Style.RESET_ALL}",
    )
    print(f"{Fore.LIGHTRED_EX} > Minor Updates And Fixes{Style.RESET_ALL}")




@ghosty.command(aliases=["h"])
async def help(ctx):
    ghosty_help = """
    # 🤑 GhoSty OwO Farm V3 🤑 
Prefix: `.`

**__Main__**
 🌟 Start: *Starts The AutoBot*
 🛑 Stop: *Stops The AutoBot*

**__Features__**
 ⚠ Ban Bypass
 🚨 Auto Detects OwO Warnings
 ⏱ Auto Cut After 1 Warning
 💎 Auto Use Gems 
 🏹 Fast And Secure

**__Made with 💖 and 🧠 by GhoSty__** 
"""
    await ctx.send(ghosty_help)  





async def parse_gems(inventory_message):
    rarity_order = ['f', 'l', 'm', 'e', 'r', 'u', 'c']
    gems_by_tier = {
        '1': [],
        '2': [],
        '3': [],
        '4': []
    }
    lines = inventory_message.split('\n')
    for line in lines:
        for tier in ['1', '2', '3', '4']:
            for rarity in rarity_order:
                pattern = fr'`(\d+)`<:({rarity}gem{tier}):\d+>'
                match = re.search(pattern, line)
                if match:
                    gem_number = match.group(1)  
                    gems_by_tier[tier].append((rarity, gem_number))
    for tier in gems_by_tier:
        gems_by_tier[tier].sort(key=lambda x: rarity_order.index(x[0]))
    selected_gems = []
    for tier in ['1', '2', '3', '4']:
        if gems_by_tier[tier]:
            selected_gems.append(gems_by_tier[tier][0][1])
    
    return selected_gems

async def do_gem_check(ctx):
    await ctx.send("owo inventory")
    await made_by_ghosty.sleep(3)  
    
    try:
        latest_messages = await ctx.channel.history(limit=2).flatten()
        
        for message in latest_messages:
            if message.author.id == 408785106942164992:  
                if "inventory" in message.content.lower():
                    gem_numbers = await parse_gems(message.content)
                    if gem_numbers: 
                        use_command = "owo use " + " ".join(gem_numbers)
                        await ctx.send(use_command)
                        await made_by_ghosty.sleep(3)
                    else:
                        print("No gems found")
                    break
    except Exception as e:
        print(f"Error in gem check: {e}")
        import traceback
        print(traceback.format_exc())


async def check_warning(ctx):
    global running
    try:
        messages = await ctx.channel.history(limit=10).flatten()
        
        for msg in messages:
            msg_content = str(msg.content).lower()
      
            checkph = [
                "captcha",
                "Please complete thi​s wit​hin 1​0 m​inutes o​r i​t m​ay r​esult i​n a​ ba​n!",
                "P​lease comple​te you​r c​aptcha t​o ver​ify th​at y​ou ar​e huma​n!",
                "a​re y​ou a​ rea​l hu​man?"
            ]
            if any(phrase.lower() in msg_content for phrase in checkph):
                try:
                    for _ in range(15):
                        winsound.Beep(1000, 500)
                        await made_by_ghosty.sleep(0.1)
                except Exception as e:
                    print(f"Sound error: {e}")
            
                global running
                running = False
                
                await ctx.send("⚠ Warning Detected! 🛑 Stopping The Process | Type .start again to re-start grinding")
                print("⚠ Warning Detected! 🛑 Stopping The Process | Type .start again to re-start grinding")
                return True
        return False
    except Exception as e:
        print(f"Warning check error: {e}")
        return False

@ghosty.command()
async def start(ctx):
    global running, last_gem_check
    running = True
    last_gem_check = time.time()
    last_command = None 

    while running:
        try:
            current_time = time.time()

            if current_time - last_gem_check >= 480:
                warning_detected = await check_warning(ctx)
                if warning_detected or not running:
                    break
                await do_gem_check(ctx)
                last_gem_check = current_time
                continue

            commands = [
                "owoh", "owo pray", "owo h", "owo b", "owob", "owoh", "owo h",
                ghostyjija.choice(["owo cf 1", "owoz", "owo s 1", "owo owo", "owoq"]),
                ghostyjija.choice(["owo pup", "owo army", "owo piku", "owo run"]),
                ghostyjija.choice(["owo punch <@408785106942164992>", "owo roll"])
            ]
            command = ghostyjija.choice(commands)

            while command == last_command:
                command = ghostyjija.choice(commands)
            last_command = command

            await ctx.send(command)

            await made_by_ghosty.sleep(0.3)
            warning_detected = await check_warning(ctx)
            if warning_detected or not running:
                break

            await made_by_ghosty.sleep(ghostyjija.uniform(6.5, 21.0))
            if ghostyjija.random() < 0.05: 
                await made_by_ghosty.sleep(ghostyjija.uniform(300, 600))  

        except Exception as e:
            print(f"Error in main loop: {e}")



@ghosty.command()  
async def stop(ctx):
    global running  
    await ctx.send(
        "🛑 Stopping | Type .start again to re-start grinding"
    )  
    running = False





with open("config.json", "r") as config_file:  
    config = ghostop.load(config_file)  

ghostyopaf = config["TOKEN"]  
ghosty.run(ghostyopaf, bot=False)
