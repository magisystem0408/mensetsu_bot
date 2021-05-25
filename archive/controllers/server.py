from .data import Data

def search():
    print('')
    for i in range(10):
        q =input('入力せよ：')
        print(Data.data.get(q))
