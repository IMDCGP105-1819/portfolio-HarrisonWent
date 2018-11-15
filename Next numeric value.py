

def hotel_cost(nights):
    return nights*70

def plane_ticket_cost(city, flight_class):

    class_multiplier = 0

    if flight_class == "economy" : class_multiplier = 1
    elif flight_class == "premium economy" : class_multiplier = 1.3
    elif flight_class == "business class" : class_multiplier = 1.6
    elif flight_class == "first class" : class_multiplier = 1.9

    if city == "New York": return "£", 2000*class_multiplier
    elif city == "Auckland": return "£", 790*class_multiplier
    elif city == "Venice": return "£", 154*class_multiplier
    elif city == "Glasgow": return "£", 65*class_multiplier

def rental_car_cost(days):
