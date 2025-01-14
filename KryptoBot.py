import requests
from urllib.request import urlopen
import json
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands

def percent(arg1,arg2):
    percentage = str(100 * int(arg2) / int(arg1))
    percentage_final = percentage[0:-12] + '%'
    return percentage_final


client = Bot(description="github.com/marios8543/KryptoBot", command_prefix="k!", pm_help = True, command_has_no_subcommand='Missing arguments!', command_not_found='Command not found. Do k!help for a list of available commands')

@client.event
async def on_ready():
 print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
 await client.change_presence(game=discord.Game(name='k!help'))

#Help
@client.command(pass_context=True)
async def help(ctx, member: discord.Member = None):
 member = ctx.message.author
 embed=discord.Embed(title="Coin prices:", color=0xdd0000)
 embed.set_author(name='KryptoBot', icon_url='https://cdn.discordapp.com/attachments/374575174432849922/380423351958765589/krypto.jpg')
 embed.add_field(name='k!btc', value='Bitcoin price', inline=False)
 embed.add_field(name='k!eth', value='Ethereum price', inline=False)
 embed.add_field(name='k!zec', value='Zcash price', inline=False)
 embed.add_field(name='k!dcr', value='Decred price', inline=False)
 embed.add_field(name='k!dash', value='Dash price', inline=False)
 embed.add_field(name='k!ltc', value='Litecoin price', inline=False)
 embed.add_field(name='k!xrp', value='Ripple price', inline=False)
 embed.add_field(name='k!etc', value='Ethereum Classic price', inline=False)
 embed.add_field(name='k!doge', value='Dogecoin price', inline=False)
 embed.add_field(name='k!bch', value='Bitcoin Cash Price', inline=False)
 #await client.say(embed=embed)
 embed2=discord.Embed(title="Mining stats:", color=0xdd0000)
 embed2.set_author(name='', icon_url='https://cdn.discordapp.com/attachments/374575174432849922/380423351958765589/krypto.jpg')
 embed2.add_field(name='k!ethermine *address*', value='Ethermine stats', inline=False)
 embed2.add_field(name='k!ethpool *address*', value='Ethpool stats', inline=False)
 embed2.add_field(name='k!ethermineetc *address*', value='Ethermine classic stats', inline=False)
 embed2.add_field(name='k!flypool *address*', value='Flypool stats', inline=False)
 #await client.say(embed=embed2)
 embed3=discord.Embed(Title="Wallet lookup:", color=0xdd0000)
 embed3.set_author(name='', icon_url='https://cdn.discordapp.com/attachments/374575174432849922/380423351958765589/krypto.jpg')
 embed3.add_field(name='k!etherscan *address*', value='Ethereum wallet lookup', inline=False)
 embed3.add_field(name='k!blockchain *address*', value='Bitcoin wallet lookup', inline=False)
 embed3.set_footer(text='KryptoBot')
 #await client.say(embed=embed3)
 await client.send_message(member, embed=embed)
 await client.send_message(member, embed=embed2)
 await client.send_message(member, embed=embed3)
 await client.say('`Help has been slid into your DMs UwU`')

#Bitcoin price
@client.command()
async def btc():
 coin_json = urlopen('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR').read()
 result_stats = json.loads(coin_json)
 usdprice = result_stats['USD']
 eurprice = result_stats['EUR']
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
 result_stats = json.loads(coin_json)
 usdprice = result_stats['USD']
 eurprice = result_stats['EUR']
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
 result_stats = json.loads(coin_json)
 usdprice = result_stats['USD']
 eurprice = result_stats['EUR']
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
 result_stats = json.loads(coin_json)
 usdprice = result_stats['USD']
 eurprice = result_stats['EUR']
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
 result_stats = json.loads(coin_json)
 usdprice = result_stats['USD']
 eurprice = result_stats['EUR']
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
 result_stats = json.loads(coin_json)
 usdprice = result_stats['USD']
 eurprice = result_stats['EUR']
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
 result_stats = json.loads(coin_json)
 usdprice = result_stats['USD']
 eurprice = result_stats['EUR']
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
 result_stats = json.loads(coin_json)
 usdprice = result_stats['USD']
 eurprice = result_stats['EUR']
 embed=discord.Embed(title='The current ethereum classic price is:', color=0x33cc33)
 embed.set_author(name='Ethereum Classic',icon_url='https://raw.githubusercontent.com/ethereumclassic/Media_Kit/master/Classic_Logo_Solid/ETC_LOGO_Full_Color_Green.png')
 embed.add_field(name='USD', value=str(usdprice)+'$', inline=False)
 embed.add_field(name='EUR', value=str(eurprice)+'€', inline=False)
 embed.set_footer(text="KryptoBot")
 await client.say(embed=embed)

#Dogecoin price
@client.command()
async def doge():
 coin_json = urlopen('https://min-api.cryptocompare.com/data/price?fsym=DOGE&tsyms=USD,EUR').read()
 result_stats = json.loads(coin_json)
 usdprice = result_stats['USD']
 eurprice = result_stats['EUR']
 embed=discord.Embed(title='The current dogecoin price is:', color=0xcc9900)
 embed.set_author(name='Dogecoin',icon_url='https://i.redd.it/ony3qesa3ebx.png')
 embed.add_field(name='USD', value=str(usdprice)+'$', inline=False)
 embed.add_field(name='EUR', value=str(eurprice)+'€', inline=False)
 embed.set_footer(text="KryptoBot")
 await client.say(embed=embed)

#Bitcoin cash prices
@client.command()
async def bch():
 coin_json = urlopen('https://min-api.cryptocompare.com/data/price?fsym=BCH&tsyms=USD,EUR').read()
 result_stats = json.loads(coin_json)
 usdprice = result_stats['USD']
 eurprice = result_stats['EUR']
 embed=discord.Embed(title='The current bitcoin cash price is:', color=0xf3c405)
 embed.set_author(name='Bitcoin Cash',icon_url='https://files.coinmarketcap.com/static/img/coins/32x32/bitcoin-cash.png')
 embed.add_field(name='USD', value=str(usdprice)+'$', inline=False)
 embed.add_field(name='EUR', value=str(eurprice)+'€', inline=False)
 embed.set_footer(text="KryptoBot")
 await client.say(embed=embed)

#Ethermine stats
@client.command()
async def ethermine(arg):
 site_stats = 'https://api.ethermine.org/miner/{}/currentStats'.format(arg)
 site_settings = 'https://api.ethermine.org/miner/{}/settings'.format(arg)
 set_json = requests.get(site_settings)
 mine_json = requests.get(site_stats)
 result_stats = json.loads(mine_json.text)
 set_stats = json.loads(set_json.text)
 payout = set_stats['data']['minPayout']
 report_hash = result_stats['data']['reportedHashrate']
 current_hash = result_stats['data']['currentHashrate']
 average_hash = result_stats['data']['averageHashrate']
 valid_shares = result_stats['data']['validShares']
 invalid_shares = result_stats['data']['invalidShares']
 stale_shares = result_stats['data']['staleShares']
 active_workers = result_stats['data']['activeWorkers']
 unpaid_balance = result_stats['data']['unpaid']
 prcnt = percent(payout, unpaid_balance)
 embed=discord.Embed(title=arg, color=0x355271)
 embed.set_author(name='Ethermine Stats', icon_url='https://ethermine.org/images/mining.png')
 embed.add_field(name='Reported Hashrate', value=str(report_hash / 1000000 )[0:-5] + ' MH/s', inline=False)
 embed.add_field(name='Actual Hashrate', value= str(current_hash / 1000000 )[0:-13] + ' MH/s', inline=False)
 embed.add_field(name='Average Hashrate', value=str(average_hash / 1000000 )[0:-13] + ' MH/s', inline=False)
 embed.add_field(name='Valid Shares', value=valid_shares, inline=False)
 embed.add_field(name='Invalid Shares', value=invalid_shares, inline=False)
 embed.add_field(name='Stale Shares', value=stale_shares, inline=False)
 embed.add_field(name='Active Workers', value=active_workers, inline=False)
 embed.add_field(name='Unpaid Balance', value=str(unpaid_balance / 1000000000000000000)[0:-12] +'ETH ('+prcnt+')', inline=False)
 embed.set_footer(text="KryptoBot")
 await client.say(embed=embed)

#Ethpool Stats
@client.command()
async def ethpool(args):
 site_stats = 'https://api.ethpool.org/miner/{}/currentStats'.format(args)
 mine_json = requests.get(site_stats)
 result_stats = json.loads(mine_json.text)
 report_hash = result_stats['data']['reportedHashrate']
 current_hash = result_stats['data']['currentHashrate']
 average_hash = result_stats['data']['averageHashrate']
 valid_shares = result_stats['data']['validShares']
 invalid_shares = result_stats['data']['invalidShares']
 stale_shares = result_stats['data']['staleShares']
 active_workers = result_stats['data']['activeWorkers']
 embed=discord.Embed(title=args, color=0x355271)
 embed.set_author(name='Ethpool Stats', icon_url='https://ethermine.org/images/mining.png')
 embed.add_field(name='Reported Hashrate', value=str(report_hash / 1000000 )[0:-5] + 'MH/s', inline=False)
 embed.add_field(name='Actual Hashrate', value= str(current_hash / 1000000 )[0:-13] + 'MH/s', inline=False)
 embed.add_field(name='Average Hashrate', value=str(average_hash / 1000000 )[0:-13] + 'MH/s', inline=False)
 embed.add_field(name='Valid Shares', value=valid_shares, inline=False)
 embed.add_field(name='Invalid Shares', value=invalid_shares, inline=False)
 embed.add_field(name='Stale Shares', value=stale_shares, inline=False)
 embed.add_field(name='Active Workers', value=active_workers, inline=False)
 embed.set_footer(text="KryptoBot")
 await client.say(embed=embed)

#Ethermine etc
@client.command()
async def ethermineetc(args):
 site_stats = 'https://api-etc.ethermine.org/miner/{}/currentStats'.format(args)
 site_settings = 'https://api-etc.ethermine.org/miner/{}/settings'.format(args)
 set_json = requests.get(site_settings)
 mine_json = requests.get(site_stats)
 result_stats = json.loads(mine_json.text)
 set_stats = json.loads(set_json.text)
 payout = set_stats['data']['minPayout']
 report_hash = result_stats['data']['reportedHashrate']
 current_hash = result_stats['data']['currentHashrate']
 average_hash = result_stats['data']['averageHashrate']
 valid_shares = result_stats['data']['validShares']
 invalid_shares = result_stats['data']['invalidShares']
 stale_shares = result_stats['data']['staleShares']
 active_workers = result_stats['data']['activeWorkers']
 unpaid_balance = result_stats['data']['unpaid']
 prcnt = percent(payout, unpaid_balance)
 embed=discord.Embed(title=args, color=0x355271)
 embed.set_author(name='Ethermine Classic Stats', icon_url='https://ethermine.org/images/mining.png')
 embed.add_field(name='Reported Hashrate', value=str(report_hash / 1000000 )[0:-5] + 'MH/s', inline=False)
 embed.add_field(name='Actual Hashrate', value= str(current_hash / 1000000 )[0:-13] + 'MH/s', inline=False)
 embed.add_field(name='Average Hashrate', value=str(average_hash / 1000000 )[0:-13] + 'MH/s', inline=False)
 embed.add_field(name='Valid Shares', value=valid_shares, inline=False)
 embed.add_field(name='Invalid Shares', value=invalid_shares, inline=False)
 embed.add_field(name='Stale Shares', value=stale_shares, inline=False)
 embed.add_field(name='Active Workers', value=active_workers, inline=False)
 embed.add_field(name='Unpaid Balance', value=str(unpaid_balance / 1000000000000000000)[0:-12] +'ETC ('+prcnt+')', inline=False)
 embed.set_footer(text="KryptoBot")
 await client.say(embed=embed)

#Flypool stats
@client.command()
async def flypool(args):
 site_stats = 'https://api-zcash.flypool.org/miner/{}/currentStats'.format(args)
 site_settings = 'https://api-zcash.flypool.org/miner/{}/settings'.format(args)
 set_json = requests.get(site_settings)
 mine_json = requests.get(site_stats)
 result_stats = json.loads(mine_json.text)
 set_stats = json.loads(set_json.text)
 payout = set_stats['data']['minPayout']
 current_hash = result_stats['data']['currentHashrate']
 average_hash = result_stats['data']['averageHashrate']
 valid_shares = result_stats['data']['validShares']
 invalid_shares = result_stats['data']['invalidShares']
 stale_shares = result_stats['data']['staleShares']
 active_workers = result_stats['data']['activeWorkers']
 unpaid_balance = result_stats['data']['unpaid']
 unconfirmed_balance = result_stats['data']['unconfirmed']
 prcnt = percent(payout, unpaid_balance)
 embed=discord.Embed(title=args, color=0x355271)
 embed.set_author(name='Flypool Zcash Stats', icon_url='https://ethermine.org/images/mining.png')
 embed.add_field(name='Actual Hashrate', value= str(current_hash / 100000000 ) + 'KH/s', inline=False)
 embed.add_field(name='Average Hashrate', value=str(average_hash / 100000000 ) + 'KH/s', inline=False)
 embed.add_field(name='Valid Shares', value=valid_shares, inline=False)
 embed.add_field(name='Invalid Shares', value=invalid_shares, inline=False)
 embed.add_field(name='Stale Shares', value=stale_shares, inline=False)
 embed.add_field(name='Active Workers', value=active_workers, inline=False)
 embed.add_field(name='Unpaid Balance', value=str(unpaid_balance / 100000000)[0:-3] +' ZEC', inline=False)
 embed.add_field(name='Unconfirmed Balance', value=str(unconfirmed_balance / 100000000)[0:-3] +' ZEC', inline=False)
 embed.set_footer(text="KryptoBot")
 await client.say(embed=embed)

#Nicehash stats
#@client.command()
#async def nicehash(args):
# site = 'https://api.nicehash.com/api?method=stats.provider&addr={}'.format(args)
# mine_json = requests.get(site)
# result_stats = json.loads(mine_json.text)
# nice_balance = result_stats['result_stats']['stats']['balance']
# reject_speed = result_stats['result_stats']['stats']['rejected_speed']
# accepted_speed = result_stats['result_stats']['stats']['accepted_speed']
# algorithm = result_stats['result_stats']['stats']['algo']
# await client.say(nice_balance)
# await client.say(reject_speed)
# await client.say(accepted_speed)
# await client.say(algorithm)

#Etherscan stats
@client.command()
async def etherscan(args):
 #coin_json = urlopen('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR').read()
 #result_stats = json.loads(coin_json)
 #usdprice = result_stats['USD']
 #eurprice = result_stats['EUR']
 etherscan_site = 'https://api.etherscan.io/api?module=account&action=balance&address={}&tag=latest&apikey='.format(args)
 check_json = requests.get(etherscan_site)
 etherscan_result_stats = json.loads(check_json.text)
 microether_balance = etherscan_result_stats['result']
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
 blockchain_result_stats = json.loads(check_json.text)
 micro_balance = blockchain_result_stats['final_balance']
 total_received = blockchain_result_stats['total_received']
 total_sent = blockchain_result_stats['total_sent']
 transactions = blockchain_result_stats['n_tx']
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

#Convert BTC
@client.command()
async def convertBTC(args):
  btc_json = urlopen('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR').read()
  btc_result_stats = json.loads(btc_json)
  btcusdprice = btc_result_stats['USD']
  btceurprice = btc_result_stats['EUR']
  usd_result_stats = float(args) * int(btcusdprice)
  eur_result_stats = float(args) * int(btceurprice)
  embed = discord.Embed(title=str(args) + 'BTC is:', color=0xf3c405)
  embed.add_field(name='USD', value= str(usd_result_stats) + '$')
  embed.add_field(name='EUR', value=str(eur_result_stats) + '€')
  embed.set_footer(text="KryptoBot")
  await client.say(embed=embed)

@client.command()
async def convertETH(args):
  eth_json = urlopen('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR').read()
  eth_result_stats = json.loads(eth_json)
  ethusdprice = eth_result_stats['USD']
  etheurprice = eth_result_stats['EUR']
  usd_result_stats = float(args) * int(ethusdprice)
  eur_result_stats = float(args) * int(etheurprice)
  embed = discord.Embed(title=str(args) + 'ETH is:', color=0x47e463)
  embed.add_field(name='USD', value= str(usd_result_stats) + '$')
  embed.add_field(name='EUR', value=str(eur_result_stats) + '€')
  embed.set_footer(text="KryptoBot")
  await client.say(embed=embed)

@client.command()
async def convertDCR(args):
  dcr_json = urlopen('https://min-api.cryptocompare.com/data/price?fsym=DCR&tsyms=USD,EUR').read()
  dcr_result_stats = json.loads(dcr_json)
  dcrusdprice = dcr_result_stats['USD']
  dcreurprice = dcr_result_stats['EUR']
  usd_result_stats = float(args) * int(dcrusdprice)
  eur_result_stats = float(args) * int(dcreurprice)
  embed = discord.Embed(title=str(args) + 'DCR is:', color=0x47d147)
  embed.add_field(name='USD', value= str(usd_result_stats) + '$')
  embed.add_field(name='EUR', value=str(eur_result_stats) + '€')
  embed.set_footer(text="KryptoBot")
  await client.say(embed=embed)



client.run('ODY0MDQxODIwMjY1OTA2MjA2.YOvrpw.I7X5iZhJyfvss9Q30TjObN7ZNMo')
