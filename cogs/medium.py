import os
import discord

from time import sleep
from datetime import datetime
from config import get_config

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from discord.ext import commands

class ScrapingMedium(commands.Cog, name='ScrapíngMedium'):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.hybrid_command(
        name="medium",
        description="Tira print de uma página do Medium",
    )
    async def medium(self, ctx: commands.Context, url: str):
        msg = await ctx.send("Espera, estou analisando a URL...")
        try:
            id_file = datetime.now().timestamp()
            file_name = "screenshot_" + str(id_file) + ".png"
            await self.capture_medium_page(url, msg, file_name)
        except Exception as e:
            print("Ocorreu um erro: " + str(e))
            await ctx.send("Deu erro, tenta de novo")
            return

        await msg.edit(content="Pronto, estou enviando a imagem")
        with open(file_name, 'rb') as img:
            await ctx.send(file=discord.File(img))
        os.remove(file_name)

    async def capture_medium_page(self, url, ctx, save_path):
        # Configurando o driver
        chrome_op = webdriver.ChromeOptions()
        chrome_op.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_op)
        driver.maximize_window()
        # Logando no Twitter
        if get_config().CREDENTIAL_TYPE.lower() == "twitter":
            await ctx.edit(content="Estou logando no Twitter...")
            driver.get(get_config().URL_LOGIN_TWITTER)
            driver.implicitly_wait(10)
            await ctx.edit(content="Estou logando no Medium...")
            sleep(1)
            username_field = driver.find_element(By.ID, 'username_or_email')
            username_field.send_keys(get_config().CREDENTIAL_USERNAME)
            password_field = driver.find_element(By.ID, 'password')
            password_field.send_keys(get_config().CREDENTIAL_PASSWORD)
            password_field.send_keys(Keys.RETURN)
            driver.implicitly_wait(10)
        else:
            raise Exception("Tipo de credencial não suportada")
        # Entrando na página
        await ctx.edit(content="Entrando no link fornecido...")
        sleep(1)
        driver.get(url)
        driver.implicitly_wait(10)
        # Tirando print
        await ctx.edit(content="Tirando print da página...")
        web_page_height = driver.execute_script("return document.body.scrollHeight")
        driver.set_window_size(1920, web_page_height)
        page_body = driver.find_element(By.TAG_NAME, 'body')
        page_body.screenshot(save_path)
        driver.quit()

async def setup(bot) -> None:
    await bot.add_cog(ScrapingMedium(bot))