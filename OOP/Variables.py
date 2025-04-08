class Computer:

    device = "Laptop"
    #device:class variable

    def __init__(self,processor,HHD):
        self.processor = processor
        self.HHD = HHD
        # processor and HHD are Instance variable


comp1 = Computer('Intel i5','512GB')
comp2 = Computer('Ryzen i5','1TB')

# print(comp1.device) #Laptop
# print(comp2.device)#laptop

# comp1.device = "Desktop"
# print(comp1.device) #Desktop
  
Computer.device = "Desktop"  
print(comp1.device) #Laptop
print(comp2.device)#laptop      