# Discord ChatGPT Bot

The provided code defines a Discord bot capable of engaging in dynamic conversations with users. Utilizing the power of OpenAI's GPT-3.5 model, it can process messages and respond intelligently in real time.

## Features
- **Easy Deployment**: With a straightforward setup, this bot can be quickly deployed to any Discord server.
- **Customizable Responses**: Specific instructions and responses can be defined for particular users or user IDs, allowing for personalized interactions.
- **Interactive Engagement**: By leveraging OpenAI's GPT-3.5 model, the bot can understand and reply to complex queries, creating a more engaging experience for users.
- **Automated Messaging**: Whether mentioned directly or addressed with a specific command, the bot listens for incoming messages and responds accordingly.

## Limitations of GPT-3.5
- **Contextual Understanding**: While GPT-3.5 is highly advanced, it may sometimes lack a deep understanding of specific or complex contexts.
- **Safety and Content Filtering**: Ensure compliance with OpenAI's use-case policy, and be cautious of potential biases or unsafe content in generated responses.
- **Token Limit**: Keep in mind the model's token limit (4096 tokens for GPT-3.5) when generating responses, as overly lengthy conversations may exceed this limit.
- **Cost**: Usage of GPT-3.5 is subject to API pricing, which might impact the feasibility of extensive or commercial use.

## Installation and Usage

### Step 1: Clone the Repository
Clone the repository to your local machine using:
```bash
git clone https://github.com/j-snyd/gpt3-5_discord_bot.git
```

### Step 2: Install Dependencies
Navigate to the repository's directory and install the necessary dependencies using:
```bash
cd gpt3-5_discord_bot
pip install -r requirements.txt
```

### Step 3: Update the .env File
In the root directory of the project, you will find a `.env` file. Update the following lines with your credentials:
```plaintext
DISCORD_TOKEN='discord_token_here'
OPENAI_KEY='openai_key_here'
```

### Step 4: Run the Bot
Once the environment variables are set up, you can run the bot using:
```bash
python bot.py
```

### Note
- The bot requires permissions to read and send messages in the channels where you invite it.
- Make sure you have the proper permissions in your Discord server to invite and interact with bots.
- Ensure that your Python environment is compatible with the versions of the libraries mentioned in `requirements.txt`. The instructions assume you are using Python 3.6 or later.

## Conclusion
This Discord ChatGPT bot offers both ease of deployment and customization. It serves as a robust foundation for various conversational needs but also comes with the inherent limitations of GPT-3.5. Proper understanding and handling of these limitations are essential for an effective and responsible usage.
