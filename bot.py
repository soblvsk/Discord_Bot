import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')
# .help


@client.event
async def on_ready():
    print('BOT connected')

    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('Готовит на кухне'))


@client.event
async def on_member_join(member):
    channel = client.get_channel(707596374140780625)

    role = discord.utils.get(member.guild.roles, id=707648923430289519)

    await member.add_roles(role)
    await channel.send(embed=discord.Embed(description=f'Пользователь **{ member.mention }**, присоеденился к нам!',
                                           color=0x0c0c0c))


@client.event
async def on_member_remove(member):
    channel = client.get_channel(707596374140780625)

    await channel.send(embed=discord.Embed(description=f'Пользователь **{ member.mention }**, покинул нас!',
                                           color=0x0c0c0c))

# Clear message


@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)
    await ctx.send(embed=discord.Embed(description=f':white_check_mark: Удалено {amount} сообщений', color=0x0c0c0c))


@client.command(pass_context=True)
async def hello(ctx):
    await ctx.send('Hello')

# Connect

token = open('token.txt', 'r').readline()

client.run(token)
