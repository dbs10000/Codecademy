# --------------------------------------

# UPSTAIRS BEDROOM PLANTS

# -------------------------------------




from .plant_maker_function.create_plant import create_plant




# --------------------------------------

# Details
pot_size = ['small', 'medium', 'large']
watering_method = ['top', 'bottom', 'misting']

# Rooms
# living_room = 1
# stairs = 2
upstairs_bedroom = 3
# balcony = 4
# basaks_old_room = 5
# sonias_old_room = 6

# id
plant_ids = list(range(1, 100))

# --------------------------------------



# UPSTAIRS BEDROOM PLANTS

pothos_plant = create_plant(plant_ids[16], "Pothos (Devil's Ivy) in the white and blue pot on the shelf", "Epipremnum aureum", pot_size[0], watering_method[0], "Water when the top 1–2 inches of soil are dry", upstairs_bedroom)

lipstick_plant = create_plant(plant_ids[17], "Black Pagoda lipstick plant (the hanging plant)", "Aeschynanthus marmoratus", pot_size[0], watering_method[1], "Water with room-temperature water when top 1–2 inches of soil are dry", upstairs_bedroom)

# x = create_plant(plant_ids[3], "nickname", "latin name", pot_size[n], watering_method[n], "watering note", room)

# --------------------------------------

upstairs_bedroom_plants = [pothos_plant, lipstick_plant]