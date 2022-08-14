##### all program functions #####
def hash_first_name_and_year(name, birth_of_year,array_2d):
    kamus = {}
    alfa = "abcdefghijklmnopqrstuvwxyz"
    for abjad in range(26):
        kamus[alfa[abjad]] = abjad
    first_name = name[0] 
    return (kamus[first_name] + int(birth_of_year)) % len(array_2d) 

def add(array_2d, data_name, data_birth_of_year, data_phone_number): 
        vetical_index = hash_first_name_and_year(data_name, data_birth_of_year,array_2d) 
        horizontal_index = array_2d[vetical_index]
        data = {"name" : data_name,
                "birth of year" : data_birth_of_year,
                "phone number" : data_phone_number}
        if not is_full(array_2d, data_name, data_birth_of_year):
            for index in range(len(horizontal_index)):
                if horizontal_index[index] == None:
                    horizontal_index[index] = data
                    break
        else: 
            resize(array_2d)
            add(array_2d, data_name, data_birth_of_year, data_phone_number)
        return array_2d

def search(array_2d, name, birth_of_year):
    vertical_index = hash_first_name_and_year(name, birth_of_year, array_2d) 
    horizontal_array = array_2d[vertical_index]
    for horizontal_index in range(0, len(horizontal_array)):
        if horizontal_array[horizontal_index] is not None :
            if horizontal_array[horizontal_index]['name'] == name and  horizontal_array[horizontal_index]['birth of year'] == birth_of_year: 
                return True, (horizontal_array[horizontal_index], vertical_index, horizontal_index) 
    return False,None

def resize(array_2d): 
    row_length = len(array_2d)
    colomn_length = len(array_2d[0])
    for i in range(row_length):
        array_2d[i] = array_2d[i]+([None]*colomn_length)
    return array_2d

def is_full(array_2d, name, birth_of_year):
    vertical_index = hash_first_name_and_year(name, birth_of_year,array_2d) 
    if array_2d[vertical_index][-1] is not None :
        return True
    return False

#END
### ALL TEST FUNCTION ###

def should_return_same_hash():
    row = 4
    cols = 4
    array_2d = [[None for i in range(row)] for j in range(cols)]
    hash_1 = hash_first_name_and_year("ribka", 2000, array_2d)
    hash_2 = hash_first_name_and_year("rania", 2004, array_2d)
    assert hash_1 == hash_2

def should_return_different_hash():
    row = 4
    cols = 4
    array_2d = [[None for i in range(row)] for j in range(cols)]
    hash_1 = hash_first_name_and_year("yechiel", 2000, array_2d)
    hash_2 = hash_first_name_and_year("yechiel", 2013, array_2d)
    assert hash_1 != hash_2

def should_add_new_data():
    row = 4
    cols = 4
    array_2d = [[None for i in range(row)] for j in range(cols)]
    data_name = "lolita"
    data_birth_of_year = 2000
    data_phone_number = "081231234123"
    new_array_2d = add(array_2d, data_name, data_birth_of_year, data_phone_number)
    is_found, data = search(new_array_2d, data_name, data_birth_of_year)
    assert is_found == True

def should_add_new_data_and_resize():
    array_2d = [[None, None, None, None],
                [None, None, None, None],
                [{'name':'ciki', 'birth of year':'2012', 'phone number':'1234'},{'name':'cilla', 'birth of year':'2016', 'phone number':'12345'},
                {'name':'caca', 'birth of year':'2012', 'phone number':'123467'},{'name':'cika', 'birth of year':'2012', 'phone number':'309824'}],
                [None, None, None, None]]
    name = "citra"
    birth_of_year = 2020
    phone_number = "098324325"
    is_full_before_insert = is_full(array_2d, name, birth_of_year)
    array_2d = add(array_2d, name, birth_of_year, phone_number)
    is_full_after_insert = is_full(array_2d, name, birth_of_year)
    is_found, data = search(array_2d, name, birth_of_year)
    assert is_found == True
    assert is_full_before_insert  == True
    assert is_full_after_insert == False

def should_return_data_with_v_and_h_index():
    array_2d = [[None, None, None, None],
                [None, None, None, None],
                [None, None, None, None],
                [None, None, None, None]]
    name = "ananda"
    birth_of_year = 2020
    phone_number = "08223898"
    array_2d = add(array_2d, name, birth_of_year, phone_number)
    is_found = search(array_2d, name, birth_of_year)
    assert is_found == (True, ({'name': 'ananda', 'birth of year': 2020, 'phone number': '08223898'}, 0, 0))

def should_not_return_data():
    array_2d = [[{'name':'ananda', 'birth of year':'2005', 'phone number':'0891999934'}, None, None, None],
                [None, None, None, None],
                [None, None, None, None],
                [None, None, None, None]]
    name = "cilla"
    birth_of_year = 2000
    is_found, data = search(array_2d, name, birth_of_year)
    assert is_found == False

def should_get_new_horizontal_array_with_new_length_2times_after_insert():
    array_2d = [[None, None, None, None],
                [None, None, None, None],
                [{'name':'cilla', 'birth of year':'2012', 'phone number':'1234'},{'name':'cilla', 'birth of year':'2016', 'phone number':'12345'},
                {'name':'caca', 'birth of year':'2012', 'phone number':'123467'},{'name':'cika', 'birth of year':'2012', 'phone number':'309824'}],
                [None, None, None, None]] 
    length_before = len(array_2d[2])
    name = "citra"
    birth_of_year = 2020
    phone_number = "098324325"
    array_2d = add(array_2d, name, birth_of_year, phone_number)
    length_after = len(array_2d[2])
    assert length_after == 2*length_before

def should_return_array_2d_with_the_same_length_like_before_after_insert():
    array_2d = [[None, None, None, None],
                [None, None, None, None],
                [None, None, None, None],
                [None, None, None, None]] 
    length_before = len(array_2d[2])
    name = "citra"
    birth_of_year = 2020
    phone_number = "098324325"
    array_2d = add(array_2d, name, birth_of_year, phone_number)
    length_after = len(array_2d[2])
    assert length_after == length_before

def should_return_true_when_array_full():
    array_2d = [[None, None, None, None],
                [None, None, None, None],
                [{'name':'cilla', 'birth of year':'2012', 'phone number':'1234'},{'name':'cilla', 'birth of year':'2016', 'phone number':'12345'},
                {'name':'caca', 'birth of year':'2012', 'phone number':'123467'},{'name':'cika', 'birth of year':'2012', 'phone number':'309824'}],
                [None, None, None, None]]
    name = "cilla"
    birth_of_year = 2020
    full = is_full(array_2d, name, birth_of_year)
    assert full == True

def should_return_false_when_array_is_not_full():
    array_2d = [[{'name':'ana', 'birth of year':'2000', 'phone number':'0891234'}, None, None, None],
                [None, None, None, None],
                [None, None, None, None],
                [None, None, None, None]]
    name = "ani"
    birth_of_year = 2000
    full = is_full(array_2d, name, birth_of_year)
    assert full == False

#END

def tests():
    #ALL TEST
    print("Start test")
    should_return_same_hash()
    should_return_different_hash()
    should_add_new_data()
    should_add_new_data_and_resize()
    should_return_data_with_v_and_h_index()
    should_not_return_data()
    should_get_new_horizontal_array_with_new_length_2times_after_insert()
    should_return_array_2d_with_the_same_length_like_before_after_insert()
    should_return_true_when_array_full()
    should_return_false_when_array_is_not_full()
    print("finish")

def only_string_input():

    while True:
        user_input = str(input("Input your name".ljust(24) + " : ")).lower()
        if not user_input.isalpha():
            print("enter only alphabetical characters for name.")
        else:
            break

def main(array_2d):
    ## my program start here
    print(" \t Das Telefonbuch \t")
    while True:
        confirmation = str(input("1. Add new number \n2. Search by name \n3. Exit \n Choise (1/2/3)? "))
        if confirmation == "1":
            names = (input("Input your name".ljust(24)+" : ")).lower()
            birth_of_years = (input("Input your birth of year : "))
            phone_numbers = (input("Input your phone number".ljust(24)+" : "))
            while names and str(birth_of_years) != " ":
                found,data = search(array_2d, names, birth_of_years)
                if not found :
                    add(array_2d, names, birth_of_years, phone_numbers)
                else: 
                    print("Can't add data\n Already exists !")
                break

        elif confirmation == "2":
            names = (input("Input your name".ljust(24)+" : ")).lower()
            birth_of_years = (input("Input your birth of year : "))
            while names and str(birth_of_years) != " ":
                found,data = search(array_2d, names, birth_of_years)
                if found :
                    phone_numbers = data[0]["phone number"]
                    print("Phone Number".ljust(24)+" :",phone_numbers)
                else:
                    print("Phone Number".ljust(24)+ " : Not Found!")
                break
                
        elif confirmation == "3":
            break
        else:
            print("Wrong input, please try again!")
    
if __name__ == "__main__":
    tests()
    row = 4
    cols = 4
    array_2d = [[None for i in range(row)] for j in range(cols)]
    main(array_2d)
