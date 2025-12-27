# MegaChat

MegaChat is a simple Telegram bot built with Python and the `python-telegram-bot` library. This bot serves as a basic example that can echo back any text message it receives and logs all interactions to a file.

## Features

*   **Welcome Message**: Greets users with a welcome message when they start a conversation using the `/start` command.
*   **Echo Functionality**: Repeats any text message it receives from a user.
*   **Interaction Logging**: Logs the user's name, chat ID, and message content to `sample.log` for monitoring and debugging purposes.

## Prerequisites

*   Python 3.x
*   A Telegram Bot API Token

## Setup and Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/mani10official/MegaChat.git
    cd MegaChat
    ```

2.  **Install the required dependency:**
    The bot relies on the `python-telegram-bot` library.
    ```sh
    pip install python-telegram-bot
    ```

## Configuration

1.  **Get a Telegram API Token:**
    You need to get an API token from the [BotFather](https://t.me/BotFather) on Telegram by creating a new bot.

2.  **Update the configuration file:**
    Open the `config.py` file and replace the placeholder `<API_TOKEN>` with the token you received from BotFather.

    ```python
    # in config.py
    API_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN_HERE'
    ```

## Usage

Once you have configured your API token, you can run the bot using the following command:

```sh
python MegaChat_teleBot.py
```

Your bot is now running and will respond to messages on Telegram. All interactions will be logged in the `sample.log` file created in the project directory.

## License

This project is licensed under the MIT License. See the [LICENSE.txt](LICENSE.txt) file for details.
