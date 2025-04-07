class Computer:

    def __init__(self,MODEL,CPU,RAM,Storage):
        self.MODEL = MODEL
        self.CPU = CPU
        self.RAM = RAM
        self.Storage = Storage
         

    def config(self):
        print("System Information")
        print(f"MODEL: {self.MODEL}")
        print(f"CPU: {self.CPU}")
        print(f"RAM: {self.RAM}")
        print(f"Storage: {self.Storage}")

comp1 = Computer('MSI','Ryzen', '8GB','512GB')
comp1.config()   
comp2 = Computer('HP','Intel', '6GB','1TB')
comp2.config() 