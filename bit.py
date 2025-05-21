import random
import time
import os
import discord
from discord.ext import commands
from discord import app_commands

reaction_add_counts = {}
#denne er for å holde styr på siste svar-tid
reaction_last_time = {}
ping_last_time = {} 

class Client(commands.Bot):
    async def on_ready(self):
        print(F'logged on as {self.user}!')
        
        try:
            guild = discord.Object(id=1303287689822601257)
            synced = await self.tree.sync(guild=guild)
            print(f'synced {len(synced)} commands to guild {guild.id}')

        #viser vis the er en error i syncen
        except Exception as e:

            print(F'error is not silly enough, syncing commands: {e}')


#under så vis du sender en melding som starter med en av orderne så vil den svare med det som a under selected ord
    async def on_message(self, message):
        if message.author == self.user:
            return 
    
        if message.content.startswith('arise'):
            await message.channel.send(f'I AM BACK BABY, let get silly! {message.author}')

        if message.content.startswith('hello'):
            await message.channel.send(f'hello there {message.author}')
        
        if message.content.startswith('silly'):
            await message.channel.send("i am silly")

        if message.content.startswith('sillybot'):
            await message.channel.send(f'{message.author} What is it?')

        if message.content.startswith('i want'):
            await message.channel.send(f'Skill issue')

        if message.content.startswith('question'):
            await message.channel.send(f'i dont know! i am just silly')

        if message.content.startswith('are you silly?'):
            await message.channel.send(f'i am silly just like you {message.author}!')   

        if message.content.startswith('you have a skill issue'):
            await message.channel.send(f'your right that is a skill issue honestly {message.author}!') 



        #for serveren V1
        if message.content.startswith('Noah'):
            await message.channel.send(f'Noah is a silly billy!')  

        if message.content.startswith('Cato'):
            await message.channel.send(f'cato is a silly billy!') 

        if message.content.startswith('Ca2'):
            await message.channel.send(f'cato is a silly billy!') 

        if message.content.startswith('Marius'):
            await message.channel.send(f'Marius is a silly billy!')  

        if message.content.startswith('Magnus'):
            await message.channel.send(f'Magnus is a silly billy!') 

        if message.content.startswith('Joakim'):
            await message.channel.send(f'Joakim is a silly billy!') 

        if message.content.startswith('Joakim'):
            await message.channel.send(f'Joakim er en suspicious billy') 

        if message.content.startswith('Eirik'):
            await message.channel.send(f'Eirik is a silly billy! and my creator!')

        if message.content.startswith('prostagma'):
            await message.channel.send(f'prostagma')


        #alien versjon av sillybot V1
        if message.content.startswith('sillybot alien'):
            await message.channel.send(f'hello there {message.author} i am sillybot alien version!')

        if message.content.startswith('vorp'):
            await message.channel.send(f'vorp?')

        if message.content.startswith('gleep!') or message.content.startswith('GLEEP!'):
            folder = 'C:/Eirik/discord-bot (yff prokjet)/img'
            img_path = os.path.join(folder, 'Bleemk.png')

            with open(img_path, 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(content="Zorvak ti'lem Bleemk'sh-nar 😺", file=picture)

        if message.content.startswith('gloop!') or message.content.startswith('GLOOP!'):
            folder = 'C:/Eirik/discord-bot (yff prokjet)/img'
            img_path = os.path.join(folder, 'gloop.png')

            with open(img_path, 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(content="Zorvak ti'lem Gloop'sh-nar 😺", file=picture)

            #herer er det for å sende melding når folk joiner og forlater serveren

        async def on_member_remove(self, member):
            channel = discord.utils.get(member.guild.text_channels, name="general")
            if channel:
                await channel.send(f"{member.mention} was a silly billy and left the server! 😿")

        async def on_member_add(self, member):
            channel = discord.utils.get(member.guild.text_channels, name="general")
            if channel:
                await channel.send(f"Velkommen {member.mention}! Du er nå en ekte silly billy! 😺")

        #ble putet her fordi det er en litt mer random ting
        
        if message.content.startswith('skill issue'):
            await message.channel.send(f'you have a skill issue {message.author}!')

        if message.content.startswith('no you have a skill issue'):
            await message.channel.send(f'nah uh {message.author} you have a skill issue!')

        if message.content.startswith('no you have'):
            await message.channel.send(f'nah uh')

        if message.content.startswith('time to go to sleep my bot'):
            await message.channel.send(f'no please dont make me go to sleep! i am just a silly bot!')
        if message.content.startswith('sorry'):
            await message.channel.send(f'i understand {message.author}')
        #brukt for å sende en gif
        if message.content.startswith('steal this'):
            gif_url = "https://tenor.com/view/power-the-server-stealing-our-power-power-this-cat-is-powering-the-server-gif-13742427947668377662"
            await message.channel.send(gif_url)

        if message.content.startswith('give me gif'):
            gif_folder = 'C:/Eirik/discord-bot (yff prokjet)/img/Gif'
            gif_list = [f for f in os.listdir(gif_folder) if f.lower().endswith('.gif')]
            if gif_list:
                chosen_gif = random.choice(gif_list)
                gif_path = os.path.join(gif_folder, chosen_gif)
                with open(gif_path, 'rb') as f:
                    gif_file = discord.File(f)
                    await message.channel.send(file=gif_file)
            else:
                await message.channel.send("Ingen GIFs funnet 😿")

        #trying the ping funksjon, some kan ping alle og noen kan ping en spesifik person

        ping_cooldown = 60  # 1 minutter
        now = time .time()
        author_id = message.author.id
        last_ping = ping_last_time.get(author_id, 0)

        if message.content.startswith('ping me'):
            if (now - last_ping) > ping_cooldown:
                await message.channel.send(f'{message.author.mention} you have been pinged!')
                ping_last_time[author_id] = now
            # Ikke send noe hvis cooldown ikke er over

        # Cooldown for ping andre brukere
        if message.content.startswith('ping ') and message.mentions:
            if (now - last_ping) > ping_cooldown:
                for user in message.mentions:
                    await message.channel.send(f'{user.mention} du har blitt pinget av {message.author.mention}!')
                ping_last_time[author_id] = now
            # Ikke send noe hvis cooldown ikke er over

        if message.content.startswith('pingrole '):
            if (now - last_ping) > ping_cooldown:
                role_name = message.content[len('pingrole '):].strip()
                role = discord.utils.get(message.guild.roles, name=role_name)
                if role:
                    await message.channel.send(f'{role.mention} du har blitt pinget!')
                else:
                    await message.channel.send(f'Fant ikke rollen "{role_name}"')
                ping_last_time[author_id] = now
            # Ikke send noe hvis cooldown ikke er over


        #sender et tilfeldig kattebilde 
        if message.content.startswith('give me cat'):

            folder = 'C:/Eirik/discord-bot (yff prokjet)/img'
            img_list = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
            if img_list:
                chosen_image = random.choice(img_list)
                img_path = os.path.join(folder, chosen_image)

                with open(img_path, 'rb') as f:
                    picture = discord.File(f)
                    await message.channel.send(file=picture)
            else:
                await message.channel.send("Ingen kattebilder funnet 😿")

    async def on_reaction_add(self, reaction, user):
        message_id = reaction.message.id
        now = time.time()
        last_time = reaction_last_time.get(message_id, 0)
        count = reaction_add_counts.get(message_id, 0)
        cooldown = 300  # sekunder pause mellom svar (5 minutter)

        if count < 3 and (now - last_time) > cooldown:
            await reaction.message.channel.send('you reacted Silly')
            reaction_add_counts[message_id] = count + 1
            reaction_last_time[message_id] = now

# Oppretter et "intents"-objekt som bestemmer hva slags informasjon og hendelser boten får fra Discord.
intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True  
intents.messages = True 
intents.members = True
Client = Client(command_prefix="!", intents=intents)


GUILD_ID = discord.Object(id=1303287689822601257)

#here har man Slash Commandene.
@Client.tree.command(name="silly", description="you are!", guild=GUILD_ID)
async def silly(interaction: discord.Interaction):
    await interaction.response.send_message("you are a silly billy")

@Client.tree.command(name="printer", description="me print everything", guild=GUILD_ID)
async def silly(interaction: discord.Interaction, printer: str):
    await interaction.response.send_message(printer)

#@Client.tree.command(name="", description="", guild=GUILD_ID)
#async def silly(interaction: discord.Interaction):
    #await interaction.response.send_message()

#herer er help commanden.
@Client.tree.command(name="help", description="Viser alle kommandoer", guild=GUILD_ID)
async def help_command(interaction: discord.Interaction):
    # Hent alle app_commands (slash commands)
    cmds = Client.tree.get_commands(guild=GUILD_ID)
    cmd_list = [f"/{cmd.name} - {cmd.description}" for cmd in cmds]
    # Hent alle tekstkommandoer (on_message)
    text_cmds = [
        "arise", "hello", "silly", "sillybot", "i want", "question", "are you silly?",
        "you have a skill issue", "Noah", "Cato", "Ca2", "Marius", "Magnus", "Joakim",
        "Eirik", "prostagma", "sillybot alien", "vorp", "gleep!", "gloop!", "skill issue",
        "no you have a skill issue", "no you have", "time to go to sleep my bot", "sorry",
        "steal this", "give me gif", "ping me", "ping @bruker", "pingrole <navn>", "give me cat"
    ]
    text_cmds_str = "\n".join([f"`{cmd}`" for cmd in text_cmds])
    embed = discord.Embed(title="SillyBot Hjelp", color=discord.Color.blurple())
    embed.add_field(name="Slash Commands", value="\n".join(cmd_list) or "Ingen", inline=False)
    embed.add_field(name="Tekstkommandoer", value=text_cmds_str, inline=False)
    await interaction.response.send_message(embed=embed)
#for å lage en button som kan brukes til å lage en ny melding
#en knapp som skrur av boten
@Client.tree.command(name="panic", description="Stopper boten (bare for eier)", guild=GUILD_ID)
async def panic(interaction: discord.Interaction):
    # Sjekk at det er deg som bruker kommandoen
    if interaction.user.id == 1182639006186471484:
        await interaction.response.send_message("Botten skrur seg av! 😱", ephemeral=True)
        await interaction.client.close()
    else:
        await interaction.response.send_message("Du har ikke lov til å bruke denne kommandoen.", ephemeral=True)


class MyView(discord.ui.View):
    @discord.ui.button(label="become silly", style=discord.ButtonStyle.green, emoji="😺")
    async def become_silly(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("you are silly now", ephemeral=True)

    @discord.ui.button(label="become not silly", style=discord.ButtonStyle.blurple, emoji="😿")
    async def become_not_silly(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("you are not silly now", ephemeral=True)

    @discord.ui.button(label="become silly again", style=discord.ButtonStyle.red, emoji="😸")
    async def become_silly_again(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("you are silly again", ephemeral=True)

@Client.tree.command(name="button", description="displaying a button", guild=GUILD_ID)
async def mybutton(interaction: discord.Interaction):
    await interaction.response.send_message(view=MyView())


#the embed code.
@Client.tree.command(name="wiki", description="testing embed", guild=GUILD_ID)
async def silly(interaction: discord.Interaction):
    embed = discord.Embed(title="sillycat wiki", url="https://sillycattvseries.fandom.com/wiki/Silly_Cat_Wiki", description="sillycat wiki", color=discord.Color.dark_magenta())
    embed.set_thumbnail(url="https://catpedia.wiki/images/5/59/Milly.png")
    embed.add_field(name="wiki is good👌", value="go and exsplore the wiki of silly cats", inline=False)
    embed.add_field(name="Do it", value="Do it")
    await interaction.response.send_message(embed=embed)



#herer are boten main code for a code boten.
Client.run()

