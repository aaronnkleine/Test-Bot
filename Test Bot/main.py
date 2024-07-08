import discord
import random
import os
import string
import json
import time

from discord import client
from discord import message
from discord import user
from discord.embeds import Embed
from discord.ext import commands
import random

# Load the config file
with open("config.json") as file:
    info = json.load(file)
    token = info["token"]
    prefix = info["prefix"]
    startupchannel = info["startupchannel"]

client = discord.Client(intents=discord.Intents.all())
client = discord.Client
client = commands.Bot(command_prefix=prefix)
client.remove_command('help')
intents = discord.Intents.default()
intents.members = True


#Version Command
@client.command(aliases=['info', 'about'])
async def version(ctx):
    
    myEmbed = discord.Embed(title="__Current Version__", description="The Bot is currently in Version 1.0.0", color=0xfa4454)
    myEmbed.add_field(name="Version Code:", value="v1.0.0", inline=False)
    myEmbed.add_field(name="Date Released:", value="MM/DD/YYYY", inline=False)
    myEmbed.add_field(name="Creator:", value= "CREATOR \nID:", inline=False)
    myEmbed.add_field(name="Invite Link:", value='[Invite Me!](https://discord.com)', inline=False)
    myEmbed.set_footer(text= "- - -", icon_url="https://cdn.discordapp.com/attachments/")

    await ctx.message.channel.send(embed=myEmbed)

#Ping Command 
@client.command()
async def ping(ctx):
    await ctx.send(f'🏓 Pong! {round(client.latency * 1000)}ms')

#8Ball Command
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                 "It is decidedly so.",
                 "Without a doubt.",
                 "Yes - definitely.",
                 "You may rely on it.",
                 "As I see it, yes.",
                 "Most likely.",
                 "Outlook good.",
                 "Yes.",
                 "Signs point to yes.",
                 "Reply hazy, try again.",
                 "Ask again later.",
                 "Better not tell you now.",
                 "Cannot predict now.",
                 "Concentrate and ask again.",
                 "Don't count on it.",
                 "My reply is no.",
                 "My sources say no.",
                 "Outlook not so good.",
                 "Very doubtful."]
    await ctx.send(f'**Question:** {question}\n**Answer:** {random.choice(responses)}')

#Clear Command
@client.command(aliases=['purge', 'delete'])
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

#Kick Command
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

#Ban Command
@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Succesfully banned {member.mention}.')

#Unban Command
@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Succesfully unbanned {user.mention}.')
            return

#Start Message
@client.event
async def on_ready():
    await client.change_presence(status= discord.Status.do_not_disturb, activity= discord.Game('+help'))
    general_channel = client.get_channel(904386739454488658)

    await general_channel.send('🟢 Hello, world! I am back online.')
 

client.run(token)