# --------------------------------------

# STAIRS PLANTS

# --------------------------------------




from .plant_maker_function.create_plant import create_plant




# --------------------------------------

# Details
pot_size = ['small', 'medium', 'large']
watering_method = ['top', 'bottom', 'misting']

# Rooms
# living_room = 1
stairs = 2
# upstairs_bedroom = 3
# balcony = 4
# basaks_old_room = 5
# sonias_old_room = 6

# id
plant_ids = list(range(1, 100))

# --------------------------------------



# STAIRS PLANTS
basil_1 = create_plant(plant_ids[12], "Basil in orange plastic pot sitting on the books", "Ocimum basilicum", pot_size[0], watering_method[1], "keep soil consistently moist but not waterlogged", stairs)

basil_2 = create_plant(plant_ids[13], "Basil in orange plastic pot sitting on the books, sitting in bowl", "Ocimum basilicum", pot_size[0], watering_method[1], "keep soil consistently moist but not waterlogged", stairs)

pothos_plant = create_plant(plant_ids[14], "Pothos (Devil's Ivy) in the white pot by the books", "Epipremnum aureum", pot_size[0], watering_method[0], "Water when the top 1–2 inches of soil are dry", stairs)

basil_3 = create_plant(plant_ids[15], "Basil in grey plastic pot sitting on the grey plate", "Ocimum basilicum", pot_size[0], watering_method[1], "keep soil consistently moist but not waterlogged", stairs)

# x = create_plant(plant_ids[3], "nickname", "latin name", pot_size[n], watering_method[n], "watering note", room)

# --------------------------------------

stairs_plants = [basil_1, basil_2, pothos_plant, basil_3]