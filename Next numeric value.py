

def hotel_cost(nights):
    return nights*70

def plane_ticket_cost(city, flight_class):

    class_multiplier = 0

    if flight_class == "economy" : class_multiplier = 1
    elif flight_class == "premium economy" : class_multiplier = 1.3
    elif flight_class == "business class" : class_multiplier = 1.6
    elif flight_class == "first class" : class_multiplier = 1.9

    if city == "New York": return 2000*class_multiplier
    elif city == "Auckland": return 790*class_multiplier
    elif city == "Venice": return 154*class_multiplier
    elif city == "Glasgow": return 65*class_multiplier
    else:
        print("City not understood")
        return 0

def rental_car_cost(days):
    cost = days*30
    if days > 7:
        cost -= 50
    elif days > 3:
        cost -=30
    return cost

def total_cost(city, days, flight_class):
    total = rental_car_cost(days) + hotel_cost(days-1) + plane_ticket_cost(city,flight_class)
    print("Car: £", rental_car_cost(days),
          "Hotel: £", hotel_cost(days-1),
          "Plane: £", plane_ticket_cost(city,flight_class),
          "Total: £", total)

city = input("Where are you travelling? (New York, Auckland, Venice, Glasgow")
flight_class = input("Which flight class? (economy,premium economy,business class, first class)")
days = int(input("How many days will you be staying?"))

total_cost(city,days,flight_class)