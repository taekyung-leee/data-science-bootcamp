#Holiday price calculator depending on user's destination, number of nights staying, and rental cost.

#default hotel per night and daily car rental price:
default_hotel_cost = 110
default_car_rental = 80

#calculate return flight tickets price for selected destination.

def plane_cost():
    while True:
        city_flights = input("Where are you flying to? (a. New York - £550, b. Paris - £100, c. Brussel: £80, d. Dubai - £700, e. Tokyo - £900 ): ")

        if city_flights == "a":
            plane_cost = 550
        elif city_flights == "b":
            plane_cost = 100
        elif city_flights == "c":
            plane_cost = 80
        elif city_flights == "d":
            plane_cost = 700
        elif city_flights == "e":
            plane_cost = 900
        elif city_flights not in ["a", "b", "c", "d", "e"]:
            print("Wrong input. Please enter your destination again.")
            continue

        print(f"Your return tickets cost £{plane_cost}.")
        return plane_cost
        
        
#calculate total hotel cost.
def hotel_cost():
    while True:
        try: 
            num_nights = int(input("How many nights are you staying at the hotel?: "))
            hotel_cost = num_nights * default_hotel_cost
            print(f"Your total cost for hotel is £{hotel_cost}.")
            break
        except:
            ValueError
            print("Please enter an integer only.")

    return hotel_cost


#calculate total car rental cost.
def car_rental():
    while True:
        try:
            rental_days = int(input("How many days are you renting a car?: "))
            car_rental = rental_days * default_car_rental
            print(f"Your total cost for car rental is £{car_rental}.")
            break
        except:
            ValueError
            print("Invalid value, please enter number only.")
    
    return car_rental

#calculate 
def holiday_costs():
    holiday_costs = hotel_cost() + plane_cost() + car_rental()
    print(f"Your holiday will cost you £{holiday_costs} in total")
    return holiday_costs


holiday_costs()
