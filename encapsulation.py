class Bank:
    def __init__(self,holder_name,initial_deposit) -> None:
        self.holder_name=holder_name
        self.__balance = initial_deposit

rafsun = Bank('Choto bro',1000) 

print(rafsun.holder_name)
# rafsun.balance= 0
print(rafsun.__balance)