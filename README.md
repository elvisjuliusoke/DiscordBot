# Discord Bot 🤖

A powerful and modular Discord bot built with discord.py, ready for deployment!

## Features ✨

- ✅ Prefix commands (`!ping`, `!hello`)
- ✅ Slash commands (`/hello`, `/help`)
- ✅ Member join/leave event tracking
- ✅ Modular cog system for easy scaling
- ✅ Error handling and logging
- ✅ Ready for production deployment

## Prerequisites 📋

- Python 3.8 or higher
- Discord.py library
- A Discord server and bot token

## Setup Instructions 🚀

### 1. Clone the Repository
```bash
git clone https://github.com/elvisjuliusoke/DiscordBot.git
cd DiscordBot
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Get Your Discord Bot Token
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application"
3. Go to "Bot" section and click "Add Bot"
4. Copy the token

### 5. Configure Environment
```bash
# Create .env file from template
cp .env.example .env

# Edit .env and paste your token
# DISCORD_TOKEN=your_token_here
```

### 6. Invite Bot to Server
1. In Developer Portal, go to OAuth2 > URL Generator
2. Select scopes: `bot`
3. Select permissions: `Send Messages`, `Read Messages`, `Embed Links`, etc.
4. Copy and open the generated URL

### 7. Run the Bot
```bash
python bot.py
```

You should see: `[Your Bot Name] has connected to Discord!`

## Available Commands 💬

### Prefix Commands
- `!ping` - Check bot latency/response time
- `!hello` - Say hello to the bot

### Slash Commands (/)
- `/hello` - Greet yourself
- `/help` - Show all available commands

## Project Structure 📁

```
DiscordBot/
├── bot.py                 # Main bot file
├── requirements.txt       # Dependencies
├── .env.example          # Token template
├── .gitignore            # Git ignore rules
├── README.md             # This file
└── cogs/                 # Modular command files
    └── example.py        # Example cog template
```

## Creating Custom Cogs 🛠️

Add new commands by creating cogs in the `cogs/` directory:

```python
# cogs/my_commands.py
from discord.ext import commands
import discord

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="mycommand")
    async def my_command(self, ctx):
        await ctx.send("Hello from my cog!")

async def setup(bot):
    await bot.add_cog(MyCog(bot))
```

The bot will automatically load all cogs from the `cogs/` directory!

## Deployment Options 🌐

### Option 1: Heroku
```bash
heroku login
heroku create your-bot-name
git push heroku main
heroku config:set DISCORD_TOKEN="your_token"
heroku ps:scale worker=1
```

### Option 2: Railway.app
1. Push to GitHub
2. Connect repo to Railway
3. Add `DISCORD_TOKEN` environment variable
4. Deploy!

### Option 3: VPS (Linux)
```bash
# SSH into your server
# Install Python, clone repo, setup venv
# Use screen or systemd service to keep bot running

# Using screen:
screen -S discord-bot
python bot.py

# Or use systemd service for auto-restart
```

### Option 4: Docker
```bash
# Build
docker build -t discord-bot .

# Run
docker run -e DISCORD_TOKEN="your_token" discord-bot
```

## Troubleshooting 🔧

### Bot doesn't respond
- Check if token is correct in `.env`
- Verify bot has permissions in the server
- Check if bot is online in Discord

### Commands not working
- Run `/` commands after bot starts (they sync with Discord)
- Check bot role is above members' roles
- Verify bot has "Send Messages" permission

### Import errors
- Reinstall dependencies: `pip install -r requirements.txt --force-reinstall`
- Check Python version: `python --version` (should be 3.8+)

## Contributing 🤝

Feel free to:
- Add new commands via cogs
- Improve error handling
- Add database integration
- Optimize performance

## License 📜

This project is open source and available under the MIT License.

## Support 💬

For issues and questions:
- Check [discord.py documentation](https://discordpy.readthedocs.io/)
- Open an issue on GitHub
- Join Discord.py community server

---

**Happy Botting!** 🚀
