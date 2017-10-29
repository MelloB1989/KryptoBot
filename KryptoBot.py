from urllib.request import urlopen
import json
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands


client = Bot(description="https://github.com/marios8543/", command_prefix="k!", pm_help = True)
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')


@client.command()
async def bitcoin():
 coin_json = urlopen('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR').read()
 result = json.loads(coin_json)
 usdprice = result['USD']
 eurprice = result['EUR']
 embed=discord.Embed(title='The current bitcoin price is:', color=0xf3c405)
 embed.set_author(name='Bitcoin',icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
 embed.add_field(name='USD', value=str(usdprice)+'$', inline=False)
 embed.add_field(name='EUR', value=str(eurprice)+'€', inline=False)
 await client.say(embed=embed)


@client.command()
async def ethereum():
 coin_json = urlopen('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR').read()
 result = json.loads(coin_json)
 usdprice = result['USD']
 eurprice = result['EUR']
 embed=discord.Embed(title='The current ethereum price is:', color=0x47e463)
 embed.set_author(name='Ethereum',icon_url='https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png')
 embed.add_field(name='USD', value=str(usdprice)+'$', inline=False)
 embed.add_field(name='EUR', value=str(eurprice)+'€', inline=False)
 await client.say(embed=embed)

@client.command()
async def zcash():
 coin_json = urlopen('https://min-api.cryptocompare.com/data/price?fsym=ZEC&tsyms=USD,EUR').read()
 result = json.loads(coin_json)
 usdprice = result['USD']
 eurprice = result['EUR']
 embed=discord.Embed(title='The current zcash price is:', color=0x47e463)
 embed.set_author(name='Zcash',icon_url='https://www.zcashcommunity.com/wp-content/uploads/2017/01/cropped-yellow-zcash-logo.png')
 embed.add_field(name='USD', value=str(usdprice)+'$', inline=False)
 embed.add_field(name='EUR', value=str(eurprice)+'€', inline=False)
 await client.say(embed=embed)

@client.command()
async def decred():
 coin_json = urlopen('https://min-api.cryptocompare.com/data/price?fsym=DCR&tsyms=USD,EUR').read()
 result = json.loads(coin_json)
 usdprice = result['USD']
 eurprice = result['EUR']
 embed=discord.Embed(title='The current decred price is:', color=0x47e463)
 embed.set_author(name='Decred',icon_url='https://forum.decred.org/styles/material/uix/logo.png')
 embed.add_field(name='USD', value=str(usdprice)+'$', inline=False)
 embed.add_field(name='EUR', value=str(eurprice)+'€', inline=False)
 await client.say(embed=embed)

@client.command()
async def dash():
 coin_json = urlopen('https://min-api.cryptocompare.com/data/price?fsym=DASH&tsyms=USD,EUR').read()
 result = json.loads(coin_json)
 usdprice = result['USD']
 eurprice = result['EUR']
 embed=discord.Embed(title='The current dash price is:', color=0x47e463)
 embed.set_author(name='Dash',icon_url='http://bitcoinchaser.com/wp-content/uploads/2017/03/dashcoin-300x300.png')
 embed.add_field(name='USD', value=str(usdprice)+'$', inline=False)
 embed.add_field(name='EUR', value=str(eurprice)+'€', inline=False)
 await client.say(embed=embed)


client.run('YOUR_BOT_TOKEN_HERE')
