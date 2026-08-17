from plants_code.living_room_plants import living_room_plants
from plants_code.bedroom import upstairs_bedroom_plants
from plants_code.stairs import stairs_plants
from plants_code.balcony import balcony_plants

def sql_data(plants):
    for plant in plants:
        print(plant)


sql_data(living_room_plants)
sql_data(upstairs_bedroom_plants)
sql_data(stairs_plants)
sql_data(balcony_plants)