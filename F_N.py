#!/usr/bin/python3.6
import discord
import asyncio
from discord.ext import commands
from collections import defaultdict
import random
import time
import json
import sqlite3
import pyttsx3
import os
import sys
import subprocess
from textgenrnn import textgenrnn
import tensorflow
TEST_MODE = True
bot = commands.Bot(command_prefix='++')
TOKEN = 'NDQ1NzE5Njc5NjkyOTYzODQx.DpqYyg.ZxFnQ2gWgDAVtaNc8BLSBPP9MLw'
prefix = '++'
messages = defaultdict(lambda: 0)
client = discord.Client()
global leaderlord
leaderlord = 0
global hhh
global winning_boi
winning_boi = 'Default cunt'
randomhexcolors = [0x00ff15,
                   0xeeff00,
                   0x001dff,
                   0xff00f6,
                   0xff002a,
                   0x9000ff]
global Disconnect_bot
Disconnect_bot = False
hhh = 0
kids = []
textgen = textgenrnn()
temp_for_bot = 1.5
dm_jenqa = True

def cmti(usermention):
    return usermention.replace('<', '').replace('>', '').replace('!', '').replace('@', '')

async def remindlater(amessage, user, number, messagecon):
    await asyncio.sleep(int(number))
    await client.send_message(amessage.channel, f'{user.mention} {messagecon}')

async def traindatabase(hhh, temp_bot):
    textgen.train_from_file('Database.txt', num_epochs=1)
    start_time = time.time()
    kek = textgen.generate(1, temperature=1, return_as_list=True)
    await client.send_message(hhh, str(kek).replace("'",'').replace('[', '').replace(']','') + '\n')
    with open('Database.txt', 'r+') as f:
        f.readline()
        data = f.read()
        f.seek(0)
        f.write(data)
        f.truncate()
        with open("Database.txt") as fp:
            for i, line in enumerate(fp):
                if i == 6:
                    lines = fp.readlines()
                    lines = lines[:-1]
                    break
    print("--- %s seconds ---" % (time.time() - start_time))
    print(kek)

async def traindatabase2(hhh, temp_bot):
    textgen.train_from_file('Database.txt', num_epochs=1)
    start_time = time.time()
    kek = textgen.generate(1, temperature=1.5, return_as_list=True)
    await client.send_message(hhh, str(kek).replace("'",'').replace('[', '').replace(']','') + '\n')
    with open('Database.txt', 'r+') as f:
        f.readline()
        data = f.read()
        f.seek(0)
        f.write(data)
        f.truncate()
        with open("Database.txt") as fp:
            for i, line in enumerate(fp):
                if i == 6:
                    lines = fp.readlines()
                    lines = lines[:-1]
                    break
    print("--- %s seconds ---" % (time.time() - start_time))
    print(kek)

if not discord.opus.is_loaded():
    discord.opus.load_opus()

engine = pyttsx3.init()



@client.event
async def on_message(message):
    if message.author != client.user:
        randm = [f"Okay then {message.author}, fucking cunt",
        f"No fuckass cunt bitch",
        f"What the actual fuck {message.author}"
        ]

        with open('jenqadm.txt', 'r') as x:
            dm_jenqa_fin = x.read()
            print(dm_jenqa_fin)
            if dm_jenqa_fin == 'T':
                dm_jenqa = True
            elif dm_jenqa_fin == 'F':
                dm_jenqa = False

        if message.content.startswith('+=jenqadm'):
            if message.author.id == '267068037264441344':

                if dm_jenqa == False:
                    dm_jenqa = True
                    with open('jenqadm.txt', 'w') as p:
                        p.write('T')
                    await client.send_message(message.channel, 'Enabled Dm')
                elif dm_jenqa == True:
                    dm_jenqa = False
                    with open('jenqadm.txt', 'w') as p:
                        p.write('F')
                    await client.send_message(message.channel, 'Disabled Dm')
                return dm_jenqa
            else:
                await client.send_message(message.channel, "Bro you ain't jenqa")

        #Dms Cracc (me)
        msg = f'{message.author}: {message.content}'
        crac = await client.get_user_info('399392841308045312')
        await client.send_message(crac, msg)
        #Dms jenqa
        if dm_jenqa == True:
            msg = f'{message.author}: {message.content}'
            jenqa = await client.get_user_info('267068037264441344')
            await client.send_message(jenqa, msg)


        if message.content == '+=info': #This outputs a static message
            await client.send_message(message.channel, "")


        elif message.content == '+=dm':
            usaa = await client.get_user_info(f'{message.author.id}')
            await client.send_message(usaa, random.choice(randm))

        #Time for the leaderboard thing

        if message.content == '+=Leaderboardreset':
            if message.author.id == '399392841308045312':
                leaderboard=discord.Embed(title="Total message score", description="Please speak kids", color=0x00ff00)
                leaderboard.add_field(name="Fucking speak wtf", value=69, inline=False)
                global hhh
                hhh = await client.send_message(client.get_channel('553352042635329537'), embed=leaderboard)
                with open('message.id.txt', 'w') as x:
                    x.write(str(hhh))
                    return hhh
                h = -1
                global kids
                kids = []
                server = client.get_server(id="245194375670267904")
                for member in server.members:
                    messages[member] = 0
                    kids += ({'user': str(member), 'messages': messages[member.id]}, )
                with open('json_fuckfest.txt', 'w', encoding='UTF-8') as erased:
                    erased.write('')
                return hhh
            else:
                await client.send_message(message.channel, 'Lmao no')
        server = client.get_server(id="245194375670267904")
        with open('json_fuckfest.txt', 'w', encoding='UTF-8') as x:
            x.write('')

        with open('json_fuckfest.txt', 'a', encoding='UTF-8') as databased:
            for member in server.members:
                if member.id == message.author.id:
                    if not member.bot:
                        messages[member.id] += 1
                        print(f'{member} = {messages[member.id]}')
                        kids += ({'user': str(member), 'messages': messages[member.id]}, )
                        databased.write(f'{member.id} {messages[member.id]}\n')
                else:
                    kids += ({'user': str(member), 'messages': messages[member.id]}, )
                    databased.write(f'{member.id} {messages[member.id]}\n')


        if message.content == '+=myplace':
            for x in sortkids:
                hm += 1
                c = json.dumps(x)
                ff = json.loads(c)
                if message.author == ff['user']:
                    if hm == 0:
                        await client.send_message(message.channel, 'You are in 1st')
                    if hm == 1:
                        await client.send_message(message.channel, 'You are in 2nd')
                    if hm == 2:
                        await client.send_message(message.channel, 'You are in 3rd')
                    else:
                        rh = hm
                        rh += 1
                        await client.send_message(message.channel, f'You are in {x}th place')
                        return



        if message.content.startswith('+=tempchange'):
            if message.author.id == '399392841308045312':
                temp_for_list = message.content.split()
                print(temp_for_list)
                temp_for_bot == temp_for_list[1]
                await client.send_message(message.channel, f'Successfully changed temp to {temp_for_list[1]}')
                return temp_for_bot


        if message.content.startswith('+=setscore') == True:
            if message.channel.id == '389803272413773825':
                settingscore = message.content.split()
                print(settingscore[1])
                crac = await client.get_user_info(cmti(settingscore[1]))
                thekidscore2 = int(settingscore[2])
                print(thekidscore2)

                for member in server.members:
                    if member.mention == f'{settingscore[1]}':
                        if not member.bot:
                            messages[member.id] = int(thekidscore2)
                            print(f'{member} = {messages[member.id]}')
                            kids += ({'user': str(member), 'messages': messages[member.id]}, )
                            await client.send_message(message.channel, f"{crac.name}'s score is now set to {messages[member.id]} ")

                    else:
                        kids += ({'user': str(member), 'messages': messages[member.id]}, )


        if message.content.startswith('+=mentionlater') == True:
            remindlate = message.content.split()
            commandcount = len(remindlate[1])
            commandcount += 16
            remindmessage = message.content[commandcount:]
            commandcount = 0
            if int(remindlate[1]) < 99999:
                await client.send_message(message.channel, f'Reminding in {remindlate[1]} seconds.')
                await remindlater(message, message.author, remindlate[1], remindmessage)
            else:
                await client.send_message(message.channel, 'The time must be less than 100000s')


        if message.channel.id == '581586829921484845':
            await client.send_message(client.get_channel('245194375670267904'), message.content)


        try:
            try:

                if message.content.startswith('+=tts') == True:

                    messagetts = message.content[6:]
                    print('works')
                    print('This is the message itself')
                    print(messagetts)
                    print('This is the name of the file')
                    final_messagetts = messagetts.replace(' ', '_').replace(':', '_').replace('?', '').replace('!', '')
                    print(final_messagetts)
                    said_final_messagetts = final_messagetts.replace('.', '(_(').replace(',', '(')
                    print('This is the message thats pronounced')
                    print(said_final_messagetts)
                    os.system(r"eSpeak\command_line\espeak.exe -w Textspeechlogs\audio_" + final_messagetts + '.mp3' + ' ' + said_final_messagetts + '\n')
                    await client.send_file(message.channel, f'Textspeechlogs/audio_{final_messagetts}.mp3')

                    try:
                        global voice_chat
                        voice_chat = await client.join_voice_channel(client.get_channel('585601770873421828'))
                        voice_chat_play = voice_chat.create_ffmpeg_player(f'Textspeechlogs/audio_{final_messagetts}.mp3')
                        voice_chat_play.start()
                        print('Connecting now')
                    except:
                        print('Already connected')
                        voice_chat_play = voice_chat.create_ffmpeg_player(f'Textspeechlogs/audio_{final_messagetts}.mp3')
                        voice_chat_play.start()



            except FileNotFoundError:
                await client.send_message(message.channel, 'Error, invalid charactor or too long for conversion.')

        except OSError:
            await client.send_message(message.channel, 'Mentions/emojis are not allowed for conversion')


        if message.content == '+=help':
            helpmessage=discord.Embed(title="Help and commands", description=f"Check out all those commands", color=int(random.choice(randomhexcolors)))
            helpmessage.add_field(name='+=info', value=str('This shows the info about the bot'), inline=False)
            helpmessage.add_field(name='+=dm', value=str('The bot dms you random stuff/messages'), inline=False)
            helpmessage.add_field(name='+=tts (message)', value=str('Bot converts the message into speech and sends the file to you (now works in vc too)'), inline=False)
            helpmessage.add_field(name='+=mentionlater (seconds) (message)', value=str('Bot sends you a message in the following seconds you input'), inline=False)
            await client.send_message(message.channel, embed=helpmessage)


        if message.content == '+=toxicity':
            await client.send_message(message.channel, 'E-THOT <@189669495420354561>')


        if message.content.startswith('+=speak') == True:
            if len(message.content) < 1024:
                f = open('Database.txt', 'a')
                f.write(f'{message.content[8:]}\n')
                await client.send_typing(message.channel)
                await traindatabase(message.channel, temp_for_bot)
                #await client.send_message(message.channel, str(fmt).replace("'",'').replace('[', '').replace(']','') + '\n')
            else:
                await client.send_message(message.channel, 'The message exceeds the limit')
        if message.content.startswith('==') == False:
            if message.channel.id == '595886307150921728':
                if len(message.content) < 1024:
                    f = open('Database.txt', 'a')
                    f.write(f'{message.content}\n')
                    await client.send_typing(message.channel)
                    await traindatabase2(message.channel, temp_for_bot)
                    #await client.send_message(message.channel, str(fmt).replace("'",'').replace('[', '').replace(']','') + '\n')
                else:
                    await client.send_message(message.channel, 'The message exceeds the limit')

            #uwu you found me
        #uwu time everybody


        excluded_channels = ['403586852176658442',
                            '389803723137744898',
                            '424303577339789323',
                            '248844395955093504'
                            ]


        if message.channel.id != f'{excluded_channels}':

            sortkids = sorted(kids, key = lambda i: i['messages'], reverse=True)
            kids = []


            global winning_boi
            leaderboard=discord.Embed(title="Total message score", description=f"Looks like {winning_boi} is ahead", color=int(random.choice(randomhexcolors)))
            hm = -1

            for x in sortkids:
                c = json.dumps(x)
                ff = json.loads(c)
                if hm == -1:
                    winning_boi = f"{ff['user']}"
                hm += 1
                if hm == 0:
                    leaderboard.add_field(name=f"1st place: {ff['user']}", value=str(ff['messages']), inline=False)

                elif hm == 1:
                    leaderboard.add_field(name=f"2nd place: {ff['user']}", value=str(ff['messages']), inline=False)

                elif hm == 2:
                    leaderboard.add_field(name=f"3rd place: {ff['user']}", value=str(ff['messages']), inline=False)

                elif hm != 10:
                    hm += 1
                    hm2 = hm
                    hm -= 1
                    leaderboard.add_field(name=f"{hm2}th place: {ff['user']}", value=str(ff['messages']), inline=False)
                if hm == 10:
                    with open('messageid.txt', 'r') as xnc:
                        hhhf = xnc.read()
                        hhhr = client.get_channel('553352042635329537')
                        hhh = await client.get_message(hhhr, f'{hhhf}')
                        print(hhh)
                        await client.edit_message(hhh, embed=leaderboard)
                    return winning_boi

            hm = -1

            print(str(sortkids))
            print("--- %s seconds ---")

global hhhh
hhhh = ''

@client.event
async def on_ready():
    fffff = 0
    global kids
    kids = []
    print('BOT STARTED UP')
    if TEST_MODE == False:
        with open('messageid.txt', 'r') as x:
            hhh = x.readlines()
        with open('json_fuckfest.txt', 'r+', encoding='UTF-8') as x:
            server = client.get_server(id="245194375670267904")
            for j in x:
                for member in server.members:
                    if not member.bot:
                        fffkids = j.split()

                        if fffkids[0] == member.id:
                            messages[member.id] = int(fffkids[1])
                            print(fffkids[1])
                            kids += ({'user': str(member), 'messages': messages[member.id]}, )
                            fffff+=1
                            x.write('')
                        else:
                            fffff1 = fffff
                            fffff1 *= 100
                            fffff1 /= len(server.members)
                            print(f'{float(fffff1)}%')
        print(kids)



    with open('json_fuckfest.txt', 'w', encoding='UTF-8') as x:
        x.write('')

    await client.change_presence(game=discord.Game(name=''))
    start_time = time.time()

client.run(TOKEN)
