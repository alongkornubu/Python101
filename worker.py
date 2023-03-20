class KhanomKrok:
    # Attribute
    StoreName = 'ขนมครกปากซอย'
    
    # Constructor
    def __init__(self,candy='ขนมครก'):
        # print('ให้แสดงข้อความนี้ เมื่อมีการสร้าง Instance')
        self.candy = candy
    # Method
    def hello(self):
        print('สวัสดีตอนเช้า ยินดีต้อนรับลูกค้าทุกท่าน')
    def kanom(self):
        print(f'ทางร้านเรามีสินค้าชื่อว่า {self.candy}')
    def thank(self):
        print('ขอบคุณทุกท่าน')
    
class Store(KhanomKrok):
    def __init__(self,name, candy,price):
        super().__init__(candy)
        self.name = name
        self.candy = candy
        self.price = price
    
    def checkPrice(self):
        if self.price >= 40:
            print(f'ได้ {self.candy} 4 กล่อง')
        elif self.price >= 30:
            print(f'ได้ {self.candy} 3 กล่อง')
        else:    
            print(f'ไม่ได้ {self.candy}')    
# Instance
customer = Store('มาณี ลมโชย', 'ขนมครก' , 45)
customer.hello()
customer.kanom()
customer.thank()
print(f'ชื่อร้าน: {customer.StoreName}')
print(f'ชื่อลูกค้า: {customer.name}')
print(f'ชื่อขนม: {customer.candy}')
print(f'ราคา: {customer.price}')
customer.checkPrice()


