import pandas as pd

def big_countries(world):
    population_df = pd.DataFrame(world[(world["population"] >= 25000000) | (world["area"] >= 3000000)])
    print(population_df.loc[:, ["name", "population", "area"]])

# alternate function which is better in both time and space complexity
def big_countries(world):
    return world[(world["population"] >= 25000000) | (world["area"] >= 3000000)][["name", "population", "area"]]

data = [['Afghanistan', 'Asia', 652230, 25500100, 20343000000], ['Albania', 'Europe', 28748, 2831741, 12960000000], ['Algeria', 'Africa', 2381741, 37100000, 188681000000], ['Andorra', 'Europe', 468, 78115, 3712000000], ['Angola', 'Africa', 1246700, 20609294, 100990000000]]
World = pd.DataFrame(data, columns=['name', 'continent', 'area', 'population', 'gdp']).astype({'name':'object', 'continent':'object', 'area':'Int64', 'population':'Int64', 'gdp':'Int64'})
big_countries(World)