import numpy as np
import pandas as pd
stock_change=np.random.normal(0,1,(10,5))
print(stock_change)
pd.DataFrame(data=stock_change,index=stock)
stock=['股票{}'.format(i) for i in range(10)]
pd.date_range(start='20201001',end='20200106')
