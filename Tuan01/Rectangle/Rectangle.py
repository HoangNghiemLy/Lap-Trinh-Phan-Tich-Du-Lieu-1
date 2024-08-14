'''
Cài đặt lớp hình chữ nhật theo thiết kế
Có 2 fields (thuộc tính): width, height
Có các phương thức:
- tính diện tích
- tính chu vi
- hiển thị cơ bản
Phạm vi khai báo class Rectangle được tính từ phím tab sau class Rectangle
'''
class Rectangle:
    def __init__(self,width,length):
        self.width = width
        self.length = length
    def area(self):
        result = self.width * self.length
        return result
    def perimeter(self):
        result = (self.width + self.length) * 2
        return result
    def display(self):
        print(f'Rộng: {self.width}, dài: {self.length}, chu vi: {self.perimeter():.2f}, diện tích: {self.area():.2f}\n')