print("***** ***** *****  NOKIA  ***** ***** *****  NOKIA  ***** *****  *****  NOKIA  ***** ***** *****")
print(
    '///////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|||||||||||||||||||//////////////\\\\\\\\\\\\\\\\\\\\\\\\\/////////////|||')
print("***** ***** *****  NOKIA  ***** ***** *****  NOKIA  ***** *****  *****  NOKIA  ***** ***** *****")
print()


def games():
    print("""GAMES ***** ***** NOKIA  GAMES  ***** ***** GAMES 
                (1)Snake||
                (2)Space Impact
                (3)Bantu-mi
                (4)Pairs||
                (5)Game Setting""")
    command = input('enter 0 for previous menu or T to end application: ')
    if command.upper() == 'T':
        return exit()
    elif command == '0':
        return function_input_command()
    else:
        print('enter a valid command', games())


def phonebook():
    print(""" ***** ***** *****  PHONEBOOK  ***** ***** ***** 
                1. Search
                2. Service No
                3. Add name
                4. Erase
                5. Edit
                6. Assign tone
                7. Send b’card
                8. Options
                9. Speed dials
                10. Voice tags
                0. Back
                : """)
    command = input('enter 0 for previous menu or T to end application: ')
    if command.upper() == 'T':
        return exit()
    elif command == '8':
        return phone_book_option()
    elif command == '0':
        return function_input_command()
    else:
        print('invalid command', phonebook())


def function_input_command():
    function_command = (
        input("""NOKIA ***** ***** FUNCTION  MENU  ***** ***** NOKIA 
        \n(1) Phonebook \n(2) Messages \n(3) Chat \n(4) CallRegister\n(5) Tones \n(6) Setting"""
              """\n(7) Call Divert \n(8) Reminder \n(9) Calculator \n(10) Clock\n(11) Sim Services \n(12) Profile"""
              """\n(13) Game \nEnter Command: """))
    if function_command == '1':
        return phonebook()
    elif function_command == '2':
        return messages()
    elif function_command == '3':
        print(chat())
    elif function_command == '4':
        print(call_register())
    elif function_command == '5':
        print(tones())
    elif function_command == '6':
        print(setting())
    elif function_command == '7':
        print(call_divert())
    elif function_command == '8':
        print(reminder())
    elif function_command == '9':
        print(calculator())
    elif function_command == '10':
        print(clock())
    elif function_command == '11':
        return sim_services()
    elif function_command == '12':
        print(profiles())
    elif function_command == '13':
        return games()
    elif function_command.upper() == 'T':
        exit()
    else:
        print("invalid Command", function_input_command())


def phone_book_option():
    print(' (1) Type of view \n(2) Memory status')
    command = input('enter 0 for previous menu or T to end application: ')
    if command == '0':
        return phonebook()
    elif command.upper() == 'T':
        exit()
    else:
        print('enter a valid command: ', phone_book_option())


def messages():
    print(""" ///////MESSAGES/////////MESSAGES/////////MESSAGES//////////
                1. Write messages
                2. Inbox
                3. Outbox
                4. Picture messages
                5. Templates
                6. Smileys
                7. Message settings                                                   
                8. Info service
                9. Voice mailbox number
                10.Service command editor """)
    command = input('enter 0 for previous menu or T to end application: ')
    if command.upper() == 'T':
        exit()
    elif command == '0':
        return function_input_command()
    elif command == '7':
        return message_setting()
    else:
        print('invalid command', messages())


def message_setting():
    print('Message Setting\n1. Set\n2. Common')
    command = input('enter 0 for previous menu or T to end application: ')
    if command.upper() == 'T':
        exit()
    elif command == '0':
        return messages()
    elif command == '1':
        return set_setting()
    elif command == '2':
        return common()
    else:
        print('invalid command', message_setting())


def common():
    print('Common Setting\n1. Delivery report\n2. Reply via same center\n3. Character support')
    command = input('enter 0 for previous menu or T to end application: ')
    if command.upper() == 'T':
        exit()
    elif command == '0':
        return message_setting()
    else:
        print('invalid command', common())


def set_setting():
    print('Set\n1. Message\n2. Message Sent As\n3.Message Validity')
    command = input('enter 0 for previous menu or T to end application: ')
    if command.upper() == 'T':
        exit()
    elif command == '0':
        return message_setting()
    else:
        print('invalid command', set_setting())


def chat():
    print("""%%%%%%%CHAT%%%%%%%%%CHAT%%%%%%%%%CHAT%%%%%%%%%
            (1)New chat 
            (2)Chat Name 
            (3)Chat History""")
    command = input('enter 0 for previous menu or T to end application: ')
    if command.upper() == 'T':
        exit()
    elif command == '0':
        return function_input_command()
    else:
        print('invalid command', chat())


def call_register():
    print("""₦₦₦₦₦₦₦₦₦₦₦₦CALL REGISTER₦₦₦₦₦₦₦₦₦₦₦₦₦CALL REGISTER₦₦₦₦₦₦₦₦₦₦₦CALL REGISTER₦₦₦₦₦₦₦₦₦₦₦
    
                1. Missed calls
                2. Received calls
                3. Dialled numbers
                4. Erase recent call lists
                5. Show call duration                             
                6. Show call costs
                7. Call cost settings
                8. Prepaid credit """)
    command = input('enter 0 for previous menu or T to end application: ')
    if command.upper() == 'T':
        exit()
    elif command == '0':
        return function_input_command()
    elif command == '5':
        return show_call_duration()
    elif command == '6':
        return show_call_cost()
    elif command == '7':
        return call_cost_settings()
    else:
        print('invalid command', call_register())


def call_cost_settings():
    print('Call Cost Setting\n1. Call cost limit\n2. Show costs in')
    command = input('enter 0 for previous menu or T to end application: ')
    if command.upper() == 'T':
        exit()
    elif command == '0':
        return call_register()
    else:
        print('invalid command', call_cost_settings())


def show_call_cost():
    print('Show Call Cost\n1. Last call cost\n2. All calls cost\n3. Clear counters')
    command = input('enter 0 for previous menu or T to end application: ')
    if command.upper() == 'T':
        exit()
    elif command == '0':
        return call_register()
    else:
        print('invalid command', show_call_cost())


def show_call_duration():
    print('show call duration\n 1. Last call duration \n2. All calls’ duration'
          '\n3. Received calls’ duration\n4. Dialled calls  duration\n5. Clear timers  ')
    command = input('enter 0 for previous menu or T to end application: ')
    if command.upper() == 'T':
        exit()
    elif command == '0':
        return call_register()
    else:
        print('invalid command', show_call_duration())


def tones():
    print("""%%&&%%&&TONES%%&&%%&&%%TONES&&%%&&%%TONES&&%%%&&&
                1. Ringing tone
                2. Ringing volume
                3. Incoming call alert
                4. Composer
                5. Message alert tone
                6. Keypad tones
                7. Warning and game tones
                8. Vibrating alert
                9. Screen saver """)
    command = input('enter 0 for previous menu or T to end application: ')
    if command.upper() == 'T':
        exit()
    elif command == '0':
        return function_input_command()
    else:
        print('invalid command', tones())


def setting():
    print("""\/\/\/\/\/\/SETTING\/\/\/\/\/SETTING/\/\/\/\/SETTING/\/\/\/\/\/
                (1) Call setting   
                (2) Phone Setting 
                (3) Security setting 
                (4) Restore Factory Setting """)
    command = input('enter 0 for previous menu or T to end application: ')
    if command == '1':
        return call_setting()
    elif command == '2':
        return phone_setting()
    elif command == '3':
        return security_setting()
    elif command == '0':
        return function_input_command()
    elif command == 't':
        exit()
    elif command == '4':
        print('null: ', setting())
    else:
        print('enter a valid command: ', setting())


def security_setting():
    print('Security Setting\n1. PIN code request \n2. Call barring service \n3. Fixed dialling '
          '\n4. Closed user group \n5. Phone security \n6. Change access codes')
    command = input('enter 0 for previous menu or T to end application: ')
    if command == '0':
        return setting()
    elif command.upper() == 'T':
        exit()
    else:
        print('enter a valid command: ', security_setting())


def phone_setting():
    print("""Phone Setting\n1. Language \n2. Cell info display \n3. Welcome note \n4. Network selection \n5. Lights2\n
    6. Confirm SIM service actions""")
    command = input('enter 0 for previous menu or T to end application: ')
    if command == '0':
        return setting()
    elif command.upper() == 'T':
        exit()
    else:
        print('enter a valid command: ', phone_setting())


def call_setting():
    print("""Call Setting\n1. Automatic redial\n 
    2. Speed dialling \n3. Call waiting options\n
    4. Own number sending \n5. Phone line in use \n6. Automatic answer """)
    command = input('enter 0 for previous menu or T to end application: ')
    if command == '0':
        return setting()
    elif command.upper() == 'T':
        exit()
    else:
        print('enter a valid command: ', call_setting())


def call_divert():
    print("""@#@#@#@#₦@CALL DIVERT@#@#@#@#@#@CALL DIVERT@@#@#@#@#@#@#@#@#
                (1)Divert When Busy 
                (2)Divert All Not Reachable Call
                (3)Cancel All Divert""")
    command = input('enter 0 for previous menu or T to end application: ')
    if command == '0':
        return function_input_command()
    elif command.upper() == 'T':
        exit()
    else:
        print('enter a valid command: ', call_divert())


def calculator():
    print("""+%*-=<>CALCULATOR-=<>+%^2=1CALCULATOR-=+%*()<>CALCULATOR<>()+__-==34*
            (1)Arithmetic 
            (2)Currency Conversion""")
    command = input('enter 0 for previous menu or T to end application: ')
    if command == '0':
        return function_input_command()
    elif command.upper() == 'T':
        exit()
    else:
        print('enter a valid command: ', calculator())


def reminder():
    print("""|||||||||||REMINDER|||||||REMINDER||||||||REMINDER|||||||||
               (1)Add New 
               (2)Erase 
               (3)View All 
               (4)Edit 
               (5)Send 
               (6)Snooze""")
    command = input('enter 0 for previous menu or T to end application: ')
    if command == '0':
        return function_input_command()
    elif command.upper() == 'T':
        exit()
    else:
        print('enter a valid command: ', reminder())


def clock():
    print("""~~~~~~~~~CLOCK~~~~~~~~~CLOCK~~~~~~~~CLOCK~~~~~~~~~~
            (1)AlarmClock 
            (2) Clock settings 
            (3) Date setting 
            (4) Stopwatch 
            (5) Countdown timer 
            (6) Auto update of date and time""")
    command = input('enter 0 for previous menu or T to end application: ')
    if command == '0':
        return function_input_command()
    elif command.upper() == 'T':
        exit()
    else:
        print('enter a valid command: ', clock())


def profiles():
    print(r"""<<<<<<<<<<<PROFILE>>>>>>>>>>PROFILE<<<<<<<<<<<PROFILE>>>>>>>>>>>>>
            (1)General 
            (2)Silent 
            (3)Personalise""")
    command = input('enter 0 for previous menu or T to end application: ')
    if command == '0':
        return function_input_command()
    elif command.upper() == 'T':
        exit()
    else:
        print('enter a valid command: ', profiles())


def sim_services():
    print('No Service')
    command = input('enter 0 for previous menu or T to end application: ')
    if command == '0':
        return function_input_command()
    elif command.upper() == 'T':
        exit()
    else:
        print('enter a valid command: ', sim_services())


function_input_command()
