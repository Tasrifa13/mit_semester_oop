class Person:
    def __init__(self,name,age,address):
        self.__name = name      #variabel private
        self._age = age         #variabel protected
        self.address = address  #variabel public

    def get_name(self):
        return self.__name
    
    def set_name(self,name):
        self.__name = name

    def info(self):
        print (f"nama : {self.__name}, umur: {self._age}, alamat : {self.address}")

class Employee(Person):
    def __init__(self,name,age,address,employee_id,department):
        super().__init__(name,age,address)
        self.__employee_id = employee_id
        self._department = department
        self.status = "aktif"

    def get_employee_id(self):
        return self.__employee_id
    
    def set_employee_id(self,employee_id):
        self.__employee_id = employee_id

    def info_employee(self):
        print (f"Nama: {self.get_name()}, Umur: {self._age}, Alamat: {self.address}")
        print (f"ID Karyawan: {self.__employee_id},  Department: {self._department}, Status: {self.status}")

        #mengubah data private melalui setter kelas induk
        self.set_name("Tasrifa")
        sapi = self.get_name()
        print(f"nama setelah diubah : {sapi}")


exp1 = Employee("Ifa",25,"Jl. Lurus","abc123","IT")
exp1.info_employee()
exp1.info()


