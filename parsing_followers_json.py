import json


def open_json():
    json_file = "json_followers.json"

    with open(json_file) as f:
        data = json.load(f)
    return data


# globals:
global item_count
global items
global that_name
global new_name
global followers_names
item_count = 0
items = []
that_name = False
new_name = None
followers_names = []

global user_name
global searched_items
global user_item
global available_items
global start
user_item = {}
user_name = ""
searched_items = ""
available_items = []
start = 1


def getting_to_loc(data, point):
    global that_name
    global followers_names
    global new_name

    global user_name
    global searched_items
    global user_item

    d = data

    for item in d:
        # multiple answer case:
        # if new_name is not None:
        if item == "name":
            user_name = d[item]

        if item == point:
            print('here')
            print("{}: {}".format(item, d[item]))
            searched_items = d[item]

        if searched_items != "" and user_name != "":
            user_item.update({user_name: searched_items})
            user_name = ""
            searched_items = ""

        # parse all the data:
        if item == "name" and d[item] not in followers_names:
            followers_names.append(d[item])

        if item == point:
            global item_count
            global items
            item_count += 1
            items.append(d[item])

        if type(d[item]) == list:
            for i in range(len(d[item])):
                try:
                    new_item = d[item][i]
                    getting_to_loc(new_item, point)
                except KeyError:
                    pass
                except TypeError:
                    pass

        elif type(d[item]) == dict:
            item = d[item]
            getting_to_loc(item, point)

        if start == 1 and item not in available_items and type(item) != dict and type(item) != list:
            available_items.append(item)

    if new_name is None:
        return item_count, items, point, followers_names, user_item, available_items


def if_more_than_one(p_data, point):
    count = p_data[0]
    p_items = p_data[1]
    name = p_data[2]
    f_names = p_data[3]
    u_item = p_data[4]

    # printing items:
    print("\n")
    print("There are total {} {}s found: \n".format(count, name))
    for item in enumerate(p_items):
        print(str(item[0] + 1) + ")", str(item[1]))
    print("\nfor users:\n")
    for item in enumerate(f_names):
        print(str(item[0] + 1) + ")", str(item[1]))

    cont = str(input("Would you like to get all the available {}s of a specific user? (y/n)".format(point)))

    if cont.capitalize() == "Yes" or cont.upper() == "Y":
        user_answer = str(input("Please enter a username or number that corresponds to the username: "))

        if user_answer.isdigit():
            try:
                resulted_data = u_item[f_names[(int(user_answer) - 1)]]
                print("{}'s {}: {}".format(f_names[(int(user_answer) - 1)], point, resulted_data))
                return resulted_data
            except IndexError:
                print("unable to access data...")
            except KeyError:
                print("unable to access data...")
        else:
            resulted_data = u_item[user_answer]
            return resulted_data
            # print("{}'s {}: {}".format(user_answer, point, resulted_data))
    else:
        pass


def dispay_data():
    global item_count
    global items
    global that_name
    global new_name
    global followers_names
    item_count = 0
    items = []
    that_name = False
    new_name = None
    followers_names = []

    start = 1
    available_items = getting_to_loc(open_json(), None)[5]
    start = 0

    print("Here are all available items for you to search: \n\n")
    for item in enumerate(available_items):
        print(str(item[0] + 1) + ")", str(item[1]))
    print("\n")

    main_point = str(input("Enter a key to search: "))

    parsed_data = getting_to_loc(open_json(), main_point)
    print(parsed_data)

    if int(parsed_data[0]) > 2:
        items_to_find = if_more_than_one(parsed_data, main_point)
    else:
        pass

    continue_parsing = str(input("Would you like to search for more items? (y/n)"))
    if continue_parsing.capitalize() == "Yes" or continue_parsing.upper() == "Y":
        dispay_data()
    else:
        pass


if __name__ == '__main__':
    dispay_data()





























































































































