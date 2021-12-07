import os
import discord
import random
import requests
from webserver import keep_alive

my_secret = os.environ['TOKEN']
client = discord.Client()


@client.event
async def on_ready():
    print('{0.user} your mic is on.'.format(client))


@client.event
async def on_message(message):
    if message.content.startswith('fruit bar') or message.content.startswith(
            'furbiez'):
        await message.reply(
            'im eating a coconut fruit bar\nhttps://www.twitch.tv/furbies/clip/AnimatedProtectiveBearCharlietheUnicorn-lUqw_ojvWu6fjobT'
        )
        return
    elif message.content.startswith('smite night'):
        await message.reply(
            'smiter\nhttps://clips.twitch.tv/YawningExcitedMallardPJSugar-uUOwCHsQbA6kuNzG'
        )
        return
    elif message.content.startswith(
            'your mic is on') or message.content.startswith(
                'mics on') or message.content.startswith('egg'):
        await message.reply(
            'https://media.discordapp.net/attachments/823397292596920320/910932509141917766/FEfPHLAVkAYRapN.png?width=506&height=683'
        )

        return
    elif message.content.startswith('motivation monday'):
        await message.reply(
            'https://tenor.com/view/hasbulla-fighting-gif-22916682')
        return
    elif message.content.startswith('sup g') or message.content.startswith(
            'Sup g') or message.content.startswith('sup gs'):
        num = random.randrange(0, 7)
        if num == 0:
            await message.reply(
                'https://media.discordapp.net/attachments/823397292596920320/910287252930826250/2F4B9038-D1FB-4A85-82E3-FB91330414D1.jpg?width=512&height=683'
            )
        elif num == 1:
            await message.reply(
                'https://media.discordapp.net/attachments/823397292596920320/905546896834170920/C5F1A568-A907-453B-A5B9-B9FBC17F75EE.jpg?width=512&height=683'
            )
        elif num == 2:
            await message.reply(
                'https://media.discordapp.net/attachments/786658932662730776/917439563989930074/image0.jpg?width=512&height=683'
            )
        elif num == 3:
            await message.reply(
                'https://media.discordapp.net/attachments/786658932662730776/917439590753771550/Screenshot_2021-05-23_003907.png'
            )
        elif num == 4:
            await message.reply(
                'https://media.discordapp.net/attachments/786658932662730776/917439696504754196/unknown-1.png?width=942&height=614'
            )
        elif num == 5:
            await message.reply(
                'https://cdn.discordapp.com/attachments/823397292596920320/916770072855445534/973303D4-3F8D-4521-820C-CDDBFF26B81E.jpg'
            )
        else:
            await message.reply(
                'https://cdn.discordapp.com/attachments/823397292596920320/912477066769858611/IMG_0332.jpg'
            )
        return
    elif message.content.startswith('fruit bot commands'):
        await message.reply(
            'hey daddi, here are my commands:\n- fruit bot commands\n- fruit bar\n- furbiez\n- your mic is on\n- mics on\n- motivation monday\n- sup g\n- Sup g\n- sup gs\n- vektus tinder\n- furbies stream\n- double fisted\n- ceramiclord\n- buckly\n- barf\n- zaddi\n- soyboy liberal cuck\n- drak\n- sifu\n- !aigen TEXT\n\tai generated from text\n- barf love\n- call buckly'
        )
        return
    elif message.content.startswith(
            'vektus tinder') or message.content.startswith('furbies stream'):
        await message.reply(
            'https://media.discordapp.net/attachments/823397292596920320/910964357339422770/IMG_1980.png?width=948&height=447'
        )
        return
    elif message.content.startswith('double fisted'):
        await message.reply(
            'https://cdn.discordapp.com/attachments/786658932662730776/912427881479671838/Screenshot_2021-05-23_003907.png'
        )
        return
    elif message.content.startswith('shittom'):
        await message.reply(
            'https://media.discordapp.net/attachments/786658932662730776/903374651659546624/unknown.png'
        )
        return
    elif message.content.startswith('ceramiclord'):
        await message.reply(
            'https://cdn.discordapp.com/attachments/786658932662730776/888562026283171860/3x.gif'
        )
        return
    elif message.content.startswith('buckly'):
        await message.reply(
            'https://cdn.discordapp.com/attachments/823397292596920320/912431799852994591/IMG_1992.png'
        )
        return
    elif message.content.startswith('barf'):
        await message.reply(
            'https://cdn.discordapp.com/attachments/786658932662730776/912432954947543110/274563ea-7c4a-4d6f-8651-1127a324de92_450_1a1cn1.png'
        )
        return
    elif message.content.startswith('zaddi') or message.content.startswith(
            'tycho'):
        await message.reply(
            'https://cdn.discordapp.com/attachments/786658932662730776/912433181192486912/unknown.png'
        )
        return
    elif message.content.startswith(
            'soyboy liberal cuck') or message.content.startswith('toph'):
        await message.reply(
            'https://cdn.discordapp.com/attachments/786658932662730776/912436619427086378/stsmall507x507-pad600x600f8f8f8.png'
        )
        return
    elif message.content.startswith('drak'):
        await message.reply(
            'https://cdn.discordapp.com/attachments/593944864580829193/911444700492341298/0641B4E9-E846-446B-A393-634D4D00A5E8.jpg'
        )
        return
    elif message.content.startswith('sifu'):
        await message.reply(
            'https://www.youtube.com/watch?v=1FQ1YO3Ks2U&ab_channel=PlayStation'
        )
        return
    elif message.content.startswith('!aigen '):
        msg = message.content
        msg = msg.split(" ")[1:][0]

        r = requests.post(
            "https://api.deepai.org/api/text2img",
            data={
                'text': msg,
            },
            headers={'api-key': '62363f0a-e849-4c6d-98e4-e92eb3987c7e'})

        await message.reply(r.json()['output_url'])
        return
    elif message.content.startswith('love barf'):
        await message.reply(
            'https://profiles.d8u.com/profile/Malk486_just_casual_gamer_guy.html'
        )
        return
    elif message.content.startswith(
            'call buckly') or message.content.startswith('call hasbulla'):
        await message.reply(
            'https://media.discordapp.net/attachments/912765942205915167/915771654511132722/A1B55640-2C24-4444-9D48-D69963343BCB.png?width=528&height=521'
        )
        return
    elif message.content.startswith('penis'):
        await message.reply(
            'https://cdn.discordapp.com/attachments/786658932662730776/917576955451302048/mZWuQrH.png'
        )


keep_alive()

TOKEN = os.environ.get("DISCORD_BOT_SECRET")

client.run(my_secret)
