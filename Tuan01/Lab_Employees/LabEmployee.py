import matplotlib.pyplot as plt
import Employee as emp
import os 
menu_option={
    1:'Load data from file',
    2:'Add new employee',
    3:'Display list of employees',
    4:'Show employee details',
    5:'Update employee information',
    6:'Delete employee',
    7:'Increase salary of employee',
    8:'Decrease salary of employee',
    9:'Show total employee a month',
    10:'Show total salary a month',
    11:'Show average of salary a month',
    12:'Show average of age',
    13:'Show maximum age',
    14:'Sort list of employee according to salary by ascending',
    15:'Draw salary according to age',
    16:'Draw average of salary chart by age group',
    17:'Draw percentage of salary by age group',
    18:'Draw perentage of total employee by age group',
    19:'Store data to file',
    'Others':'Exit program'
}
def print_menu():
    for key in menu_option.keys():
        print(key,'--',menu_option[key])
dsNhanVien = []
while(True):
    os.system('cls')
    print_menu()
    userChoice=""
    try:
        userChoice = int(input('Input choice: '))
    except:
        print('Invalid input, try again....')
        continue
    if userChoice == 1:
        fr = open('dbemp_input.db',mode='r',encoding='utf-8')
        for line in fr:
            stripLine = line.strip('\n')
            ds=stripLine.split(',')
            maso=ds[0]
            ten=ds[1]
            tuoi=int(ds[2])
            luong=float(ds[3])
            nv = emp.Employee(maso,ten,tuoi,luong)
            dsNhanVien.append(nv)
        fr.close()
        os.system('pause')
    elif userChoice == 2:
        maso = input('Input code: ')
        ten = input('Input name: ')
        tuoi = int(input('Input age: '))
        luong = float(input('Input salary: '))
        nv = emp.Employee(maso,ten,tuoi,luong)
        dsNhanVien.append(nv)
        os.system('pause')
    elif userChoice == 3:
        if dsNhanVien.count==0:
            print('Empty list')
        else:
            for item in dsNhanVien:
                item.display()
        os.system('pause')
    elif userChoice == 4:
        if dsNhanVien.count==0:
            print('Empty list')
        else:
            ma=input('Input code: ')
            for item in dsNhanVien:
                if(item.code == ma):
                    item.display()
        os.system('pause')
    elif userChoice == 5:
        if dsNhanVien.count==0:
            print('Empty list')
        else:
            ma=input('Input code for update: ')
            for item in dsNhanVien:
                if(item.code == ma):
                    item.display()
                    menu={
                        1:'Update name',
                        2:'Update age',
                        3:'Update salary',
                        'Others':'Exit'
                    }
                    def xuat_menu():
                        for key in menu.keys():
                            print(key,'--',menu[key])
                    while(True):
                        xuat_menu()
                        traloi=""
                        try:
                            traloi=int(input('Input choice: '))
                        except:
                            print('Invalid input, try again....')
                            continue
                        if traloi==1:
                            ten=input('Input name: ')
                            item.name = ten
                            item.display()
                        elif traloi==2:
                            tuoi=int(input('Input age: '))
                            item.age = tuoi
                            item.display()
                        elif traloi==3:
                            luong=float(input('Input salary: '))
                            item.salary = luong
                            item.display()
                        else:
                            print('Ket thuc chinh sua')
                            break
        os.system('pause')
    elif userChoice == 6:
        if dsNhanVien.count==0:
            print('Empty list')
        else:
            ma=input('Input code for delete: ')
            for item in dsNhanVien:
                if(item.code == ma):
                    item.display()
                    tl = input('Do you want to delete this employee? (Y/N): ')
                    if tl=='Y':
                        dsNhanVien.remove(item)
        for item in dsNhanVien:
            item.display()
        os.system('pause')
    elif userChoice == 7:
        if dsNhanVien.count==0:
            print('Empty list')
        else:
            ma=input('Input code for update: ')
            for item in dsNhanVien:
                if(item.code == ma):
                    item.display()
                    luongtang=float(input('Input increase salary: '))
                    item.salary += luongtang
                    item.display()
        os.system('pause')
    elif userChoice == 8:
        if dsNhanVien.count==0:
            print('Empty list')
        else:
            ma=input('Input code for update: ')
            for item in dsNhanVien:
                if(item.code == ma):
                    item.display()
                    luonggiam=float(input('Input decrease salary: '))
                    item.salary -= luonggiam
                    item.display()
        os.system('pause')
    elif userChoice == 9:
        if dsNhanVien.count==0:
            print('Empty list') 
        else:
            tongsonv= 0
            for item in dsNhanVien:
                tongsonv += 1
                item.display()
            print('Total employee = ',tongsonv)
        os.system('pause')
    elif userChoice == 10:
        sumSalary = 0.0
        for item in dsNhanVien:
            sumSalary += item.salary
        print(f'Total salary: {sumSalary}')
        os.system('pause')
    elif userChoice == 11:
        if dsNhanVien.count==0:
            print('Empty list')
        else:
            tongsnv = 0
            tongluong = 0.0
            for item in dsNhanVien:
                tongsnv += 1
                tongluong += item.salary
                item.display()
            luongtb = tongluong / tongsnv
            print(f'Average salary employee: {luongtb}')
        os.system('pause')
    elif userChoice == 12:
        if dsNhanVien==0:
            print('Empty list')
        else:
            tongtuoi = 0
            tongsnv = 0
            for item in dsNhanVien:
                tongsnv += 1
                tongtuoi += item.age
                item.display()
            tuoitb = tongtuoi / tongsnv
            print(f'Average age employee: {tuoitb}')
        os.system('pause')
    elif userChoice == 13:
        if dsNhanVien.count==0:
            print('Empty list')
        else:
            for item in dsNhanVien:
                tuoimax = item.age
                break
            for item in dsNhanVien:
                if(item.age > tuoimax):
                    tuoimax = item.age
            print('Tuoi lon nhat = ',tuoimax)
        os.system('pause')
    elif userChoice == 14:
        if dsNhanVien.count==0:
            print('Empty list')
        else:
            tongsnv = 0
            for item in dsNhanVien:
                tongsnv += 1
                item.display()
            print("Tong so nhan vien = ",tongsnv)
        os.system('pause')
    elif userChoice == 15:
        arrTuoi = []
        arrLuong = []
        for item in dsNhanVien:
            arrTuoi.append(item.age)
            arrLuong.append(item.salary)
        plt.figure(figsize=(15,5))
        plt.title("Age and salary chart")
        plt.xlabel("Ox: age")
        plt.ylabel("Oy: salary")
        plt.plot(arrTuoi,arrLuong,"go")
        plt.show()
        os.system('pause')
    elif userChoice == 16:
        arrTuoi = []
        arrLuong = []
        for item in dsNhanVien:
            arrTuoi.append(item.age)
            arrLuong.append(item.salary)
        plt.figure(figsize=(15,5))
        plt.title("Age and salary chart")
        plt.xlabel("Ox: age")
        plt.ylabel("Oy: salary")
        plt.plot(arrTuoi, arrLuong, "go")
        plt.show()
        os.system('pause')
    elif userChoice == 17:
        arrTuoi  = []
        arrLuong = []
        for item in dsNhanVien:
            arrTuoi.append(item.age)
            arrLuong.append(item.salary)
        plt.figure(figsize=(15,5))
        plt.title("Age and salary chart")
        plt.xlabel("Ox: age")
        plt.ylabel("Oy: salary")
        plt.plot(arrTuoi,arrLuong,"go")
        plt.show()
        os.system('pause')
    elif userChoice==18:
        arrTuoi = []
        arrLuong =[]
        for item in dsNhanVien:
            arrTuoi.append(item.age)
            arrLuong.append(item.salary)
        plt.figure(figsize=(15,5))
        plt.title("Age and salary chart")
        plt.xlabel("Ox: age")
        plt.ylabel("Oy: salary")
        plt.plot(arrTuoi,arrLuong,"go")
        plt.show()
        os.system('pause')
    elif userChoice == 19:
        arrTuoi = []
        arrLuong= []
        for item in dsNhanVien:
            arrTuoi.append(item.age)
            arrLuong.append(item.salary)
        plt.figure(figsize=(15,5))
        plt.title("Age and salary chart")
        plt.xlabel("Ox: age")
        plt.ylabel("Oy: salary")
        plt.plot(arrTuoi,arrLuong,"go")
        plt.show()
        os.system('pause')
    else:
        print('BYE BYE')
        break
    
        
        
                    