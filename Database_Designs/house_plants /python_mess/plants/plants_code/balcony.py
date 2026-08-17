# --------------------------------------

# BALCONY PLANTS

# -------------------------------------




from .plant_maker_function.create_plant import create_plant




# --------------------------------------

# Details
pot_size = ['small', 'medium', 'large']
watering_method = ['top', 'bottom', 'misting']

# Rooms
# living_room = 1
# stairs = 2
# upstairs_bedroom = 3
balcony = 4
# basaks_old_room = 5
# sonias_old_room = 6

# id
plant_ids = list(range(1, 100))

# --------------------------------------



# UPSTAIRS BEDROOM PLANTS

basil_1 = create_plant(plant_ids[18], "Basil in orange clay pot", "Ocimum basilicum", pot_size[0], watering_method[1], "keep soil consistently moist but not waterlogged", balcony)

basil_2 = create_plant(plant_ids[19], "Basil in grey plastic pot", "Ocimum basilicum", pot_size[0], watering_method[1], "keep soil consistently moist but not waterlogged", balcony)

wisteria = create_plant(plant_ids[20], "Wisteria in the giant blue pot", "Wisteria sinensis", pot_size[2], watering_method[0], "Water deeply when the top 1–2 inches are dry; keep consistently moist during hot summer days", balcony)

bowles_mauve = create_plant(plant_ids[21], "Bowles' Mauve in the short but wide orange clay pot", "Erysimum linifolium", pot_size[1], watering_method[0], "Water when the top 1–2 inches of soil are dry (ensure sharp drainage)", balcony)

thyme = create_plant(plant_ids[22], "Thyme in the metal funky pot thing", "Thymus vulgaris", pot_size[0], watering_method[0], "Water when the top 1–2 inches of soil are dry (ensure sharp drainage and avoid soggy roots)", balcony)

marjoram = create_plant(plant_ids[23], "Marjoram in the small orange clay pot", "Origanum majorana", pot_size[0], watering_method[0], "Water when the top 1 inch of soil is dry (ensure sharp drainage)", balcony)

geranium_1 = create_plant(plant_ids[24], "Geranium in the red plastic pot", "Pelargonium hortorum", pot_size[1], watering_method[0], "Water when the top 1–2 inches of soil are dry (water soil directly, avoid wetting foliage)", balcony)

canna_lily = create_plant(plant_ids[25], "Canna Lily in the medium-large grey pot", "Canna indica", pot_size[1], watering_method[0], "Water deeply when the top 1–2 inches are dry; keep consistently moist during hot summer days", balcony)

blue_potato_bush = create_plant(plant_ids[26], "Blue Potato Bush in the plastic orange pot", "Lycianthes rantonnetii", pot_size[0], watering_method[0], "Water when the top 1–2 inches of soil are dry (ensure sharp drainage)", balcony)


camellia = create_plant(plant_ids[27], "Camelia in the large orange clay pot that is shaped like a flower", "Camellia japonica", pot_size[2], watering_method[0], "Keep soil evenly moist; water deeply when the top 1 inch feels dry", balcony)

lavender = create_plant(plant_ids[28], "Lavender in the small orange clay pot", "Lavandula angustifolia", pot_size[0], watering_method[0], "Allow top 2 inches (or most of the pot) to dry out between deep waterings", balcony)

halcyon_hosta_1 = create_plant(plant_ids[29], "Halcyon hosta in plastic grey pot", "Hosta Halcyon", pot_size[1], watering_method[0], "Keep soil consistently moist but well-drained; water at the base to protect blue leaf wax", balcony)

halcyon_hosta_2 = create_plant(plant_ids[30], "Halcyon hosta in plastic orange pot", "Hosta Halcyon", pot_size[1], watering_method[0], "Keep soil consistently moist but well-drained; water at the base to protect blue leaf wax", balcony)

halcyon_hosta_3 = create_plant(plant_ids[31], "Halcyon hosta in plastic orange pot", "Hosta Halcyon", pot_size[1], watering_method[0], "Keep soil consistently moist but well-drained; water at the base to protect blue leaf wax", balcony)

fern_1 = create_plant(plant_ids[32], "Fern in the plastic grey pot", "Dryopteris filix-mas", pot_size[1], watering_method[0], "Keep soil consistently moist and humus-rich; water at the base around the edge to avoid the crown", balcony)

fern_2 = create_plant(plant_ids[33], "Fern in the plastic grey pot", "Dryopteris filix-mas", pot_size[1], watering_method[0], "Keep soil consistently moist and humus-rich; water at the base around the edge to avoid the crown", balcony)

# small plastic orange pot
ivy = create_plant(plant_ids[34], "Ivy in the small orange plastic pot", "Hedera helix", pot_size[0], watering_method[0], "Water thoroughly when the top inch of soil is dry; ensure sharp drainage and avoid soggy roots", balcony)

geranium_2 = create_plant(plant_ids[35], "Geranium in the small grey plastic pot", "Pelargonium hortorum", pot_size[0], watering_method[0], "Water when the top 1–2 inches of soil are dry (water soil directly, avoid wetting foliage)", balcony)

# x = create_plant(plant_ids[3], "nickname", "latin name", pot_size[n], watering_method[n], "watering note", room)

# --------------------------------------

balcony_plants = [basil_1, basil_2, wisteria, bowles_mauve, thyme, marjoram, geranium_1, canna_lily, blue_potato_bush, camellia, lavender, halcyon_hosta_1, halcyon_hosta_2, halcyon_hosta_3, fern_1, fern_2, ivy, geranium_2]