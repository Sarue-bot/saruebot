import discord
import datetime
import os 



client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("테스트봇")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith('!정보'):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color = 0xA9F5F2)
        embed.add_field(name="이름",value=message.author.name, inline=True)
        embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" +str(date.day) + "일", inline=True)
        embed.add_field(name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)


@client.event
async def on_message(message):
    if message.author == client.user:
          return
    if message.content.startswith('!명령어'):
        emb = discord.Embed(title = '!정보',description='자신의 프로필을 확인할수있습니다.', color = 0x516a93)
        await message.channel.send(content = None , embed = emb)








access_token = os. environ["BOT_TOKEN"]
client.run(access_token)
