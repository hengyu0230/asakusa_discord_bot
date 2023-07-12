from discord.ext import commands
import discord
from discord.ext.commands import bot
import json
import random

 
bot = commands.Bot(command_prefix=">")


#淺草籤json -> python
with open("淺草籤.json","r",encoding = "utf8") as file:
    omikuji = json.load(file)



#機器人啟動告知/Discord顯示狀態
#discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name = "籤筒"))
    print(">>機器人準備完成<<")
    return


#抽籤
@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return
    if msg.content.startswith(">抽籤") or msg.content.startswith(">おみくじ"):
        num = random.randint(0, 99)
        luck = omikuji[num]

        #內文      
        i = luck["id"]#["籤號"]
        t = luck["type"]#["籤運"]
        p = luck["poem"]#["籤詩"]
        e = luck["explain"]#["籤解"]
        r = luck["result"]#["運勢"]
        n = luck["note"]#["註解"]
        
        #result的key值
        result = ""
        for key in r:
            result += "★" + str(key) + ":" + str(r[key]) + "\n"

        #籤詩內容
        lib = discord.Embed(title="你今天抽到怎樣的籤呢?",description = "籤號: " + str(i) + "\n籤運: " + str(t) + "\n" + "\n籤詩: " + str(p) + "\n" +"\n籤解: " + str(e) + "\n" + "\n運勢: " +
        "\n" + result +
        "\n" + "\n註解: " + str(n) , 
        color = discord.Colour.random())
        lib.set_author(name="淺草籤")
        lib.set_thumbnail(url = "https://illust8.com/wp-content/uploads/2020/01/omikuji_daikitchi_6574.png")
        await msg.channel.send(embed = lib)
        return
          
       
#指令查詢
    if msg.author == bot.user:
        return
    if msg.content.startswith(">help") or msg.content.startswith(">Help") or msg.content.startswith(">指令"):
        embed = discord.Embed(title="指令", description="目前可以使用的指令", color=0xffbdbd)
        embed.set_author(name="おみくじ")
        embed.add_field(name=">抽籤 or >おみくじ", value="進行一次抽籤", inline=False)
        embed.set_thumbnail(url = "https://imgur.com/csrRIGu.png")
        await msg.channel.send(embed=embed)
        return


bot.run("token") 


#淺草籤:https://gist.github.com/mmis1000/d94bb0a9f37cfd362453
#特別感謝: i_li , seiin , VistanZ
