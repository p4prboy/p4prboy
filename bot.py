import discord
import os
import random
from discord.ext import commands
client = commands.Bot(command_prefix='!')
@client.event
async def on_ready():
  print('Bot is running as {0.user}!'.format(client))
  await client.change_presence(status=discord.Status.idle, activity=discord.Game('How to kill Humanity (fast)'))
@client.event
async def on_member_join(member):
  print(f'{member} has joined the Server!')
async def on_member_remove(member):
  print(f'{member} has left the Server!')
@client.command()
async def ping(ctx):
  await ctx.send(f'Pong! im catching {round(client.latency *1000)}ms')
  return
@client.command()
async def whoami(ctx):
  username = ctx.message.author.name
  await ctx.reply(f'You are {username}!')
  await client.change_presence(status=discord.Status.idle, activity=discord.Game('Collecting Names'))
  
@client.command()
async def hello(ctx):
  username = ctx.message.author.name
  await ctx.reply(f'Hello {username}!')
  await client.change_presence(status=discord.Status.idle, activity=discord.Game('greetings'))
  return
@client.command()
async def randomnr(ctx):
  randomnr = random.randrange(1000000)
  await ctx.reply(f'Deine Nummer ist {randomnr}')
  await client.change_presence(status=discord.Status.idle, activity=discord.Game('maths'))
  return
@client.command()
async def randomnr_10(ctx):
  randomnr = random.randrange(10)
  await ctx.reply(f'Deine Nummer ist {randomnr}')
  await client.change_presence(status=discord.Status.idle, activity=discord.Game('maths'))
  return
@client.command()
async def randomnr_100(ctx):
  randomnr = random.randrange(100)
  await ctx.reply(f'Deine Nummer ist {randomnr}')
  await client.change_presence(status=discord.Status.idle, activity=discord.Game('maths'))
  return
@client.command()
async def randomnr_1000(ctx):
  randomnr = random.randrange(1000)
  await ctx.reply(f'Deine Nummer ist {randomnr}')
  await client.change_presence(status=discord.Status.idle, activity=discord.Game('maths'))
  return
@client.command()
async def rickroll(ctx):
  await client.change_presence(status=discord.Status.idle, activity=discord.Game('Rolling the Rick'))
  await ctx.reply('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣰⣲⣦⣿⣿⣿⠷⢶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣪⣿⣿⣿⣿⣿⣿⣿⣶⣽⣷⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠛⣠⡽⠛⠛⠛⠋⠉⠉⠉⣿⣿⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢾⣿⠀⠀⣀⡀⠀⣀⡀⠀⢸⣿⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⣾⣿⣀⠬⠿⢹⡄⠹⠿⠯⢸⣏⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠐⠉⠀⣿⡅⣿⠀⢀⣠⣧⠄⣆⠀⢘⣿⡈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⠀⢠⣤⣀⣤⣿⢀⣞⠁⠀⠐⠦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣦⠈⢫⣸⠟⠁⢸⡛⠀⠀⠀⠀⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣦⠘⣁⡀⠀⢸⡿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠐⣰⢿⣯⡄⠀⠀⣠⡾⠁⣿⣿⣿⣶⣶⣶⣦⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣤⣴⣾⣿⣿⣰⣿⠛⡿⣇⣤⡾⠋⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠄⠀⠀⠀
⠀⠀⢠⣶⣾⣿⣿⣿⣿⣿⣿⣿⣟⢀⡷⣮⣭⣤⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀
⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣟⣛⣛⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠈⣟⣚⣒⣒⣲⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⡿⠶⠾⠯⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀
⠀⠀⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⢿⣭⣿⣿⣟⣿⣿⣿⡏⠀⠉⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀
⠀⢠⣿⣿⣿⣿⣿⡿⢻⣿⣿⣿⡿⣻⣛⣛⣛⣛⢻⣿⣿⣿⣇⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀
⠀⠻⣿⣿⣿⣿⠅⠂⠰⣿⣿⣿⡇⣿⡿⢿⠯⠭⠭⣽⣿⣿⣿⣤⡀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄
⠀⣠⣿⣿⡿⠃⠀⠀⠀⢹⣿⣿⡷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣰⣿⣿⣿⣣⣷⣄⠀⢠⣾⣿⣿⣇⣿⣿⣓⣒⣒⣺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀
⠈⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠉⠉⠉⠉⠉⠀⠀
⠀⠈⠋⠛⠛⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⡟⠉⠉⠉⠉⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀''')
  return
@client.command()
async def kick(ctx,member : discord.Member,*, reason=None):
    await member.kick(reason=reason)
    return
@client.command()
async def ban(ctx,member : discord.Member,*, reason=None):
    await member.ban(reason=reason)
    return
@client.command()
async def commands(ctx):
  await client.change_presence(status=discord.Status.idle, activity=discord.Game('!commands'))
  
  await ctx.send('''
!command - list commands
!ping - get your ping
!randomnr - get random number
!randomnr_10 - get random number from 0-10
!randomnr_100 - get random number from 0-100
!randomnr_1000 - get random number from 0-1000
!ban - ban user
!kick - kick user
!rickroll -rickroll
!hello - greet
!bye - goodbye
!whoami - get your username
!iq - get your iq''')

#Get-IQ
@client.command()
async def iq(ctx):
  randomnr2 = random.randrange(140)
  n = 130
  x = 80
  y = 50
  a =30
  print(randomnr2)
  if randomnr2 >= 100:
    await ctx.reply(f'Your IQ is {randomnr2}, damn how much Nobelprizes do you got?')
  elif randomnr2 <= 60 and randomnr2 > y:
    await ctx.reply(f"Your IQ is {randomnr2}, thats decent but nothing special")
  elif randomnr2 <= y and randomnr2 > a:
    await ctx.reply(f'Your IQ is {randomnr2} what a shame,you have the IQ of wood')
  elif randomnr2 <= a:
    await ctx.reply(f'Your IQ is {randomnr2} i dont have to explain this because you would not understand it anyways LMAO')
  elif randomnr2 >=90 and randomnr2 < 110:
    await ctx.reply(f'Your IQ is {randomnr2} pfeeew...lucky you, youre not a shame for humanity!')
    return
#Delete channel
@client.command()
async def delete(ctx, channel_name):
  guild = ctx.message.guild
  existing_channel = discord.utils.get(guild.channels, name =channel_name)
  if existing_channel is not None:
    await existing_channel.delete()
    await ctx.reply(f'{existing_channel} got deleted!')
  else:
    await ctx.reply(f'No Channel named,{existing_channel}!')
    return
@client.command()
async def tc(ctx,*, name =None):
  guild = ctx.message.guild
  if name == None:
    await ctx.reply('Sorry but you have to insert a name')
  else:
    await guild.create_text_channel(name)
    await ctx.reply(f'I created the Text Channel {name}!')
    return
@client.command()
async def vc(ctx,*, name =None):
  guild = ctx.message.guild
  if name == None:
    await ctx.reply('Sorry but you have to insert a name')
  else:
    await guild.create_voice_channel(name)
    await ctx.reply(f'I created the Voice Channel {name}!')
    return
@client.command()
async def jebaited(ctx):
  await client.change_presence(status=discord.Status.idle, activity=discord.Game('Trolling'))
  await ctx.reply('''⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣠⣤⣤⣤⣄⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⢷⣄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⢠⣌⢻⣿⣿⣿⣿⣿⣿⣿⣿⡯⠻⠿⣿⣿⡿⠿⠛⢷⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⣤⣤⠼⠟⠛⠄⠠⣭⡙⠋⠉⠄⠄⠚⠟⠋⠃⠐⠸⢟⣦⠄⠄
⠄⠄⠄⠄⢀⣴⣿⡿⠋⠄⢀⣤⣤⣶⠈⢷⡄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⢻⠆⠄
⠄⠄⠄⠄⣿⣿⣍⠉⠻⠄⢻⣿⣿⣿⣶⣾⡿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠐⠨⣾⠄
⠄⠄⠄⣸⡿⣩⣟⣿⡦⡲⣿⣿⣿⡿⠙⠟⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢈⠁⠄
⠄⠄⠄⣿⣏⣉⠉⠛⠢⠈⣻⣿⣿⡍⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⠄⠄⠈⠄⠄
⠄⠄⠄⣿⣿⣿⣿⣶⣾⣿⣿⣿⣿⡏⠄⠄⠄⠄⠄⠄⠄⠄⢷⠄⡌⠄⠄⠄⠄⠄
⠄⠄⠸⠿⣿⣿⣿⡿⠟⠉⠿⠿⠁⠄⠄⠄⠄⠄⠄⢄⠄⠐⠁⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⢠⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⣾⣇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⣠⣿⣿⣷⣴⣶⣶⠄⠄⠄⠄⠄⠄⠄⠄⢀⣆⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄''')

  
  
  

    
    
  
  
  
  
      

client.run('OTg3MzYyMTk2MTY0MDY3Mzgy.Gglj37.KAOMXTuH99qyQPBmDHRFYWIexB33RjuHsRLIGk')
