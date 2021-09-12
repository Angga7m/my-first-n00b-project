data = open('data.txt', 'r')
final = open('final.txt', 'a+')


hitam = {
    'band1': '0',
    'band2': '0',
    'band3': '',
}
coklat = {
    'band1': '1',
    'band2': '1',
    'band3': '×10^1',
    'band4': '±1%',
}
merah = {
    'band1': '2',
    'band2': '2',
    'band3': '×10^2',
    'band4': '±2%',
}
jingga = {
    'band1': '3',
    'band2': '3',
    'band3': '×10^3',
}
kuning = {
    'band1': '4',
    'band2': '4',
    'band3': '×10^4',
}
hijau = {
    'band1': '5',
    'band2': '5',
    'band3': '×10^5',
    'band4': '±0.5%'
}
biru = {
    'band1': '6',
    'band2': '6',
    'band3': '×10^6',
    'band4': '±0.25%'
}
ungu = {
    'band1': '7',
    'band2': '7',
    'band3': '×10^7',
    'band4': '±0.1%'
}
abu = {
    'band1': '8',
    'band2': '8',
    'band3': '×10^8',
    'band4': '±0.05%'
}
putih = {
    'band1': '9',
    'band2': '9',
    'band3': '×10^9',
}
emas = {
    'band3': '×10^-1',
    'band4': '±5%'
}
perak = {
    'band3': '×10^-2',
    'band4': '±10%'
}
final_list = []
for things in data:
    new_list = []
    new_use = things.split('\t')
    if new_use[0] == 'Hitam':
        new_list.append(hitam['band1'])
    elif new_use[0] == 'Coklat' or new_use[0] == 'Cokelat':
        new_list.append(coklat['band1'])
    elif new_use[0] == 'Merah':
        new_list.append(merah['band1'])
    elif new_use[0] == 'Jingga':
        new_list.append(jingga['band1'])
    elif new_use[0] == 'Kuning':
        new_list.append(kuning['band1'])
    elif new_use[0] == 'Hijau':
        new_list.append(hijau['band1'])
    elif new_use[0] == 'Biru':
        new_list.append(biru['band1'])
    elif new_use[0] == 'Ungu':
        new_list.append(ungu['band1'])
    #pita pertama

    if new_use[1] == 'Hitam':
        new_list.append(hitam['band2'])
    elif new_use[1] == 'Coklat' or new_use[0] == 'Cokelat':
        new_list.append(coklat['band2'])
    elif new_use[1] == 'Merah':
        new_list.append(merah['band2'])
    elif new_use[1] == 'Jingga':
        new_list.append(jingga['band2'])
    elif new_use[1] == 'Kuning':
        new_list.append(kuning['band2'])
    elif new_use[1] == 'Hijau':
        new_list.append(hijau['band2'])
    elif new_use[1] == 'Biru':
        new_list.append(biru['band2'])
    elif new_use[1] == 'Ungu':
        new_list.append(ungu['band2'])
    #pita kedua

    if new_use[2] == 'Hitam':
        new_list.append(hitam['band2'])
    elif new_use[2] == 'Coklat' or new_use[0] == 'Cokelat':
        new_list.append(coklat['band3'])
    elif new_use[2] == 'Merah':
        new_list.append(merah['band3'])
    elif new_use[2] == 'Jingga':
        new_list.append(jingga['band3'])
    elif new_use[2] == 'Kuning':
        new_list.append(kuning['band3'])
    elif new_use[2] == 'Hijau':
        new_list.append(hijau['band3'])
    elif new_use[2] == 'Biru':
        new_list.append(biru['band3'])
    elif new_use[2] == 'Ungu':
        new_list.append(ungu['band3'])
    #pita 3
    if new_use[3] == 'Emas':
        new_list.append(emas['band4'])
    elif new_use[3] == 'Perak':
        new_list.append(perak['band4'])
    #pita 4, gak tau kenapa gak mau run

    final_list.append(new_list)


l = '\n'
i = 1
for each in final_list:
    done = ''.join(each)
    final.write(f'resistensi nomor {str(i)}: {done} {l}')
    i += 1
