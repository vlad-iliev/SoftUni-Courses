class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = list()

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        self._transactions.append(amount)
    @property
    def balance(self):
        return sum([x for x in self._transactions]) + self.amount

    @staticmethod
    def validate_transaction(account, amount_to_add):
        if account.amount < amount_to_add:
            raise ValueError("sorry cannot go in debt!")
        account.amount -= amount_to_add
        return f"New balance: {account.amount}"

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, idx):
        return self._transactions[idx]

    def __reversed__(self):
        reversed_list = self._transactions[::-1]
        return reversed_list

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __add__(self, other):
        name = f"{self.owner}&{other.owner}"
        amount = self.amount + other.amount
        transactions = self._transactions + other._transactions
        new_acc = Account(name,amount)
        new_acc._transactions=transactions
        return new_acc


acc = Account('bob', 10)

acc2 = Account('john')

print(acc)

print(repr(acc))

acc.add_transaction(20)

acc.add_transaction(-20)

acc.add_transaction(30)

print(acc.balance)

print(len(acc))

for transaction in acc:

    print(transaction)

print(acc[1])

print(list(reversed(acc)))

acc2.add_transaction(10)

acc2.add_transaction(60)

print(acc > acc2)

print(acc >= acc2)

print(acc < acc2)

print(acc <= acc2)

print(acc == acc2)

print(acc != acc2)

acc3 = acc + acc2

print(acc3)

print(acc3._transactions)


