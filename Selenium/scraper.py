from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import threading
import os
import discord
from discord.ext import commands
from discord.ext import tasks, commands
intents = discord.Intents.default()


    

intents.guilds = True

activity = discord.Activity(type=discord.ActivityType.watching, name="Working...")
bot = commands.Bot(command_prefix = "?", intents = intents, activity=activity, status=discord.Status.online)


    

@tasks.loop(seconds=60) # task runs every 60 seconds
async def stockupdate():

    await bot.wait_until_ready()
    chromedriver = '/Users/navin/Desktop/Selenium/chromedriver'
    browser = webdriver.Chrome(chromedriver)
    browser.get(('https://opensea.io/collection/tailopez'))

    
    
    time.sleep(3)
    
    fp = browser.find_element(By.XPATH,"/html/body/div[1]/div/main/div/div/div[1]/div[2]/div[4]/div/div[3]/a/div/div[1]/div/span/div")
    print(fp.text)
    fptext = fp.text
    
    browser.close()
    await bot.get_guild(942153314915713126).me.edit(nick="OGC Floor Price: " + fptext)
    await bot.change_presence(status = discord.Status.online, activity = discord.Activity(type=discord.ActivityType.watching, name= "Floor Price: " + fptext))

stockupdate.start()

bot.run("ODUyMTU3MzM2ODU1NTExMDcw.YMCvXQ.e25wsaeCHwQf-m2xX16UgBo1gRM")