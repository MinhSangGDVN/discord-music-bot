import discord
from discord.ext import commands, tasks
import asyncio
import os
from collections import deque

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
# REPLACE WITH THE CHANNEL ID YOU WANT THE BOT TO JOIN TO PLAY MUSIC, MULTIPLE CHANNELS CAN BE ADDED
VOICE_CHANNEL_IDS = [1403672320492703764, 1403673109613117572]

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

#YOU CAN ADD MORE SONGS HERE
song_queue = deque([
    "song1.mp3", "song2.mp3", "song3.mp3", "song4.mp3", "song5.mp3", "song6.mp3", "song7.mp3",
])

for song_file in song_queue:
    if not os.path.exists(song_file):
        print(f"Error: Music file not found '{song_file}'.")

voice_clients = {}


async def update_bot_status(voice_client):
    """
    Update bot status based on the song playing.
    """
    if voice_client and voice_client.is_playing():
       
        current_song = os.path.basename(song_queue[0])
        await bot.change_presence(
            status=discord.Status.dnd,
            activity=discord.Activity(
                type=discord.ActivityType.listening,
                name=f"nhạc: {current_song}",
            )
        )
    else:
        await bot.change_presence(
            status=discord.Status.dnd,
            activity=discord.Activity(
                type=discord.ActivityType.listening,
                name="Start the music system 24/7...",
            )
        )

@tasks.loop(seconds=5)  
async def check_and_play():
    """
    Asynchronous loop to test and play music.
    """
    for guild_id, vc in voice_clients.items():
        if not vc.is_playing():
            
            song_file = song_queue.popleft()
            song_queue.append(song_file)  
            
            try:
                source = discord.FFmpegPCMAudio(song_file)
                vc.play(source)
                print(f"Start playing music: {song_file} on channel {vc.channel.name}")
                await update_bot_status(vc)
            except discord.ClientException as e:
                print(f"Client Error while playing music: {e}")
            except Exception as e:
                print(f"An error occurred while playing music: {e}")

@bot.event
async def on_ready():
    print(f"Bot is online with name: {bot.user.name}")
    print("---------------------------------------")
    

    await update_bot_status(None)

    # Lặp qua tất cả các kênh thoại đã định nghĩa.
    for channel_id in VOICE_CHANNEL_IDS:
        channel = bot.get_channel(channel_id)
        if channel and isinstance(channel, discord.VoiceChannel):
            print(f"Trying to join voice channel: {channel.name}")
            try:
                voice_client = await channel.connect(timeout=60.0)
                voice_clients[channel.guild.id] = voice_client
                print(f"Joined channel: {channel.name}")
            except Exception as e:
                print(f"Error joining channel {channel.name}: {e}")
        else:
            print(f"Voice channel with ID not found: {channel_id}")
            
    
    if voice_clients:
        check_and_play.start()



try:
    bot.run(DISCORD_TOKEN)
except discord.LoginFailure:
    print("Invalid token. Please check your token again.")
except Exception as e:
    print(f"An error occurred: {e}")
    