import pandas as pd

data = pd.read_excel(
  io='data/raw.xlsx',
  sheet_name='Document_TB02',
  parse_dates=[['Data', 'Hora']],
  decimal=',',
)
data.drop(
  columns='Subestação/Circuito',
  inplace=True,
)
data.rename(
  columns={
    'Data_Hora': 'timestamp',
    'P (kW)': 'power',
  },
  inplace=True,
)

start = data['timestamp'].iloc[0]
end = data['timestamp'].iloc[-1]
data['timestamp'] = \
  pd.date_range(start, end, freq='15min')

data.set_index(
  ['timestamp'],
  inplace=True,
)
data = data[~data.index.duplicated()]
data.sort_index(inplace=True)

temp = data['power'].to_list()
for count, _ in enumerate(temp):
  ratio = abs(temp[count]/temp[count-1])
  if ratio > 1.5 or temp[count] == 0:
    temp[count] = temp[count-1]
        
data['power'] = temp

data.to_csv('data/preprocessed.csv')
