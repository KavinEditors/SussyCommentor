# SussyCommentor
SussyComentor is a fun Discord bot that replies to messages with witty, sarcastic, and meme-style AI-generated comments. You can comment, roast your friends by using my bot. It makes chats lively and entertaining by adding humor and playful roasts!

**1. Key Features**
Command	Description
!sussyhelp	Lists all commands and explains usage
!comment	Replies to a referenced message with a witty AI-generated comment
!roast	Replies with a humorous roast targeting the referenced message
!memecomment	Creates a meme-style, exaggerated reaction comment
!SUSpercentage	Returns a random “sus” percentage (1–100%) with no AI call

_How it works:_ The bot requires the user to reply to an existing message and invoke commands like !comment. The bot then fetches the replied message content and author, sends a prompt to an AI API, and posts the AI’s generated response tagging the original author.

**3. Technical Architecture**
a) Discord Bot
Built using discord.py or nextcord Python libraries.
Uses Intents to read messages and message content.
Commands are registered with commands.Bot(command_prefix='!').

b) AI Integration
Uses an AI API (OpenAI GPT or Cohere) to generate dynamic text responses.
Sends prompts like “Write a witty comment about this message: {content}”.
Parses and returns AI responses to Discord channels.

c) Environment & Secrets
API keys for Discord Bot Token and AI API are stored in .env files using python-dotenv.
Bot loads these securely at runtime.

d) Deployment & Hosting
The bot runs as a continuously running Python process on a server or cloud VM (AWS, Heroku, Replit, etc.).
24/7 uptime requires proper hosting with restart mechanisms or containers.

