import random

class CasinoGames(object):
    # initiate a list for transactions
    def __init__(self):
        self.transactions = []

    # get balance which is sum of all transactions
    def getBalance(self):
        self.balance = sum(self.transactions)
        return self.balance

    # append deposit amount to transactions
    def deposit(self, amount):
        self.transactions.append(amount)

    # return list of all transactions
    def transactionHistory(self):
        return self.transactions

class Lottery(CasinoGames):

    def __init__(self):
        super(Lottery, self).__init__()
        # available ticket prices
        self.options = [5, 10, 15]
        # list of tickets
        self.easyTicks = []
        self.medTicks = []
        self.hardTicks = []
        # list for winning tickets
        self.winTicks = []

    # remove ticket from current list and place with winning tickets
    def give(self, ticket, list):
        self.winTicks.append(ticket)
        list.remove(ticket)

    #  purchase tickets
    def buyTickets(self, price, amount):
        self.price = price
        self.amount = amount
        # total of current purchase
        cost = self.price * self.amount
        # only run if player has enough funds to make the purchase
        if cost <= self.getBalance():
            # add cost to transaction history
            self.transactions.append(-cost)
            # add amount of tickets to total tickets list
            for i in range(self.amount):
                ticket = [random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10)]
                # Purchase an easy tickets
                if self.price == self.options[0]:
                    self.easyTicks.append(ticket)
                    type = self.easyTicks
                # purchase a med ticket
                elif self.price == self.options[1]:
                    self.medTicks.append(ticket)
                    type = self.medTicks
                # purchase a hard ticket
                elif self.price == self.options[2]:
                    self.hardTicks.append(ticket)
                    type = self.hardTicks
            # return a list of tickets purchased
            return type
        else:
            return 'Not enough funds.'

    # view owned TICKETS
    def viewTickets(self):
        return self.easyTicks, self.medTicks, self.hardTicks, self.winTicks

    # winning tickets
    # def createWinner(self):

    def compareToWinner(self):
        # print(self.easyTicks)
        # print(self.winTicks)
        self.winner = [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]

        for ticket in self.easyTicks:
            if ticket[0] == self.winner[0]:
                self.give(ticket, self.easyTicks)
            # and ticket[1] == self.winner[1] and ticket[2] == self.winner[2] and ticket[3] == self.winner[3] and ticket[4] == self.winner[4]:
                prize = self.options[0] * 100
                self.transactions.append(prize)
            # else:
            #     prize = 0

        for ticket in self.medTicks:
            if ticket[0] == self.winner[0]:
                self.give(ticket, self.medTicks)
            # and ticket[1] == self.winner[1] and ticket[2] == self.winner[2] and ticket[3] == self.winner[3] and ticket[4] == self.winner[4]:
                prize = self.options[1] * 100
                self.transactions.append(prize)
            # else:
            #     prize = 0

        for ticket in self.hardTicks:
            if ticket[0] == self.winner[0]:
                self.give(ticket, self.hardTicks)
            # and ticket[1] == self.winner[1] and ticket[2] == self.winner[2] and ticket[3] == self.winner[3] and ticket[4] == self.winner[4]:
                prize = self.options[2] * 100
                self.transactions.append(prize)
            # else:
            #     prize = 0
        print(self.easyTicks)
        print(self.medTicks)
        print(self.hardTicks)
        print(self.winner)
        print(self.winTicks)
