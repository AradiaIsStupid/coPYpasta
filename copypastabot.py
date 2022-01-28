import random
import discord
import praw
from discord.ext import commands
import loginshit

# commands prefix. will try to use / commands later
bot = commands.Bot(command_prefix="cp!")

# reddit sign in stuff
reddit = praw.Reddit(
    client_id=loginshit.cwient_id,
    client_secret=loginshit.cwient_secwet,
    username=loginshit.usewname,
    password=loginshit.passwewd,
    user_agent=loginshit.usew_agent,
)


@bot.command()
async def copypasta(ctx):
    subreddit = reddit.subreddit("copypasta")
    all_subs = []
    top = subreddit.top(limit=50)
    for submission in top:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    body = random_sub.selftext
    em = discord.Embed(title=name)
    em = discord.Embed(description=body)
    await ctx.send(embed=em)


bot.run(loginshit.tewken)
