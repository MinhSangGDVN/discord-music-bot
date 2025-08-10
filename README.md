# Discord 24/7 Music Bot

A simple Discord bot that plays music 24/7 in one or more designated voice channels. The bot uses a queue to loop through a pre-configured list of songs.

![Preview Image](https://raw.githubusercontent.com/MinhSangGDVN/discord-music-bot/refs/heads/main/IMG_20250810_112452.jpg)

## Key Features

* **24/7 Music Playback:** The bot automatically connects and plays music in the configured voice channels.
* **Song Queue:** It uses a queue to cycle through a playlist of songs, ensuring there are no gaps between tracks.
* **Automatic Reconnect:** The bot automatically joins the voice channels upon startup.
* **Status Updates:** Displays the name of the currently playing song in the bot's status.

## Installation Guide

### Step 1: Create a Discord Bot Application and Get a Token

1.  Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2.  Click on **"New Application"** and give your bot a name.
3.  In the application's settings, select **"Bot"** from the left-hand menu.
4.  Click **"Add Bot"** and confirm.
5.  Copy your bot's **Token** by clicking **"Copy"**. **Note:** This token is your bot's password, so keep it secure.

### Step 2: Enable Intents

This bot requires the **"Message Content Intent"** to function.

1.  In the **"Bot"** section of the Discord Developer Portal, scroll down to the **"Privileged Gateway Intents"** section.
2.  Enable the **"Message Content Intent"** toggle.
3.  Click **"Save Changes"**.

### Step 3: Set up and Configure the Project

1.  **Clone or download the source code:** Download the code to your machine.
2.  **Install the required libraries:**
    * You can install them from the `requirements.txt` file:
        ```sh
        pip install -r requirements.txt
        ```
    * Or, you can install them manually:
        ```sh
        pip install discord.py PyNaCl python-dotenv
        ```
    * **Note:** The bot uses `FFmpeg` for audio processing. You must have `FFmpeg` installed on your system and accessible from the command line.
3.  **Prepare your music files:** Place your music files (in `.mp3` format or other formats supported by `FFmpeg`) in the same directory as your bot's source code.
4.  **Configure environment variables:**
    * Create a `.env` file in the same directory as your source code.
    * Add the following line to the `.env` file, replacing `YOUR_BOT_TOKEN` with the token you got in Step 1.
    ```
    DISCORD_TOKEN=YOUR_BOT_TOKEN
    ```
5.  **Configure the source code:**
    * Open your bot's file and edit these lines:
    ```python
    # REPLACE WITH THE CHANNEL ID YOU WANT THE BOT TO JOIN TO PLAY MUSIC, MULTIPLE CHANNELS CAN BE ADDED
    VOICE_CHANNEL_IDS = [1403672320492703764, 1403673109613117572]

    # ADD YOUR SONG FILENAMES TO THE QUEUE
    song_queue = deque([
        "song1.mp3", "song2.mp3", "song3.mp3", "song4.mp3", "song5.mp3", "song6.mp3", "song7.mp3",
    ])
    ```
    * Replace `VOICE_CHANNEL_IDS` with the ID of the voice channel(s) you want the bot to join. You can find a channel's ID by enabling developer mode in Discord (User Settings -> Advanced -> Developer Mode) and right-clicking on the channel to **"Copy ID"**.
    * Add the filenames of your music files to the `song_queue`.

### Step 4: Run the Bot

Run the bot with the following command:

```sh
python app.py
```

[DOWNLOAD SOURCE CODE](https://github.com/MinhSangGDVN/discord-music-bot/archive/refs/heads/main.zip)
