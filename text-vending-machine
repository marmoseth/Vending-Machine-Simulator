"""
Author Name: Aaron Mark William
Created for: University of Suffolk
"""

# ============================================
class Content:
    def __init__(self, id, state, candy, coin, value):
        self.id = id
        self.state = state
        self.candy = candy
        self.coin = coin
        self.value = value


vm1 = Content(1, 'standby_coin', 'Twin Bar', '50p', 50)
vm2 = Content(2, 'standby_choice', 'Mar Bar', '20p', 20)
vm3 = Content(3, 'vend_dispense', 'Far Bar', '10p', 10)
vm4 = Content(4, 'tx_cancel', 'Slim Bar', '5p', 5)
vm5 = Content(5, 'tx_cancel_no_balance', 'null', 'null', 'null')
vm6 = Content(6, 'tx_end', 'null', 'null', 'null')

item_avail = []
vending_state = vm1.state

print('Welcome')
# While 'vending machine' is empty, continue waiting for coin
while vending_state == vm1.state:
    print(f'Accepted coins:\n'
          f'{vm1.coin}\n'
          f'{vm2.coin}\n'
          f'{vm3.coin}\n'
          f'{vm4.coin}\n'
          f'type "cancel" anytime to cancel.\nInsert a coin:')
    try:
        balance = input()
        if balance == 'cancel':
            print('Transaction ended')
            print('******************\n')
            vending_state = vm1.state
        else:
            balance = int(balance.replace('p',''))
            if balance in (50, 20, 10, 5):
                vending_state = vm2.state
                # show choice
                while vending_state == vm2.state:
                    print(f'Balance:{balance}p\n\nPlease choose a candy bar:')
                    print(f'{vm1.candy}:{vm1.coin}') if balance >= vm1.value else None
                    print(f'{vm2.candy}:{vm2.coin}') if balance >= vm2.value else None
                    print(f'{vm3.candy}:{vm3.coin}') if balance >= vm3.value else None
                    print(f'{vm4.candy}:{vm4.coin}') if balance >= vm4.value else None
                    print('__________________')

                    choice = input().upper()
                    if choice == vm1.candy.upper():
                        balance_temp = balance - vm1.value
                        if balance_temp < 0:
                            balance_temp = balance
                            print('Invalid Input')
                            vending_state = vm2.state
                            continue
                        else:
                            balance = balance_temp
                            vending_state = vm3.state
                    elif choice == vm2.candy.upper():
                        balance_temp = balance - vm2.value
                        if balance_temp < 0:
                            balance_temp = balance
                            print('Invalid Input')
                            vending_state = vm2.state
                        else:
                            balance = balance_temp
                            vending_state = vm3.state
                    elif choice == vm3.candy.upper():
                        balance_temp = balance - vm3.value
                        if balance_temp < 0:
                            balance_temp = balance
                            print('Invalid Input')
                            vending_state = vm2.state
                        else:
                            balance = balance_temp
                            vending_state = vm3.state
                    elif choice == vm4.candy.upper():
                        balance_temp = balance - vm4.value
                        if balance_temp < 0:
                            print('Invalid Input')
                            balance_temp = balance
                            vending_state = vm2.state
                        else:
                            balance = balance_temp
                            vending_state = vm3.state
                    elif choice == 'CANCEL':
                        print('Transaction ended')
                        print('******************\n')
                        vending_state = vm1.state

                    #Quit option for debugging
                    elif choice == 'QUIT':
                        quit()

                    else:
                        vending_state = vm2.state
                        print('Invalid input')
                        continue

                    while vending_state == vm3.state:
                        print(f'\nThank you\n******************\nDispensing {choice.title()}.')
                        if balance == 0:
                            vending_state = vm5.state
                            print('Transaction ended')
                        else:
                            vending_state = vm2.state

    except:
            print('Invalid input. Please try again')

