class ClothingItem:
    def __init__(self, type, color, season, category, size, brand):
        self.type = type
        self.color = color
        self.season = season
        self.category = category 
        self.size = size
        self.brand = brand
      
      
    def __str__(self):
        return f"{self.color} {self.type} for {self.season} ({self.category}, by {self.brand})"

complementary_colors = {
    "red": "green",
    "orange": "blue",
    "green": "red",
    "blue": "orange",
    "purple": "yellow",
    "black": "white",
    "white": "black",
    "gray": "navy",
    "beige": "navy",
    "red": "navy",
    "pink": "navy",
    "blue": "green"
}

monochrome_colors = {
    "red": "red",
    "orange": "orange",
    "purple": "purple",
    "green": "green",
    "blue": "blue",
    "black": "black",
    "white": "white",
    "gray": "gray",
    "beige": "beige",
    "navy": "navy",
    "pink": "pink"
}

favorite_outfits = {
    "Green T-shirt": "green shorts",
    "Pink Pants": "Navy Shirt",
    "Beige Linen Shirt": "Navy Shorts",
    "Blue Linen Shirt": "Navy Shorts",
    "Khaki Shorts": "Sweater",
    "Orange Shirt": "Navy Shorts",
}

dress_up = [
    "Navy Suede Shoes and Brown Leather Watch", 
    "Brown Laofers and Brown Leather Watch", 
    "Burgundy Loafers and Brown Leather Watch"
]

dress_down = [
    "White Canvas Sneakers and White Watch", 
    "White Canvas Sneaker and Silver Watch", 
    "Black Timberland and Silver Watch", 
    "Black Timberland and White Watch"
]

wardrobe = [
    ClothingItem("Shirt", "Purple", "any", "Business Casual", "L", "Polo Ralph Lauren"),
    ClothingItem("Shirt", "Light Blue", "any", "Business casual", "L", "George"),
    ClothingItem("Shirt", "Beige", "Summer", "Summer Casual", "XL", "Old Navy"), 
    ClothingItem("Shirt", "Purple","any", "Business Casual", "L", "Banana Republic"), 
    ClothingItem("Pants", "Pink", "any", "Business Casual", "36 x 32", "J Crew"), 
    ClothingItem("Shorts", "Navy", "any", "Business Casual", "35", "J Crew"), 
    ClothingItem("Shirt", "Pink", "any", "Business Casual", "Large", "Polo Ralph Lauren"), 
    ClothingItem("T-Shirt", "White", "any", "Undershirt", "L Tall", "Old Navy"),
    ClothingItem("T-Shirt", "Gray", "any", "Undershirt", "L Tall", "Old Navy"),
    ClothingItem("T-Shirt", "Navy", "any", "Undershirt", "L Tall"," Old Navy"),
    ClothingItem("T-Shirt", "Blue", "any", "Undershirt", "L Tall", "Old Navy"),
    ClothingItem("T-Shirt", "Green", "any", "Undershirt", "L Tall"," Old Navy"),
    ClothingItem("T-Shirt", "Black", "any", "Undershirt", "L Tall", "Old Navy"),
    ClothingItem("T-Shirt", "Brown", "any", "Undershirt", "L Tall", "Old Navy"),
    ClothingItem("Shirt", "Red", "any", "Casual", "L", "American Eagle"), 
    ClothingItem("Shirt", "Greenish Blue", "any", "L", "Business Casual", "Banana Republic"),
    ClothingItem("Shirt", "Navy", "any", "Business Casual", "XL", "Banana Republic"),
    ClothingItem("Shirt", "Blueish Gray", "any", "Business Casual", "XL", "Banana Republic"),
    ClothingItem("Shirt", "Gray", "any", "Casual", "L", "American Eagle"),
    ClothingItem("Shirt", "Gray", "any", "Casual", "L", "Banana Republic"),
    ClothingItem("Shirt", "Olive Green", "any", "Casual", "L", "Croft and Barrow"),
    ClothingItem("Shirt", "Denim", "any", "Casual", "L", "Banana Republic"),
    ClothingItem("Shirt", "White", "any", "Business Casual", "L", "Stafford"),
    ClothingItem("Shirt", "Navy", "any", "Business Casual", "L", "George"),
    ClothingItem("Shirt", "Olive Green", "any", "Casual", "L", "Polo Ralph Lauren"),
    ClothingItem("Shirt", "Beige Linen", "any", "Summer Casual", "L", "Polo Ralph Lauren"),
]

print("LEGEND: *Unique Colors- Greenish Blue, Blueish Gray, Denim, Multi, Olive Green*\n")

print(favorite_outfits)

user_input = input("\nChoose a style: Business Casual, Summer Casual, Casual, Formal, Cold, Bold\n").lower()

matches = [item for item in wardrobe if item.category.lower() == user_input]

if matches:
    print("\nHere is a selection\n")
    for item in matches:
        print(item)

user_color = input("\nWould you like a particular color?\n").lower()


if user_color:
    print("\nHere is a a selection\n")
    color =[i for i in matches if i.color.lower() == user_color]
    for item in color:
        print(item)

outfit_suggest = input("\nWould you like a complementary or monochrome suggestion?\n").lower()

if outfit_suggest == "complementary":
    bottom_type = input("Would you like to match with pants or shorts?\n")
    complementary = complementary_colors.get(user_color)
    print(f"\nLooking for {bottom_type} in a complementary color: {complementary}")
    suggestions = [item for item in wardrobe if item.type.lower() == bottom_type.lower() and item.color.lower() == complementary]
    for item in suggestions:
        print(item)

elif outfit_suggest == "monochrome":
    bottom_type = input("Would you like to match with pants or shorts?\n")
    monochrome = monochrome_colors.get(user_color)
    print(f"\nLooking for {bottom_type} in a monochrome color: {monochrome}")
    suggestions = [item for item in wardrobe if item.type.lower() == bottom_type.lower() and item.color.lower() == monochrome]
    for item in suggestions:
     print(item)

elevate = input("\nWould you like to dress up or dress down this outfit?\n")

if elevate == "dress down":
    relax = [item for item in dress_down]
    for item in relax:
        print(item)

if elevate == "dress up":
    formal = [item for item in dress_up]
    for item in formal:
        print(item)