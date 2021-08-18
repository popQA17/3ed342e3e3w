import os
import discord
import asyncio
from discord.ext import commands
import random
from discord.utils import get
import json
import requests
from discord.ext.commands import has_permissions, MissingPermissions
from dislash.interactions import *
from dislash import SlashClient, ActionRow, Button
from web import keep_alive
import datetime
import time
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option, create_choice
intents = discord.Intents.all()
def get_prefix(client, message): 
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)] 
client = commands.Bot(command_prefix= (get_prefix), help_command=None, intents=intents)
slash2 = SlashCommand(client, sync_commands=True)
slash = SlashClient(client)

@client.command()
async def get_time(ctx):
  from datetime import datetime
  dt = datetime.now().time()
  await ctx.send(f"The current time in your timezone is {dt}!")
import textcaptcha
from discord_slash.utils.manage_commands import create_permission
from discord_slash.model import SlashCommandPermissionType
# Create a captcha fetcher to fetch captcha questions from the API

@client.event
async def on_member_join(member):
  channel = client.get_channel(860514083219308564)
  embed = discord.Embed(title="New user!")
  embed.add_field(name=f"Welcome to HypnoKiller Cult {member.name} #{member.discriminator}", value="Chill out, have fun, talk about minecraft, or just have popcorn :)")
  embed.timestamp = datetime.datetime.utcnow()
  await channel.send(embed=embed)
  codee = random.randrange(9999)
  await member.send("Hello! We need you to verify before using the server :)")
  await member.send(f"Just say `{codee}` right here and you will be verified!")
  def check(msg):
    return msg.author == member
  code = await client.wait_for("message", timeout=30, check=check)
  if code.content == str(codee):
    await member.send("🎉You are verified!")
  else:
    await member.send(f"Oof... you didn't key in the right number. Do `;verification` in a channel to verify again :) you sent: {code.content}")

@client.command()
async def verification(ctx):
  codee = random.randrange(9999)
  await ctx.send(f"Just say `{codee}` right here and you will be verified!")
  def check(msg):
    return msg.author == ctx.author
  code = await client.wait_for("message", timeout=30, check=check)
  if str(code.content) == str(codee):
    await ctx.send("🎉You are verified!")
  else:
    await ctx.send(f"Oof... you didn't key in the right number. Do `;verification` in a channel to verify again :) you sent: {code.content} and the correct code was: {codee}")
@slash2.slash(name="ban",
             description="bans a user from the server!",
              permissions={
                860471346101616690: [
                create_permission(860516520466317333, SlashCommandPermissionType.ROLE, True)]
               },
             options=[
               create_option(
                 name="user",
                 description="The user you wish to ban",
                 option_type=6,
                 required=True
                
              )], guild_ids=[860471346101616690])
async def slashban(ctx, user: str):
  await ctx.send(content=f"{user} has not been banned for obvious test reasons. Until this command is stated official, this command will **not** work.")
@slash2.slash(name="revive",
             description="Revive a channel!",
              permissions={
                860471346101616690: [
                create_permission(860516520466317333, SlashCommandPermissionType.ROLE, True)]
               },
             options=[
               create_option(
                 name="channel",
                 description="channel to send ping",
                 option_type=7,
                 required = True
              )
              ], guild_ids=[860471346101616690])
async def revival(ctx, channel: str):
  channeltosend = client.get_channel(channel.id)
  await ctx.send(content=f"Channel revived :)")
  await channel.send(f"Aye! Listen up. {ctx.author.display_name} wants this channel revived. HEARD?  <@&865410289726259251>")
@slash2.slash(name="userinfo",
             description="Gets info on a specific user.",
             options=[
               create_option(
                 name="user",
                 description="user to get info",
                 option_type=6,
                 required = False
              )
              ], guild_ids=[860471346101616690])
async def revival(ctx, user=None):
    if user == None:
      member = ctx.author
    else:
      member = user
    roles = [role for role in member.roles[1:]]
    embed = discord.Embed(
    color = discord.Color(0xff3400),
    title = f"{member.name}")
    if str(member.status) == "dnd":
      emoji = "⛔ Do Not Disturb"
    elif str(member.status) == "online":
      emoji = "✅ Online"
    elif str(member.status) == "idle":
      emoji = "🌙 Idle"
    elif str(member.status) == "offline":
      emoji = "❌Offline"
    embed.add_field(name="**•ID•**", value=f"{member.id}", inline=True)

    embed.add_field(name="**•Status•**", value=emoji, inline=True)
    embed.set_thumbnail(url=f"{member.avatar_url}")
    try:
      embed.add_field(name=f"**•Roles• ({len(member.roles) - 1})**", value='• '.join([role.mention for role in roles]), inline=False)
    except:
      embed.add_field(name=f"**•Roles•**", value=' No Roles ', inline=False)
    datetime_format = "%a, %d/%b/%Y"
    embed.add_field(name="**•Account Created At•**", value=f"{member.created_at.strftime(datetime_format)}".replace("-", "/"), inline=True)
    embed.add_field(name="**•Joined Server At•**", value=f"{member.joined_at.strftime(datetime_format)}".replace("-", "/"), inline = True)
    embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Requested by {ctx.author}")
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)
@client.command()
async def slashie(ctx, member: discord.Member):
  while True:
    
    await member.send(member.mention)
@client.event
async def on_message(message):
  if isinstance(message.channel, discord.channel.DMChannel):
    messageval = message.content
    embed = discord.Embed(tite="Mod Call", color=0xFFA500)
    embed.add_field(name="Your message:", value=messageval)
    embed.set_footer(text="Sending..")
    messagetosend = await message.author.send(embed=embed)
    await asyncio.sleep(2)
    embed2 = discord.Embed(tite="Mod Call", color=0x00FF00)
    embed2.add_field(name="Your message:", value=messageval)
    embed2.set_footer(text="Received by Mods!")
    await messagetosend.edit(embed=embed2)
    embed3 = discord.Embed(title="Mod Call", color=0x0000FF)
    embed3.add_field(name="User: ", value=f"{message.author} #{message.author.discriminator}", inline=False)
    embed3.add_field(name="Message: ", value =f"`{messageval}`", inline=False)
    embed3.add_field(name="To reply", value = f"Do `;reply {message.author.id} [message]` to respond!")
    channel = client.get_channel(875389872599343124)
    await channel.send(embed=embed3)
  await client.process_commands(message)
@client.command()
async def reply(ctx, member:discord.Member=None, *,message: str=None):
  if member == None:
    await ctx.send("<:bot_cross: 875283979241152532> Please specify a user")
    return False
  if message == None:
    await ctx.send("<:bot_cross: 875283979241152532> Please specify a message!")
    return False
  embed = discord.Embed(title="Mod Reply", color = 0xFFA500)
  embed.add_field(name="To: ", value = member.display_name)
  embed.add_field(name="Reply:", value = message, inline=False)
  embed.set_footer(text="Sending..")
  messagetoreply = await ctx.send(embed=embed)
  await asyncio.sleep(2)
  embed2 = discord.Embed(title="Mod Reply", color = 0x00FF00)
  embed2.add_field(name="To: ", value = member.display_name)
  embed2.add_field(name="Reply:", value = message, inline=False)
  embed2.set_footer(text="Sent to user!")
  await messagetoreply.edit(embed=embed2)
  embed3 = discord.Embed(title="Mod Reply", color=0x0000FF)
  embed3.add_field(name="Mod: ", value=f"{ctx.author.display_name} #{ctx.author.discriminator}", inline=False)
  embed3.add_field(name="Reply: ", value =f"`{message}`", inline=True)
  await member.send(embed=embed3)
TEST_GUILDS = [860471346101616690] # Insert the ID of your guild here

@slash.command(description="View the member count of the server!", guild_ids=TEST_GUILDS)
async def membercount(inter):
    guild = client.get_guild(inter.guild.id)
    await inter.reply(f"{inter.guild.name} is at `{guild.member_count}` members!")
@slash.command(
    guild_ids=TEST_GUILDS,
    description="Shows the avatar of the user",
   
)
async def avatar(inter, user=None):
    # If user is None, set it to inter.author
    user = user or inter.author
    # We are guaranteed to receive a discord.User object,
    # because we specified the option type as Type.USER

    emb = discord.Embed(
        title=f"{user}'s avatar",
        color=inter.author.color
    )
    emb.set_image(url=user.avatar_url)
    await inter.reply(embed=emb)
@client.command()
async def verify(ctx):
  number = await get_code()
  code = random.randrange(9999)
  code = str(code)
  number[str(code)] = []
  number[str(code)]["codeint"] = code
 
  await ctx.send(f"{ctx.author.mention}, check your DMs!")
  with open('verify.json','w') as f:
        json.dump(number,f)
  await ctx.author.send("Hello, please head to https://Modder-Offcial.popqa17.repl.co/verify to verify your account!")
  await ctx.author.send(f"Your code is ||{code}|| Key in the code into the website.")
  row_of_buttons = ActionRow(
        Button(
            style=ButtonStyle.gray,
            label="Done",
            custom_id="done",
            emoji = "👍"
        ),
        Button(
            style=ButtonStyle.gray,
            label="Cancel",
            custom_id="cancel",
            emoji = "❌"
        )
    )
    # Send a message with buttons
  msg = await ctx.author.send(
        f"Once you are done, please click 'done' below. We will then process whether you did or not enter the code. (You have **300** seconds / 5 minutes to key in the code, else your code will be invalidated!",
        components=[row_of_buttons]
  )
  on_click = msg.create_click_listener(timeout=300)
  @on_click.matching_id("done")
  async def check_code(inter):
    if code in number:
      await inter.reply("Your code was not inputted.")
    else:
      await inter.reply("Your code was inputted")
   
  @on_click.matching_id("cancel")
  async def cancel_code(inter):
    try:
      await inter.reply("code cancelled")
    except:
      await inter.reply("Something went wrong while cancelling your code...")
@client.event
async def on_guild_join(guild): #when the bot joins the guild
  with open('prefixes.json', 'r') as f: #read the prefix.json file
    prefixes = json.load(f) #load the json file
  prefixes[str(guild.id)] = '!'#default prefix
  with open('prefixes.json', 'w') as f: #write in the prefix.json "message.guild.id": "bl!"
    json.dump(prefixes, f, indent=4) #the indent is to make everything look a bit neater
  await client.process_commands()
@client.command()
async def login(ctx):

  fetcher = textcaptcha.CaptchaFetcher()
# Fetch a new captcha from the API
  captcha = fetcher.fetch()
  await ctx.send(captcha.question+" (answer in 30 seconds.)")
  def check(msg):
        return msg.author == ctx.author
  try:
   msge = await client.wait_for("message", check=check,timeout=30)
  except asyncio.TimeoutError:
   await ctx.send ("You were too slow.. be faster next time.")
  if captcha.check_answer(msge.content):
    msgauthor = ctx.message.author
    users = await updateuser()
    users[str(msgauthor.id)] = {}
    users[str(msgauthor.id)]["username"] = msgauthor.name
    users[str(msgauthor.id)]["id"] = str(msgauthor.id)
    await ctx.send(f"{ctx.author.mention}, check your dms!")
    await msgauthor.send("Hello, it seems you want to verify. Please key in a password in order to verify yourself in the website.")
    password = await client.wait_for("message", check=check,timeout=30)
    users[str(msgauthor.id)]["password"] = str(password.content)
    with open('users.json','w') as f:
        json.dump(users,f)
    await msgauthor.send("Password sent! Head to https://Modder-Offcial.popqa17.repl.co to verify your account.")
  else:
    await ctx.send ("You failed verification.. well well well. I'll give you another chance.")

@client.event
async def on_guild_remove(guild): #when the bot is removed from the guild
    with open('prefixes.json', 'r') as f: #read the file
        prefixes = json.load(f)

    prefixes.pop(str(guild.id)) #find the guild.id that bot was removed from

    with open('prefixes.json', 'w') as f: #deletes the guild.id as well as its prefix
        json.dump(prefixes, f, indent=4)
    await client.process_commands()

@client.command(pass_context=True)
@has_permissions(administrator=True)
async def changeprefix(ctx, prefix): #command: bl!changeprefix ...
     row_of_buttons = ActionRow(
        Button(
            style=ButtonStyle.green,
            label="Yes, change now.",
            custom_id="placeholdere"
        ),
        Button(
            style=ButtonStyle.red,
            label="No, nevermind.",
            custom_id="red",
        )
    )
    # Send a message with buttons
     msg = await ctx.send(
        f"Change prefix to {prefix}?",
        components=[row_of_buttons]
    )
     def check(inter):
        return inter.message.id == msg.id
     inter = await ctx.wait_for_button_click(check)
    # Send what you received
     button = inter.clicked_button
     if button.custom_id == "placeholdere":
      await inter.reply("Changing prefix..")
      with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

      prefixes[str(ctx.guild.id)] = prefix

      with open('prefixes.json', 'w') as f: #writes the new prefix into the .json
        json.dump(prefixes, f, indent=4)

      await inter.reply(f'Prefix changed to: {prefix}') #confirms the prefix it's been changed to
#next step completely optional: changes bot nickname to also have prefix in the nickname
     elif button.custom_id == "red":
       await ctx.send("Operation cancelled.")

@client.command()
async def react(ctx, emojitype: str, message: discord.Message):
  print ('triggered')
  if emojitype == "tick":
    await message.add_reaction('<a:Tick:860798543248883733>')
    await ctx.send("Reaction added! [Deprecation! p!react will discontinued due to its limited number of pre-defined emojis.]")
  elif emojitype == "cross":
    await message.add_reaction('<Cross:860822357816115210>')
    await ctx.send("Reaction added! [Deprecation! p!react will discontinued due to its limited number of pre-defined emojis.]")
@client.command(pass_context=True)
async def help(ctx):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    prefix = prefixes[str(ctx.guild.id)]
    row = ActionRow(
        Button(
            style=ButtonStyle.gray,
            label="Fun",
            custom_id="fun",
            emoji="🎉"
        ),
        Button(
            style=ButtonStyle.gray,
            label="Economy",
            custom_id="economy",
            emoji="💰"
        ),
        Button(
            style=ButtonStyle.gray,
            label="Moderation",
            custom_id="mod",
            emoji="🛠️"
        )
    )
    msg = await ctx.send("Please choose a help type.", components=[row])

    # Here timeout=60 means that the listener will
    # finish working after 60 seconds of inactivity
    on_click = msg.create_click_listener(timeout=60)

    @on_click.matching_id("fun")
    async def on_test_button(inter):
        await msg.edit(components=[])
        embed=discord.Embed(title="Commands", color=ctx.author.color)
        embed.add_field(name="Fun commands", value="Usable by all members!", inline = False)
        embed.add_field(name="Userinfo", value=f"format: {prefix}userinfo - Find out more information about a particular user!", inline=True)
        embed.add_field(name="Poll", value=f"format: {prefix}poll - Host a poll of up to 5 choices for your friends to enjoy!", inline=True)
        await inter.reply(embed=embed)
    @on_click.matching_id("economy")
    async def on_test_button(inter):
        await msg.edit(components=[])
        embed=discord.Embed(title="Commands", color=ctx.author.color)
        embed.add_field(name="Economy Commands", value="Usable by all members!", inline=False)
        embed.add_field(name="Beg", value=f"format: {prefix}beg - Get a random amount of money!", inline=True)
        embed.add_field(name="Work", value=f"format: {prefix}work - Work and earn cash, the right way.", inline=True)
        embed.add_field(name="Balance", value=f"format: {prefix}balance [user] - Get the balance of a user!", inline=True)
        embed.add_field(name="Shop", value=f"format: {prefix}shop - Get the shop filled with products!", inline=True)
        embed.add_field(name="buy", value=f"format: {prefix}buy [itemname] - Buy an item from the shop!", inline=True)
        await inter.reply(embed=embed)
    @on_click.matching_id("mod")
    async def on_test_button(inter):
        await msg.edit(components=[])
        embed=discord.Embed(title="Commands", color=ctx.author.color)
        embed.add_field(name="Moderator Commands:", value="(If you have the `administrator` permission)", inline = False)
        embed.add_field(name="Mute", value=f"format: {prefix}mute - Mutes a specific user with a reason (optional)", inline=True)
        embed.add_field(name="Unmute", value=f"format: {prefix}unmute - unmutes a specific user.", inline=True)
        embed.add_field(name="Kick", value=f"format: {prefix}kick - kick a specific user.", inline=True)
        embed.add_field(name="Ban", value=f"format: {prefix}ban - Ban a specific user.", inline=True)
        embed.add_field(name="Warn", value=f"format: {prefix}warn [user] - Warn a user.", inline=True)
        embed.add_field(name="Warnings", value=f"format: {prefix}warnings [user] - Get the amount of warnings a user has.", inline=True)
        embed.add_field(name="Delete Warnings", value=f"format: {prefix}deletewarning - Delete a warning from a user.", inline=True)
        embed.add_field(name="Clear Warnings", value=f"format: {prefix}clearwarnings [user] - Clear all warnings from a user.", inline=True)
        await inter.reply(embed=embed)
    @on_click.timeout
    async def on_timeout():
        await msg.edit(components=[])
@client.command(pass_context=True)
async def poll(ctx):
    row = ActionRow(
        Button(
            style=ButtonStyle.gray,
            label="Create a choice",
            custom_id="create",
            emoji="🌟"
        ),
        Button(
            style=ButtonStyle.green,
            label="Send the poll",
            custom_id="continue",
            emoji="📩"
        )
    )
    await ctx.send("Firstly, where would the poll be sent?")
    def check(m):
      return m.author == ctx.author and m.channel == ctx.channel
    msge = await client.wait_for('message', timeout=30.0, check = check)
    c_id = msge.content
    try:
      c_id = int(c_id)
    except:
      await ctx.send("Not a valid channel id! Please redo the command and fill in the right channel id!")
      return
    channel = client.get_channel(c_id)
    await ctx.send("What will be the poll's question?")
    pollQ = await client.wait_for('message', timeout=30.0, check = check)
    msg =  await ctx.send("Choose your next move. Create a new choice, or continue with the poll?", components=[row])
    on_click = msg.create_click_listener(timeout=60)
    embed = discord.Embed(title=f"New poll by{ctx.author}!", color=ctx.author.color)
    embed.add_field(value=f"Question: ***{pollQ.content}***", name="** **", inline=False)
    @on_click.matching_id("create")
    async def oncreate(inter):
      await inter.reply("What will be your choice?")
      choice = await client.wait_for('message', timeout=30.0, check = check)
      embed.add_field(name="** **", value=f"{choice.content}", inline=False)
      e2 = discord.Embed(title="Sucess!")
      e2.add_field(name="** **", value=f"Choice added! [Click me](https://discordapp.com/channels/{ctx.guild.id}/{ctx.channel.id}/{msg.id}) to add a new choice!")
      await ctx.send(embed=e2)
    @on_click.matching_id("continue")
    async def on_continue(inter):
      await inter.reply("Sending poll..")
      embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Hosted by {ctx.author}")
      embed.timestamp = datetime.datetime.utcnow()
      pollmsg = await channel.send(embed=embed)
      await pollmsg.add_reaction("1️⃣")
      await pollmsg.add_reaction("2️⃣")
      await pollmsg.add_reaction("3️⃣")
      await pollmsg.add_reaction("4️⃣")
      await pollmsg.add_reaction("5️⃣")
    @on_click.not_from_user(ctx.author, cancel_others=True, reset_timeout=False)
    async def on_wrong_user(inter):
      await inter.reply("Your not the hoster...", ephemeral=True)

@client.command()
async def webhook_test(ctx):
  webhook_url = 'https://hook.integromat.com/lqztt2rmpjut8lt8b25v9cyii6ut0f9l'
  data = { 'name': 'This is an example for webhook' }
  requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})




@client.command()
async def say(ctx):
 users = await get_config_data()
 if users[str(ctx.guild.id)]["Fun"] == "on":
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name=f"United Kingdom. u!help for commands"))
  def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel
  def check2(msge):
      return msge.author == ctx.author and msge.channel == ctx.channel
  await ctx.send("What do you want to say? (answer within `120` secconds!")
  msg = await client.wait_for("message", check=check ,timeout=120)
  await ctx.send("where do you want your message to be sent? (Please copy and paste the channel id.")
  msge = await client.wait_for("message", check=check2,timeout=120)
  try:
    msgeee = int(msge.content)
    msgeee = client.get_channel(msgeee)
    await msgeee.send(f"{ctx.author.mention} said: "+msg.content)
  except:
    await ctx.send("<a:Dont:830295611202732053> That was not a valid channel id!")

@client.command()

async def setup(ctx):
 guild = ctx.guild
 if get(ctx.guild.roles, name="Poll Host"):
  await ctx.send("<a:Dont:830295611202732053> Role already created!")
 else:
  status = await ctx.send("<a:Loading:860791183243345930> Creating roles..")
  await guild.create_role(name="Poll Host")
  await asyncio.sleep(2000)
  await status.edit(content="Roles created!")




@client.command()
async def kick(ctx, username: discord.Member):
 authorperms = ctx.author.guild_permissions
 if authorperms.administrator:
   try:
    await ctx.guild.kick(username)
    await ctx.send("This user has been kicked!")
   except:
        await ctx.send(f"Something went wrong in the process..")
 else:
    await ctx.send(" <:bot_cross:875283979241152532> You do not have the valid permissions!")
@client.command()
async def ban(ctx, member:discord.Member):
 authorperms = ctx.author.guild_permissions
 if authorperms.administrator:


  try:
    await username.ban(reason="none")
    await ctx.send("This user has been banned!")
  except:
    await ctx.send("Something went wrong in the process..")
 else:
    await ctx.send(" <:bot_cross:875283979241152532> You do not have the valid permissions!")
@client.command()
@has_permissions(administrator=True)
async def unban(ctx, *, member):
  users = await get_config_data()
  if users[str(ctx.guild.id)]["Mod"] == "on":

     banned_users = await ctx.guild.bans()
     member_name, member_discriminator = member.split("#")
     for ban_entry in banned_users:
      user = ban_entry.user
      if (user.name, user.discriminator) == (member_name, member_discriminator):
        await ctx.guild.unban(user)
        await ctx.send(f'Unbanned {user.mention}')
        return
@client.command()
async def apply(ctx):
 se = ctx.author.send
 role = discord.utils.find(lambda r: r.name == 'App Blacklist', ctx.message.guild.roles)
 role2 = discord.utils.find(lambda r: r.name == 'App Cooldown', ctx.message.guild.roles)
 if role in ctx.author.roles:
  await ctx.send("You have been blacklisted from taking applications.")
 elif role2 in ctx.author.roles:
  await ctx.send("You already have an app in review. Try again if your app has been denied.")
 else:
  await se("Avaliable applications (please type the number):\n1. App Reviewer Application")
  def check(msg):
    return msg.author == ctx.author
  await ctx.send(f"{ctx.author.mention}, Please check your DMs!")
  msge = await client.wait_for("message")
  if msge.content == "0":
   await ctx.author.add_roles(discord.utils.get(ctx.author.guild.roles, name="App Cooldown"))
   Q1hint = await se("Why do you want to be a mod?")
   Q1 = await client.wait_for("message", check=check)
   Q2hint =  await se("Why should we choose you?")
   Q2 = await client.wait_for("message",check=check)
   Q3hint =  await se("how can you benefit us?")
   Q3 = await client.wait_for("message",check=check)
   Q4hint =  await se("What will be your first course of action as a Moderator?")
   Q4 = await client.wait_for("message",check=check)
   Q5hint = await se("Will you abuse your power? Why or why not?")
   Q5 = await client.wait_for("message",check=check)
   await se("Thanks for submitting your application! We appreciate the time you took to do this app. This is just a confirmation message to tell you that it has been received by our App Reviewers!")
   channel = client.get_channel(867796698993524756)
   await channel.send(f"<@&867720995195191306> **New submission! (mod)** \n\n Subitted by: {ctx.message.author}\n\n `Why do you want to be a mod?`\n\n"+Q1.content+"\n\n `Why should we choose you?`\n\n"+Q2.content+"\n\n`"+Q3hint.content+"`\n\n"+Q3.content+"\n\n`"+Q4hint.content+"`\n\n"+Q4.content+"`\n\n"+Q5hint.content+"`\n\n"+ Q5.content)
   controlmsg = await channel.send('React to this message with either a ✅ or a ❌ to accept /  deny.')
   await controlmsg.add_reaction('✅')
   await controlmsg.add_reaction('❌')
   await asyncio.sleep(2)
   def check3(reaction, user):
            return str(reaction.emoji) == '✅' or str(reaction.emoji) == '❌'
   reaction, user = await client.wait_for('reaction_add',check=check3)
   if reaction.emoji == "✅":
     await controlmsg.remove_reaction('✅',client.user)
     await channel.send("The application has successfully approved!")
     role = "Moderator"
     user = str(user)
     await se("🎉Your application has been approved by "+user+"!🎉")
     await ctx.author.remove_roles(discord.utils.get(ctx.author.guild.roles, name="App Cooldown"))
     await ctx.author.add_roles(discord.utils.get(ctx.author.guild.roles, name="Moderator"))
     
   elif reaction.emoji == "❌":
     await controlmsg.remove_reaction('❌', client.user)
     await channel.send(user.mention +", why did you deny the application?")
     channel2 = client.get_channel(867719982652325918)
     def check34(msg):
        return msg.author == user
     reason = await client.wait_for("message", check=check34)
     await channel.send(f"{user.mention}, your Moderator application was sucessfully denied.")
     await channel2.send(f"{user.mention} denied {ctx.author.mention}'s' Mod Application!")
     user = str(user)
     await se(f"{ctx.author.mention}, your application was denied by"+ user + " (app reviewer) as: \n\n"+reason.content)
     await ctx.author.remove_roles(discord.utils.get(ctx.author.guild.roles, name="App Cooldown"))
  elif msge.content == "1":
   await ctx.author.add_roles(discord.utils.get(ctx.author.guild.roles, name="App Cooldown"))
   Q1hint = await se("Why do you want to be a app reviewer?")
   Q1 = await client.wait_for("message", check=check)
   Q2hint =  await se("Why should we choose you?")
   Q2 = await client.wait_for("message",check=check)
   Q3hint =  await se("how can you benefit us?")
   Q3 = await client.wait_for("message",check=check)
   Q4hint =  await se("Wil you accept applications fairly? Why?")
   Q4 = await client.wait_for("message",check=check)
   Q5hint = await se("Will you accept applications regularly? Why?")
   Q5 = await client.wait_for("message",check=check)
   await se("Thanks for submitting your application! We appreciate the time you took to do this app. This is just a confirmation message to tell you that it has been received by our App Reviewers!")
   channel = client.get_channel(867796698993524756)
   await channel.send(f"<@&867720995195191306> **New submission! (app reviewer)** \n\n Subitted by: {ctx.message.author}\n\n `Why do you want to be a app reviewer?`\n\n"+Q1.content+"\n\n `Why should we choose you?`\n\n"+Q2.content+"\n\n`"+Q3hint.content+"`\n\n"+Q3.content+"\n\n`"+Q4hint.content+"`\n\n"+Q4.content+"`\n\n"+Q5hint.content+"`\n\n"+ Q5.content)
   controlmsg = await channel.send('React to this message with either a ✅ or a ❌ to accept /  deny.')
   await controlmsg.add_reaction('✅')
   await controlmsg.add_reaction('❌')
   await asyncio.sleep(2)
   def check3(reaction, user):
            return str(reaction.emoji) == '✅' or str(reaction.emoji) == '❌'
   reaction, user = await client.wait_for('reaction_add',check=check3)
   if reaction.emoji == "✅":
     await controlmsg.remove_reaction('✅',client.user)
     await channel.send("The application has successfully approved!")
     user = str(user)
     await se("🎉Your application has been approved by "+user+"!🎉")
     await ctx.author.remove_roles(discord.utils.get(ctx.author.guild.roles, name="App Cooldown"))
     await ctx.author.add_roles(discord.utils.get(ctx.author.guild.roles, name="App Reviewer"))
     
   elif reaction.emoji == "❌":
     await controlmsg.remove_reaction('❌', client.user)
     await channel.send(user.mention +", why did you deny the application?")
     channel2 = client.get_channel(867719982652325918)
     def check34(msg):
        return msg.author == user
     reason = await client.wait_for("message", check=check34)
     await channel.send(f"{user.mention}, your application was sucessfully denied.")
     await channel2.send(f"{user.mention} denied {ctx.author.mention}'s' App Reviewer Application!")
     user = str(user)
     await se(f"{ctx.author.mention}, your App Reviewer application was denied by"+ user + " (app reviewer) as: \n\n"+reason.content)
     await ctx.author.remove_roles(discord.utils.get(ctx.author.guild.roles, name="App Cooldown"))
@client.command()
async def ping(ctx):
    await ctx.send(f'Current ping: {client.latency} seconds!')

@client.command(description="Mutes a user.")
async def mute(ctx, member: discord.Member, *, reason=None):
  authorperms = ctx.author.guild_permissions
  if authorperms.administrator: 
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)      
    else:
      await member.add_roles(mutedRole, reason=reason)
      log = client.get_channel(870263865055793162)
      await ctx.send(f"{member.mention} has been muted.")
      channel = client.get_channel(873607765711519855)
      embed =discord.Embed(title="Moderator Action", color=0xff0000)
      embed.add_field(name="User muted!", value=f"By: {ctx.author} \n Muted: {member.name} \n For: `{reason}`")
      embed.set_footer(icon_url = f"{client.user.avatar_url}", text = f"Mod logs {client.user.name}")
      embed.timestamp = datetime.datetime.utcnow()
      await channel.send(embed=embed)
      await member.send(f"You were muted in {guild.name} for `{reason}`")

  else:
    await ctx.send(" <:bot_cross:875283979241152532> You do not have the valid permissions!")
@client.command(description="Unmutes a user.")
async def unmute(ctx, member: discord.Member):
  authorperms = ctx.author.guild_permissions
  if authorperms.administrator:
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
    log = client.get_channel(870263865055793162)
    await member.remove_roles(mutedRole)
    await ctx.send(f"{member.mention} has been unmuted.")
    channel = client.get_channel(873607765711519855)
    embed =discord.Embed(title="Moderator Action", color=0x00FF00)
    embed.add_field(name="User unmuted!", value=f"By: {ctx.author} \n To: {member.name}")
    embed.set_footer(icon_url = f"{client.user.avatar_url}", text = f"Mod logs {client.user.name}")
    embed.timestamp = datetime.datetime.utcnow()
    await channel.send(embed=embed)
    await member.send(f"You were unmuted in the server {ctx.guild.name}")

  else:
    await ctx.send(" <:bot_cross:875283979241152532> You do not have the valid permissions!")
async def createwarndata(user):

    users = await getwarndata()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["warnings"] = 0

    with open('warnings.json','w') as f:
        json.dump(users,f, indent=4)

    return True


async def getwarndata():
    with open('warnings.json','r') as f:
        users = json.load(f)

    return users


async def updatewarndata(user,change=0,mode = 'warnings'):
    users = await getwarndata()

    users[str(user.id)][mode] += change

    with open('warnings.json','w') as f:
        json.dump(users,f, indents=4)
    bal = users[str(user.id)]['warnings'],users[str(user.id)]['bank']
    return bal
@client.command(aliases=['warns'])
async def warnings(ctx, member: discord.Member):
    await createwarndata(member)

    users = await getwarndata()

    wallet_amt = users[str(member.id)]["warnings"]

    em = discord.Embed(title=f'{member.name}:',color = discord.Color.red())
    em.add_field(name="Warnings: ", value=wallet_amt)
    await ctx.send(embed= em)

@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
@client.command()
async def editnick(ctx, member: discord.Member , nickname:str):
 authorperms = ctx.author.guild_permissions
 if authorperms.administrator:
    await member.edit(nick=f"! {nickname}")
    await ctx.send("Nickname has been edited!")
    channel = client.get_channel(873607765711519855)
    embed =discord.Embed(title="Moderator Action", color=ctx.author.color)
    embed.add_field(name="User's Nickname edited!", value=f"Moderator: {ctx.author} \n Moderated: {member.name} \n New nickname: `{member.display_name}`")
    embed.set_footer(icon_url = f"{client.user.avatar_url}", text = f"Mod logs {client.user.name}")
    embed.timestamp = datetime.datetime.utcnow()
    await channel.send(embed=embed)
 else:
   await ctx.send(" <:bot_cross:875283979241152532> You do not have the valid permissions!")
@client.command()
async def modnick(ctx, member: discord.Member=None):
 authorperms = ctx.author.guild_permissions
 if authorperms.administrator:
  if member==None:
    await ctx.send("Please a member!")
  else:
    await member.edit(nick=f"! Moderated Nickname")
    await ctx.send("Nickname has been moderated!")
    channel = client.get_channel(873607765711519855)
    embed =discord.Embed(title="Moderator Action", color=ctx.author.color)
    embed.add_field(name="User's Nickname Moderated!", value=f"Moderator: {ctx.author} \n Moderated: {member.name} \n New nickname: `{member.display_name}`")
    embed.set_footer(icon_url = f"{client.user.avatar_url}", text = f"Mod logs {client.user.name}")
    embed.timestamp = datetime.datetime.utcnow()
    await channel.send(embed=embed)
 else:
   await ctx.send(" <:bot_cross:875283979241152532> You do not have the valid permissions!")
@client.command()
async def warn(ctx, member: discord.Member, *, reason):
  authorperms = ctx.author.guild_permissions
  if authorperms.administrator:
    await createwarndata(member)
    
    user = member
    users = await getwarndata()

    earnings = 1

    await ctx.send(f' <:bot_correct:875284201937727499> {ctx.author.mention} Warned {user.mention}!')

    users[str(user.id)]["warnings"] += earnings
    
    with open("warnings.json",'w') as f:
        json.dump(users,f, indent=4)
    channel = client.get_channel(873607765711519855)
    embed =discord.Embed(title="Moderator Action", color=0xff0000)
    embed.add_field(name="User warned!", value=f"Moderator: {ctx.author} \n To: {member.name} \n For: `{reason}`")
    embed.set_footer(icon_url = f"{client.user.avatar_url}", text = f"Mod logs {client.user.name}")
    embed.timestamp = datetime.datetime.utcnow()
    await channel.send(embed=embed)
  else:
    await ctx.send(" <:bot_cross:875283979241152532> You do not have the valid permissions!")
@client.command()
async def membercount(ctx):
  guild = client.get_guild(ctx.guild.id)
  await ctx.send(f"{ctx.guild.name} is at `{guild.member_count}` members!")
@client.command()
async def removewarning(ctx, member: discord.Member, amt:str):
 authorperms = ctx.author.guild_permissions
 if authorperms.administrator:
  if ctx.author == member:
   await ctx.send("You can't remove your own warnings...")
  else:
    user = member
    await createwarndata(member)
    amt = int(amt)
    users = await getwarndata()
    removed = users[str(member.id)]["warnings"] - amt
    users[str(user.id)]["warnings"] = removed
    warnings = users[str(user.id)]["warnings"]
    await ctx.send(f"removed `{amt}` warning(s) from {member.name}! He/ She currently have `{warnings}` warning(s).")
    with open('warnings.json','w') as f:
        json.dump(users,f, indent=4)
 else:
    await ctx.send(" <:bot_cross:875283979241152532> You do not have the valid permissions!")
@client.command()
@has_permissions(administrator=True)
async def clearwarnings(ctx, member: discord.Member):
  if ctx.author == member:
    await ctx.send("You can't clear your own warnings...")
  else:
    user = member
    await createwarndata(member)
    users = await getwarndata()
    users[str(user.id)]["warnings"] = 0
    await ctx.send(f"cleared {member.name}'s warnings!")
    with open('warnings.json','w') as f:
        json.dump(users,f, indent=4)
mainshop = [{"name":"DJ","price":1000,"description":'Get access to rythm!'}, {"name":"Diamond","price":10000,"description":'Super expensive, can be bought multiple times.'},{"name":"Mona-Lisa","price":1000000,"description":'Crazy expensive, yet crazy rare!'}]
@client.command(aliases=['bal'])
async def balance(ctx, member: discord.Member=None):
  try:
    await open_account(member)
    user = member
    users = await get_bank_data()
    ownself = True
  except:
    user = ctx.author
    await open_account(user)
    users = await get_bank_data()
    ownself = False
  wallet_amt = users[str(user.id)]["wallet"]
  bank_amt = users[str(user.id)]["bank"]
  if ownself == True:
    user = member.name
  else:
    user = ctx.author
  em = discord.Embed(title=f'{user}:',color = discord.Color.red())
  em.add_field(name="Wallet Balance", value=wallet_amt)
  em.add_field(name='Bank Balance',value=bank_amt)
  await ctx.send(embed= em)
@client.command()
async def beg(ctx):
  role2 = discord.utils.find(lambda r: r.name == 'beg cooldown', ctx.message.guild.roles)
  print("trigered 2")
  if role2 in ctx.author.roles:
    print("cooldown")
    await ctx.send("You are under `45` seconds cooldown.")
  else:
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(101)

    await ctx.send(f'{ctx.author.mention} Got {earnings} Bitcoin!!')

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json",'w') as f:
        json.dump(users,f)
    await ctx.author.add_roles(discord.utils.get(ctx.author.guild.roles, name="beg cooldown"))
    await asyncio.sleep(45)
    await ctx.author.remove_roles(discord.utils.get(ctx.author.guild.roles, name="beg cooldown"))
@client.command(aliases=['wd'])
async def withdraw(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[1]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    await update_bank(ctx.author,amount)
    await update_bank(ctx.author,-1*amount,'bank')
    await ctx.send(f'{ctx.author.mention} You withdrew {amount} Bitcoin')
@client.command(aliases=['dep'])
async def deposit(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    await update_bank(ctx.author,-1*amount)
    await update_bank(ctx.author,amount,'bank')
    await ctx.send(f'{ctx.author.mention} You deposited {amount} Bitcoin')
@client.command()
async def send(ctx,member : discord.Member,amount = None):
  role2 = discord.utils.find(lambda r: r.name == 'send cooldown', ctx.message.guild.roles)
  print("trigered 2")
  if role2 in ctx.author.roles:
    print("cooldown")
    await ctx.send("You are under `45` seconds cooldown.")
  else:
    await open_account(ctx.author)
    await open_account(member)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)
    if amount == 'all':
        amount = bal[0]

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    await update_bank(ctx.author,-1*amount,'wallet')
    await update_bank(member,amount,'wallet')
    await ctx.send(f'{ctx.author.mention} You gave {member} {amount} Bitcoin')
    await ctx.author.add_roles(discord.utils.get(ctx.author.guild.roles, name="send cooldown"))
    await asyncio.sleep(45)
    await ctx.author.remove_roles(discord.utils.get(ctx.author.guild.roles, name="send cooldown"))
@client.command(aliases=['rb'])
async def rob(ctx,member : discord.Member):
  print("triggered")
  role2 = discord.utils.find(lambda r: r.name == 'interactive cooldown', ctx.message.guild.roles)
  print("trigered 2")
  if role2 in ctx.author.roles:
    print("cooldown")
    await ctx.send("You are under `45` seconds cooldown.")
  else:
    await open_account(ctx.author)
    await open_account(member)
    bal = await update_bank(member)
    if bal[0]<10001:
        await ctx.send('It is useless to rob him :(')
        return
    bal2 = bal[0] - 10000
    earning = random.randrange(1,bal2)

    await update_bank(ctx.author,earning)
    await update_bank(member,-1*earning)
    await ctx.send(f'{ctx.author.mention} You robbed {member} and got {earning} Bitcoin')
    await ctx.author.add_roles(discord.utils.get(ctx.author.guild.roles, name="interactive cooldown"))
    await asyncio.sleep(45)
    await ctx.author.remove_roles(discord.utils.get(ctx.author.guild.roles, name="interactive cooldown"))
@client.command()
async def shop(ctx):
    em = discord.Embed(title = "Shop")

    for item in mainshop:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        em.add_field(name = name, value = f"${price} | {desc}")

    await ctx.send(embed = em)
@client.command()
async def buy(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await buy_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("That Object isn't there!")
            return
        if res[1]==2:
            await ctx.send(f"You don't have enough Bitcoin in your wallet to buy {amount} {item}")
            return

    await ctx.send(f"You just bought {amount} {item}")
    if item == "DJ":
      await ctx.author.add_roles(discord.utils.get(ctx.author.guild.roles, name="DJ"))
@client.command()
async def inv(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []


    em = discord.Embed(title = "Inventory")
    for item in bag:
        name = item["item"]
        amount = item["amount"]

        em.add_field(name = name, value = amount)    

    await ctx.send(embed = em)


async def buy_this(user,item_name,amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0]<cost:
        return [False,2]


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            obj = {"item":item_name , "amount" : amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item":item_name , "amount" : amount}
        users[str(user.id)]["bag"] = [obj]        

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost*-1,"wallet")

    return [True,"Worked"]
async def open_account(user):

    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 1000
        users[str(user.id)]["bank"] = 10000

    with open('mainbank.json','w') as f:
        json.dump(users,f)

    return True


async def get_bank_data():
    with open('mainbank.json','r') as f:
        users = json.load(f)

    return users


async def update_bank(user,change=0,mode = 'wallet'):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open('mainbank.json','w') as f:
        json.dump(users,f)
    bal = users[str(user.id)]['wallet'],users[str(user.id)]['bank']
    return bal
@client.command()
async def work(ctx):
  role = discord.utils.find(lambda r: r.name == 'Work Cooldown', ctx.message.guild.roles)
  if role in ctx.author.roles:
    await ctx.send("You are under cooldown. Wait `45` more seconds before you proceed.")
  else:
    await open_account(ctx.author)
    user = ctx.author.id

    users = await get_bank_data()

    earnings = random.randrange(10000)

    await ctx.send(f'{ctx.author.mention} Got {earnings} Bitcoin!!')
    await ctx.author.add_roles(discord.utils.get(ctx.author.guild.roles, name="Work Cooldown"))
    users[str(user)]["wallet"] += earnings
    await asyncio.sleep(45)
    await ctx.author.remove_roles(discord.utils.get(ctx.author.guild.roles, name="Work Cooldown"))

    with open("mainbank.json",'w') as f:
        json.dump(users,f)
@client.command()
async def reset_all(ctx, member: discord.Member):
 role2 = discord.utils.find(lambda r: r.name == 'Money Manager', ctx.message.guild.roles)
 if role2 in ctx.author.roles:
  await ctx.send("THIS WILL RESET SOMEONE'S CASH TO 0! ARE YOU SURE? (y/n)")
  def check(msg):
        return msg.author == ctx.author
  decision = await client.wait_for('message', check = check)
  if decision.content == "y":
        await ctx.send("attempting to reset..")
        users = await get_bank_data()
        await ctx.send("Json fetched...")
        user = member
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0
        await ctx.send("CASH RESETTED.")
        with open("mainbank.json",'w') as f:
          json.dump(users,f)
  elif decision.content == "n":
    await ctx.send("OPERATION CANCELLED.")
 else:
   await ctx.send("You don't have the perms..")
@client.command()
async def top_up(ctx, member:discord.Member, amt):
 role2 = discord.utils.find(lambda r: r.name == 'Money Manager', ctx.message.guild.roles)
 if role2 in ctx.author.roles:
  await ctx.send("Attempting to get data..")
  amt = int(amt)
  users = await get_bank_data()
  await ctx.send("Json fetched...")
  user = member
  totalamt =  users[str(user.id)]["wallet"] + amt
  users[str(user.id)]["wallet"] = totalamt 
  await ctx.send("CASH Topped-up.")
  with open("mainbank.json",'w') as f:
          json.dump(users,f)
 else:
   await ctx.send("You don't have the perms..")
@client.command()
async def invite(ctx):
  em = discord.Embed(title="Invite", desciption="Add the bot!", color=ctx.author.color)
  em.add_field(value="[Invite the bot](https://discord.com/api/oauth2/authorize?client_id=861159291523301377&permissions=8&scope=bot) | [Website](https://sites.google.com/view/poller-discord/home) | [Support server](https://discord.gg/tr6DHNNG7S)", name="** **")
  avatar = str(client.user.avatar_url)
  em.set_thumbnail(url=avatar)
  await ctx.send(embed=em)


@client.command()
async def purge(ctx, amt:int):
      await ctx.message.delete()
      await ctx.channel.purge(limit=amt)
@client.command()
async def userinfo(ctx,member: discord.Member = None):
    if member == None:
      member = ctx.author
    roles = [role for role in member.roles[1:]]
    embed = discord.Embed(
    color = discord.Color(0xff3400),
    title = f"{member.name}")
    if str(member.status) == "dnd":
      emoji = "⛔ Do Not Disturb"
    elif str(member.status) == "online":
      emoji = "✅ Online"
    elif str(member.status) == "idle":
      emoji = "🌙 Idle"
    elif str(member.status) == "offline":
      emoji = "❌Offline"
    embed.add_field(name="**•ID•**", value=f"{member.id}", inline=True)

    embed.add_field(name="**•Status•**", value=emoji, inline=True)
    embed.set_thumbnail(url=f"{member.avatar_url}")
    embed.add_field(name=f"**•Roles• ({len(member.roles) - 1})**", value='• '.join([role.mention for role in roles]), inline=False)
    datetime_format = "%a, %d/%b/%Y"
    embed.add_field(name="**•Account Created At•**", value=f"{member.created_at.strftime(datetime_format)}".replace("-", "/"), inline=True)
    embed.add_field(name="**•Joined Server At•**", value=f"{member.joined_at.strftime(datetime_format)}".replace("-", "/"), inline = True)
    embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Requested by {ctx.author}")
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)

async def get_config_data():
    with open('configs.json','r') as f:
        configs = json.load(f)

    return configs
@client.command()
async def config(ctx):
  users = await get_config_data()
  if str(ctx.guild.id) in users:
        embed = discord.Embed(title="Configurations: ", color=ctx.author.color)
        embed.add_field(name="Mod", value = users[str(ctx.guild.id)]["Mod"])
        embed.add_field(name="Fun", value = users[str(ctx.guild.id)]["Fun"])
        embed.add_field(name="Economy", value = users[str(ctx.guild.id)]["Economy"])
        embed.add_field(name="Verify", value = users[str(ctx.guild.id)]["Verify"])
        await ctx.send(embed=embed)
  else:
        users[str(ctx.guild.id)] = {}
        users[str(ctx.guild.id)]["Mod"] = "on"
        users[str(ctx.guild.id)]["Fun"] = "on"
        users[str(ctx.guild.id)]["Economy"] = "on"
        users[str(ctx.guild.id)]["Verify"] = "off"
        with open('configs.json','w') as f:
          json.dump(users,f)
          await ctx.send(f"{ctx.guild.name} is now configured with Modder!")
          return True
@client.command()
async def edit_config(ctx, configtype:str=None):
  users = await get_config_data()
  if configtype is None:
    await ctx.send("Please choose a config type, like `mod`, `economy`, `fun` and `verify`")
  elif configtype == "mod":
    if users[str(ctx.guild.id)]["Mod"] == "on":
      users[str(ctx.guild.id)]["Mod"] = "off"
      await ctx.send("Moderation commands are now `off`")
      with open('configs.json','w') as f:
          json.dump(users,f)
    elif users[str(ctx.guild.id)]["Mod"] == "off":
      users[str(ctx.guild.id)]["Mod"] = "on"
      await ctx.send("Moderation commands are now `on`")
      with open('configs.json','w') as f:
          json.dump(users,f)
  elif configtype == "economy":
    if users[str(ctx.guild.id)]["Economy"] == "on":
      users[str(ctx.guild.id)]["Economy"] = "off"
      
      await ctx.send("Economy commands are now `off`")
      with open('configs.json','w') as f:
          json.dump(users,f)
    elif users[str(ctx.guild.id)]["Economy"] == "off":
      users[str(ctx.guild.id)]["Economy"] = "on"
      
      await ctx.send("Economy commands are now `on`")
      with open('configs.json','w') as f:
          json.dump(users,f)
  elif configtype == "fun":
    if users[str(ctx.guild.id)]["Fun"] == "on":
      users[str(ctx.guild.id)]["Fun"] = "off"
      await ctx.send("Fun commands are now `off`")
      with open('configs.json','w') as f:
          json.dump(users,f)
    elif users[str(ctx.guild.id)]["Fun"] == "off":
      users[str(ctx.guild.id)]["Fun"] = "on"
      await ctx.send("Fun commands are now `on`")
      with open('configs.json','w') as f:
          json.dump(users,f)
  elif configtype == "verify":
    await ctx.send("WIP!")
    with open('configs.json','w') as f:
          json.dump(users,f)

@commands.Cog.listener()
async def on_member_join(self, member):
    for channel in member.guild.channels:
        if str(channel) == "👋┃joins-n-leaves":
            embed = discord.Embed(color=0x4a3d9a)
            embed.add_field(name="Welcome", value=f"{member.name} has joined {member.guild.name}", inline=False)
            embed.set_image(url="https://cdn.discordapp.com/attachments/860514083219308564/875640930194034718/This_is_HypnoKillers_Cult..png")
            await channel.send(embed=embed)

keep_alive()
my_secret = os.environ['TOKEN']
client.run(my_secret)