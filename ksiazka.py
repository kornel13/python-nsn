
class person(object):
  def __init__(self,name,surname,phone,mail,street,number):
    self.name = name
    self.surname = surname
    self.phone = phone
    self.mail = mail
    self.street = street
    self.number = number

  def name_surn(self):
    return self.name+' '+self.surname

  def contact(self):
    return 'phone: '+str(self.phone)+'mail: '+self.mail

  def adress(self):
    return 'street: '+self.street+'nr '+str(self.number)

  def __str__(self):
    return self.name_surn() + self.contact() + self.adress()

class adress(object):
  def __init__(self,street):
    self.people = []
    self.street = street

  def add_person(self,_person):
    self.people.append(_person);

  def show(self):
    print("street: "+self.street)
    for i in self.people:
      print('nr '+str(i.number)+' person: '+i.name+' '+i.surname)
 
class book(object):
  def __init__(self):
    self.list_person = []
    self.list_adress = []
  
  def get_adress_index(self,street):
    for i in range(len(self.list_adress)):
      if street == self.list_adress[i].street:
        return i
    return -1
      
	
  def add_person(self,name,surname,phone,mail,street,number):
    _person = person(name,surname,phone,mail,street,number)
    self.list_person.append(_person)
    index = self.get_adress_index(street)
    if index == -1:
      _adress = adress(street)
      _adress.add_person(_person)
      self.list_adress.append(_adress)
    else:
      self.list_adress[index].add_person(_person)

  def show_people(self):
    if not len(self.list_person):
      print('No people in adressbook')
    else:
      for i in self.list_person:
        print(i)

  def show_adresses(self):
    if not len(self.list_adress):
      print('No people in adressbook')
    else:
      for i in self.list_adress:
        i.show()

  def find_adress(self):
    print('write a street')
    _adress = input()
    index = get_adress_index(_adress)
    if index != -1:
      self.list_adress[index].show()
    else:
      print('no such a adress');

  def find_person(self):
    print('write a surname')
    surname = input()
    is_found = False;
    for i in self.list_person:
      if surname == i.surname:
        print(i)
        is_Found = True
    if not is_Found:
      print('no such a person');


b = book()
b.add_person('ala','kwak',12345,'ala@koko.com','bialostocka',3)
b.add_person('ola','kowalska',2254536,'ququ@cos.pl','workowa',5)   
b.add_person('kasia','workowiec',36346,'worek@qpa.com','bialostocka',4)    
b.add_person('marek','szynszyla',90809,'zwierz@qq.pl','mala',10)    
b.add_person('abelard','pyton',58758,'hej@ho.com','workowa',3)

b.show_people()
b.show_adresses()
    
 
  
    

    
