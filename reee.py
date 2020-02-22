import discord
from discord.ext import commands
import datetime
import random
import nacl
import os
import json
import http.client


help_file_name = 'Help.txt'

def logg(msg):
    time = datetime.datetime.now()
    time_stamp = time.strftime("%H:%M:%S - ")
    
    log_file = open("Logs_" + str(time.strftime("%d-%m-%y" )) + ".txt" ,"a")
    log_file.write(time_stamp + msg + "\n")
    log_file.close()
    
    print(time_stamp + msg)
    send(time_stamp + msg)

def send(message):
    try:
 
        # your webhook URL
        webhookurl = "https://discordapp.com/api/webhooks/679003014945701935/gj2nc7jnTqaHqqw3Cb9FQN2-g1td_miGVY8QEbg9_4RAb6gN8zi8OqS41wJsHHHGcpKF"
     
        # compile the form data (BOUNDARY can be anything)
        formdata = "------:::BOUNDARY:::\r\nContent-Disposition: form-data; name=\"content\"\r\n\r\n" + message + "\r\n------:::BOUNDARY:::--"
      
        # get the connection and make the request
        connection = http.client.HTTPSConnection("discordapp.com")
        connection.request("POST", webhookurl, formdata, {
            'content-type': "multipart/form-data; boundary=----:::BOUNDARY:::",
            'cache-control': "no-cache",
            })
      
        # get the response
        response = connection.getresponse()
        result = response.read()
      
        # return back to the calling function with the result
    
        return result.decode("utf-8")
    except :
        pass
 



def isree(message):

    try:
        l = []
        re_point = 0
        
        for i in (str(message.content).lower()):
            l.append(i)

        if l[0] == "r" or l[0] == "R":
            re_point = re_point + 1
            
        if l[1] == "e" or l[0] == "E":
            re_point = re_point + 1
            

        l.remove(l[0])
       
        for a in l:
            
            if a == "e" or a == "E":
                pass
            else:
               
                re_point = 0
                break
    except(IndexError):
        return False

        
        
    if re_point < 2:
        
        return False
    else:
        return True
    

#getting the prefix specific for the server
def get_prefix(client, prefix_message):
    with open('prefix.json', 'r') as f:
        prefix = json.load(f)

    return prefix[str(prefix_message.guild.id)]

#setting default prefix for the server
def set_default_prefix(guild):
    with open('prefix.json', 'r') as f:
        prefix = json.load(f)

    prefix[str(guild.id)] = '.'

    with open('prefix.json', "w") as f:
        json.dump(prefix, f, indent = 4)

#cleaning the json file
def remove_server_from_prefix_json(guild):
    with open('prefix.json', 'r') as f:
        prefix = json.load(f)

    prefix.pop(str(guild.id))

    with open('prefix.json', "w") as f:
        json.dump(prefix, f, indent = 4)


#getting channel for re
async def get_channel(message):

    try:
        with open('channel.json', 'r') as f:
            channel = json.load(f)
        
        return channel[str(message.guild.id)]
    except:
       await message.channel.send("I am confused, please use the command 'prefix + setre + channel for re ' -> eg. '!setre general' to tell me where to reeeee")
       logg("Reee bot is confused in '" + str(message.guild) + "' server")
        
    
    



#setting client
client = commands.Bot(command_prefix = get_prefix ,case_insensitive = False)

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
    set_default_prefix(guild)
   

#events that happen when the bot is removed froma server
@client.event
async def on_guild_remove(guild):
    logg("Left '" + str(guild) + "'")
    remove_server_from_prefix_json(guild)

@client.command()
async def cdp(ctx, pref):
    with open('prefix.json', 'r') as f:
        prefix = json.load(f)

    prefix[str(ctx.guild.id)] = pref

    with open('prefix.json', "w") as f:
        json.dump(prefix, f, indent = 4)

    await ctx.send("Changed prefix to '" + str(pref) + "'")
    logg("Prefix changed to '" + str(pref) + "'")


@client.command()
async def setre(ctx, ch):

    ch = ch.replace("#","")
    ch = ch.replace("<","")
    ch = ch.replace(">","")

    
    
    
    with open('channel.json', 'r') as f:
        channel = json.load(f)

    channel[str(ctx.guild.id)] = str(ch)

    with open('channel.json', "w") as f:
        json.dump(channel, f, indent = 4)

    await ctx.send("Everything is set - please re in the channel you have set")
    logg("Reeee bot was set in '" + str(ctx.guild) + "' server")

@client.command(aliases = ['r'])
async def report(ctx, report):

    try:
        time = datetime.datetime.now()
        time_stamp = time.strftime("%H:%M:%S - ")
        myid = '<@377844133576048642>'
        msg = ('  %s ' % myid) + time_stamp + str(ctx.guild) + " - " + str(ctx.message.author.name)+ " - " + str(ctx.message.content)
        send(msg)
        await ctx.send("You have subbmitted your bug report")
    except:
        await ctx.send("You forgot to include a msg")
    

#ping command
@client.command()
async def ping(ctx):
    ping_msg = f'Pong! {round(client.latency * 1000)}ms'
    await ctx.send(ping_msg)
    logg("Recieved command 'ping' -> replied with '" + ping_msg + "'")


@client.command(aliases = ['h'])
async def help(ctx):
    he = open("help.txt","r+")
    he_l = he.readlines()

    help_msg = ""

    for i in he_l:
        i.strip()
        help_msg = help_msg + i

    await ctx.send(help_msg)


@client.event
async def on_message(message):
    # await message.channel.send("Nice meme Eugene")
    
    if message.author.bot:
        return
    
    msg = str(message.content).lower()
    count_e = 0
    count_r = 0
    over_char_limit = False

    
       
    n_channel = await get_channel(message)
    
    chnl = message.channel
    chnl = str(chnl)
    chnl = chnl.replace("#","")
    chnl = chnl.replace("<","")
    chnl = chnl.replace(">","")
    if str(chnl) == n_channel or str(message.channel.id) == n_channel:

        for i in msg:
            if i == "e":
                count_e = count_e + 1

            if i == "r":
                count_r = count_r + 1

        if isree(message):


       

            if count_e > 499:
                reply = "r" +  str("E"*1999)
                reply2 = "E" +  str("E"*1999)
                logg("re is over char limit")
                over_char_limit = True
                

            else:
                
                if count_r == 0:
                    
                    if count_e == 0:
                        reply = "r" +  ("E"*(count_e*4)) + "E"
                    else:
                        
                        reply = "r" +  ("E"*(count_e*4))
                else:
                    
                    if count_e == 0:
                        reply = "r" +  ("E"*(count_e*4)) + "E"
                       
                    else:
                        
                        reply = "r" +  ("E"*(count_e*4))
                      

            
            logg("Multiplied by 4 '" + str(message.content) + "' in '" + str(message.guild) + "' from '" + str(message.author.name) + "'")
            await message.channel.send("I can do better") 
            await message.channel.send(reply)
            
            if over_char_limit:
                
                await message.channel.send(reply2)
             
            return

        else:
            
            #await message.channel.send("Not a re try again")
            logg("not a reee" + "' in '" + str(message.guild) + "' from '" + str(message.author.name) + "'")
            
        

          

    await client.process_commands(message)
 
    

#running the client
client.run('')
