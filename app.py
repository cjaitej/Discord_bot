import discord
import pandas as pd
import random
import datetime
from discord.ext import commands
from keep_alive import keep_alive

prefix = '#'

client = commands.Bot(command_prefix= prefix)



@client.command()
@commands.has_permissions(ban_members = True)
async def prefix(ctx, prefix = '#'):
  prefix = prefix
  p = await ctx.send(f' >>> Prefix is changed to -- {prefix}')
  await discord.Message.edit(p,content='I am Ironman')



greetings = [
  '`yo! What’s happening?`:sunglasses: :sunglasses: ',
  ':love_you_gesture_tone1: `Hey, What’s up?`:love_you_gesture_tone1: ',
  '`Hey, How was your day?` :kissing_closed_eyes: :kissing_closed_eyes: ',
  '`Hey! buddy, How’s everything` :question: :question: ',
  '`Nice to see you again.` :eyes: :eyes: ',
  ':timer:`Long time!!!no see!` :eyes:',
  '`Good day, how are you today?`:sparkling_heart: :sparkling_heart:',
  '`Look who it is!!!!!! Whattsssupppppp maaaaannnnnnn!!!`!`:scream_cat: :scream_cat: :scream_cat: :scream_cat: ',
  ':sunny: :sunny: :sunny: :sunny: `Hello, sunshine! How are you? Oh, your rays are already making my day brighter!` :heart_eyes: :heart_eyes: :heart_eyes: ',
  ':man_superhero_tone1: :man_superhero_tone1:`I am DRAGON. Who are you, gorgeous?`',
  '`Hiiiii, baaaaaby!` :kissing_heart: :kissing_heart: ',
  ':door: :door:`Knock knock… who is there? oh!!! It’s me, DRAGON! :dragon_face: :dragon_face: '
]

hugs = [
    'https://media.tenor.com/images/6bc667c45027dedb2bda98fda6d3dfdd/tenor.gif',
    'https://media.tenor.com/images/93f692bfae991b2ad599982a3b9e7223/tenor.gif',
    'https://media.tenor.com/images/e63ae6d78e58c2beab015de5f6826859/tenor.gif',
    'https://media.tenor.com/images/50c2f13c590fdb27c087d6a6736218e0/tenor.gif'
]


@client.event
async def on_ready(): #status
    await client.change_presence(status= discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name= 'Action Kamen' ))
    prefix = '#'
    print('Bot is ready.')

@client.command()
async def myinfo(ctx):
  await ctx.send(f'{ctx.author} is your ID {ctx.author.mention}')


@client.command(aliases = ['start bank'])
async def startbank(ctx):
  df = pd.read_csv('bank_details.csv')
  m = await ctx.send('We are working on your Bankaccount!')
  await discord.Message.edit(m,content = 'Checking all the files....')
  await discord.Message.edit(m,content = 'Checking all the files........')
  await discord.Message.edit(m,content = 'Checking all the files........ .........')
  await discord.Message.edit(m,content = 'Checking all the files........ ......... .....')
  await discord.Message.edit(m,content = 'Checking your photo id!.....')
  await discord.Message.edit(m,content = 'Checking your photo id!.....:bearded_person_tone1: ')
  await discord.Message.edit(m,content = 'Checking your photo id!.....:bearded_person_tone1: ')
  await discord.Message.edit(m,content = 'Checking your photo id!.....:bearded_person_tone1: ')
  await discord.Message.edit(m,content = 'Checking your photo id!.....:bearded_person_tone1: ')
  await discord.Message.edit(m,content = 'Checking your photo id!.....:bearded_person_tone1: ')
  await discord.Message.edit(m,content = 'Checking your photo id!.....:bearded_person_tone1: ')
  await discord.Message.edit(m,content = 'Verifing Date of Birth')
  await discord.Message.edit(m,content = 'Verifing Date of Birth')
  await discord.Message.edit(m,content = 'Verifing Date of Birth')                                            

  await discord.Message.edit(m,content = 'Loading.. **FINAL REPORT**')
  await discord.Message.edit(m,content = 'Loading.... **FINAL REPORT** ')
  await discord.Message.edit(m,content = 'Loading...... **FINAL REPORT** ')
  await discord.Message.edit(m,content = 'Loading......... **FINAL REPORT** !')
  await discord.Message.edit(m,content = '**FINAL REPORT**')
  await discord.Message.delete(m)
  if ctx.author.id in list(df['discord_id']):
    embed=discord.Embed(title="BANK ACCOUNT", description=f"Oh shit! we found that you already have an account! Are you trying to scam us????... {ctx.author.mention}", color=0xf70808)
    embed.add_field(name="Application Status", value="Rejected :x: ", inline=False)
    embed.set_footer(text="pls type #bal to view your account Details.")
    await ctx.send(embed=embed)

  else:
    embed=discord.Embed(title="BANK ACCOUNT", description=f"All your papers are perfect!....And your bank account is ready! {ctx.author.mention}", color=0x26c01b)
    embed.add_field(name="Application Status", value="Accepted :ballot_box_with_check:", inline=False)
    embed.set_footer(text="pls type #bal to view your account Details.")
    await ctx.send(embed=embed)

    f = open('bank_details.csv','a')
    f.write(f'\n{ctx.author.id},{ctx.author.name},{int(100)},{int(5000)}')
    f.close()

@client.command()
async def bal(ctx):
  df = pd.read_csv('bank_details.csv')
  d = df.loc[df['discord_id'] == ctx.author.id]
  wallet = int(d['wallet'])
  bank = int(d['bank'])
  

  embed=discord.Embed(title=f"{ctx.author.name}'s Bank details.", color=0xd5e40c)
  embed.add_field(name="Wallet :", value= f'{wallet}:coin:    ', inline=True)
  embed.add_field(name="Bank :", value=f'{bank} :moneybag:', inline=True)  
  await ctx.send(embed=embed)


@client.command()
async def dep(ctx, num):
  df = pd.read_csv('bank_details.csv')
  d = df.loc[df['discord_id'] == ctx.author.id]
  wallet = int(d['wallet'])
  bank = int(d['bank'])
  if num in ['max','all']:
    df.loc[df['discord_id'] == ctx.author.id, ['wallet','bank']] = [wallet - wallet, bank + wallet]
    df.to_csv('bank_details.csv',index = False)
    
    await ctx.send(f'{ctx.author.mention} deposited {wallet}:coin:  ')

  elif wallet - int(num) >= 0:
    df.loc[df['discord_id'] == ctx.author.id, ['wallet','bank']] = [wallet - int(num), bank + int(num)]
    df.to_csv('bank_details.csv',index = False)
    
    await ctx.send(f'{ctx.author.mention} has deposited {num}:coin:  ')
  else:
    await ctx.send(f"{ctx.author.mention} Heyuu!! You don't have that much Money in your wallet!!")  

@client.command(aliases = ['with'])
async def _with(ctx, num):
  df = pd.read_csv('bank_details.csv')
  d = df.loc[df['discord_id'] == ctx.author.id]
  wallet = int(d['wallet'])
  bank = int(d['bank'])
  if num in ['max','all']:
    df.loc[df['discord_id'] == ctx.author.id, ['wallet','bank']] = [wallet + bank ,0]
    df.to_csv('bank_details.csv',index = False)
    
    await ctx.send(f'{ctx.author.mention} withdrawn {bank} :moneybag: to your wallet!')
  
  elif bank >= int(num):
    df.loc[df['discord_id'] == ctx.author.id, ['wallet','bank']] = [wallet + int(num), bank - int(num)]
    df.to_csv('bank_details.csv',index = False)
    
    await ctx.send(f'{ctx.author.mention} has withdrawn {num} :moneybag: to your Wallet!')
  else:
    await ctx.send(f"{ctx.author.mention} Heyuu!! You don't have that much money in your bank :sneezing_face: ")

@client.command()
async def give(ctx,num,member : discord.Member):
  senderid = ctx.author.id
  receiverid = member.id
  df = pd.read_csv('bank_details.csv')
  d = df.loc[df['discord_id'] == senderid]
  p = df.loc[df['discord_id'] == receiverid]
  walletsender = int(d['wallet'])
  walletreceiver = int(p['wallet'])
  
  if num in ['max','all']:
    num = walletsender
  
  if senderid == receiverid:
    await ctx.send(f'{ctx.author.mention} Hey! man you crazyyy?? Why do you want to send money to your self???')
  elif int(num) <= walletsender:
    df.loc[df['discord_id'] == senderid, ['wallet']] = [walletsender - int(num)]
    df.loc[df['discord_id'] == receiverid, ['wallet']] = [walletreceiver+int(num)]
    df.to_csv('bank_details.csv',index = False)
    await ctx.send(f'{ctx.author.mention} has sent {num}:coin:  to {member.mention}')
  else:
    await ctx.send(f"{ctx.author.mention} Hey! dumb... you don't have enough money in your wallet to send.")

@client.command()
async def beg(ctx):
  num = [0,1,2,3,4,5,6,7,8,9]
  rnum = str(random.choice(num)) + str(random.choice(num)) + str(random.choice(num))
  
  df = pd.read_csv('bank_details.csv')
  d = df.loc[df['discord_id'] == ctx.author.id]
  wallet = int(d['wallet'])
  bank = int(d['bank'])
  df.loc[df['discord_id'] == ctx.author.id, ['wallet']] = [wallet + int(rnum)]
  df.to_csv('bank_details.csv',index = False)

  await ctx.send(f'{ctx.author.mention} take this {rnum} :coin:...  begger! ')

@client.command()
async def check(ctx, name,device):
  m = await ctx.send(f"Getting access to {name}'s {device}!")
  await discord.Message.edit(m,content = f"Getting access to {name}'s {device}!")
  await discord.Message.edit(m,content = f"Getting access to {name}'s {device}!")
  await discord.Message.edit(m,content = f"Getting access to {name}'s {device}!")
  await discord.Message.edit(m,content = f"Getting access to {name}'s {device}!")
  await discord.Message.edit(m,content = 'Collecting data from google history!')
  await discord.Message.edit(m,content = 'Collecting data from google history!')
  await discord.Message.edit(m,content = 'Collecting data from google history!')
  await discord.Message.edit(m,content = 'Collecting data from google history!')
  await discord.Message.edit(m,content = 'Collecting data from google history!')
  await discord.Message.edit(m,content = 'Collecting data from google history!')
  await discord.Message.edit(m,content = '1. X$$deo.com')
  await discord.Message.edit(m,content = '1. X$$deo.com\n2. des$$$rls.com')
  await discord.Message.edit(m,content = '1. X$$deo.com\n2. des$$$rls.com\n3. How to sleep 6hrs in 2 hrs?? ')
  await discord.Message.edit(m,content = '1. X$$deo.com\n2. des$$$rls.com\n3. How to sleep 6hrs in 2 hrs??\n')
  await discord.Message.edit(m,content = 'Collecting information from whatsapp')
  await discord.Message.edit(m,content = 'Collecting data from google history!')
  await discord.Message.edit(m,content = 'Collecting data from google history!')
  await discord.Message.edit(m,content = 'Collecting data from google history!')
  await discord.Message.edit(m,content = 'Collecting data from google history!')
  await discord.Message.edit(m,content = 'Reading all the chats in whatsapp')
  await discord.Message.edit(m,content = 'Reading all the chats in whatsapp')
  await discord.Message.edit(m,content = 'Reading all the chats in whatsapp')
  await discord.Message.edit(m,content = 'Reading all the chats in whatsapp')
  await discord.Message.edit(m,content = 'Reading all the chats in whatsapp')
  await discord.Message.edit(m,content = 'Dirty photos identified!')
  await discord.Message.edit(m,content = 'Dirty photos identified!')
  await discord.Message.edit(m,content = 'Dirty photos identified!')
  await discord.Message.edit(m,content = 'Dirty photos identified!')
  await discord.Message.edit(m,content = 'NOW he is verified as SIMP')
  await discord.Message.edit(m,content = 'NOW he is verified as SIMP')
  await discord.Message.edit(m,content = 'NOW he is verified as SIMP')
  await discord.Message.edit(m,content = 'NOW he is verified as SIMP')
  await discord.Message.edit(m,content = f'Exposing {name} is completed! :fist_tone1:')
  



  
@client.command()
@commands.has_permissions(ban_members = True)
async def spam(ctx, num = 100, * , content = 'Jooooodddddddd'):
  for i in range(int(num)):
    await ctx.send(content)
    


@client.command()
async def hello(ctx):
  await ctx.send(random.choice(greetings))

@client.command()
async def hug(ctx , name):
  await ctx.send(f'I wanna hug you! {name}')
  await ctx.send(random.choice(hugs))
  

@client.command() ## its command not commands!!! bitch
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)}ms')



@client.command()
async def exam(ctx , name1, name2, name3, name4, name5):
  rec = [name1, name2, name3, name4, name5]
  sen = [name1, name2, name3, name4, name5]  
  j = 0
  for i in sen:
    p = random.choice(rec)
    while p == i:
      p = random.choice(rec)
    j = j + 1
    await ctx.send(f'{i} is your question maker! {p}')
    rec.remove(p)
    if j == 4:
      break
  print("- Function exam() is Finshed!")
   
  
@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member ,*, reason = "No reason provided"):
  await member.kick(reason=reason)
  await member.send("You are kicked from bot-test, Reason: "+ reason)

@client.command()
@commands.has_permissions(ban_members = True)
async def msg(ctx, member : discord.Member ,*, msg = "Helloooo"):
  await member.send(msg) 


@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member ,*, reason = "No reason provided"):
  try:
    await member.send("You are banned by Admin, Reason: "+reason)
    await member.ban(reason=reason)
    await ctx.send(member.name + " is banned., Reason: " +reason)
  except:
    await ctx.send("You don't have The Authority to ban.")

@client.command()
@commands.has_permissions(ban_members = True)
async def warn(ctx, member : discord.Member , count,*,reason = "No reason provided"):
  await ctx.send(f"```Name : {member.mention}{member.name}```")
  await ctx.send("```Warn : You are warned by admin!```")
  await ctx.send("`Warn Level :`" + ':star:'*int(count))
  await ctx.send(f"```Reason : {reason}```")
  

@client.command()
@commands.has_permissions(ban_members = True)
async def unban(ctx,*, member):
  banned_users = await ctx.user.guild.ban()
  member_name, member_disc = member.split('#')

  for banned_entry in banned_users:
    user = banned_entry.user

    if (user.name, user.discriminator) == (member_name, member_disc):
      await ctx.guild.unban(user)
      await ctx.send(f"{member} has been unbanned.")
      return
  
  await ctx.send("Member not found.")


@client.command(aliases = ['ask']) #you can use these name for calling the command
async def _ask(ctx, *, question):
    response = [
        "It is certain.",
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
        "Very doubtful."
    ]
    await ctx.send(f' Question : {question}  \nAnswer : {random.choice(response)}')

@client.command()
@commands.has_permissions()
async def alarm(ctx, n): #to delete messages
    now = datetime.datetime()
    await ctx.send(f'You have set alarm for {n} mins')
    while now.mins() > int(n):
      print(now().mins)
    await ctx.send(f'{n} mins are completed!')
    
    


@client.command()
@commands.has_permissions(ban_members = True)
async def clear(ctx, ammount=5): #to delete messages
    await ctx.channel.purge(limit=(ammount+1))

keep_alive()

client.run('Nzk0ODAyMTQ2MTk2OTc5NzQy.X_AHLg.4DuwFs4BFWiP741YQuVwtN6CBDY')
