from replit import db
import os
import discord
import random
import requests
from webserver import keep_alive

my_secret = os.environ['TOKEN']
client = discord.Client()

command = ['fruit bar', 'smite night', 'mics on', 'motivation monday', 'fruit bot commands', 'vektus tinder', 'double fisted', 'shittom', 'ceramiclord', 'buckly','barf','zaddi','soyboy liberal cuck','drak','sifu','love barf','call buckly','penis']
response = ['im eating a coconut fruit bar\nhttps://www.twitch.tv/furbies/clip/AnimatedProtectiveBearCharlietheUnicorn-lUqw_ojvWu6fjobT', 'smiter\nhttps://clips.twitch.tv/YawningExcitedMallardPJSugar-uUOwCHsQbA6kuNzG', 'https://media.discordapp.net/attachments/823397292596920320/910932509141917766/FEfPHLAVkAYRapN.png?width=506&height=683', 'https://tenor.com/view/hasbulla-fighting-gif-22916682', 'hey daddi, here are my commands:\n- fruit bot commands\n- fruit bar\n- furbiez\n- your mic is on\n- mics on\n- motivation monday\n- sup g\n- Sup g\n- sup gs\n- vektus tinder\n- furbies stream\n- double fisted\n- ceramiclord\n- buckly\n- barf\n- zaddi\n- soyboy liberal cuck\n- drak\n- sifu\n- !aigen TEXT\n\tai generated from text\n- barf love\n- call buckly', 'https://media.discordapp.net/attachments/823397292596920320/910964357339422770/IMG_1980.png?width=948&height=447', 'https://cdn.discordapp.com/attachments/786658932662730776/912427881479671838/Screenshot_2021-05-23_003907.png', 'https://media.discordapp.net/attachments/786658932662730776/903374651659546624/unknown.png','https://cdn.discordapp.com/attachments/786658932662730776/888562026283171860/3x.gif','https://cdn.discordapp.com/attachments/823397292596920320/912431799852994591/IMG_1992.png','https://cdn.discordapp.com/attachments/786658932662730776/912432954947543110/274563ea-7c4a-4d6f-8651-1127a324de92_450_1a1cn1.png','https://cdn.discordapp.com/attachments/786658932662730776/912433181192486912/unknown.png','https://cdn.discordapp.com/attachments/786658932662730776/912436619427086378/stsmall507x507-pad600x600f8f8f8.png','https://cdn.discordapp.com/attachments/593944864580829193/911444700492341298/0641B4E9-E846-446B-A393-634D4D00A5E8.jpg','https://www.youtube.com/watch?v=1FQ1YO3Ks2U&ab_channel=PlayStation','https://profiles.d8u.com/profile/Malk486_just_casual_gamer_guy.html','https://media.discordapp.net/attachments/912765942205915167/915771654511132722/A1B55640-2C24-4444-9D48-D69963343BCB.png?width=528&height=521','https://cdn.discordapp.com/attachments/786658932662730776/917576955451302048/mZWuQrH.png']

@client.event
async def on_ready():
    print('{0.user} your mic is on.'.format(client))

@client.event
async def on_message(message):
    # Create a custom command and response
    if message.content.startswith('!newcommand '):
      msg = message.content
      cmdTxt = message.content
      cmdTxt = msg.split(" ")[1:][0]
      respTxt = message.content
      
      # Get response, verify a response is given
      try:
        respTxt = msg.split(" ")[2:][0]
      except IndexError:
        if cmdTxt != 'info':
          await message.reply("You forgot the response <:2999pepega:884819722519068673>")
        respTxt = "You forgot the response <:2999pepega:884819722519068673>"

      # !newcommand info ; lists requirements for function
      if cmdTxt == 'info':
        await message.reply('Commands must be in this format:\n!newcommand <command> <response>\n\t- Only one word commands and responses\n\t- <:7260peepono:884819725186650143> spaces in <command> and <response>')
      elif cmdTxt in command:
        await message.reply('<:2999pepega:884819722519068673> Command already exists! <:2999pepega:884819722519068673>')
      else:
        # Add to database
        db[cmdTxt] = respTxt
        await message.reply("<:2940coolpepe:884819724259692555> " + cmdTxt + " command added <:2940coolpepe:884819724259692555>")
      return
    
    # If command is within the list above
    elif  message.content in command:
      index = command.index(message.content)
      await message.reply(response[index])
    
    # If command is in the database
    elif message.content in db.keys():
      await message.reply(db[message.content])

    # Random response
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

    # Generate ai image from given text
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

    # Updated 12/9/21
    elif message.content.startswith('patch notes'):
      await message.reply("**<:2705peepodealwithit:884819725140525086>NEW UPDATE!<:2705peepodealwithit:884819725140525086>**\nLast updated 12/9/21\n\t- Custom commands are now persistant and will not reset<:6573peepoyes:884819725392183356>\n\t- Capable of holding at max 5000 commands")
  

keep_alive()

TOKEN = os.environ.get("DISCORD_BOT_SECRET")

client.run(my_secret)
