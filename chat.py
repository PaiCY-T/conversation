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
    output = []
    name = None
    for line in products:
        if 'Allson' in line: 
            if '傳送' in line:
                name = 'Allson'
                continue   
            else:
                continue         
        elif '你' and '傳送' in line:
            name = '你'
            continue  
        elif name:   
            output.append(name + ': ' + line)
    return output

def main(input_file, output_file):
    products = []
    if os.path.isfile(input_file):
        products = read_file(input_file)
    else:
        print('file does not exist')
    products = modification(products)
    write_back(output_file, products)

import os
main('input.txt','output.txt')