import sys

print("현재 파이썬 버전:", sys.version)

import pandas as pd
import numpy as np
import time
import pyupbit



### 전체 코인 목록 
print(pyupbit.get_tickers())
### 원화/달라/btc 매장별로 가능한 코인 목록
print(pyupbit.get_tickers(fiat="KRW"))

