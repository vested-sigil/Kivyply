import random


genders_list = ["Male", "Female"]
age_groups_list = ["Adult", "Mature", "Elder"]
clothing_styles_list = ["Casual", "Formal", "Business", "Sporty", "Bohemian", "Gothic", "Vintage", "Hipster", "Preppy", "Streetwear", "Retro", "Eclectic"]
ethnicities_list = ["Caucasian", "African American", "Asian", "Hispanic", "Native American", "Middle Eastern", "Mixed", "Pacific Islander", "South Asian"]
occupations_list = ["Doctor", "Engineer", "Teacher", "Artist", "Musician", "Writer", "Lawyer", "Police Officer", "Firefighter", "Pilot", "Psychologist", "Nurse", "Banker", "Software Developer", "Entrepreneur", "Chef", "Architect", "Journalist", "Fashion Designer", "Veterinarian", "Astronaut", "Actor", "Athlete"]
hair_colors_list = ["Black", "Brown", "Blonde", "Red", "Brunette", "Gray", "White", "Bald", "Silver", "Blue", "Purple", "Green", "Pink"]
boy_hairstyles_list = ["Short", "Medium", "Long", "Curly", "Wavy", "Straight", "Buzz Cut", "Mohawk", "Pompadour", "Dreadlocks", "Bald", "Afro", "Shaved", "Bun", "Spiky"]
girl_hairstyles_list = ["Long Straight", "Long Wavy", "Long Curly", "Medium Straight", "Medium Wavy", "Medium Curly", "Short Straight", "Short Wavy", "Short Curly", "Pixie Cut", "Braids", "Ponytail", "Bob", "Top Knot", "Messy Bun", "Fishtail Braid", "Cornrows", "French Twist", "Layered", "Shaggy"]
eye_colors_list = ["Brown", "Blue", "Green", "Hazel", "Gray", "Amber", "Violet", "Teal", "Heterochromia"]
skin_tones_list = ["Light", "Fair", "Medium", "Olive", "Dark", "Ebony", "Pale", "Bronze"]
body_types_list = ["Slim", "Athletic", "Curvy", "Muscular", "Stocky", "Petite", "Tall", "Average", "Plus Size", "Bodybuilder"]

import random



def select_attribute(attribute_name, options):
    print(f"Select {attribute_name}:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    choice = int(input("Enter your choice (number): "))
    return options[choice - 1]

def build_character():
    character = {
        "Gender": select_attribute("Gender", genders_list),
        "Age Group": select_attribute("Age Group", age_groups_list),
        "Clothing Style": select_attribute("Clothing Style", clothing_styles_list),
        "Ethnicity": select_attribute("Ethnicity", ethnicities_list),
        "Occupation": select_attribute("Occupation", occupations_list),
        "Hair Color": select_attribute("Hair Color", hair_colors_list),
        "Eye Color": select_attribute("Eye Color", eye_colors_list),
        "Skin Tone": select_attribute("Skin Tone", skin_tones_list),
        "Body Type": select_attribute("Body Type", body_types_list),
    }

    if character["Gender"] == "Male":
        character["Hairstyle"] = select_attribute("Hairstyle", boy_hairstyles_list)
    else:
        character["Hairstyle"] = select_attribute("Hairstyle", girl_hairstyles_list)

    return character

custom_character = build_character()
print(custom_character)
def generate_character():
    character = {
        "Gender": random.choice(genders_list),
        "Age Group": random.choice(age_groups_list),
        "Clothing Style": random.choice(clothing_styles_list),
        "Ethnicity": random.choice(ethnicities_list),
        "Occupation": random.choice(occupations_list),
        "Hair Color": random.choice(hair_colors_list),
        "Eye Color": random.choice(eye_colors_list),
        "Skin Tone": random.choice(skin_tones_list),
        "Body Type": random.choice(body_types_list),
    }

    if character["Gender"] == "Male":
        character["Hairstyle"] = random.choice(boy_hairstyles_list)
    else:
        character["Hairstyle"] = random.choice(girl_hairstyles_list)

    return character

action_phrases = [
   "{action_verb} {action_flavor}",
   "{action_verb} with a sense of {emotion}",
   "{action_verb} while {action_flavor}",
   "{action_verb} in a {setting}"
]
subject_phrases = [
   "A {char_type} with {char_disc}, located in {location_disc}",
   "A {char_type} with a {clothing_style} clothing style, wearing a {hairstyle} hairstyle",
   "A {char_type} with {hair_color} hair, {eye_color} eyes, and {skin_tone} skin",
   "A {char_type} with a {body_type} body type, located in {location_disc}"
]
desc_templates = [
    "A {age_group} {ethnicity} {gender} with {hair_color} hair styled in a {hairstyle}, {eye_color} eyes, and {skin_tone} skin, dressed in {clothing_style} clothes as a {occupation}.",
    "This {gender} {ethnicity} {age_group}, sporting a {hairstyle} hairstyle and {eye_color} eyes, is clad in {clothing_style} attire, showcasing their role as a {occupation}.",
    "Dressed in {clothing_style} fashion, the {age_group} {gender} {ethnicity} with {hair_color} hair in a {hairstyle} cut, and deep {eye_color} eyes, stands out as a {occupation}.",
    "In {clothing_style} wear, a {gender} {ethnicity} {age_group} with {hairstyle} {hair_color} hair and {eye_color} eyes represents the quintessence of a {occupation}.",
    "The {age_group} {ethnicity} {gender}, with their {hair_color} hair done in a {hairstyle} and {eye_color} eyes, dressed in {clothing_style} garb, perfectly embodies a {occupation}.",
    "A {ethnicity} {gender} in the {age_group} category, with {hair_color} hair styled as a {hairstyle} and striking {eye_color} eyes, dressed in {clothing_style} outfits, is the epitome of a {occupation}.",
    "Clad in {clothing_style} attire, the {gender} {ethnicity} {age_group} with a {hairstyle} of {hair_color} hair and {eye_color} eyes, exudes the charisma of a {occupation}.",
    "The {age_group} {gender} {ethnicity}, with {hair_color} hair arranged in a {hairstyle} and eyes of {eye_color}, dressed in the distinct {clothing_style} style, captures the essence of being a {occupation}.",
    "Adorned in {clothing_style} fashion, a {gender} {ethnicity} {age_group} with {hair_color} {hairstyle} hair and captivating {eye_color} eyes, personifies a true {occupation}.",
    "Gleaming with {eye_color} eyes, a {gender} {ethnicity} {age_group} with {hairstyle} {hair_color} hair, donning {clothing_style} apparel, epitomizes the life of a {occupation}.",
    "A {gender} {ethnicity} {age_group}, with a unique {hairstyle} of {hair_color} hair and {eye_color} eyes, decked in {clothing_style} attire, lives the role of a {occupation}.",
    "Emanating grace, the {age_group} {gender} {ethnicity} with {hair_color} hair in a {hairstyle} style and {eye_color} eyes, dressed in {clothing_style}, is a natural {occupation}.",
    "In the attire of a {occupation}, a {gender} {ethnicity} {age_group} with {hairstyle} {hair_color} hair and {eye_color} eyes becomes a symbol of {clothing_style} elegance.",
    "A {ethnicity} {gender} of {age_group} age, with {hair_color} hair in a {hairstyle} and {eye_color} eyes, draped in {clothing_style} attire, channels the spirit of a {occupation}.",
    # Feel free to add more templates for even greater variety
]

clothing_styles_dict = {
    "Men's": {
        "Casual": ["Jeans and T-shirt", "Shorts and polo shirt", "Sweatpants and hoodie"],
        "Formal": ["Business suit", "Tuxedo", "Dress shirt and slacks"],
        "Sporty": ["Athletic shorts and sports jersey", "Running leggings and tank top", "Track pants and athletic shirt"],
        "Business Casual": ["Chinos and button-down shirt", "Blazer and khakis", "Loafers and dress shirt"],
        "Outdoor": ["Hiking boots and cargo pants", "Camouflage jacket and cap", "Raincoat and hiking shorts"],
        "Hip Hop": ["Baggy jeans and oversized hoodie", "Basketball jersey and sneakers", "Snapback cap and chains"],
        "Punk": ["Leather jacket and ripped jeans", "Band T-shirt and combat boots", "Spiked accessories"],
        "Smart Casual": ["Khaki pants and V-neck sweater", "Loafers and dress shirt", "Tweed jacket and jeans"],
        "Preppy": ["Polo shirt and khakis", "Cable knit sweater and skirt", "Blazer and oxford shoes"],
        "Retro": ["Bell-bottom pants and disco shirt", "Mini skirt and go-go boots", "Flared jeans and tie-dye shirt"],
        "Military": ["Camouflage pants and combat boots", "Utility jacket and tactical vest", "Beret and dog tags"],
        "Cruise": ["Linen shirt and shorts", "Hawaiian print shirt and flip-flops", "Straw hat and sunglasses"],
    },
    "Women's": {
        "Casual": ["Jeans and T-shirt", "Shorts and tank top", "Sundress", "Sweatpants and hoodie"],
        "Formal": ["Evening gown", "Cocktail dress", "Pencil skirt and blouse"],
        "Sporty": ["Athletic shorts and sports bra", "Running leggings and workout tank", "Yoga pants and athletic top"],
        "Bohemian": ["Maxi dress", "Flowy skirt and blouse", "Boho-chic attire"],
        "Beachwear": ["Swimsuit and cover-up", "Beach dress", "Straw hat and flip-flops"],
        "Vintage": ["Retro dress and petticoat", "High-waisted trousers and suspenders", "Floral tea dress"],
        "Business Professional": ["Pant suit and blouse", "Sheath dress and heels", "Pearl accessories"],
        "Gothic": ["Black lace dress and choker", "Corset and leather skirt", "Fishnet stockings and platform boots"],
        "Streetwear": ["Graphic hoodie and joggers", "Sneakers and snapback cap", "Denim jacket and distressed jeans"],
        "Classic": ["A-line dress and pearls", "Trench coat and pencil skirt", "Pumps and tailored blazer"],
        "Festival": ["Boho crop top and shorts", "Fringe vest and flower crown", "Glitter makeup and boots"],
        "Corporate": ["Power suit and briefcase", "Pencil skirt and silk blouse", "Stiletto heels and statement jewelry"],
    }
}
def create_character_description(character_dict):
    # Select a description template
    desc_template = random.choice(desc_templates)

    # Fill the template with the provided character attributes
    description = desc_template.format(
        gender=character_dict.get("Gender", "Unknown"),
        age_group=character_dict.get("Age Group", "Unknown"),
        clothing_style=character_dict.get("Clothing Style", "Unknown"),
        ethnicity=character_dict.get("Ethnicity", "Unknown"),
        occupation=character_dict.get("Occupation", "Unknown"),
        hair_color=character_dict.get("Hair Color", "Unknown"),
        hairstyle=character_dict.get("Hairstyle", "Unknown"),
        eye_color=character_dict.get("Eye Color", "Unknown"),
        skin_tone=character_dict.get("Skin Tone", "Unknown")
    )

    return description

