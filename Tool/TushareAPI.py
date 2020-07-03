import tushare as ts


class TushareAPI:
    def __init__(self):
        self.pro = ts.pro_api(token='5c0e27dddb8a9c16aa6976b5437950f922037ede7b0a9a3b1a163642')
