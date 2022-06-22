# Algorand Wallet Vanity Generation

Generate wallets that start with your desired phrase for the Algorand chain.

To run, make sure you have Python 3 and pip available from your command line, then:

```
    pip install -r requirements.txt
    python3 main.py COOL
```

Above command will start generating wallets that start with the phrase "COOL".
Change the phrase as you see fit, but keep in mind that only letters of the English alphabet and numbers 2345679 can ever be found in an Algorand wallet address.

You can run the program several times on the same computer, but each run will start up to 16 generation threads.

Generated wallets are saved to *accounts.csv* in your run directory with the format:

```
    ADDRESS;"your mnemonic wallet key"
```
