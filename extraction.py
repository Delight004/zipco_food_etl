import pandas as pd
def run_extraction():
    try:
        data = pd.read_csv(r'rawdata/zipco_transaction.csv')
        print('Data Extracted Successfully')
    except Exception as e:
        print(f'An error occured: {e}')
        