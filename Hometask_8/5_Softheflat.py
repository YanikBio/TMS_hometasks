def flat_S(rooms):
    S = 0
    for room in rooms:
        S += room['length'] + room['width']

    return S

def rooms():
    rooms = [
        {"name": "Kitchen", "length": 6, "width": 4}, \
        {"name": "Room 1", "length": 5.5, "width": 4.5}, \
        {"name": "Room 2", "length": 5, "width": 4,}, \
        {"name": "Room 3", "length": 7, "width": 6.3}
        ]
    return rooms 

def show_info(S):
    print(S, 'м^3')

def main():
    all_rooms = rooms()
    S = flat_S(all_rooms)
    show_info(S)

if __name__ == '__main__':
    main()