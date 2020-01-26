#https://devhints.io/xpath

from lxml import html
import requests

measures = [' cups ', 'cup ', ' teaspoons ', ' teaspoon ', ' tablespoons ', 'tablespoon ', ' plus ',\
    ' pinch ', ' stick ', ' for serving', ' ounces ', ' ounce ', ' stalk', ' for topping', 'Finely grated zest ', ' of ',\
    'can ', ' pounds ', ' pound ', 'chopped', 'chopped ', 'halved', 'cooked ', ' to ', ' for frying', ' minced'\
    'minced ', 'diced ', 'diced', ' smashed', ' for oiling the grill grates', 'small', 'lower', 'juiced'\
    , ' zested ', 'shredded ', ' shredded', 'handful']

img_predict = "food" ###TODO: this needs to set as the response from Google Cloud
if (img_predict == "pad_thai"):
    food_name = "pad-thai"
else:
    food_name = img_predict

BASE_DIR = "https://www.foodnetwork.com/search/"
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
    tmp = ''.join([i for i in item if (i.isalpha() or i==' ')]).lower()
    for m in measures:
        tmp = tmp.replace(m, '')
    parsed_ingredients.append(tmp)

print(parsed_ingredients)