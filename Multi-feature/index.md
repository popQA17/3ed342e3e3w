# Emoji Index 

- <:bot_cross: 875283979241152532> -> Default Wrong Bot emoji
- <:bot_correct: 875284201937727499> -> Default Correct Bot emoji

# Quick referring index

## If statements:
```py
authorperms = ctx.author.guild_permissions
  if authorperms.administrator:
    #extra code
  else:
    await ctx.send(" <:bot_cross:875283979241152532> You do not have the valid permissions!")
```

## Logs:
### Moderation
```py
channel = client.get_channel(873607765711519855)
embed =discord.Embed(title="Moderator Action", color=ctx.author.color)
embed.add_field(name="User warned!", value=f"By: {ctx.author} \n To: {member.name}")
embed.set_footer(icon_url = f"{client.user.avatar_url}", text = f"Mod logs {client.user.name}")
embed.timestamp = datetime.datetime.utcnow()
await channel.send(embed=embed)
```

## Colors:

- Red (strong action) -> 0xff0000

- Green (Sucessful action) -> 0x00FF00