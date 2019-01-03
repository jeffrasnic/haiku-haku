import discord
import yaml
with open('client.yaml') as f:
    # use safe_load instead load
    token = yaml.safe_load(f)

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!\n'.format(self.user))
        print("{0}\n".format(discord.__version__))
        print('Version: {0}'.format(token["version"]))

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.guild != None and message.author.permissions_in(message.channel).administrator:
            if message.content.startswith('!message'):
                newmsg = message.content.split()
                channelString = newmsg[1].replace("<", "").replace(">", "").replace("#", "")
                channel = message.guild.get_channel(int(channelString))
                print(newmsg[0])
                print(newmsg[1])

                string = ""
                for f in newmsg[2:]:
                    string+=f
                    string+=' '

                await channel.send(string)
                
                if message.content.startswith('!messagedel'):
                    await message.delete()
            elif message.content.startswith('!reaction'):
                newmsg = message.content.split()
                channelString = newmsg[1].replace("<", "").replace(">", "").replace("#", "")
                channel = message.guild.get_channel(int(channelString))
                print(newmsg[0])
                print(newmsg[1])
                msgReact = await channel.get_message(newmsg[2])
                if message.content.startswith('!reaction_remove'):
                    await msgReact.remove_reaction(newmsg[3], self.user)

                elif message.content.startswith('!reaction_add'):
                    await msgReact.add_reaction(newmsg[3])

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
        elif message.content.startswith('!help'):
            channel = message.channel
            await channel.send('I can give you pronoun roles on Haiku Haven! Just use !he or !she or !they for your role, if you already have that role, I will remove it.')
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

client = MyClient()
client.run(token["token"])