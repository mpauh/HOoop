import atm_machine
mi_cuenta1= atm_machine.Account(3,'Paula',50000)
mi_cuenta2= atm_machine.Account(4,'Paula',0)
print ("En la cuenta uno hay $",mi_cuenta1.check_balance())
print ("En la cuenta dos hay $",mi_cuenta2.check_balance())
"""Transfiero 10000 de la cuenta 1 a la cuenta 2 y uso todos los metodos de la clase"""
mi_cuenta1.transfer_money(10000,mi_cuenta2)
print ("Luego de transferir 10000 quedan en la cuenta1 $",mi_cuenta1.balance)
print ("El balance en la cuenta 2 es $",mi_cuenta2.balance)
