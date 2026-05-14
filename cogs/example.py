from discord.ext import commands
import discord

class ExampleCog(commands.Cog):
    """Example cog with sample commands"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="example")
    async def example_command(self, ctx):
        """Example prefix command"""
        await ctx.send(f"Hello {ctx.author.name}! This is an example command from a cog.")
    
    @commands.Cog.listener()
    async def on_message(self, message):
        """Listen to all messages (excluding bot's own messages)"""
        if message.author == self.bot.user:
            return
        
        if message.content.lower() == "hello bot":
            await message.channel.send(f"Hello {message.author.name}!")

async def setup(bot):
    """Required function to load the cog"""
    await bot.add_cog(ExampleCog(bot))
