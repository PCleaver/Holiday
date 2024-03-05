city_flight = input("Enter your flight here ").strip()  # User enters a flight and strips any leading/trailing spaces.
num_nights = int(input("Enter your number of nights "))  # User enters the number of nights.
rental_days = int(input("Enter your number of rental days "))  # User enters the number of rental days.

def plane_cost(city_flight):
    """
    Calculate the cost of the flight based on the destination city.
    """
    if city_flight == "Manchester":
        return 500  # Price per flight
    elif city_flight == "London":
        return 750
    elif city_flight == "Nottingham":
        return 350
    elif city_flight == "Birmingham":
        return 100
    else:
        return 0

def hotel_cost(num_nights):
    """
    Calculate the cost of the hotel based on the number of nights.
    """
    price_per_night = 5  # Price per night in the hotel.
    return num_nights * price_per_night

def car_rental(rental_days):
    """
    Calculate the cost of car rental based on the number of rental days.
    """
    price_per_day = 25  # Price per day for car rental.
    return rental_days * price_per_day

def holiday_cost(city_flight, num_nights, rental_days):
    """
    Calculate the total cost for flights, nights, and car rental.
    """
    ticket_cost = plane_cost(city_flight)
    room_cost = hotel_cost(num_nights)
    car_price = car_rental(rental_days)
    total_cost = ticket_cost + room_cost + car_price
    return total_cost

print(
    f"The holiday for {num_nights} nights in the city of {city_flight} "
    f"and includes car hire for {rental_days} days.", end=" "
)

print("The total cost for this holiday is", holiday_cost(city_flight, num_nights, rental_days), "pounds.")