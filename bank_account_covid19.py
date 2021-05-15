# software for administrating bank accounts
#
# annotation ! it will recognize system date,
# and apply some functions like daily limit to withdraw,
# or non-refundable loan to company-type accounts
# if system date set before 1.04.2020
#
# for every user automatically create separate file
# and if account will be closed, delete the file from HDD
import pickle
import datetime

DEPO: int = 1
WITH = 2
OP = 3
CLO = 4
SAVE = 5
LOAD = 6
EXIT: int = 7
name = 0
o = 0
bankaccount = {'name': '0',
               'balance': 0,
               'nationality': '0',
               'company': '0',
               'd2': datetime.date(2020, 4, 1),
               'today': float(0),
               'restriction': '0',
               'last_access': '0',
               'last_access_today': 0
               }


def main():
    choice = 0
    while choice != EXIT:
        choice = get_menu_choice()
        if choice == DEPO:
            deposit(bankaccount)
        elif choice == WITH:
            withdraw(bankaccount)
        elif choice == OP:
            opena(bankaccount)
        elif choice == CLO:
            closea(bankaccount)
        elif choice == SAVE:
            save(bankaccount)
        elif choice == LOAD:
            loada()
        elif choice == EXIT:
            end()


def get_menu_choice():
    print('Welcome to: ')
    print("********************************************************")
    print('***                   super-duper                    ***')
    print('***    bank administration software v. eternity      ***')
    print('***            made by: Sebastian Stasik             ***')
    print('********************************************************')
    print('')
    print('')
    from datetime import date
    today = date.today()
    print('////////////////////////////////////////////////////////')
    print("////             Today's date:", today, '          ////')
    print('////////////////////////////////////////////////////////')
    import time
    a = 0
    while a < 2:
        a = a + 1
        print("...")
        time.sleep(1)
        if a == 2:
            break
    print('annotation: every time you deposit or withdraw money')
    print('program will automatically save changes in file!')
    print('')
    print('')
    print('What you what to do?')
    print('Annotation: Chose number only!')
    print('')
    print('1        Deposit money?                      1')
    print('2        Withdraw money?                     2')
    print('3        Open a new account?                 3')
    print('4        Close existing account?             4')
    print('5        Save customers data to a file?      5')
    print('6        Load customers from a file?         6')
    print('7        Close program?                      7')

    try:
        # Get the user's choice.
        print('')
        print('Enter your choice: ')
        choice = int(input('-->>'))
        # Validate the choice.
        while choice < DEPO or choice > EXIT:
            choice = input('Please chose only NUMBERS ONLY from 1 to 7!'
                           '')
        else:
            return choice
        # return the user's choice.

    except ValueError:
        print('You have entered letters or symbols, dont you?')
        print('')
        print('Please chose only NUMBERS ONLY from 1 to 7!')
        print('')
        main()


def quitting():
    print('')
    print('Returning to main menu')
    import time
    b = 0
    while b < 2:
        b = b + 1
        print("...")
        time.sleep(1)  # Delay for 1 second.
    else:
        main()


def withdraw(bankaccount):
    # prompt if user want to withdraw cash
    print('enter ONLY! :y or :n')
    print('')
    print('Chose if you sure to withdraw money: ')
    again = input('-->>')
    while again == 'y' or again == 'n':
        # Get data from the user.
        if again.lower() == 'y':
            print('')
            print('enter name of customer:')
            filename = input('-->>')
            try:
                pickle_in = open(filename, "rb")
                bankaccount = pickle.load(pickle_in)
                pickle_in.close()
                questions(bankaccount)
                print('')
                print('file loaded successfully')
            except (KeyError, EOFError, FileNotFoundError):
                print('user not found')
                quitting()

            covid19(bankaccount)

            restriction = bankaccount['restriction']
            while restriction == 'yes':
                try:
                    cash = input('How much would you like to withdraw? ')
                    bal = bankaccount['balance']
                    while float(cash) > float(bal):
                        print('insufficient money')
                        cash = float(input('Chose smaller amount: '))
                        print('')
                        print('')
                    else:
                        print('I will withdraw that from your account.')
                        # Display the balance.
                        print('Your account balance is: RUB ',
                              format(float(bal) - float(cash), ',.2f'),
                              sep='')
                        endmath = float(bal) - float(cash)
                        format(endmath, ',.2f')
                        bankaccount['balance'] = endmath
                        print('')
                        print('')
                        save(bankaccount)
                except ValueError:
                    print('you chosen wrong')
                    print('returning to the beginning of operation')
                    import time
                    a = 0
                    while a < 2:
                        a = a + 1
                        print("...")
                        time.sleep(1)  # Delay for 1 second.
                    else:
                        withdraw(bankaccount)

            else:
                try:
                    print('')
                    print('How much money will you like do withdraw: ')
                    cash = float(input('-->>'))
                    print('')
                    nationalitya = bankaccount['nationality']
                    while nationalitya == 'pl':
                        balw = float(bankaccount['last_access_today'])
                        while balw > cash:
                            while cash < 1000:
                                bal = bankaccount['balance']
                                while float(cash) > float(bal):
                                    print('insufficient money')
                                    cash = float(input('Chose smaller amount: '))
                                    print('')
                                    print('')
                                else:
                                    from datetime import date
                                    todays = date.today()
                                    bankaccount['last_access'] = todays
                                    bankaccount['today'] = cash
                                    print('I will withdraw that from your account.')
                                    # Display the balance.
                                    print('Your account balance is: RUB ',
                                          format(float(bal) - float(cash), ',.2f'),
                                          sep='')
                                    print('')
                                    print('')
                                    endmath = float(bal) - float(cash)
                                    format(endmath, ',.2f')
                                    bankaccount['balance'] = endmath
                                    save(bankaccount)
                            else:
                                print('')
                                print("you can only withdraw ", balw, 'RUB more today...')
                                print('')
                                quitting()
                        else:
                            covid19(bankaccount)
                            quitting()
                    else:
                        covid19(bankaccount)
                        bal = bankaccount['balance']
                        while float(cash) > float(bal):
                            print('insufficient money')
                            try:
                                cash = float(input('Chose smaller amount: '))
                                print('')
                                print('')
                            except ValueError:
                                print('chose number only')
                                print('')
                        else:
                            from datetime import date

                            todays = date.today()
                            bankaccount['last_access'] = todays
                            bankaccount['today'] = cash
                            print('')
                            print('I will withdraw that from your account.')
                            print('')
                            print('Your account balance is: RUB ',
                                  format(float(bal) - float(cash), ',.2f'),
                                  sep='')
                            print('')
                            print('')
                            endmath = float(bal) - float(cash)
                            format(endmath, ',.2f')
                            bankaccount['balance'] = endmath
                            save(bankaccount)
                            quitting()
                except ValueError:
                    print('you have entered symbols or letters, dont you?')
                    print('')
                    print('returning to the beginning of operation')
                    import time
                    a = 0
                    while a < 2:
                        a = a + 1
                        print("...")
                        time.sleep(1)  # Delay for 1 second.
                    else:
                        withdraw(bankaccount)

        else:
            print('')
            quitting()
    else:
        print('wrong answer')
        print('chose only betwen y or n')
        print('returning to beginning of operation')
        print('')
        print('')
        withdraw(bankaccount)


def old_depo(bankaccount):
    # Get the starting balance.
    balancea = bankaccount['balance']

    # Display the balance.
    print('Your account balance is: RUB ',
          format(float(balancea), ',.2f'),
          sep='')

    cash = float(input('How much would you like to deposit? '))
    print('')
    print('')
    print('We will deposit that to your account.')
    print('')

    import time
    a = 0
    while a < 2:
        a = a + 1
        print("...")
        time.sleep(1)  # Delay for 1 second.

    # Display the balance.
    bal = float(balancea) + float(cash)

    print('Your account balance is RUB',
          format(float(balancea) + cash, ',.2f'),
          sep='')

    bankaccount['balance'] = bal
    print('')
    print('')

    import datetime
    bankaccount['last_access'] = datetime.date.today()
    # saving !

    filename = bankaccount.get('name')

    pickle_out = open(filename, "wb")
    pickle.dump(bankaccount, pickle_out)
    pickle_out.close()
    import time
    a = 0
    while a < 2:
        a = a + 1
        print("...")
        time.sleep(1)  # Delay for 1 second.
    else:
        quitting()
    print('Data has been successfully save to a file')
    print('')
    print('')
    again = input('Would you like to repeat steps (y/n): ')
    if again == 'n':
        quitting()
    else:
        old_depo(bankaccount)


def deposit(bankaccount):
    print('chose between:')
    print('e - existing       n - new one')
    print('')
    again = input('account already existing or u want to create a new one?:')
    if again == 'e' or again == 'n':
        while again == 'e':
            filename = input('enter name of customer:')
            try:
                pickle_in = open(filename, "rb")
                bankaccount = pickle.load(pickle_in)
                print('')
                questions(bankaccount)
                old_depo(bankaccount)
            except (KeyError, EOFError, FileNotFoundError):
                print('not found')
                print('')
                print('')
                quitting()
        else:
            print('do u want to create mew one? y/n')
            print('')
            x = input('-->>')
            while x == 'y' or x == 'n':
                if x == 'y':
                    opena(bankaccount)
                else:
                    quitting()
    else:
        print('')
        print('')
        print('wrong answer!')
        print('')
        print('returning to beginning of operation')
        deposit(bankaccount)


def opena(bankaccount):
    print('Would you like to crave a new account (y/n):')
    chose = input('-->>')
    import datetime
    todays = datetime.date.today()
    bankaccount['last_access'] = todays
    while chose == 'y' or chose == 'n':
        if chose == 'y':
            print('Enter name of customer')
            namea = input("-->>")
            bankaccount['name'] = namea
            print('')
            print('your new account name is:   ', namea)
            print('')
            print('')
            print('p - personal')
            print('c - company')
            print('')
            print('what kind of type will be this account:')
            print('')
            companya = input('-->>')
            print('')
            if companya == 'c' or companya == 'p':
                bankaccount['company'] = companya
            elif companya == 'c' or companya == 'p':
                print('wrong choice!')
                print('')
                print('chose between  p - personal  or  c - company account type ')
                print('')
                companya = input('-->>')
                print('')
                bankaccount['company'] = companya
            else:
                print('your answer was 2 times wrong!')
                print('')
                print('returning to the beginning of the operation...')
                import time
                a = 0
                while a < 2:
                    print('...')
                    a = a + 1
                    time.sleep(1)
                opena(bankaccount)

            print('')
            print('chose betwen  pl - polish  or,  int - international type ')
            print('')
            nationalitya = input('-->>')
            print('')
            if nationalitya == 'pl' or nationalitya == 'int':
                bankaccount['nationality'] = nationalitya
            elif nationalitya != 'pl' or nationalitya != 'int':
                print('wrong choice!')
                print('')
                print('')
                print('chose between  pl - polish  or,  int - international type ')
                print('')
                nationalitya = input('-->>')
                bankaccount['nationality'] = nationalitya
            else:
                print('your answer was 2 times wrong!')
                print('')
                print('returning to the beginning of the operation...')
                import time

                a = 0
                while a < 2:
                    print('...')
                    a = a + 1
                    time.sleep(1)
                else:
                    opena(bankaccount)

            covid19(bankaccount)
            covid19_company(bankaccount)

            print('')
            print('y - deposit')
            print('n - return to main menu')
            print('')
            print('')
            print('do u want to deposit cash on your new account?')
            print('')
            dep = input('-->>')
            print('')
            if dep == 'y' or dep == 'n':
                if dep == 'y':
                    old_depo(bankaccount)
                else:
                    save(bankaccount)
            elif dep != 'y' or dep != 'n':
                print('wrong choice !!!')
                print('')
                print('y - deposit')
                print('n - return to main menu')
                print('')
                print('do u want to deposit cash on your new account?')
                print('')
                dep = input('-->>')
                if dep == 'y':
                    old_depo(bankaccount)
                else:
                    save(bankaccount)
            else:
                print('your answer was 2 times wrong!')
                print('')
                print('returning to the beginning of the operation...')

                import time
                a = 0
                while a < 2:
                    print('...')
                    a = a + 1
                    time.sleep(1)
                else:
                    opena(bankaccount)
        else:
            quitting()
    else:
        print('wrong choice')
        print('chose only y/n')
        opena(bankaccount)


def closea(bankaccount):
    print('annotation: type only names of person who have already bank account!')
    print('')
    print('enter your account name:')
    filename = input('-->>')
    bankaccount_wtf = {'balance_delete': 0}
    try:
        pickle_in = open(filename, "rb")
        bankaccount = pickle.load(pickle_in)
        print('')
        pickle_in.close()
    except (KeyError, EOFError, FileNotFoundError):
        print('not found')
        print('')
        print('')
        quitting()
    closing = bankaccount['restriction']
    bankaccount_wtf['balance_delete'] = bankaccount['balance']
    if closing != 'yes':

        print('Closing bank account', filename)
        print("")
        print('y- close account')
        print('n - abandon operation and return to main menu')
        print('')
        close = input('are you sure to close account?')
        print('')
        print('')
        if close == 'y':
            print('fist, you have to withdraw all cash,')
            print('or you can transfer it to other account')
            print("")
            print('chose between:')
            print('')
            print('t = transfer')
            print('w = withdraw')
            print('')
            transfer = input('enter your choice')
            print('')
            if transfer == 't':
                # transfer to other account method
                print('enter name of customer to transfer money:')
                filename2 = input('-->')

                try:
                    pickle_in = open(filename2, "rb")
                    bankaccount = pickle.load(pickle_in)
                    print('')
                    pickle_in.close()
                    questions(bankaccount)
                    balance_existing = float(bankaccount['balance'])
                    balance_delete = str(bankaccount_wtf['balance_delete'])
                    balance_delete = balance_delete.replace(',', '')
                    # float(balance_delete.strip().strip(","))
                    float(balance_delete)
                    bale = float(balance_delete) + balance_existing
                    bankaccount['balance'] = bale
                    import time
                    a = 0
                    while a < 2:
                        a = a + 1
                        print("...")
                        time.sleep(1)
                        if a == 2:
                            break
                    print('')
                    pickle_out = open(filename2, "wb")
                    pickle.dump(bankaccount, pickle_out)
                    pickle_out.close()
                    print('Account named', filename2, ' received yor transfer')
                    print('')
                    print('this account balance is now RUB: ',
                          format(float(balance_delete) + float(balance_existing), ',.2f'),
                          sep='')
                    print('')
                    print('thank you for cooperation')
                    print('')
                    print('closing your account')
                    import time
                    a = 0
                    while a < 2:
                        a = a + 1
                        print("...")
                        time.sleep(1)
                        if a == 2:
                            break
                    import os
                    import shutil
                    root_dir = os.path.dirname(os.path.abspath(__file__))
                    config_path = os.path.join(root_dir, filename2)

                    os.remove(config_path)
                    print('successfully closed!')
                    quitting()
                except (KeyError, EOFError, FileNotFoundError):
                    print('user not found')
                    print('')
                    print('')
                    quitting()
            elif transfer == 'w':
                balance_delete = bankaccount_wtf['balance_delete']
                print('here is your cash RUB: ',
                      format(float(balance_delete), ',.2f'),
                      sep='')
                import os
                root_dir = os.path.dirname(os.path.abspath(__file__))
                config_path = os.path.join(root_dir, filename)
                os.remove(config_path)

                print('')
                print('thank you for cooperation')
                print('')
                quitting()
            else:

                print('wrong choice, returning to beginning of operation')
                import time
                a = 0
                while a < 2:
                    a = a + 1
                    print("...")
                    time.sleep(1)  # Delay for 1 second.
                else:
                    closea(bankaccount)

        elif close == 'n':
            quitting()
        else:
            print('')
            print('wrong choice')
            print('')
            quitting()

    else:

        print('')
        print('')
        print('you cannot close company account !')
        print('covid19 restriction !')
        quitting()


def save(bankaccount):
    import pickle
    filename = bankaccount.get('name')

    pickle_out = open(filename, "wb")
    pickle.dump(bankaccount, pickle_out)
    pickle_out.close()
    print()
    print('Saving...')
    import time
    a = 0
    while a < 2:
        a = a + 1
        print("...")
        time.sleep(1)  # Delay for 1 second.
    else:
        print('')
        print('Data has been successfully save to a file')
        print('')
        quitting()


def loada():
    filename = input('enter name of customer:  ')
    print('')
    print('')
    try:
        pickle_in = open(filename, "rb")
        bankaccount = pickle.load(pickle_in)
        questions(bankaccount)
        print('')
        quitting()
    except (KeyError, EOFError, FileNotFoundError):
        print('')
        print('')
        print('not found')
        print('')
        print('')
        print('Returning to main menu')
        quitting()


def covid19(bankaccount):
    d1 = bankaccount['last_access']
    d3 = bankaccount['d2']
    # print(d1)
    # print(d3)
    if d3 < d1:
        if bankaccount['nationality'] == 'pl':
            compa = bankaccount['company']
            if compa == 'p':
                from datetime import date
                today = date.today()
                if d1 == today:
                    d = bankaccount['today']
                    if float(d) < 1000:
                        print('today you have already withdrawn: RUB ', bankaccount['today'])
                        endmath = 1000 - float(d)
                        bankaccount['last_access_today'] = endmath
                        print('you can withdraw: RUB ', endmath, 'more.')
                        print('')
                    else:
                        print('you can only withdraw 1k a day')
                        print('')
                        quitting()
                else:
                    print('remember about limit 1000 per day')
                    print('')
            else:
                return
        else:
            print('')
            print('you are not from here')
            print('restrictions do not apply to you')
            print('')
    else:
        print('')
        print('Corona virus didnt attacked yet ;)')
        print('')


def covid19_company(bankaccount):
    d1 = bankaccount['last_access']
    d3 = bankaccount['d2']
    # print(d1)
    # print(d3)
    if d3 < d1:
        if bankaccount.get('company') == 'p':
            bankaccount['restriction'] = 'no'
            print('')
            print('individual account type')
            print('nothing changed, your account have no restriction to close')
            print('you can only withdraw 1000 RUB per day !')
            print('')
        else:
            bankaccount['restriction'] = 'yes'
            print('')
            print('this is company account')
            print('you cannot close this account')
            print('')
            if bankaccount.get('balance') == 0:
                print('5000 RUB has been transferred to you account')
                bankaccount['balance'] = int(5000)
                print('')
                print('your new account balance is now: ', bankaccount.get('balance'))
            else:
                print('you already received help for your company!')
    else:
        print('')
        print('5k on start - this offer is not yet available ;)')


def questions(bankaccount):
    print('Client name:  ', bankaccount['name'])
    print('')
    if bankaccount['company'] == 'c':
        print('COMPANY type account')
        print('')
    else:
        print('INDIVIDUAL type account')
        print('')
    if bankaccount['nationality'] == 'pl':
        print('NATIONAL client')
        print('')
    else:
        print('INTERNATIONAL client')
        print('')

    print('Your account balance is:  RUB ',
          format(bankaccount['balance'], ',.2f'),
          sep='')
    print('')
    date = bankaccount['last_access']
    print('Last access: ', date)
    print('')
    print('Closing Restriction: ', bankaccount['restriction'])
    print('')
    print('')


def end():
    print('finally the end')
    print('im looking forward to good grade ;)')
    import time
    a = 0
    while a < 2:
        a = a + 1
        print("...")
        time.sleep(1)  # Delay for 1 second.
        if a == 2:
            break
    exit()


main()
