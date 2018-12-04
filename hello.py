import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        print(discord.__version__)

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.guild != None:
            if message.content.startswith('!message'):
                channel = message.guild.get_channel(518131736362614809)
                await channel.send(message.content[9:])
                await message.delete()
            elif message.content.startswith('!reaction'):
                newmsg = message.content.split()
                channel = message.guild.get_channel(518131736362614809)
                print(newmsg[0])
                msgReact = await channel.get_message(newmsg[1])
                if message.content.startswith('!reaction_remove'):
                    await msgReact.remove_reaction(newmsg[2], self.user)

                elif message.content.startswith('!reaction_add'):
                    await msgReact.add_reaction(newmsg[2])

        if message.content.startswith('!she'):
            guild = client.get_guild(467521350643351566)
            channel = message.channel
            member = guild.get_member(message.author.id)
            sheRole = discord.utils.get(guild.roles, id=469254726911787028)
            if discord.utils.find(lambda m: m.id == 469254726911787028, member.roles) == None:
                await member.add_roles(sheRole)
                await channel.send('I have added the She/Her role to you on Haiku Haven!')
            else:
                await member.remove_roles(sheRole)
                await channel.send('I have removed the She/Her role from you on Haiku Haven!')
        elif message.content.startswith('!he'):
            guild = client.get_guild(467521350643351566)
            channel = message.channel
            member = guild.get_member(message.author.id)
            heRole = discord.utils.get(guild.roles, id=469254624155664394)
            if discord.utils.find(lambda m: m.id == 469254624155664394, member.roles) == None:
                await member.add_roles(heRole)
                await channel.send('I have added the He/Him role to you on Haiku Haven!')
            else:
                await member.remove_roles(heRole)
                await channel.send('I have removed the He/Him role from you on Haiku Haven!')
        elif message.content.startswith('!they'):
            guild = client.get_guild(467521350643351566)
            channel = message.channel
            member = guild.get_member(message.author.id)
            theyRole = discord.utils.get(guild.roles, id=469254800358506497)
            if discord.utils.find(lambda m: m.id == 469254800358506497, member.roles) == None:
                await member.add_roles(theyRole)
                await channel.send('I have added the They/Them role to you on Haiku Haven!')
            else:
                await member.remove_roles(theyRole)
                await channel.send('I have removed the They/Them role from you on Haiku Haven!')
        elif message.content.startswith('!help'):
            channel = message.channel
            await channel.send('I can give you pronoun roles on Haiku Haven! Just use !he or !she or !they for your role, if you already have that role, I will remove it.')

client = MyClient()
client.run('NDY5MjYxNDEyMTk2Mjg2NDY0.DjFM6A.nI3bhn56F3z0yEpueencffzNvOI')