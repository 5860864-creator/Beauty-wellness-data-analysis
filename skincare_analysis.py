# Skincare Product Data Analysis
# Week 1 - Beauty and Wellness Internship

products = [
    {"name": "Gentle Cleanser", "category": "Cleanser", "price": 250, "rating": 4.2},
    {"name": "Hydrating Cleanser", "category": "Cleanser", "price": 300, "rating": 4.5},
    {"name": "Daily Moisturizer", "category": "Moisturizer", "price": 400, "rating": 4.4},
    {"name": "Light Moisturizer", "category": "Moisturizer", "price": 350, "rating": 4.1},
    {"name": "Daily Sunscreen", "category": "Sunscreen", "price": 500, "rating": 4.7},
    {"name": "Matte Sunscreen", "category": "Sunscreen", "price": 450, "rating": 4.3}
]

print("SKINCARE PRODUCT DATA ANALYSIS")
print("-" * 35)

# Display all products
for product in products:
    print(product["name"], "-", product["rating"], "stars")

# Calculate average rating for each category
categories = {}

for product in products:
    category = product["category"]

    if category not in categories:
        categories[category] = []

    categories[category].append(product["rating"])

print("\nAverage Rating by Category:")

for category, ratings in categories.items():
    average = sum(ratings) / len(ratings)
    print(category, ":", round(average, 2), "stars")

# Find the highest-rated product
best_product = max(products, key=lambda product: product["rating"])

print("\nHighest-Rated Product:")
print(best_product["name"], "-", best_product["rating"], "stars")

print("\nNote: This project uses sample data for demonstration.")
