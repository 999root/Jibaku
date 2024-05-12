
# Imports
import requests




class Scrape:
    def __init__(self):
        self.url = "https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&proxy_format=protocolipport&format=text"
        self.file_name = "scraped_proxies.txt"
        self.open_type = "w"
        self.array = []

    def scrape_proxies(self) -> str:
        proxies_response = requests.get(self.url)
        proxies_text = proxies_response.text
        return proxies_text

    def write_to_txt(self, proxies: str) -> None:
        with open(self.file_name, self.open_type) as f:
            f.write(proxies)

    def structure(self) -> list:
        with open(self.file_name, 'r') as f:
            proxies = f.readlines()
        for proxy in proxies:
            self.array.append(proxy.strip())
        return self.array

    def full_scrape(self) -> list:
        proxies = self.scrape_proxies()
        self.write_to_txt(proxies)
        array = self.structure()
        return array




class Filter:
    def __init__(self):
        self.socks4_proxies = []
        self.socks5_proxies = []
        self.http_proxies = []
        self.https_proxies = []
        
        self.socks4 = "socks4://"
        self.socks5 = "socks5://"
        self.http = "http://"
        self.https = "https://"

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
            response = requests.get("https://999root.xyz", proxies={"socks4": proxy}, timeout=5)
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
            response = requests.get("https://999root.xyz", proxies={"socks5": proxy}, timeout=5)
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

class HTTP:
    def check_http_proxy(proxy):
        try:
            response = requests.get("https://999root.xyz", proxies={"http": proxy}, timeout=5)
            if response.status_code == 200:
                return "SUCCESS"
            else:
                return "FAIL"
        except Exception as e:
            return "FAIL"
        
    def check_http_proxies(http_proxies) -> list:
        results = []
        for proxy in http_proxies:
            result = HTTP.check_http_proxy(proxy)
            results.append(result)
            print(f"Proxy {proxy}: {result}")
        return results

class HTTPS:
    def check_https_proxy(proxy):
        try:
            response = requests.get("https://999root.xyz", proxies={"https": proxy}, timeout=5)
            if response.status_code == 200:
                return "SUCCESS"
            else:
                return "FAIL"
        except Exception as e:
            return "FAIL"
        
    def check_https_proxies(https_proxies) -> list:
        results = []
        for proxy in https_proxies:
            result = HTTPS.check_https_proxy(proxy)
            results.append(result)
            print(f"Proxy {proxy}: {result}")
        return results




class Proxio:
    def __init__(self):
        """ Quick use of the entire proxio module """
        self.filter = Filter()
        self.scraper = Scrape()

    def auto_socks5_check(self) -> list:
        """
        Scrapes, Structures, Filters, and Checks Activity of Socks5 Proxies automatically for you
        """
        proxies = self.scraper.full_scrape()
        socks5_proxies = self.filter.filter_socks5_proxies(proxies)
        return Socks5.check_socks5_proxies(socks5_proxies)
    
    def auto_socks4_check(self) -> list:
        """
        Scrapes, Structures, Filters, and Checks Activity of Socks4 Proxies automatically for you
        """
        proxies = self.scraper.full_scrape()
        socks4_proxies = self.filter.filter_socks4_proxies(proxies)
        return Socks4.check_socks4_proxies(socks4_proxies)
    
    def auto_http_check(self) -> list:
        """
        Scrapes, Structures, Filters, and Checks Activity of HTTP Proxies automatically for you
        """
        proxies = self.scraper.full_scrape()
        http_proxies = self.filter.filter_http_proxies(proxies)
        return  HTTP.check_http_proxies(http_proxies)
    
    def auto_https_check(self) -> list:
        """
        Scrapes, Structures, Filters, and Checks Activity of HTTPS Proxies automatically for you
        """
        proxies = self.scraper.full_scrape()
        https_proxies = self.filter.filter_https_proxies(proxies)
        return HTTPS.check_https_proxies(https_proxies)
