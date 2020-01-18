class CloudTech:
  #creating a cloud Cloud
  def __init__(self, name, age, cert):
    #initialize name, age, cert
    self.name = name
    self.age = age
    self.cert = cert

  def show_cert(self):
    #simulate cloudtech showing off his cert.
    print(f'I {self.name} has a {self.cert} certification.')

  def shout(self):
    #shout tech name
    print(f'My name is {self.name}, my age is {self.age} and i am proud of my {self.cert}.')

tech1 = CloudTech('Terrell', 36, 'AWS')
tech2 = CloudTech('Eric', 33, 'Security+')
print(f'{tech1.name} is my name.')
tech1.show_cert()
tech2.shout()