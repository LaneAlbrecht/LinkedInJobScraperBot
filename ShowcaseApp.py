import time
import discord
from discord.ext import commands
import scraper as jobs
import os, sys

token = 'A VALID TOKEN IS PUT HERE :)'

def embed(jobListing):
  msg = discord.Embed(
    title = jobListing["title"],
    description = "@" + jobListing["company"] + " in " + jobListing["location"],
    url = jobListing["link"]
  )
  return msg

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='$', intents=intents)

@client.event
async def on_ready():
  print("SCRAPPER ONLINE, READY TO SCRAPE...")

@client.command()
async def giveJobs(ctx, arg=None):
  if(arg != None):
    await ctx.send("Finding jobs for: " + arg)
  else:
     await ctx.send("Finding Jobs...")
  i = 0
# send X jobs every X days
  while i < 5:
    if(arg == "gd" or arg == "game" or arg == "gamedev"):
        await ctx.send(embed=embed(jobs.get_jobs("GameDeveloper")[i]))
    elif(arg == "cm" or arg == "communitymanager"):
        await ctx.send(embed=embed(jobs.get_jobs("CommunityManager")[i]))
    elif(arg == "sm" or arg == "social" or arg == "socialmedia"):
        await ctx.send(embed=embed(jobs.get_jobs("SocialMedia")[i]))
    elif(arg == "sw" or arg == "software" or arg == "soft"):
        await ctx.send(embed=embed(jobs.get_jobs("SoftwareEngineer")[i]))
    else:
        await ctx.send("No Jobs of type: " + arg + " found.")
    i += 1


client.run(token)