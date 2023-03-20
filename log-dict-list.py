Python 3.9.13 (main, Aug 25 2022, 23:51:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> box = []
>>> box.append('ปากกา')
>>> box.append('ดินสอ')
>>> box.append('ยางลบ')
>>> print(box)
['ปากกา', 'ดินสอ', 'ยางลบ']
>>> print(box[1])
ดินสอ
>>> 
>>> print(box[0])
ปากกา
>>> print(box[-2])
ดินสอ
>>> brand = {}
>>> brand = {'pen':['Lamy','pentel','Faber-castel'],'pencil':['hourse','steidler'],'eraser':['hourse']}
>>> print(brad['pen'])
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(brad['pen'])
NameError: name 'brad' is not defined
>>> print(brand['pen'])
['Lamy', 'pentel', 'Faber-castel']
>>> print(brand['pen'][0])
Lamy
>>> 
KeyboardInterrupt
>>> print(brand['pencil'][0])
hourse
>>> print(brand['eraser'][0])
hourse
>>> 