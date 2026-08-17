# --------------------------------------

# LIVING ROOM PLANTS

# --------------------------------------




from .plant_maker_function.create_plant import create_plant




# --------------------------------------

# Details
pot_size = ['small', 'medium', 'large']
watering_method = ['top', 'bottom', 'misting']

# Rooms
living_room = 1
# stairs = 2
# upstairs_bedroom = 3
# balcony = 4
# basaks_old_room = 5
# sonias_old_room = 6

# id
plant_ids = list(range(1, 100))

# --------------------------------------



# LIVING ROOM PLANTS
basil_1 = create_plant(plant_ids[0], "Basil in silver pot", "Ocimum basilicum", pot_size[0], watering_method[1], "keep soil consistently moist but not waterlogged", living_room)

basil_2 = create_plant(plant_ids[1], "Basil in orange pot, sitting in bowl", "Ocimum basilicum", pot_size[0], watering_method[1], "keep soil consistently moist but not waterlogged", living_room)

monstera_1 = create_plant(plant_ids[2], "Monstera in green pot", "Monstera deliciosa", pot_size[1], watering_method[0], "Water when the top 2–3 inches of soil are dry", living_room)

fiddle_leaf = create_plant(plant_ids[3], "Fiddle leaf fig in white pot", "Ficus lyrata", pot_size[1], watering_method[0], "Water when the top 2–3 inches of soil are dry", living_room)

poinsettia = create_plant(plant_ids[4], "Poinsettia (the Christmas plant) in white tin with blue art", "Euphorbia pulcherrima", pot_size[0], watering_method[0], "Water when the top inch of soil feels dry", living_room)

polka_dot_begonia = create_plant(plant_ids[5], "Polka dot begonia in plastic orange pot", "Begonia maculata", pot_size[0], watering_method[1], "keep soil consistently moist but not waterlogged", living_room)

oxalis_triangularis_1 = create_plant(plant_ids[6], "Oxalis triangularis (the butterfly plant) in orange clay pot", "Oxalis triangularis", pot_size[0], watering_method[1], "Water when the top inch of soil is dry; reduce significantly during dormancy", living_room)

oxalis_triangularis_2 = create_plant(plant_ids[7], "Oxalis triangularis (the butterfly plant) in red pot", "Oxalis triangularis", pot_size[0], watering_method[1], "Water when the top inch of soil is dry; reduce significantly during dormancy", living_room)

orchid = create_plant(plant_ids[8], "Orchid in white pot", "Phalaenopsis", pot_size[0], watering_method[1], "Soak when potting medium is dry and roots turn silvery-gray; avoid water in crown", living_room)

boston_fern = create_plant(plant_ids[9], "Boston fern in funky white pinecone pot", "Nephrolepis exaltata", pot_size[1], watering_method[1], "keep soil consistently moist but not waterlogged", living_room)

pothos_plant = create_plant(plant_ids[10], "Pothos (Devil's Ivy) in the white pot on the wooden bookshelf", "Epipremnum aureum", pot_size[0], watering_method[0], "Water when the top 1–2 inches of soil are dry", living_room)

spider_plant = create_plant(plant_ids[11], "Spider plant in little orange plastic pot on the bookshelf", "Chlorophytum comosum", pot_size[0], watering_method[1], "Water when the top 1–2 inches of soil are dry", living_room)

# x = create_plant(plant_ids[3], "nickname", "latin name", pot_size[n], watering_method[n], "watering note", room)

# --------------------------------------

living_room_plants = [basil_1, basil_2, monstera_1, fiddle_leaf, poinsettia, polka_dot_begonia, oxalis_triangularis_1, oxalis_triangularis_2, orchid, boston_fern, pothos_plant, spider_plant]