# bot.py
import os
import discord
import random
import asyncio
from dotenv import load_dotenv
from discord.ext import commands
from os import listdir
from os.path import isfile, join
from Database import Database
import sqlite3
from mine_sim import MineUser


def main():
    db = Database()
    db.fill_db()
    # Loads .env file in folder
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')

    # 2 sets  command prefix for  bot
    bot = commands.Bot(command_prefix='g!')

    class Work(commands.Cog):
        """
        Work class, will define all work possible.
        """
        def __init__(self, bot):
            self.bot = bot

        @commands.Cog.listener()
        async def on_ready(self):
            print('Work Cog has been loaded.\n--------\n')

        @commands.group()
        async def work(self, ctx):
            if ctx.invoked_subcommand is None:
                await ctx.send('Type g!work help to see a list of work available.')

        @work.command()
        async def mine(self, ctx):
            discid = str(ctx.author.id)
            db.c.execute('SELECT discid FROM miners WHERE discid == ?', (discid,))
            isminer = db.c.fetchall()
            if isminer:
                authorname = ctx.author
                description = 'Click the :pick: to mine!'
                authoricon = authorname.avatar_url
                embed = discord.Embed(title='Mining', description=description)
                embed.set_author(name=authorname, icon_url=authoricon)
                embed.set_image(url='https://github.com/Haxorgz/SuperCoolGame/blob/main/Images/goodrock.png?raw=true')
                # https://github.com/Haxorgz/SuperCoolGame/blob/main/Images/goodrock.png?raw=true https://i.imgur.com/hAaNOoP.png?1
                embed.set_footer(text='EpicGameBot')
                mine = await ctx.send(embed=embed)
                await mine.add_reaction('\N{pick}')
            else:
                await ctx.send("Sorry, you're not a miner!")

        @work.command(name='help')
        async def help(self, ctx):
            await ctx.send("To mine, type g!work mine.\n That's about it...")

        # @commands.group(name='addcredits')
        # async def addcredits(self, ctx):
        #     if ctx.invoked_subcommand is None:
        #         await ctx.send('Type g!addcredits *username* to add credits to a user.')
            # discid = ctx.author
            # db.c.execute('SELECT * FROM users;')
            # users = db.c.fetchall()
            # for user in users:
            #     if str(discid) == user:
            #         db.c.execute(UPDATE)


    bot.add_cog(Work(bot)) # Adds work class to bot

    @bot.event # Displays in console bot is connected
    async def on_ready():
        print(f'{bot.user.name} has connected to Discord!\n--------')

    @bot.command(name='start', help='Starts your adventure! :D') #Creates embed of icons to choose
    async def start(message):
        discid = message.author.id
        try:
            db.c.execute('INSERT INTO users VALUES(?, 0, 0);', (discid,))  # Puts discord ID into SQLite database
            db.c.execute('INSERT INTO starters VALUES (?)', (discid, ))
            message1 = 'Welcome to your Adventure! \n'\
            'Please select a job!\n' \
            '\n' \
            ':pick: for Miner.\n'\
            ':fishing_pole_and_fish: for Fisherman.\n'\
            ':corn: for Farmer.\n'\
            ':bow_and_arrow: for Hunter.\n'\
            ':mushroom: for Gatherer.\n'\
            ':axe: for Lumberjack.\n'\
            ':compass: for Explorer.\n'
            emojis = ['\N{pick}', '🎣', '🌽', '🏹', '🍄', '🪓', '🧭']
            embed = discord.Embed(title='Welcome to EpicGamebot!', description=message1)
            authorname = message.author
            authoricon = authorname.avatar_url
            embed.set_author(name=authorname, icon_url=authoricon)
            embed.set_footer(text='EpicGameBot')
            choice = await message.send(embed=embed)  # Sends message
            for emoji in emojis:
                await choice.add_reaction(emoji) # Adds reaction emojis to message
        except Exception as e:
            print(e)
            await message.send('Already playing!')
        # db.commit()
        db.c.execute('SELECT * FROM users;')
        print(db.c.fetchall()) # Debug

    @bot.event
    async def on_reaction_add(reaction, user):
        emoji = reaction.emoji #Gets emoji from reaction
        discid = str(user.id) # String of discord ID
        db.c.execute('SELECT * FROM starters;')# Gets all users currently picking a class.
        starts = db.c.fetchall()
        if starts:
            og_discid = starts[0][0]# Discid formatted like ([id])
        else:
            og_discid = None
        message = reaction.message.channel # Original message of starting the game
        if user.bot:
            return
        if og_discid == discid:
            if emoji == '\N{pick}':
                    try:
                        db.c.execute('INSERT INTO miners VALUES (?, ?)', (discid, 0)) # Puts user as miner
                        db.c.execute('INSERT INTO ores VALUES(?, 0, 0, 0, 0, 0, 0, 0, 0)', (discid,)) # Puts user into ore table
                        await message.send("You're now a miner! :D")
                        db.c.execute('DELETE FROM starters WHERE discid == ?;', (discid, )) # Not starting anymore
                        await reaction.message.delete()
                    except Exception as e:
                        print(e) # Debug
            elif emoji == '🎣':
                try:
                    db.c.execute('INSERT INTO fishers VALUES (?, ?)', (discid, 0))
                    await message.send("You're now a fisher! :D")
                    db.c.execute('DELETE FROM starters WHERE discid == ?;', (discid,))
                    await reaction.message.delete()
                except Exception as e:
                    print(e)  # Debug
            elif emoji == '🏹':
                try:
                    db.c.execute('INSERT INTO hunters VALUES (?, ?)', (discid, 0))
                    await message.send("You're now a hunter! :D")
                    db.c.execute('DELETE FROM starters WHERE discid == ?;', (discid,))
                    await reaction.message.delete()
                except Exception as e:
                    print(e)  # Debug
            elif emoji == '🌽':
                try:
                    db.c.execute('INSERT INTO farmers VALUES (?, ?)', (discid, 0))
                    await message.send("You're now a farmer! :D")
                    db.c.execute('DELETE FROM starters WHERE discid == ?;', (discid,))
                    await reaction.message.delete()
                except Exception as e:
                    print(e)  # Debug
            elif emoji == '🍄':
                try:
                    db.c.execute('INSERT INTO gatherers VALUES (?, ?)', (discid, 0))
                    await message.send("You're now a gatherer! :D")
                    db.c.execute('DELETE FROM starters WHERE discid == ?;', (discid,))
                    await reaction.message.delete()
                except Exception as e:
                    print(e)  # Debug
            elif emoji == '🪓':
                try:
                    db.c.execute('INSERT INTO lumberjacks VALUES (?, ?)', (discid, 0))
                    await message.send("You're now a lumberjack! :D")
                    db.c.execute('DELETE FROM starters WHERE discid == ?;', (discid,))
                    await reaction.message.delete()
                except Exception as e:
                    print(e)  # Debug
            elif emoji == '🧭':
                try:
                    db.c.execute('INSERT INTO explorers VALUES (?, ?)', (discid, 0))
                    await message.send("You're now an explorer! :D")
                    db.c.execute('DELETE FROM starters WHERE discid == ?;', (discid,))
                    await reaction.message.delete()
                except Exception as e:
                    print(e)  # Debug
            else:
                await message.send('That class is SHIT! Pick another one.')
        else:
            # Completely different reaction function
            # Only for mining
            # DOESN'T WORK PROPERLY SHOULD CHECK ALL MINERS IF MORE THAN 1
            db.c.execute('SELECT * FROM miners;')  # Gets miners
            miner = db.c.fetchall()
            if miner:
                og_discid = miner[0][0]  # Discid formatted like ([id])
                print(og_discid)
            else:
                og_discid = None
                print(og_discid)
            ogmessage = reaction.message  # Original message of starting the game
            if discid == og_discid:
                await ogmessage.delete()
                db.c.execute('SELECT * FROM ores WHERE discid = ?;', (og_discid,))
                user = db.c.fetchall()
                user = list(user[0])
                user.append(5)
                mine = MineUser(user[0], user[1], user[2], user[3], user[4], user[5], user[6], user[7], user[8], user[9])
                ore, gain = mine.mine()
                await message.send(f'You have mined {gain} {ore}! LOL XD ROFLMAO')
                ore = ore.lower()
                if ore == 'copper':
                    total = mine.copper_amnt
                elif ore == 'iron':
                    total = mine.iron_amnt
                elif ore == 'silver':
                    total = mine.silver_amnt
                elif ore == 'stone':
                    total = mine.stone_amnt
                db.c.execute("""UPDATE ores
                                SET (%s) = ?
                                WHERE discid = ?
                              """% (ore), (total, og_discid))


    @bot.command(name='profile', help='Shows your profile.')
    async def profile(message): # Displays fake profile at the moment
        authorname = message.author
        description = 'This is ' + str(authorname) + "'s profile."
        authoricon = authorname.avatar_url
        embed = discord.Embed(title='Profile', description=description)
        embed.set_author(name=authorname, icon_url=authoricon)
        embed.add_field(name='Jobs', value=0, inline=True)
        embed.add_field(name='Credits', value=0, inline=True)
        embed.set_footer(text='EpicGameBot')
        await message.send(embed=embed)

    @bot.command(name='ores', help='Shows all your ores')
    async def ores(ctx):
        authorname = ctx.author
        authorid = authorname.id
        description = str(authorname) + "'s  ores."
        authoricon = authorname.avatar_url
        db.c.execute('SELECT * FROM ores WHERE discid = ?', (authorid,))
        ores = db.c.fetchall()
        aether = ores[0][1]
        diamond = ores[0][2]
        platinum = ores[0][3]
        gold = ores[0][4]
        silver = ores[0][5]
        copper = ores[0][6]
        iron = ores[0][7]
        stone = ores[0][8]
        embed = discord.Embed(title='Miner ores', description=description)
        embed.set_author(name=authorname, icon_url=authoricon)
        embed.add_field(name="Aether", value=aether, inline=True)
        embed.add_field(name="Diamond", value=diamond, inline=True)
        embed.add_field(name="Platinum", value=platinum, inline=True)
        embed.add_field(name="Gold", value=gold, inline=True)
        embed.add_field(name="Silver", value=silver, inline=True)
        embed.add_field(name="Copper", value=copper, inline=True)
        embed.add_field(name="Iron", value=iron, inline=True)
        embed.add_field(name="Stone", value=stone, inline=True)
        embed.set_footer(text='EpicGameBot')
        await ctx.send(embed=embed)

    # @bot.command(name='nigger', help='Fuck niggers.') # UH OH!!!
    # async def nigger(message):
    #     await message.send('Fuck you stupid nigger! :monkey:')
    # if message.content.upper().startswith('START'):
    #
    #     user = message.server.get_member("116273596605049942")  # Fake snowflake, will not work
    #     if not user:
    #         return  # Can't find the user, then quit
    #     pfp = user.avatar_url
    #     embed = discord.Embed(title="test", description='{}, test'.format(user.mention), color=0xecce8b)
    #     embed.set_image(url=(pfp))
    #     await client.send_message(message.channel, embed=embed)


    bot.run(TOKEN) # Starts bot


if __name__ == '__main__':
    main()
