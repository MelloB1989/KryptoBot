import requests
from urllib.request import urlopen
import json
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands

 
client = Bot(description="github.com/marios8543/KryptoBot", command_prefix="k!", pm_help = True, command_has_no_subcommand='Missing arguments!', command_not_found='Command not found. Do k!commands for a list of available commands')
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    await client.change_presence(game=discord.Game(name='k!help'))
#Help
@client.command()
async def help():
 embed=discord.Embed(title="Coin prices:", color=0xdd0000)
 embed.set_author(name='KryptoBot', icon_url='https://pm1.narvii.com/6328/5a29ffab58fa1271161d4cdc82d566ec8659d47e_hq.jpg')
 embed.add_field(name='k!btc', value='Bitcoin price', inline=False)
 embed.add_field(name='k!eth', value='Ethereum price', inline=False)
 embed.add_field(name='k!zec', value='Zcash price', inline=False)
 embed.add_field(name='k!dcr', value='Decred price', inline=False)
 embed.add_field(name='k!dash', value='Dash price', inline=False)
 embed.add_field(name='k!ltc', value='Litecoin price', inline=False)
 embed.add_field(name='k!xrp', value='Ripple price', inline=False)
 embed.add_field(name='k!etc', value='Ethereum Classic price', inline=False)
 embed.set_footer(text="KryptoBot")
 await client.say(embed=embed)
 embed2=discord.Embed(title="Mining stats:", color=0xdd0000)
 embed2.set_author(name='KryptoBot', icon_url='https://pm1.narvii.com/6328/5a29ffab58fa1271161d4cdc82d566ec8659d47e_hq.jpg')
 embed2.add_field(name='k!ethermine *address*', value='Ethermine stats', inline=False)
 embed2.add_field(name='k!ethpool *address*', value='Ethpool stats', inline=False)
 embed2.add_field(name='k!ethermineetc *address*', value='Ethermine classic stats', inline=False)
 embed2.add_field(name='k!flypool *address*', value='Flypool stats', inline=False)
 embed2.set_footer(text="KryptoBot")
 await client.say(embed=embed2)
 embed3=discord.Embed(Title="Wallet lookup:", color=0xdd0000)
 embed3.set_author(name='KryptoBot', icon_url='https://pm1.narvii.com/6328/5a29ffab58fa1271161d4cdc82d566ec8659d47e_hq.jpg')
 embed3.add_field(name='k!etherscan *address*', value='Ethereum wallet lookup', inline=False)
 embed3.add_field(name='k!blockchain *address*', value='Bitcoin wallet lookup', inline=False)
 embed3.set_footer(text='KryptoBot')
 await client.say(embed=embed3)

#Bitcoin price
@client.command()
async def btc():
 coin_json = urlopen('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR').read()
 result = json.loads(coin_json)
 usdprice = result['USD']
 eurprice = result['EUR']
 embed=discord.Embed(title='The current bitcoin price is:', color=0xf3c405)
 embed.set_author(name='Bitcoin',icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
 embed.add_field(name='USD', value=str(usdprice)+'$', inline=False)
 embed.add_field(name='EUR', value=str(eurprice)+'€', inline=False)
 embed.set_footer(text="KryptoBot")
 await client.say(embed=embed)

#Ethereum price
@client.command()
async def eth():
 coin_json = urlopen('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR').read()
 result = json.loads(coin_json)
 usdprice = result['USD']
 eurprice = result['EUR']
 embed=discord.Embed(title='The current ethereum price is:', color=0x47e463)
 embed.set_author(name='Ethereum',icon_url='https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png')
 embed.add_field(name='USD', value=str(usdprice)+'$', inline=False)
 embed.add_field(name='EUR', value=str(eurprice)+'€', inline=False)
 embed.set_footer(text="KryptoBot")
 await client.say(embed=embed)

#Zcash price
@client.command()
async def zec():
 coin_json = urlopen('https://min-api.cryptocompare.com/data/price?fsym=ZEC&tsyms=USD,EUR').read()
 result = json.loads(coin_json)
 usdprice = result['USD']
 eurprice = result['EUR']
 embed=discord.Embed(title='The current zcash price is:', color=0xffad33)
 embed.set_author(name='Zcash',icon_url='https://www.zcashcommunity.com/wp-content/uploads/2017/01/cropped-yellow-zcash-logo.png')
 embed.add_field(name='USD', value=str(usdprice)+'$', inline=False)
 embed.add_field(name='EUR', value=str(eurprice)+'€', inline=False)
 embed.set_footer(text="KryptoBot")
 await client.say(embed=embed)

#Decred price
@client.command()
async def dcr():
 coin_json = urlopen('https://min-api.cryptocompare.com/data/price?fsym=DCR&tsyms=USD,EUR').read()
 result = json.loads(coin_json)
 usdprice = result['USD']
 eurprice = result['EUR']
 embed=discord.Embed(title='The current decred price is:', color=0x47d147)
 embed.set_author(name='Decred',icon_url='https://forum.decred.org/styles/material/uix/logo.png')
 embed.add_field(name='USD', value=str(usdprice)+'$', inline=False)
 embed.add_field(name='EUR', value=str(eurprice)+'€', inline=False)
 embed.set_footer(text="KryptoBot")
 await client.say(embed=embed)

#Dash price
@client.command()
async def dash():
 coin_json = urlopen('https://min-api.cryptocompare.com/data/price?fsym=DASH&tsyms=USD,EUR').read()
 result = json.loads(coin_json)
 usdprice = result['USD']
 eurprice = result['EUR']
 embed=discord.Embed(title='The current dash price is:', color=0x0080ff)
 embed.set_author(name='Dash',icon_url='http://bitcoinchaser.com/wp-content/uploads/2017/03/dashcoin-300x300.png')
 embed.add_field(name='USD', value=str(usdprice)+'$', inline=False)
 embed.add_field(name='EUR', value=str(eurprice)+'€', inline=False)
 embed.set_footer(text="KryptoBot")
 await client.say(embed=embed)

#Litecoin price
@client.command()
async def ltc():
 coin_json = urlopen('https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=USD,EUR').read()
 result = json.loads(coin_json)
 usdprice = result['USD']
 eurprice = result['EUR']
 embed=discord.Embed(title='The current litecoin price is:', color=0xC8C8C8)
 embed.set_author(name='Litecoin',icon_url='http://ltc.133.io/images/logosizes/ltc800.png')
 embed.add_field(name='USD', value=str(usdprice)+'$', inline=False)
 embed.add_field(name='EUR', value=str(eurprice)+'€', inline=False)
 embed.set_footer(text="KryptoBot")
 await client.say(embed=embed)

#Ripple price
@client.command()
async def xrp():
 coin_json = urlopen('https://min-api.cryptocompare.com/data/price?fsym=XRP&tsyms=USD,EUR').read()
 result = json.loads(coin_json)
 usdprice = result['USD']
 eurprice = result['EUR']
 embed=discord.Embed(title='The current ripple price is:', color=0x1a53ff)
 embed.set_author(name='Ripple',icon_url='http://bitcoinist.com/wp-content/uploads/2016/08/Ripple-logo.png')
 embed.add_field(name='USD', value=str(usdprice)+'$', inline=False)
 embed.add_field(name='EUR', value=str(eurprice)+'€', inline=False)
 embed.set_footer(text="KryptoBot")
 await client.say(embed=embed)

#Ethereum classic price
@client.command()
async def etc():
 coin_json = urlopen('https://min-api.cryptocompare.com/data/price?fsym=ETC&tsyms=USD,EUR').read()
 result = json.loads(coin_json)
 usdprice = result['USD']
 eurprice = result['EUR']
 embed=discord.Embed(title='The current ethereum classic price is:', color=0x33cc33)
 embed.set_author(name='Ethereum Classic',icon_url='https://raw.githubusercontent.com/ethereumclassic/Media_Kit/master/Classic_Logo_Solid/ETC_LOGO_Full_Color_Green.png')
 embed.add_field(name='USD', value=str(usdprice)+'$', inline=False)
 embed.add_field(name='EUR', value=str(eurprice)+'€', inline=False)
 embed.set_footer(text="KryptoBot")
 await client.say(embed=embed)

#Ethermine stats
@client.command()
async def ethermine(args):
 site = 'https://api.ethermine.org/miner/{}/currentStats'.format(args)
 mine_json = requests.get(site)
 result = json.loads(mine_json.text)
 status = result['status']
 report_hash = result['data']['reportedHashrate']
 current_hash = result['data']['currentHashrate']
 average_hash = result['data']['averageHashrate']
 valid_shares = result['data']['validShares']
 invalid_shares = result['data']['invalidShares']
 stale_shares = result['data']['staleShares']
 active_workers = result['data']['activeWorkers']
 unpaid_balance = result['data']['unpaid']
 embed=discord.Embed(title=args, color=0x355271)
 embed.set_author(name='Ethermine Stats', icon_url='https://ethermine.org/images/mining.png')
 embed.add_field(name='Reported Hashrate', value=str(report_hash / 1000000 ), inline=False)
 embed.add_field(name='Actual Hashrate', value= str(current_hash / 1000000 ), inline=False)
 embed.add_field(name='Average Hashrate', value=str(average_hash / 1000000 ), inline=False)
 embed.add_field(name='Valid Shares', value=valid_shares, inline=False)
 embed.add_field(name='Invalid Shares', value=invalid_shares, inline=False)
 embed.add_field(name='Stale Shares', value=stale_shares, inline=False)
 embed.add_field(name='Active Workers', value=active_workers, inline=False)
 embed.add_field(name='Unpaid Balance', value=unpaid_balance, inline=False)
 embed.set_footer(text="KryptoBot")
 await client.say(embed=embed)

#Ethpool Stats
@client.command()
async def ethpool(args):
 site = 'https://api.ethpool.org/miner/{}/currentStats'.format(args)
 mine_json = requests.get(site)
 result = json.loads(mine_json.text)
 status = result['status']
 report_hash = result['data']['reportedHashrate']
 current_hash = result['data']['currentHashrate']
 average_hash = result['data']['averageHashrate']
 valid_shares = result['data']['validShares']
 invalid_shares = result['data']['invalidShares']
 stale_shares = result['data']['staleShares']
 active_workers = result['data']['activeWorkers']
 unpaid_balance = result['data']['unpaid']
 embed=discord.Embed(title=args, color=0x355271)
 embed.set_author(name='Ethpool Stats', icon_url='https://ethermine.org/images/mining.png')
 embed.add_field(name='Reported Hashrate', value=report_hash, inline=False)
 embed.add_field(name='Actual Hashrate', value=current_hash, inline=False)
 embed.add_field(name='Average Hashrate', value=average_hash, inline=False)
 embed.add_field(name='Valid Shares', value=valid_shares, inline=False)
 embed.add_field(name='Invalid Shares', value=invalid_shares, inline=False)
 embed.add_field(name='Stale Shares', value=stale_shares, inline=False)
 embed.add_field(name='Active Workers', value=active_workers, inline=False)
 embed.add_field(name='Unpaid Balance', value=unpaid_balance, inline=False)
 embed.set_footer(text="KryptoBot")
 await client.say(embed=embed)

#Ethermine etc
@client.command()
async def ethermineetc(args):
 site = 'https://api-etc.ethermine.org/{}/currentStats'.format(args)
 mine_json = requests.get(site)
 result = json.loads(mine_json.text)
 status = result['status']
 report_hash = result['data']['reportedHashrate']
 current_hash = result['data']['currentHashrate']
 average_hash = result['data']['averageHashrate']
 valid_shares = result['data']['validShares']
 invalid_shares = result['data']['invalidShares']
 stale_shares = result['data']['staleShares']
 active_workers = result['data']['activeWorkers']
 unpaid_balance = result['data']['unpaid']
 embed=discord.Embed(title=args, color=0x355271)
 embed.set_author(name='Ethermine Etc Stats', icon_url='https://ethermine.org/images/mining.png')
 embed.add_field(name='Reported Hashrate', value=report_hash, inline=False)
 embed.add_field(name='Actual Hashrate', value=current_hash, inline=False)
 embed.add_field(name='Average Hashrate', value=average_hash, inline=False)
 embed.add_field(name='Valid Shares', value=valid_shares, inline=False)
 embed.add_field(name='Invalid Shares', value=invalid_shares, inline=False)
 embed.add_field(name='Stale Shares', value=stale_shares, inline=False)
 embed.add_field(name='Active Workers', value=active_workers, inline=False)
 embed.add_field(name='Unpaid Balance', value=unpaid_balance, inline=False)
 embed.set_footer(text="KryptoBot")
 await client.say(embed=embed)

#Flypool stats
@client.command()
async def flypool(args):
 site = 'https://api-zcash.flypool.org/{}/currentStats'.format(args)
 mine_json = requests.get(site)
 result = json.loads(mine_json.text)
 status = result['status']
 report_hash = result['data']['reportedHashrate']
 current_hash = result['data']['currentHashrate']
 average_hash = result['data']['averageHashrate']
 valid_shares = result['data']['validShares']
 invalid_shares = result['data']['invalidShares']
 stale_shares = result['data']['staleShares']
 active_workers = result['data']['activeWorkers']
 unpaid_balance = result['data']['unpaid']
 embed=discord.Embed(title=args, color=0x355271)
 embed.set_author(name='Flypool Stats', icon_url='https://ethermine.org/images/mining.png')
 embed.add_field(name='Reported Hashrate', value=report_hash, inline=False)
 embed.add_field(name='Actual Hashrate', value=current_hash, inline=False)
 embed.add_field(name='Average Hashrate', value=average_hash, inline=False)
 embed.add_field(name='Valid Shares', value=valid_shares, inline=False)
 embed.add_field(name='Invalid Shares', value=invalid_shares, inline=False)
 embed.add_field(name='Stale Shares', value=stale_shares, inline=False)
 embed.add_field(name='Active Workers', value=active_workers, inline=False)
 embed.add_field(name='Unpaid Balance', value=unpaid_balance, inline=False)
 embed.set_footer(text="KryptoBot")
 await client.say(embed=embed)

#Nicehash stats
#@client.command()
#async def nicehash(args):
# site = 'https://api.nicehash.com/api?method=stats.provider&addr={}'.format(args)
# mine_json = requests.get(site)
# result = json.loads(mine_json.text)
# nice_balance = int(result['result']['stats']['balance'])
# reject_speed = int(result['result']['stats']['rejected_speed'])
# accepted_speed = int(result['result']['stats']['accepted_speed'])
# algorithm = int(result['result']['stats']['algo'])
# await client.say(nice_balance)
# await client.say(reject_speed)
# await client.say(accepted_speed)
# await client.say(algorithm)

#Etherscan stats
@client.command()
async def etherscan(args):
 #coin_json = urlopen('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR').read()
 #result = json.loads(coin_json)
 #usdprice = result['USD']
 #eurprice = result['EUR']
 etherscan_site = 'https://api.etherscan.io/api?module=account&action=balance&address={}&tag=latest&apikey='.format(args)
 check_json = requests.get(etherscan_site)
 etherscan_result = json.loads(check_json.text)
 microether_balance = etherscan_result['result']
 ether_balance = int(microether_balance) / 1000000000000000000
 #usd_balance = ether_balance * usdprice
 #eur_balance = ether_balance * eurprice
 ether_balance_string = str(ether_balance)
 #usd_balance_string = str(usd_balance)
 #eur_balance_string = str(eur_balance)
 embed=discord.Embed(title='Ethereum Stats', color=0x47e463)
 embed.set_author(name=args,icon_url='https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png')
 embed.add_field(name='Balance', value=ether_balance_string[0:11] + 'ETH' , inline=False)
 #embed.add_field(name='USD', value=usd_balance_string[0:] + '$', inline=False)
 #embed.add_field(name='EUR', value= + '€', inline=False)
 embed.set_footer(text="KryptoBot")
 await client.say(embed=embed)

#Blockchain.info stats
@client.command()
async def blockchain(args):
 blockchain_site = 'https://blockchain.info/rawaddr/{}'.format(args)
 check_json = requests.get(blockchain_site)
 blockchain_result = json.loads(check_json.text)
 micro_balance = blockchain_result['final_balance']
 total_received = blockchain_result['total_received']
 total_sent = blockchain_result['total_sent']
 transactions = blockchain_result['n_tx']
 bitcoin_balance = int(micro_balance) / 100000000
 bitcoin_balance_string = str(bitcoin_balance)
 received_int = int(total_received) / 100000000
 received_string = str(received_int)
 sent_int = int(total_sent) / 100000000
 sent_str = str(sent_int)
 embed=discord.Embed(title='Bitcoin Stats', color=0xf3c405)
 embed.set_author(name=args,icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
 embed.add_field(name='Balance', value=bitcoin_balance_string + 'BTC' , inline=False)
 embed.add_field(name='Total Received', value=received_string + 'BTC', inline=False)
 embed.add_field(name='Total Sent', value=sent_str + 'BTC', inline=False)
 embed.add_field(name='No. of transactions', value=transactions, inline=False)
 embed.set_footer(text="KryptoBot")
 await client.say(embed=embed)


#Nicehash Stats
#Coming soon...


client.run('YOUR_BOT_TOKEN_HERE')
