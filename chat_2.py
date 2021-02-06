#寫入檔案
def write_back(file_name, products):
    with open(file_name, 'w', encoding= 'utf-8') as f:
        for p in products:
            f.write(p + '\n')
#讀取檔案
def read_file(file_name):
    products = []
    with open(file_name, 'r', encoding= 'utf-8-sig') as f:
        for line in f:
            products.append(line.strip())
        #print(products)
    return products
def modification(products):
    name = ''
    time = ''
    word_count_1 = 0
    word_count_2 = 0
    picture_count_1 = 0
    picture_count_2 = 0
    sticker_count_1 = 0
    sticker_count_2 = 0
    for line in products:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == '世煌simon':
            if s[2] == '圖片':
                picture_count_1 += 1
            elif s[2] == '貼圖':
                sticker_count_1 += 1
            else:
                for i in s[2:]:
                    word_count_1 += len(i)
        if name == 'John':
            if s[3] == '圖片':
                picture_count_2 += 1
            elif s[3] == '貼圖':
                sticker_count_2 += 1
            else:
                for i in s[3:]:
                    word_count_2 += len(i)
    print('Simon的貼圖數：',sticker_count_1)
    print('Simon的圖片數：',picture_count_1)
    print('Simon的總字數：',word_count_1)
    print('John的貼圖數：',sticker_count_2 )
    print('John的圖片數：',picture_count_2)
    print('John的總字數：',word_count_2)
def main(input_file, output_file):
    products = []
    if os.path.isfile(input_file):
        products = read_file(input_file)
    else:
        print('file does not exist')
    products = modification(products)
 #   write_back(output_file, products)

import os
main('simon.txt','simon_output.txt')