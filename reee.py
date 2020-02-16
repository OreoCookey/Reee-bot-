import discord
from discord.ext import commands
import datetime
import random
import nacl
import os
import json


help_file_name = 'Help.txt'

def logg(msg):
    time = datetime.datetime.now()
    time_stamp = time.strftime("%H:%M:%S - ")
    
    log_file = open("Logs_" + str(time.strftime("%d-%m-%y" )) + ".txt" ,"a")
    log_file.write(time_stamp + msg + "\n")
    log_file.close()
    
    print(time_stamp + msg)
    



#setting client
client = commands.Bot(command_prefix = '<' ,case_insensitive = False)

#removing stock help command
client.remove_command('help')

#getting bot ready
@client.event
async def on_ready():
    logg("Bot initialized")

#event when removed from server
@client.event
async def on_guild_join(guild):
    logg("Joined '" + str(guild) + "'")
   

#events that happen when the bot is removed froma server
@client.event
async def on_guild_remove(guild):
    logg("Left '" + str(guild) + "'")


#ping command
@client.command()
async def ping(ctx):
    ping_msg = f'Pong! {round(client.latency * 1000)}ms'
    await ctx.send(ping_msg)
    logg("Recieved command 'ping' -> replied with '" + ping_msg + "'")


def get_banned_words():
    f = open("banned_words.txt", "r+")
    w = f.readlines()
    return w



@client.event
async def on_message(message):
    # await message.channel.send("Nice meme Eugene")
    if message.author.bot:
        return
    msg = str(message.content).lower()
    count_e = 0
    count_r = 0

    
        
        
    
    chnl = message.channel
    if str(chnl) == "👿reeeeeeeeeeeeeeeeeeee":

        for i in msg:
            if i == "e":
                count_e = count_e + 1

            if i == "r":
                count_r = count_r + 1
        reply = ""
        
        if count_r == 0:
            if count_e == 0:
                reply = "r" +  ("e"*(count_e*4)) + "e"
            else:
                
                reply = "r" +  ("e"*(count_e*4))
        else:
           if count_e == 0:
                reply = "r" +  ("e"*(count_e*4)) + "e"
           else:
                
                reply = "r" +  ("e"*(count_e*4))

        
        
        await message.channel.send(reply)
        await message.channel.send("I bet tou can't beat me ;)")
        logg("Doubled '" + str(message.content) + "' in '" + str(message.guild) + "' from '" + str(message.author.name) + "'")
        return
        
        

          

    await client.process_commands(message)
 
    

#running the client
client.run('Njc4NzMwNjE5Nzk4NDIxNTA0.XknDQQ.Lz6bjyD5MguTaJyNRy8PBCK8fJI')
