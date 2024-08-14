import os 
import Rectangle as rect
menu_option={
    1:'Thêm mới hình chữ nhật',
    2:'Hiển thị danh sách hình chữ nhật',
    3:'Tính tổng diện tích các hình chữ nhật',
    4:'Hiển thị hình chữ nhật có chu vi nhỏ nhất',
    'Others':'Thoát chương trình'
}
def print_menu():
    for key in menu_option:
        print(key,'--',menu_option[key])

dsHCN=[]
while(True):
    os.system('cls')
    print_menu()
    userChoice=" "
    try:
        userChoice = int(input('Nhập tùy chọn: '))
    except:
        print('Nhập sai định dạng, hãy nhập lại....')
        continue
    if userChoice==1:
        cr = float(input('Nhập chiều rộng: '))
        cd = float(input('Nhập chiều dài: '))
        hcn=rect.Rectangle(cr,cd)
        dsHCN.append(hcn)
        os.system('pause')
    elif userChoice==2:
        for item in dsHCN:
            item.display()
        os.system('pause')
    elif userChoice==3:
        dientich=0.0
        for item in dsHCN:
            dientich+= item.area()
        print(f'Tổng diện tích là: {dientich}')
        os.system('pause')
    elif userChoice==4:
        if dsHCN.count==0:
            print('Danh sách rỗng')
        else:
            chuvinn=dsHCN[0].perimeter()
            for item in dsHCN:
                if chuvinn > item.perimeter():
                    chuvinn = item.perimeter()
            for item in dsHCN:
                if item.perimeter()==chuvinn:
                    item.display()
        os.system('pause')
    else:
        print('Thoát chương trình BYE BYE')
        break