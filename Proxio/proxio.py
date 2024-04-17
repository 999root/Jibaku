import requests

def scrape_proxies() -> str:
    url = "https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&proxy_format=protocolipport&format=text"
    proxies_response = requests.get(url)
    proxies_text = proxies_response.text
    return proxies_text

def write_to_txt(proxies) -> None:
    with open("scraped_proxies.txt", 'w') as f:
        f.write(proxies)

def structure() -> list:
    array = []
    with open("scraped_proxies.txt", 'r') as f:
        proxies = f.readlines()
    for proxy in proxies:
        array.append(proxy.strip())  # Strip newline characters
    return array

def default_scrape() -> list:
    proxies = scrape_proxies()
    write_to_txt(proxies)
    array = structure()
    return array



class Filter:
    def filter_socks4_proxies(proxies: list) -> list:
        socks4_proxies = []
        for proxy in proxies:
            if proxy.startswith("socks4://"):
                socks4_proxies.append(proxy)
        return socks4_proxies
    
    def filter_socks5_proxies(proxies: list) -> list:
        socks5_proxies = []
        for proxy in proxies:
            if proxy.startswith("socks5://"):
                socks5_proxies.append(proxy)
        return socks5_proxies
    
    def filter_http_proxies(proxies: list) -> list:
        http_proxies = []
        for proxy in proxies:
            if proxy.startswith("http://"):
                http_proxies.append(proxy)
        return http_proxies
    
    def filter_https_proxies(proxies: list) -> list:
        https_proxies = []
        for proxy in proxies:
            if proxy.startswith("https://"):
                https_proxies.append(proxy)
        return https_proxies



class Socks4:
    def check_socks4_proxy(proxy):
        try:
            response = requests.get("https://www.example.com", proxies={"socks4": proxy}, timeout=5)
            if response.status_code == 200:
                return "SUCCESS"
            else:
                return "FAIL"
        except Exception as e:
            return "FAIL"

    def check_socks4_proxies(socks4_proxies) -> list:
        results = []
        for proxy in socks4_proxies:
            result = Socks4.check_socks4_proxy(proxy)
            results.append(result)
            print(f"Proxy {proxy}: {result}")
        return results
    
class Socks5:
    def check_socks5_proxy(proxy):
        try:
            response = requests.get("https://www.example.com", proxies={"socks5": proxy}, timeout=5)
            if response.status_code == 200:
                return "SUCCESS"
            else:
                return "FAIL"
        except Exception as e:
            return "FAIL"
        
    def check_socks5_proxies(socks5_proxies) -> list:
        results = []
        for proxy in socks5_proxies:
            result = Socks5.check_socks5_proxy(proxy)
            results.append(result)
            print(f"Proxy {proxy}: {result}")
        return results
