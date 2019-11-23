import ccxt

exchange = ccxt.bitmex({
    'apiKey': 'ENTER API KEY HERE',
    'secret': 'ENTER API SECRET HERE',
    'enableRateLimit': True,
})
