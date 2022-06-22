#!/usr/bin/env python3
"""
Generate Vanity Algorand addresses using multithreading
"""

__author__ = "Grzegorz Raczek, Vestige"
__version__ = "1.0.0"
__license__ = "MIT"

from algosdk import account
from algosdk.mnemonic import from_private_key
from threading import Thread
import sys

THREADS = 16
VALID_CHARACTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ2345679'


def main():
    if len(sys.argv) > 1:
        phrase = str(sys.argv[1]).upper()
        for char in phrase:
            if char not in VALID_CHARACTERS:
                print("ERROR: Generation phrase cannot contain character: {}".format(char))
                exit(1)
        if len(phrase) > 6:
            print("Warning: wallet generation for long phrases can take months to complete. It's best to stick to phrases with length up to 6 characters.")
        print('Account generation for phrase {} started.'.format(phrase))

        def get_accounts():
            while True:
                private_key, address = account.generate_account()
                if address.startswith(phrase):
                    print('Found: {}'.format(address))
                    with open('accounts.csv', 'a') as accounts:
                        accounts.write('{};"{}"\n'.format(address, from_private_key(private_key)))

        threads = [Thread(target=get_accounts) for _ in range(0, THREADS)]

        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
    else:
        print('ERROR: No generation phrase provided.')
        exit(1)


if __name__ == "__main__":
    main()
