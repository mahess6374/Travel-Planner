import random

def generate_itinerary(city_data, days):
    places = city_data["places"]
    itinerary = []
    used_places = []

    for i in range(days):
        place = random.choice(places)

        # Avoid repeating same place
        while place in used_places:
            place = random.choice(places)

        itinerary.append(place)
        used_places.append(place)

    return itinerary


def calculate_budget(city_data, days, total_budget, style):
    hotel_total = city_data["hotel_cost_per_day"] * days

    # Allocate budget based on travel style
    if style == "Budget":
        food = total_budget * 0.25
        transport = total_budget * 0.2
    elif style == "Luxury":
        food = total_budget * 0.4
        transport = total_budget * 0.3
    else:  # Balanced
        food = total_budget * 0.3
        transport = total_budget * 0.25

    remaining = total_budget - (hotel_total + food + transport)

    return {
        "Hotel": hotel_total,
        "Food": food,
        "Transport": transport,
        "Activities": max(remaining, 0) 
    }