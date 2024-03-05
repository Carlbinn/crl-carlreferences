class Resto:
    """An attempt to create a resto with resto description and cuisine type"""
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.order_num = 0

    def open(self):
        """An attempt to open the resto"""
        print(f"{self.name} is now open! Come in! We are serving {self.cuisine} cuisine!")

    def close(self):
        """An attempt to close the resto"""
        print(f"{self.name} is now closed! Come back tomorrow.")

    def current_service(self):
        """An attemp to print current customer being served"""
        print(f"Currently serving customer number {self.order_num}")

    def increment_service(self, cust_num):
        """An attempt to increment the service number"""
        if cust_num > 0:
            self.order_num += cust_num
        else:
            print(f"You can't rollback the service number served.")

    def update_service(self, cust_override):
        """An attemp to manually override the service number"""
        if cust_override >= self.order_num:
            self.order_num = cust_override
        else:
            print(f"You can't rollback the service number served.")

my_resto = Resto("Italliani's", "Italian")
my_resto.open()
my_resto.close()
my_resto.current_service()
my_resto.increment_service(2)
my_resto.current_service()
my_resto.increment_service(-2)
my_resto.current_service()
my_resto.update_service(20)
my_resto.current_service()
my_resto.update_service(3)
my_resto.current_service()
my_resto.increment_service(3)
my_resto.current_service()