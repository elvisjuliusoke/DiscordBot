import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Create bot instance
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print('------')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

# Event: Member joins
@bot.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

# Event: Member leaves
@bot.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

# Command: Ping
@bot.command(name='ping')
async def ping(ctx):
    """Check bot latency"""
    latency = round(bot.latency * 1000)
    await ctx.send(f'Pong! {latency}ms')

# Slash Command: Hello
@bot.tree.command(name="hello", description="Greet the user")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f'Hello {interaction.user.name}!')

# Slash Command: Help
@bot.tree.command(name="help", description="Show available commands")
async def help_command(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Bot Commands",
        description="Here are the available commands:",
        color=discord.Color.blue()
    )
    embed.add_field(name="!ping", value="Check bot latency", inline=False)
    embed.add_field(name="/hello", value="Greet yourself", inline=False)
    embed.add_field(name="/help", value="Show this message", inline=False)
    await interaction.response.send_message(embed=embed)

# Load cogs (optional)
async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
            print(f'Loaded {filename}')

# Main function
async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
