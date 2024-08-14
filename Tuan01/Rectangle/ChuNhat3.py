import Rectangle as rect
import os
fr = open('input.db',mode='r',encoding='utf-8')
listRectangle=[]
for line in fr:
    stripLine = line.strip('\n')
    ds=stripLine.split(',')
    cr = float(ds[0])
    cd = float(ds[1])
    hcn=rect.Rectangle(cr,cd)
    listRectangle.append(hcn)
fr.close()
fw=open('output.db',mode='w',encoding='utf-8')
for item in listRectangle:
    fw.write(f'{item.width}-{item.length}-{item.perimeter()}-{item.area()}\n')
fw.close()

menu={
    1:'1-Đọc dữ liệu từ file input.db',
    2:'2-Thêm mới hình chữ nhật',
    3:'3-Hiển thị danh sách hình chữ nhật',
    4:'4-Lưu danh sách hình chữ nhật xuống file demo4output.db',
    'Others':'Thoát'
}
def print_menu():
    for key in menu.keys():
        print(key,'--',menu[key])
while(True):
    os.system('cls')
    print_menu()
    chon=""
    try:
        chon = int(input('Nhập tùy chọn: '))
    except:
        print('Nhập sai định dạng, hãy nhập lại...')
        continue
    if chon==1:
        fr=open('input.db',mode='r',encoding='utf-8')
        dsHCN=[]
        for line in fr:
            stripLine = line.strip('\n')
            ds=stripLine.split(',')
            cr=float(ds[0])
            cd=float(ds[1])
            hcn=rect.Rectangle(cr,cd)
            dsHCN.append(hcn)
        fr.close()
        os.system('pause')
    elif chon==2:
        cr=float(input('Nhập chiều rộng: '))
        cd=float(input('Nhập chiều dài: '))
        hcn=rect.Rectangle(cr,cd)
        dsHCN.append(hcn)
        os.system('pause')
    elif chon==3:
        if dsHCN.count==0:
            print('Danh sách rỗng')
        else:
            for item in dsHCN:
                item.display()
        os.system('pause')
    elif chon==4:
        fw=open('outputdemo4.db',mode='w',encoding='utf-8')
        for item in dsHCN:
            fw.write(f'{item.width}-{item.length}-{item.perimeter()}-{item.area()}\n')
        fw.close()
        os.system('pause')
    else:
        print('Kết thúc chương trình')
        break
        