import discord
import datetime
from discord.ext import commands 
from colorama import Fore, init
from datetime import datetime






init()

intents = discord.Intents.all()
intents.message_content = True
intents.reactions = True

bot = commands.Bot(command_prefix=".", intents=intents)

token = ""

logchatid = 000

admin = 000        

now = datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")

#--------------------------------- On ready

@bot.event
async def  on_ready():

    logchat = bot.get_channel(logchatid)

    print(Fore.GREEN + f"Secutiry is On /  : {now}")

    embed = discord.Embed(
        title="Security Stats"
        
    )

    embed.add_field(
        name="**Stats**",
        value="On / :green_square:",
        inline=False
    )

    embed.add_field(
        name="**Hour**",
        value=f"```{now}```",
        inline=False
    )

    embed.set_footer(text="StormMint Security ©")

    await logchat.send(embed=embed)


@bot.event
async def on_message_delete(message):

    logchat = bot.get_channel(logchatid)

    autor = message.author.name
    texto = message.content
    foto = message.author.display_avatar.url
    imagem = message.attachments
    canal = message.channel

    embed = discord.Embed(
        title=f"Mensagem deletada / #{canal}",
        description=f"```{texto}```",
        color=0xff0000
        
    )

    embed.add_field(
        name="Autor",
        value=f"@{autor}"
    )


    embed.set_footer(text=f"{now} / StormMint Security ©")
    
    if message.attachments:
        embed.set_image(url=message.attachments[0].url)

    embed.set_author(name=autor, icon_url=foto,)

    await logchat.send(embed=embed)
    

@bot.event
async def on_reaction_remove(reaction, user):

    logchat = bot.get_channel(logchatid)

    message = reaction.message

    autor = message.author.name
    texto = message.content or "Sem texto"
    foto = message.author.display_avatar.url
    canal = message.channel.name

    embed = discord.Embed(
        title=f"Reação removida / #{canal}",
        description=f"```{texto}```",
        color=0xff0000
    )

    embed.add_field(
        name="Autor",
        value=user.mention
    )

    embed.add_field(
        name="Emoji",
        value=str(reaction.emoji)
    )

    embed.set_author(name=autor, icon_url=foto,)

    embed.set_footer(text=f"{now} / StormMint Security ©")

    await logchat.send(embed=embed)


@bot.event
async def on_reaction_add(reaction, user):

    logchat = bot.get_channel(logchatid)

    message = reaction.message

    autor = message.author.name
    texto = message.content or "Sem texto"
    foto = message.author.display_avatar.url
    canal = message.channel.name

    embed = discord.Embed(
        title=f"Reação adicionada / #{canal}",
        description=f"```{texto}```",
        color=0x69f048
    )

    embed.add_field(
        name="Autor",
        value=user.mention
    )

    embed.add_field(
        name="Emoji",
        value=str(reaction.emoji)
    )

    embed.set_author(name=autor, icon_url=foto,)

    embed.set_footer(text=f"{now} / StormMint Security ©")

    await logchat.send(embed=embed)

@bot.event
async def on_message_edit(before, after):

    if before.content == after.content:
        return

    logchat = bot.get_channel(logchatid)

    autor = after.author.name
    foto = after.author.display_avatar.url
    canal = after.channel

    embed = discord.Embed(
        title=f"Mensagem editada / #{canal.name}",
        color=0xFBBC05
    )

    embed.set_author(name=autor, icon_url=foto)

    embed.add_field(
        name="- Antes",
        value=f"```{before.content}```",
        inline=False
    )

    embed.add_field(
        name="- Depois",
        value=f"```{after.content}```",
        inline=False
    )

    embed.add_field(
        name="Autor",
        value=after.author.mention
    )

    embed.set_footer(text=f"{now} / StormMint Security ©")

    await logchat.send(embed=embed)


@bot.event
async def on_member_join(membro: discord.Member):
    guild = membro.guild
    hi = guild.get_member(admin)
    if membro.bot:
        await membro.kick(reason="Bots não são permitidos")
        log = bot.get_channel(logchatid)
        await log.send(f"{hi.mention} API detectada! ({membro.mention})")

@bot.event
async def on_voice_state_update(member, before, after):
    
    log_chat = bot.get_channel(logchatid)

    if log_chat is None:
        return

    if before.channel == after.channel:
        return

    embed = discord.Embed(
        title=f"Chamada de voz update / {now}"
    )

    embed.set_author(
        name=str(member),
        icon_url=member.avatar.url if member.avatar else None
    )

    if before.channel is None:
        embed.title = " Entrou na chamada"
        embed.description = f"{member.mention} entrou em `{after.channel.name}`"
        embed.color = discord.Color.green()
        embed.set_footer(text=f"{now} / StormMint Security ©")

    elif after.channel is None:
        embed.title = "Saiu da chamada"
        embed.description = f"{member.mention} saiu de `{before.channel.name}`"
        embed.color = discord.Color.red()
        embed.set_footer(text=f"{now} / StormMint Security ©")

    else:
        embed.title = "Mudou de chamada"
        embed.description = (
            f"{member.mention} saiu de `{before.channel.name}`\n"
            f"Entrou em `{after.channel.name}`"
        )
        embed.color = discord.Color.blue()
        embed.set_footer(text=f"{now} / StormMint Security ©")

    await log_chat.send(embed=embed)
    return

@bot.command()
async def sayadmin1(ctx:commands.Context, texto):
    await ctx.reply(texto)

@bot.command()
async def somar(ctx:commands.Context, num1:int, num2:int):
    result = num1 + num2
    await ctx.send(f"{num1} + {num2}= {result}", ephemeral=True)

@bot.command()
async def ping(ctx:commands.Context,):
    await ctx.reply("pong :ping_pong: ", ephemeral=True) 

@bot.command()
async def ip(ctx: commands.Context):
    
    embed = discord.Embed(
        title="🌐 IP do servidor",
        color=0x32db3e
    )

    embed.add_field(
        name="Bedrock",
        value="infelizmente não temos suporte ainda para bedrock.",
        inline=False
    )

    embed.add_field(
        name="Java",
        value="XXXXXXXXX",
        inline=False
    )

    embed.set_footer(text="StormMint Security ©")

    await ctx.reply(embed=embed)
    

@bot.command()
async def limpar1(ctx, num: int):

    staff = ctx.guild.get_role(admin)

    if staff in ctx.author.roles:
        await ctx.channel.purge(limit=num)
        await ctx.reply("Pronto!")
    else:
        await ctx.reply("Não é permitido esse comando para membros!",)





bot.run(token)