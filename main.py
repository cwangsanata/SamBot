import discord
import random

from discord.ext import commands
from random import choice
from data import derogatory

"""
TODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODO.

made by Obama
kitowang@yahoo.com
"""

# Ion wanna touch anything here cause it works
bot = discord.Client()
help_command = commands.DefaultHelpCommand(no_category='Commands')
bot = commands.Bot(command_prefix='.')


# TODO: Fix "help" function.


@bot.event
async def on_ready():
    guild_count = 0

    for guild in bot.guilds:
        print(f"- {guild.id} (name: {guild.name})")

        guild_count += 1

    print("SamBot is in " + str(guild_count) + " guilds.")


@bot.event
async def on_member_join(member):
    await member.send("HI " + str(member) + ". I AM SAM <3")


@bot.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send("> I AM SAM, BOW BEFORE ME. USE \".help\" TO LEARN MORE ABOUT ME :wink:."
                               "\n\n> I AM CURRENTLY IN :sparkles: PRE-PRE-PRE-PRE-ALPHA :sparkles: SO PLEASE "
                               "BE GENTLE! :heart: MY PREFIX IS \".\""
                               "\n\n> IF I DON'T WORK SOMETIMES, ITS PROBABLY YOUR FAULT :smiley:"
                               )
        break


@bot.command()
async def spam(ctx, num, *args):
    """
    Use .spam <number> <message> to spam a phrase a number of times.
    :param ctx: context object needed in method call; from "command"
    :param num: the amount of times the String gets repeated
    :param args: The list that takes infinite arguments and gets repeated.
    :return a phrase with the selected amount of repeats of a single word
    """
    msg = ""
    for i in range(int(num)):
        for j in range(len(args)):
            msg += args[j] + ' '
    if len(msg) >= 2000:
        msg = "> Please send less than 2000 characters. Current length: " + str(len(msg))
    await ctx.channel.send(msg)


@bot.command()
async def mock(ctx, *args):
    """
    Use .mock <phrase> to return a "mocked" version of the phrase. (ex. hElLo WOrLD)
    :param ctx: Context awaits input from a user
    :param args: Takes Strings to be "mocked"
    :return: returns a psuedo-camel cased version of the input string
    """
    result = ''
    for arg in args:
        arg = arg + ' '
        for letter in arg:
            if random.randint(0, 1) == 0:
                result += letter.upper()
            else:
                result += letter.lower()
    await ctx.channel.send(str(result))


@bot.command()
async def insult(ctx):
    """
    Use .insult to get insulted.
    :param ctx: context object needed in method call
    :return: String with a random insult
    """
    await ctx.channel.send("YOU " + choice(derogatory).upper() + "!")


@bot.command()
async def sus(ctx):
    """
    Use .sus for funny.
    :return: Jerma985
    """
    await ctx.channel.send("\t      ⡯⡯⡾⠝⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢊⠘⡮⣣⠪⠢⡑⡌"
                           "\n⠀⠀⠀ ⠟⠝⠈⠀⠀⠀⠡⠀⠠⢈⠠⢐⢠⢂⢔⣐⢄⡂⢔⠀⡁⢉⠸⢨⢑⠕⡌"
                           "\n⠀⠀⡀⠁⠀⠀⠀⡀⢂⠡⠈⡔⣕⢮⣳⢯⣿⣻⣟⣯⣯⢷⣫⣆⡂⠀⠀⢐⠑⡌"
                           "\n⢀⠠⠐⠈⠀⢀⢂⠢⡂⠕⡁⣝⢮⣳⢽⡽⣾⣻⣿⣯⡯⣟⣞⢾⢜⢆⠀⡀⠀⠪"
                           "\n⣬⠂⠀⠀⢀⢂⢪⠨⢂⠥⣺⡪⣗⢗⣽⢽⡯⣿⣽⣷⢿⡽⡾⡽⣝⢎⠀⠀⠀⢡"
                           "\n⣿⠀⠀⠀⢂⠢⢂⢥⢱⡹⣪⢞⡵⣻⡪⡯⡯⣟⡾⣿⣻⡽⣯⡻⣪⠧⠑⠀⠁⢐"
                           "\n⣿⠀⠀⠀⠢⢑⠠⠑⠕⡝⡎⡗⡝⡎⣞⢽⡹⣕⢯⢻⠹⡹⢚⠝⡷⡽⡨⠀⠀⢔"
                           "\n⣿⡯⠀⢈⠈⢄⠂⠂⠐⠀⠌⠠⢑⠱⡱⡱⡑⢔⠁⠀⡀⠐⠐⠐⡡⡹⣪⠀⠀⢘"
                           "\n⣿⣽⠀⡀⡊⠀⠐⠨⠈⡁⠂⢈⠠⡱⡽⣷⡑⠁⠠⠑⠀⢉⢇⣤⢘⣪⢽⠀⢌⢎"
                           "\n⣿⢾⠀⢌⠌⠀⡁⠢⠂⠐⡀⠀⢀⢳⢽⣽⡺⣨⢄⣑⢉⢃⢭⡲⣕⡭⣹⠠⢐⢗"
                           "\n⣿⡗⠀⠢⠡⡱⡸⣔⢵⢱⢸⠈⠀⡪⣳⣳⢹⢜⡵⣱⢱⡱⣳⡹⣵⣻⢔⢅⢬⡷"
                           "\n⣷⡇⡂⠡⡑⢕⢕⠕⡑⠡⢂⢊⢐⢕⡝⡮⡧⡳⣝⢴⡐⣁⠃⡫⡒⣕⢏⡮⣷⡟"
                           "\n⣷⣻⣅⠑⢌⠢⠁⢐⠠⠑⡐⠐⠌⡪⠮⡫⠪⡪⡪⣺⢸⠰⠡⠠⠐⢱⠨⡪⡪⡰"
                           "\n⣯⢷⣟⣇⡂⡂⡌⡀⠀⠁⡂⠅⠂⠀⡑⡄⢇⠇⢝⡨⡠⡁⢐⠠⢀⢪⡐⡜⡪⡊"
                           "\n⣿⢽⡾⢹⡄⠕⡅⢇⠂⠑⣴⡬⣬⣬⣆⢮⣦⣷⣵⣷⡗⢃⢮⠱⡸⢰⢱⢸⢨⢌"
                           "\n⣯⢯⣟⠸⣳⡅⠜⠔⡌⡐⠈⠻⠟⣿⢿⣿⣿⠿⡻⣃⠢⣱⡳⡱⡩⢢⠣⡃⠢⠁"
                           "\n⡯⣟⣞⡇⡿⣽⡪⡘⡰⠨⢐⢀⠢⢢⢄⢤⣰⠼⡾⢕⢕⡵⣝⠎⢌⢪⠪⡘⡌⠀"
                           "\n⡯⣳⠯⠚⢊⠡⡂⢂⠨⠊⠔⡑⠬⡸⣘⢬⢪⣪⡺⡼⣕⢯⢞⢕⢝⠎⢻⢼⣀⠀"
                           "\n⠁⡂⠔⡁⡢⠣⢀⠢⠀⠅⠱⡐⡱⡘⡔⡕⡕⣲⡹⣎⡮⡏⡑⢜⢼⡱⢩⣗⣯⣟"
                           "\n⢀⢂⢑⠀⡂⡃⠅⠊⢄⢑⠠⠑⢕⢕⢝⢮⢺⢕⢟⢮⢊⢢⢱⢄⠃⣇⣞⢞⣞⢾"
                           "\n⢀⠢⡑⡀⢂⢊⠠⠁⡂⡐⠀⠅⡈⠪⠪⠪⠣⠫⠑⡁⢔⠕⣜⣜⢦⡰⡎⡯⡾⡽")


# TODO: implement time of day feature to make it more useful; might want to import time of day package thingy
@bot.command()
async def remind(ctx, day):
    """
    Use .remind <day> to send a message to remind.
    :param ctx: context object required in method call
    :param day: a String used in the message
    :return: a String that tells the user which day the next meeting is
    """
    await ctx.channel.send("We have a meeting this " + str(day) + ". All Hail Sam!")


@bot.command()
async def ping(ctx):
    """
    Use .ping to return the latency between user and bot server
    :param ctx: context object required in api
    :return: the latency between user and bot server
    """
    await ctx.send('Pong! {0}'.format(round(bot.latency, 1)))


# TODO: Make monkey command that pulls a random monkey from Google images (.monkey)

# TODO: Webscrape lyrics in >sing command; take http, access the lyric metadata; send to channel; if too long,
#  break into two

#TODO: Don't be a Yandev and learn switch statements

@bot.event
async def on_message(message):
    if 'sus' in message.content:
        await message.channel.send("WHEN THE IMPOSTER IS SUS!?!?!")
    elif 'among us' in message.content:
        await message.channel.send("amogus")
    elif 'thank' in message.content and 'sam bot' in message.content.lower():
        await message.channel.send("YOU'RE WELCOME :triumph:")
    elif 'n' in message.content.split():
        await message.channel.send('i\nc\ne')
    elif '69' in message.content.split():
        await message.channel.send('nice')
    elif 'valorant' in message.content.lower():
        await message.channel.send('HOP ON VALORANT :couplekiss:')
    await bot.process_commands(message)


def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()

bot.run(token)
