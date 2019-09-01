import discord
import yaml
import datetime
from discord.ext import commands
import random
import copy

description = '''Bot for Haiku Haven moderation and contests.'''
bot = commands.Bot(command_prefix='!', description=description)

with open('client.yaml') as f:
    # use safe_load instead load
    token = yaml.safe_load(f)

@bot.command()
async def version(ctx):
    await ctx.send(token["version"])

@bot.command()
async def message(ctx):
    message = ctx.message
    newmsg = message.content.split()
    channelString = newmsg[1].replace("<", "").replace(">", "").replace("#", "")
    channel = message.guild.get_channel(int(channelString))

    if ctx.message.author.permissions_in(ctx.message.channel).administrator:
        print(newmsg[0])
        print(newmsg[1])

        sendMsgI = len(newmsg[0]) + len(newmsg[1]) + 2
                    
        await channel.send(message.content[sendMsgI:])
    
@bot.command()
async def messagedel(ctx):
    message = ctx.message
    newmsg = message.content.split()
    channelString = newmsg[1].replace("<", "").replace(">", "").replace("#", "")
    channel = message.guild.get_channel(int(channelString))

    if ctx.message.author.permissions_in(ctx.message.channel).administrator:
        print(newmsg[0])
        print(newmsg[1])

        sendMsgI = len(newmsg[0]) + len(newmsg[1]) + 2
                    
        await channel.send(message.content[sendMsgI:])
        await message.delete()

@bot.command()
async def purge(ctx):
    message = ctx.message
    newmsg = message.content.split()
    channelString = newmsg[1].replace("<", "").replace(">", "").replace("#", "")
    channel = message.guild.get_channel(int(channelString))

    if ctx.message.author.permissions_in(channel).administrator:

        confirmNum = random.randint(1, 10000)
        number = int(newmsg[2])
        print(newmsg[0])
        print(newmsg[1])

        print(confirmNum)
        
        if channel == message.channel:
            history = channel.history(limit=number + 3)
        else:
            history = channel.history(limit=number)

        await message.channel.send('Waiting for admin confirmation: Please type ``' + str(confirmNum) + '`` to execute purge of ' + str(number) + ' messages, or type ``cancel' + str(confirmNum) + '`` to cancel.')

        def check(m):
            return m.channel == message.channel and m.author.permissions_in(channel).administrator

        msg = await bot.wait_for('message', check=check)

        if msg.content == str(confirmNum):
            async for m in history:
                await m.delete()
            await message.channel.send('Done.')
        elif msg.content == 'cancel'+str(confirmNum):
            await message.channel.send('Purge canceled.')

@bot.command()
async def reaction_add(ctx):
    message = ctx.message
    newmsg = message.content.split()
    channelString = newmsg[1].replace("<", "").replace(">", "").replace("#", "")
    channel = message.guild.get_channel(int(channelString))

    if ctx.message.author.permissions_in(channel).administrator:
        print(newmsg[0])
        print(newmsg[1])

        msgReact = await channel.fetch_message(newmsg[2])

        reaction = newmsg[3].replace("<", "").replace(">", "").replace("#","")
        await msgReact.add_reaction(reaction)

@bot.command()
async def reaction_remove(ctx):
    message = ctx.message
    newmsg = message.content.split()
    channelString = newmsg[1].replace("<", "").replace(">", "").replace("#", "")
    channel = message.guild.get_channel(int(channelString))
        
    if ctx.message.author.permissions_in(channel).administrator:
        print(newmsg[0])
        print(newmsg[1])
        msgReact = await channel.fetch_message(newmsg[2])

        reaction = newmsg[3].replace("<", "").replace(">", "").replace("#","")
        await msgReact.remove_reaction(reaction, bot.user)

@bot.command()
async def contest_reactions(ctx):
    message = ctx.message
    newmsg = message.content.split()
    channelString = newmsg[1].replace("<", "").replace(">", "").replace("#", "")
    channel = message.guild.get_channel(int(channelString))

    if ctx.message.author.permissions_in(channel).administrator:
        print(newmsg[0])
        print(newmsg[1])
        number = int(newmsg[2])

        reaction = newmsg[3].replace("<", "").replace(">", "").replace("#","")

        print(number)
        print(reaction)
        
        async for m in channel.history(limit=number):
            await m.add_reaction(reaction)
        if not message.content.endswith(' \silence'):
            await message.channel.send('Done! Added ' + str(number) + ' reactions.')

@bot.command()
async def contest_reactions_del(ctx):
    message = ctx.message
    newmsg = message.content.split()
    channelString = newmsg[1].replace("<", "").replace(">", "").replace("#", "")
    channel = message.guild.get_channel(int(channelString))

    if ctx.message.author.permissions_in(channel).administrator:
        print(newmsg[0])
        print(newmsg[1])
        number = int(newmsg[2])

        reaction = newmsg[3].replace("<", "").replace(">", "").replace("#","")

        print(number)
        print(reaction)
        
        async for m in channel.history(limit=number):
            await m.remove_reaction(reaction, bot.user)
        if not message.content.endswith(' \silence'):
            await message.channel.send('Done! Removed ' + str(number) + ' reactions.')

@bot.command()
async def she(ctx):
    message = ctx.message
    guild = bot.get_guild(467521350643351566)
    channel = message.channel
    member = guild.get_member(message.author.id)
    sheRole = discord.utils.get(guild.roles, id=469254726911787028)
    if discord.utils.find(lambda m: m.id == 469254726911787028, member.roles) == None:
        await member.add_roles(sheRole)
        await channel.send('I have added the She/Her role to you on Haiku Haven!')
    else:
        await member.remove_roles(sheRole)
        await channel.send('I have removed the She/Her role from you on Haiku Haven!')

@bot.command()
async def he(ctx):
    message = ctx.message
    guild = bot.get_guild(467521350643351566)
    channel = message.channel
    member = guild.get_member(message.author.id)
    sheRole = discord.utils.get(guild.roles, id=469254624155664394)
    if discord.utils.find(lambda m: m.id == 469254624155664394, member.roles) == None:
        await member.add_roles(sheRole)
        await channel.send('I have added the He/Him role to you on Haiku Haven!')
    else:
        await member.remove_roles(sheRole)
        await channel.send('I have removed the He/Him role from you on Haiku Haven!')

@bot.command()
async def they(ctx):
    message = ctx.message
    guild = bot.get_guild(467521350643351566)
    channel = message.channel
    member = guild.get_member(message.author.id)
    sheRole = discord.utils.get(guild.roles, id=469254800358506497)
    if discord.utils.find(lambda m: m.id == 469254800358506497, member.roles) == None:
        await member.add_roles(sheRole)
        await channel.send('I have added the They/Them role to you on Haiku Haven!')
    else:
        await member.remove_roles(sheRole)
        await channel.send('I have removed the They/Them role from you on Haiku Haven!')

@bot.event
async def on_ready():
        print('Logged on as {0}!\n'.format(bot.user))
        print("Discord.py Version: {0}\n".format(discord.__version__))
        print('Version: {0}'.format(token["version"]))

@bot.event
async def on_message(message):
        if message.author == bot.user:
            return
        await bot.process_commands(message)

@bot.event
async def on_raw_reaction_add(payload):
    print("Detected reaction add")
    if payload.message_id == 611698983412170764:
        print("Detected reaction on message")
        guild = bot.get_guild(467521350643351566)
        user = guild.get_member(payload.user_id)
        await user.add_roles(discord.utils.get(guild.roles, id=610160581768511562))

@bot.event
async def on_raw_reaction_remove(payload):
    print("Detected reaction remove")
    if payload.message_id == 611698983412170764:
        print("Detected reaction on message")
        guild = bot.get_guild(467521350643351566)
        user = guild.get_member(payload.user_id)
        await user.remove_roles(discord.utils.get(guild.roles, id=611698983412170764))

bot.run(token["token"])