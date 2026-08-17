# --------------------------------------

# PLANTS MAKER FUNCTION

# --------------------------------------

def create_plant(id, nickname, species, pot_size, watering_method, watering_instructions, room_id):
    values = [id, nickname, species, pot_size, watering_method, watering_instructions, room_id]
    formatted = []
    
    for val in values:
        if isinstance(val, str):
            # Escape internal single quotes for SQL (e.g. "it's" -> 'it''s')
            escaped = val.replace("'", "''")
            formatted.append(f"'{escaped}'")
        elif val is None:
            formatted.append("NULL")
        else:
            formatted.append(str(val))
            
    return f"({', '.join(formatted)})"
