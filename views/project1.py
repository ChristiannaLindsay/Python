import streamlit as st
#import numpy as np
import pandas as pd
#import matplotlib
#import matplotlib.pyplot as plt
#import streamlit.components.v1 as components

st.title("Nutritious Foods Tool", anchor=False)

st.write("Python Code for this project: https://github.com/ChristiannaLindsay/Nutrition_Tool")


# Project overview
st.write(
    """
As someone who has always been interested in nutrition, I built a simple tool to help
visualize what foods are highest in certain nutrients. I want someone to be able to choose what
macronutrient, micronutrient, or mineral they are interested in (e.g. protein, magnesium, etc.),
and learn what foods contain the highest densities of that nutrient.
I am only
interested in raw, whole (single-ingredient) foods, rather than processed, prepared, or fortified foods.
All code for this project can be found on my GitHub.
"""
)

# Data set description
st.subheader("Data Set Description", anchor=False)
st.write(
    """
    I am using the
    "FNDDS Nutrient Values.xlsx" data from the United States Department of Agriculture's Food and
    Nutrient Database for Dietary Studies (https://www.ars.usda.gov/northeast-area/beltsville-md-bhnrc/beltsville-human-nutrition-research-center/food-surveys-research-group/docs/fndds-download-databases/).
    This dataset contains micronutrient and macronutrient amounts per 100g of various foods,
    including whole foods
    (e.g. carrots), generic foods (e.g. chocolate milk), and branded items (e.g. Kellogg cereal).
    Each food is identified by a unique eight-digit 'Food code' and is also described by 
    a 'Main food description' a WWEIA Category Description,
    and a four-digit 'WWEIA Category number.'
    This is what the dataset looks like:
"""
)

nutrients = pd.read_csv("./assets/FNDDS Nutrient Values.csv", skiprows=[0])
st.dataframe(nutrients)

# Data cleaning
st.subheader("Data Cleaning", anchor=False)


st.markdown("""
<style>
.big-font {font-size:20px !important;}
</style>
""", unsafe_allow_html=True)
st.markdown('<p class="big-font">Remove Unwanted Entries</p>', unsafe_allow_html=True)


st.write(
    """
    The main data cleaning task is to remove the unwanted foods
    from the original list of 5624 items.
    I will use three steps to remove the unwanted food items.

    1. Use the first two digits of the WWEIA Category number
    to remove the following food categories:
    
    - Milk desserts and sauces = 13
    - Frozen meals, soups, gravies = 28
    - Egg mixture = 32 
    - Egg substitutes = 33 
    - Yeast breads, rolls = 51 
    - Quick breads = 52 
    - Cakes, cookies, pies, pastries, bars = 53 
    - Crackers, snack products = 54 
    - Pancakes, waffles, French toast, other grain products = 55 
    - Grain mixtures, frozen meals, soups = 58 
    - Meat substitutes = 59 
    - Fruits and juices baby food = 67 
    - Vegetables with meat, poultry, fish = 77 
    - Mixtures mostly vegetables without meat, poultry, fish = 78 
    - Salad dressings = 83 
    - 'For use' with a sandwich or vegetable = 89 
    - Formulated nutrition beverages, energy drinks, sports drinks = 95 

    2. Remove foods with a WWEIA Category description containing certain words
    (e.g. 'sandwich', 'fried', 'Formula').

    3. Remove the remaining unwanted items based on their Main food description.
    """
    )

st.markdown("""
<style>
.big-font {font-size:20px !important;}
</style>
""", unsafe_allow_html=True)
st.markdown('<p class="big-font">Calculate Nutrient %DV</p>', unsafe_allow_html=True)

st.write("""
    We also want to calculate the Percent Daily Value (%DV),
    which is the percentage of the recommended Daily Value for each nutrient in a serving of food.
    The FDA's website is used as a reference for the %DV's (https://www.fda.gov/food/nutrition-facts-label/daily-value-nutrition-and-supplement-facts-labels).
    Note that some nutrients do not have defined Daily Values.

    Here is what the cleaned data set looks like. With the extraneous items removed, the data set is reduced from 5624 entries to 269 entries.
     """)

### Clean data

## Fix column names
newcols = []
for col in nutrients.columns:
    splitcol = col.split("\n")
    cleancol = " ".join(splitcol)
    newcols.append(cleancol)
nutrients.columns = newcols

## Remove items
drop_indices = []
for i in range(nutrients.shape[0]): #row indices
    
    code = nutrients["Food code"][i] #Food code
    cat = nutrients["WWEIA Category description"][i] #Food category
    des = nutrients["Main food description"][i]
    
    #Remove items based on food code
    if int(str(code)[:2]) in [13,28,32,33,51,52,53,54,55,58,59,67,77,78,83,89,95]:
        drop_indices.append(i)
    
    #Remove items based on Food category
    elif "substitutes" in cat or "sauces" in cat or "desserts" in cat:
        drop_indices.append(i)
    elif "Smoothies" in cat or "Formula" in cat or "Flavored" in cat:
        drop_indices.append(i)
    elif "shakes" in cat or "Pizza" in cat or "sandwich" in cat:
        drop_indices.append(i)
    elif "Baby" in cat or "Mix" in cat or "mix" in cat:
        drop_indices.append(i)
    elif "patties" in cat or "dinner" in cat or "sauce" in cat:
        drop_indices.append(i)
    elif "Burger" in cat or "Soup" in cat or "Processed" in cat:
        drop_indices.append(i)
    elif "Fried" in cat or "chip" in cat or "condiment" in cat:
        drop_indices.append(i) 
    elif "combination" in cat or "juice" in cat or "Margarine" in cat:
        drop_indices.append(i)
    elif "dressing" in cat or "topping" in cat or "sorbet" in cat:
        drop_indices.append(i)
    elif "Candy" in cat or "soft drink" in cat or "diet" in cat:
        drop_indices.append(i)
    elif "fried" in cat or "baked" in cat or "Pudding" in cat:
        drop_indices.append(i)
    elif "Liquor" in cat or "Wine" in cat or "Beer" in cat:
        drop_indices.append(i)    
    elif "Soft drinks" in cat or "Pickle" in cat or "pickle" in cat:
        drop_indices.append(i)
    elif "dish" in cat or "Dried fruit" in cat or "Pasta" in cat:
        drop_indices.append(i)
    elif "Cracker" in cat or "cured" in cat or "Sausages" in cat:
        drop_indices.append(i)
    elif "Coleslaw" in cat or "Fruit drinks" in cat or "creamed" in cat:
        drop_indices.append(i)
    elif "Oatmeal" in cat or "cereal" in cat or "Frankfurter" in cat:
        drop_indices.append(i)
        
    #Remove items based on Main food description
    elif "reconstituted" in des or "evaporated" in des or "flavor" in des or "parfait" in des:
        drop_indices.append(i)
    elif "imitation" in des or "topping" in des or "sugar free" in des or "beverage" in des:
        drop_indices.append(i)     
    elif "blend" in des or "lowfat" in des or "reduced" in des or "fat free" in des:
        drop_indices.append(i)
    elif "low fat" in des or "light" in des or "spread" in des or "dessert" in des:
        drop_indices.append(i)
    elif "processed" in des or "with" in des or "pressurized" in des or "Imitation" in des:
        drop_indices.append(i)
    elif "pickled" in des or "baked" in des or "nonfat" in des or "NS as to" in des:
        drop_indices.append(i)
    elif "roasted" in des or "rotisserie" in des or "stewed" in des or "fried" in des:
        drop_indices.append(i)
    elif "grilled" in des or "Spam" in des or "packaged" in des or "cooked" in des:
        drop_indices.append(i)
    elif "steamed" in des or "smoked" in des or "cooked" in des or "mixed" in des:
        drop_indices.append(i)
    elif "fat added" in des or "pie" in des or "no meat" in des or "stew" in des:
        drop_indices.append(i)
    elif "pasta" in des or "Pasta" in des or "lower" in des or "fortified" in des:
        drop_indices.append(i)
    elif "juice" in des or "syrup" in des or "Cereal" in des or "Cream of" in des:
        drop_indices.append(i)
    elif "Sauce" in des or "ingredient" in des or "enhanced" in des or "diet" in des:
        drop_indices.append(i)
    elif "Wine" in des or "drink" in des or "mix" in des or "instant" in des:
        drop_indices.append(i)
    elif "Iced" in des or "Cappuccino" in des or "cafe " in des or "sauce" in des:
        drop_indices.append(i)
    elif "tub" in des or "drippings" in des or "Fritter" in des or "Stuffed " in des:
        drop_indices.append(i)
    elif "creamed" in des or "bottled" in des or "bubble" in des or "substitute" in des:
        drop_indices.append(i)
    elif "Latte" in des or "Mocha" in des or "brew" in des or "powder" in des:
        drop_indices.append(i)
    elif "macchiato" in des or "Cuban" in des or "Sugar, cinnamon" in des or "confectioner" in des:
        drop_indices.append(i)      
    elif "Sun-dried" in des or "Mix" in des or "Table fat, NFS" in des or "Honey butter" in des:
        drop_indices.append(i)
    elif "chocolate" in des or "bread" in des or "boil" in des or "candied" in des:
        drop_indices.append(i)
    elif "Dal" in des or "jelly" in des or "Congee" in des or "cocktail" in des:
        drop_indices.append(i)
    elif "Bacon bits" in des or "restaurant" in des or "frank" in des or "Wasabi peas" in des:
        drop_indices.append(i)        
    elif "Shrimp scampi" in des or "vegetarian" in des or "baked" in des or "Baked" in des:
        drop_indices.append(i)
    elif "Fried" in des or "nugget" in des or "Duck, pressed, Chinese" in des or "pot roast" in des:
        drop_indices.append(i)
    elif "coated" in des or "cracklings" in des or "saute" in des or "other sources" in des:
        drop_indices.append(i) 
    elif "Soy nut" in des or "NFS" in des or "and" in des or "sandwich" in des:
        drop_indices.append(i)    
    elif "maraschino" in des or "Tahini" in des or " butter" in des or " salted" in des:
        drop_indices.append(i) 
    elif "canned" in des or "decaffeinated" in des or "from frozen" in des or "casserole" in des:
        drop_indices.append(i)       
    elif "Liver, paste or pate" in des or "Pork skin rinds" in des or "patty" in des or "Cream, whipped" in des:
        drop_indices.append(i) 
    elif "Fish, stick" in des or "white only" in des or "yolk only" in des or "Almond paste" in des:
        drop_indices.append(i)
    elif "salad" in des or "Broccoli raab" in des or "lactose free" in des or "Fufu" in des:
        drop_indices.append(i)  
    elif ", fruit" in des:
        drop_indices.append(i)

nutrients = nutrients.drop(drop_indices)

# Define PDV function
def PDV(amount, DV):
    return((amount/DV)*100)

# Define %DVs
nutrients['Protein PDV'] = PDV(amount=nutrients['Protein (g)'], DV=50)
nutrients['Carbohydrate PDV'] = PDV(amount=nutrients['Carbohydrate (g)'], DV=275)
nutrients['Total Fat PDV'] = PDV(amount=nutrients['Total Fat (g)'], DV=78)
nutrients['Cholesterol PDV'] = PDV(amount=nutrients['Cholesterol (mg)'], DV=300)
nutrients['Vitamin A, RAE PDV'] = PDV(amount=nutrients['Vitamin A, RAE (mcg_RAE)'], DV=900)
nutrients['Thiamin PDV'] = PDV(amount=nutrients['Thiamin (mg)'], DV=1.2)
nutrients['Riboflavin PDV'] = PDV(amount=nutrients['Riboflavin (mg)'], DV=1.3)
nutrients['Vitamin B-6 PDV'] = PDV(amount=nutrients['Vitamin B-6 (mg)'], DV=1.7)
nutrients['Folate, DFE PDV'] = PDV(amount=nutrients['Folate, DFE (mcg_DFE)'], DV=400)
nutrients['Choline, total PDV'] = PDV(amount=nutrients['Choline, total (mg)'], DV=550)
nutrients['Vitamin B-12 PDV'] = PDV(amount=nutrients['Vitamin B-12 (mcg)'], DV=2.4)
nutrients['Vitamin C PDV'] = PDV(amount=nutrients['Vitamin C (mg)'], DV=90)
nutrients['Vitamin D (D2 + D3) PDV'] = PDV(amount=nutrients['Vitamin D (D2 + D3) (mcg)'], DV=20)
nutrients['Vitamin E (alpha-tocopherol) PDV'] = PDV(amount=nutrients['Vitamin E (alpha-tocopherol) (mg)'], DV=15)
nutrients['Vitamin K (phylloquinone) PDV'] = PDV(amount=nutrients['Vitamin K (phylloquinone) (mcg)'], DV=120)
nutrients['Calcium PDV'] = PDV(amount=nutrients['Calcium (mg)'], DV=1300)
nutrients['Phosphorus PDV'] = PDV(amount=nutrients['Phosphorus (mg)'], DV=1250)
nutrients['Magnesium PDV'] = PDV(amount=nutrients['Magnesium (mg)'], DV=420)
nutrients['Iron PDV'] = PDV(amount=nutrients['Iron (mg)'], DV=18)
nutrients['Zinc PDV'] = PDV(amount=nutrients['Zinc (mg)'], DV=11)
nutrients['Copper PDV'] = PDV(amount=nutrients['Copper (mg)'], DV=0.9)
nutrients['Selenium PDV'] = PDV(amount=nutrients['Selenium (mcg)'], DV=55)
nutrients['Potassium PDV'] = PDV(amount=nutrients['Potassium (mg)'], DV=4700)
nutrients['Sodium PDV'] = PDV(amount=nutrients['Sodium (mg)'], DV=2300)

        
# Show cleaned data frame
st.dataframe(nutrients)

# Visualize data
st.subheader("Interactive Nutrient Tool", anchor=False)

st.write(
    """
    This tool is rather self-explanatory. If, for instance, one were trying to get
    more selenium in their diet, they would select "Selenium (mcg)" in the "Nutrient" dropdown,
    and choose the number of foods to show that are highest in selenium using the "Number of foods" dropdown. The bar chart 
    shows that Brazil nuts dwarf all other foods in selenium content with 1917 mcg per 100g.
    If one wanted to know the %DV of selenium that Brazil nuts provide, they could either use the
    interactive table to scroll to the "Selenium PDV" column or select "Selenium PDV" in the Nutrient dropdown to see
    that 100g of Brazil nuts provide 3,485% of the recommended Daily Value.
"""
)

just_nut = nutrients.drop(['Food code', 'WWEIA Category number', 'WWEIA Category description'],axis=1)

# Choose nutrient to plot top N foods for

nutrient_choice = st.selectbox("Nutrient:", just_nut.columns[1:])
N = st.number_input('Number of foods:', min_value=1, max_value=10, value=5, step=1)
topNfoods = just_nut.sort_values(nutrient_choice, ascending=False).iloc[:N]
st.dataframe(topNfoods)

st.bar_chart(topNfoods, x='Main food description', y=nutrient_choice, color='#d5b9d5')


