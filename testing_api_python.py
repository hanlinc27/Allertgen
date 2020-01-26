#https://devhints.io/xpath

from lxml import html
import requests

BASE_DIR = "https://www.foodnetwork.com/search/"
food_name = "curry"
search_query = BASE_DIR + food_name + "-"

search_recipes = requests.get(search_query)
# if (search_recipes.status_code == 200):
tree1 = html.fromstring(search_recipes.content)
first_recipe = tree1.xpath('//h3[@class="m-MediaBlock__a-Headline"]/a/@href')[0]
print(first_recipe)

recipe_response = requests.get("https:" + first_recipe)
tree2 = html.fromstring(recipe_response.content)
ingredients = tree2.xpath('//p[@class="o-Ingredients__a-Ingredient"]/text()')

print(ingredients)

parsed_ingredients = []

for item in ingredients:
    tmp = ''.join([i for i in item if (i.isalpha() or i==' ')])
    parsed_ingredients.append(tmp.replace(' cups', '').replace(' cup','').replace(' teaspoons', '').replace(' teaspoon', '')\
        .replace(' tablespoons','').replace(' tablespoon', '').replace(' plus', '').replace(' pinch of', '').replace(' pinch','')\
            .replace(' stick', '').replace(' for serving', '').replace())

print(parsed_ingredients)