from seller import Seller #nuevo
from ownable import Ownable #nuevo
class Cart(Ownable):
    from item_manager import show_items
    #from ownable import set_owner #nuevo
    from wallet import Wallet #nuevo
    
    def __init__(self, owner):
        self.set_owner(owner)
        self.items = []

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)

    def check_out(self, seller):
        #seller = Seller("tienda DIC")#
        #print("el valor de self.owner.wallet es: ",self.owner.wallet.balance)
        #print("el valor de self.total_amount() es: ",self.total_amount())
        #print("el valor de seller.wallet.balance es: ",seller.wallet.balance)
        
        if self.owner.wallet.balance > self.total_amount():
            #pass    # Eliminar pase al codificar el método check_out.
            # Requisitos
            #: el monto de la compra de todos los artículos en el carrito (Cart#items) se transfiere de la billetera del propietario del carrito a la billetera del propietario del artículo.
            #: la propiedad de todos los artículos del carrito (Cart#items) se transfiere al propietario del carrito.
            # - El contenido del carrito (Cart#items) está vacío.
            # Consejo
            # - Cartera del propietario del carrito ==> self.owner.wallet
            # - Cartera del propietario del artículo ==> item.owner.wallet
            # - El dinero se transferirá ==> Esa cantidad se retirará de la billetera de (?) y se depositará en la billetera de (?).
            # - La propiedad del artículo se transfiere al propietario del carrito ==> Reescribir propietario (item.owner =?)
            #pass
            
            self.owner.wallet.withdraw(self.total_amount()) #nuevo: se retira
            cantidad = self.total_amount()
            seller.wallet.deposit(cantidad)                 #nuevo: se deposita
            for item in self.items:         
                item.owner = self.owner           #se utiliza consejo de linea 40 
            self.items.clear()                    #se vacia canasta

    '''def deposit(self, amount):
        self.balance += int(amount)

    def withdraw(self, amount):
        if not self.balance >= amount:
            return
        self.balance -= int(amount)
        return amount'''