# Discord ChatGPT Bot

This Discord ChatGPT bot is capable of engaging in dynamic conversations with users. It's easy to use and easy to deploy. Utilizing the power of OpenAI's GPT-3.5 model, it can process messages and respond intelligently in real time.

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

### Step 1: Create a Discord Application

1. **Go to the Discord Developer Portal**: Open your web browser and navigate to the [Discord Developer Portal](https://discord.com/developers/applications).
2. **Create a New Application**: Click on the "New Application" button in the upper right corner.
   - Enter a name for your application and click "Create."
   - Note: This name will be used to identify your application in the Developer Portal but does not have to be the same name as your bot.
3. **Access the Bot Section**: 
   - In the left-hand menu, click on the "Bot" section.
   - Click on the "Add Bot" button on the right.
   - Confirm by clicking "Yes, do it!" in the pop-up window.
   - This will create a bot user associated with your application.
4. **Configure the Bot User**:
   - You can give your bot a username and avatar.
   - Note the "TOKEN" section; you'll use the token here later to authenticate your bot in the code.

### Step 2: Set Up Bot Permissions

1. **Go to the OAuth2 Section**:
   - In the left-hand menu of your application, click on the "OAuth2" section.
2. **Configure OAuth2 URL**:
   - In the "OAuth2 URL Generator" section, scroll down to the "OAuth2 Scope" and check the "bot" box.
   - Below that, in the "Bot Permissions" section, select the permissions your bot needs. For the bot you are creating, you'll want to select:
     - **Send Messages**: Allows the bot to send messages in the channel.
     - **Read Message History**: Allows the bot to read the message history of the channel.
     - **Mention Everyone**: Allows the bot to mention everyone in the channel.
3. **Generate the Invite Link**:
   - After selecting the permissions, scroll back up to the "OAuth2 URL Generator" section, and there will be a generated URL under "URL."
   - Click the "Copy" button to copy this URL to your clipboard.
4. **Add the Bot to Your Server**:
   - Open the copied URL in your web browser.
   - Select the server you want to invite the bot to from the dropdown menu.
   - Click "Authorize" and complete any CAPTCHA if required.
   - Your bot will now be added to the selected server, and you should see it appear in the member list.

### Step 3: Open VSCode and Clone the GitHub Repository

1. **Open Visual Studio Code (VSCode)**:
   - If you don't have VSCode installed, download and install it from the [official website](https://code.visualstudio.com/).

2. **Open the Terminal in VSCode**:
   - You can access the terminal from the top menu `View -> Terminal` or use the shortcut `Ctrl+`` (backtick).

3. **Install Git if Required**:
   - If you don't have Git installed, you may need to install it.
   - For Windows, you can download it from the [official website](https://git-scm.com/download/win).
   - For macOS, you can install it using Homebrew: `brew install git`.
   - For Linux, you can install it using your package manager, such as `sudo apt-get install git` for Ubuntu/Debian or `sudo yum install git` for RedHat/Fedora.

4. **Clone the GitHub Repository**:
   - Run the following command in the terminal:
     ```bash
     git clone https://github.com/j-snyd/gpt3-5_discord_bot.git
     ```

### Step 4: Navigate to the Project Directory

1. **Open the Cloned Repository in VSCode**:
   - Use the `File -> Open Folder` menu to navigate to the cloned repository's folder and open it.

### Step 5: Configure the .env File

1. **Update the .env File**:
   - Open the `.env` file within the project folder.
   - Update it with your Discord bot token and OpenAI key:
     ```plaintext
     DISCORD_TOKEN='discord_token_here'
     OPENAI_KEY='openai_key_here'
     ```

### Step 6: Install Dependencies

1. **Install Required Packages**:
   - Run the following command in the terminal:
     ```bash
     pip install -r requirements.txt
     ```

### Step 7: Run the Bot Locally

1. **Start the Bot**:
   - Run the following command in the terminal:
     ```bash
     python bot.py
     ```

### Step 8: Test the Bot in Discord

1. **Interact with the Bot**:
   - Go to the Discord server where you invited the bot.
   - Mention the bot or use specific commands to test the bot's responses.

### Conclusion

You have now set up and run your Discord bot locally in VSCode. Remember that the bot relies on GPT-3.5, and there are limitations and costs associated with using OpenAI's models. Ensure that you handle these aspects according to your specific needs and OpenAI's policies.
