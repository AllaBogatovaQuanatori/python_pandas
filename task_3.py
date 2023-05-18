import pandas as pd
import lxml as lx

if __name__ == '__main__':
    url = 'https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html'

    tables = pd.read_html(url)
    print(tables[0])
