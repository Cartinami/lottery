import sys
sys.path.insert(1, '/Users/conno/Documents/Programming/modules')
import games
import classes2


lotto = classes2.Lottery()


choice = None
while choice != 0:
    choice = int(games.askNum('What would you like to do?'))

    # make a deposit
    if choice == 1:
        # get deposit amount and add it to transactions
        cash = games.askNum('How much would you like to deposit?')
        lotto.deposit(int(cash))
        print('\r')
        print('Deposited:')
        print('$', cash)
        print('New Balance:')
        print('$', lotto.getBalance())


    elif choice == 2:
        print('\r')
        print('Transaction History:')
        for i in lotto.transactionHistory():
            print('$', i)
        print('Total Balance:')
        print('$', lotto.getBalance())
        print('\r')

    # buy tickets
    elif choice == 3:
        # get price of tickets, move on once its equal to one of the options specified
        price = None
        while price not in lotto.options:
            price = games.askNum('Would you like $5, $10, or $15 tickets?')
            if price not in lotto.options:
                print('Please try again.')
        # get amount of tickets desired
        amount = games.askNum('How many would you like?')
        # put buyTickets() return value into a variable
        buy = lotto.buyTickets(price, amount)
        # if variable is a list, print out returned tickets
        if type(buy) == list:
            print('\r')
            print('Tickets:')
            # print each ticket in tickets list
            for i in buy:
                print(i)
            print('\r')
            print('Balance:')
            print('$', lotto.getBalance())
        # otherwise print returned 'not enough funds'
        else:
            print(buy)
        print('\r')

    # view tickets
    elif choice == 4:
        tickets = lotto.viewTickets()
        print('\r')
        print('Tickets:')

        print('\r')
        print('easy')
        if len(tickets[0]) > 0:
            for i in tickets[0]:
                print(i)
        else:
            print('<No Tickets>')

        print('\r')
        print('med')
        if len(tickets[1]) > 0:
            for i in tickets[1]:
                print(i)
        else:
            print('<No Tickets>')

        print('\r')
        print('hard')
        if len(tickets[2]) > 0:
            for i in tickets[2]:
                print(i)
        else:
            print('<No Tickets>')
        print('\r')

        print('\r')
        print('Win')
        if len(tickets[3]) > 0:
            for i in tickets[3]:
                print(i)
        else:
            print('<No Tickets>')
        print('\r')

    elif choice == 5:
        print(lotto.compareToWinner())
