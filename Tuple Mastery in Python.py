flight_itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]

for index,(name,origin,destination) in enumerate(flight_itineraries):
    print(f'Itinerary {index + 1}: {name} - from {origin} to {destination}')
    

