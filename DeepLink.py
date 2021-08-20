#!/usr/bin/env
from subprocess import  Popen, PIPE, STDOUT

class Terminal(Popen):
	def __init__(self, exec):
		super(Terminal, self).__init__(
			args=exec,
			shell=True,
			stderr=STDOUT,
			stdout=PIPE
		)
		
class TrustWallet(object):
    def __init__(self, **kwargs):
        self.__url_deep_link = "https://link.tw.co/"
        self.__coin_id = kwargs.get("coin_id") or 20000714
        self.__contracaddress = kwargs.get("contractaddress")
        self.exec = Terminal
        
    def getCoin_id(self):
        return self.__coin_id
    
    def getContractAddress(self, x):
        return self.__contracaddress
    
    def setCoin_id(self, x):
        self.__coin_id = x

    def setContractAddress(self, x):
        self.__coin_id = x

    def __exec(self, deeplink):
        return self.exec(f"am start -a android.intent.action.VIEW -d {deeplink} com.wallet.crypto.trustapp").communicate()
        
    def openBrowser(self, url):
        self.__exec(f"{self.__url_deep_link}open_url?coin_id={self.__coin_id}&url={url}")

    def openCoin(self):
        return self.__exec(f"{self.__url_deep_link}open_coin?asset={self.__coin_id}")

    def addAsset(self):
        self.__exec(f"{self.__url_deep_link}add_asset?asset={self.__coin_id}_t{self.__contracaddress}")

#deep = TrustWallet(contractaddress="0x5a726a26edb0df8fd55f03cc30af8a7cea81e78d")
#print(deep.openCoin())
