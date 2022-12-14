
import pandas as pd

def infoUsers():
    users = pd.read_csv('../Data/users.csv')
    return users

def infoWallet():
    wallet = pd.read_csv('../Data/wallet.csv')
    return wallet

def infoDateTime():
    datetime = pd.read_csv('../Data/datetime.csv')
    return datetime

def infoMerchant():
    merchant = pd.read_csv('../Data/merchant.csv', encoding='latin1')
    return merchant

def infoTransactions():
    transactions = pd.read_csv('../Data/transactions.csv')
    return transactions