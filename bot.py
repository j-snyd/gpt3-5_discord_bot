# bot.py
import os
import discord
import openai
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_KEY = os.getenv('OPENAI_KEY')

# Set up the OpenAI API client
openai.api_key = OPENAI_KEY

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# test sending and receiving a message from the bot
'''@client.event
async def on_message(message):
    if message.author == client.user:
        return
 
    if message.content.startswith('Hey chatbot'):
        await message.channel.send('Hello how are you?')'''

@client.event
async def on_message(message):
    # Only respond to messages from other users, not from the bot itself
    if message.author == client.user:
        return

    # Check if the bot is mentioned in the message
    if client.user in message.mentions:
        messageContent = f"{message.content}"
        print(messageContent)
        print(message)

        #check name of user posting message and give specific instructions for specific users
        if message.author.name == 'user_name':
            content = "Content/instructions for specific user here"
        #elif message.author.id == 'USER_ID_2':
        #    content = "Treat USER_ID_2 like an idiot, give true answers but in sarcastic ways."
        else:
            content = "content/instructions here for all other users"

        # Use the OpenAI API to generate a response to the message
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content":content},{'role': 'user', 'content': messageContent}],
            max_tokens=2048,
            temperature=0.5,
        )
        
        # assign message content to a variable to use in follow-on function
        content_to_send = response.choices[0]['message']['content']
        print(content_to_send)
        # Send the response as a message
        await message.channel.send(content_to_send)

# Start the bot
client.run(TOKEN)
