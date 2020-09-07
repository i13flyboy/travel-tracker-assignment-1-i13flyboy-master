from operator import itemgetter

menu = """L - List places
A - Add new place
M - Mark a place visited
Q - Quit
>>>>"""


def main():
    in_file = open("places.csv", "r")
    data = in_file.readlines()
    places = []
    for n in data:
        values = n.strip().split(',')
        places.append(values)
    for i in range(len(places)):
        places[i][2] = int(places[i][2])
    places.sort(key=itemgetter(0, 3))
    in_file.close()
    print("Travel Tracker 1.0 - by <Kyle Kunz>")
    print("3 places loaded form places.csv")
    print("Menu:")
    choice = input(menu).upper()
    while choice != "Q":
        if choice == "L":
            list_places(places)
            print("Menu:")
        elif choice == "A":
            places.append(add_places())
            places.sort(key=itemgetter(0, 3))
            print("Menu:")
        elif choice == "M":
            places = mark_places(places)
            print("Menu:")
        else:
            print("Invalid menu choice")
        choice = input(menu).upper()
    save_places(places)


def list_places(places):
    i = 0
    not_visited = 0
    while i < len(places):
        if places[i][3] == "n":
            print("{:2}. * {:10} in {:12}    priority {}".format(i, places[i][0], places[i][1], places[i][2]))
            not_visited = not_visited + 1
        else:
            print("{:2}.   {:10} in {:12}    priority {}".format(i, places[i][0], places[i][1], places[i][2]))
        i = i + 1
    places_visited = len(places) - not_visited
    print("{} places visited, {} places still to visit".format(places_visited, not_visited))
    return places


def add_places():
    new_place = []
    place_name = str(input("Name of Place: "))
    while True:
        try:
            place_country = str(input("Country: "))
            if place_country == '' or place_country == ' ':
                print("Input can not be blank")
                continue
            if '  ' in place_country:
                print("Input contains too many spaces")
            break
        except ValueError:
            print("Input can not be a number")
    while True:
        try:
            place_pri = int(input("Priority: "))
            if place_pri < 0:
                print("Number must be >= 0")
                continue
            break
        except ValueError:
            print("Invalid input; enter a valid number")
    new_place.append(place_name)
    new_place.append(place_pri)
    new_place.append(place_country)
    new_place.append('n')
    print("{} from {}  priority {} added to travel list.".format(place_name, place_country, place_pri))
    return new_place


def mark_places(places):
    while True:
        try:
            places_visited = int(input("Enter the number of a place to mark as visited: "))
            if 'v' in places[places_visited]:
                print("You have already visited {} ".format(places[places_visited][0]))
                continue
            if places_visited < 0 or places_visited > len(places) - 1:
                print("Please enter a valid number")
                continue
            break
        except ValueError:
            print("please enter a number")
    places[places_visited][3] = 'v'
    print("{} from {} has been visited".format(places[places_visited][0], places[places_visited][1]))
    return places


def save_places(places):
    print("Thank you. Places saved to CSV".format(len(places)))
    out_file = open("places.csv", 'w')
    for place in places:
        print("{},{},{},{}".format(place[0], place[1], place[2], place[3]), file=out_file)
    out_file.close()


if __name__ == '__main__':
    main()


