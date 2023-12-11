from prettytable import PrettyTable

data = [{'nama':1,'golongan':1,'kwh':1,'harga':1,'total':1,'status':1},
        {'nama':2,'golongan':2,'kwh':2,'harga':2,'total':2,'status':2},
        {'nama':3,'golongan':3,'kwh':3,'harga':3,'total':3,'status':3},]


tabel = PrettyTable(['nama', 'golongan', 'kwh', 'harga', 'total', 'status'])
for i in data:
    nama = i.get('nama')
    golongan = i.get('golongan')
    kwh = i.get('kwh')
    harga = i.get('harga')
    total = i.get('total')
    status = i.get('status')
    tabel.add_row([nama,golongan,kwh,harga,total,status])
tabel.add_autoindex('No.')


print(tabel)