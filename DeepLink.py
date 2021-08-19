from subprocess import Popen, PIPE, STDOUT
class TrustWallet(Popen):
    def __init__(self, **kwargs):
        self.stdout = PIPE
        self.stderr = STDOUT
        self.__url_deep_link = "https://link.trustwallet.com/"
        self.__coin_id = kwargs.get("coin_id") or 20000714
        self.__contracaddress = kwargs.get("contractaddress")

    def setCoin_id(self, x):
        self.__coin_id = x

    def setContractAddress(self, x):
        self.__coin_id = x

    def __exec(self, deeplink):
        self.args = f"am start -a android.intent.action.VIEW -d {deeplink}"
        result = self.communicate()
        self.terminate()
        return result

    def openBrowser(self, url):
        self.__exec(f"{self.__url_deep_link}open_url?coin_id={self.__coin_id}&url={url}")

    def openCoin(self):
        self.__exec(f"{self.__url_deep_link}open_coin?asset={self.__coin_id}")

    def addAsset(self):
        self.__exec(f"{self.__url_deep_link}add_asset?asset={self.__coin_id}_t{self.__contracaddress}")
