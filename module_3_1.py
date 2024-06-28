
calls = 0

def count_calls():
    global calls
    calls += 1
    return

def string_info(string):
    count_calls()
    cort = [len(string),string.upper(),string.lower()]
    return cort



def is_contained(string, list_to_search):
    count_calls()
    string = string.lower()
    list_to_search = [i.lower() for i in list_to_search]
    return string in list_to_search









print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contained('Urban', ['ban', 'BaNaN', 'UrbAn'])) # Urban ~ urBAN
print(is_contained('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)










