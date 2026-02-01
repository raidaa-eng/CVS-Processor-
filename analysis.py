import numpy as np

def get_subregions_data(country_data):

    """
    Creates a list of unique subregions from given country data.

    Parameters: 
        country_data (list): A list of country records read from the country data CSV file. 

    Returns:
        list: A list of unique sub-region names.
    """
    subregions = [] 

    for row in country_data:
        sub_region = row[2]
        if sub_region not in subregions:
            subregions.append(sub_region)
    return subregions
    
def get_subregion(country_data): 

    """
    Displays numbered list of UN sub-regions and prompts user to select one.

    Parameters: 
        country_data (list): A list of country records. 

    Returns:
        str: The name of selected UN sub-region.
    """
    subregions = get_subregions_data(country_data)

    while True:
        print("Available UN Sub Regions:")

        for i in range(len(subregions)):
            print(f"{i+1}. {subregions[i]}")

        user_choice = input("Enter sub-region number: ")

        if user_choice.isdigit():
            index = int(user_choice) - 1
            
            if 0 <= index < len(subregions):
                return subregions[index]

        print("Input invalid. Please try again.")

def get_countries_in_subregion(country_data, chosen_subregion):

    """
    Filters country data to include only countries within selected sub-region.

    Parameters: 
        country_data (list): A list of country records read from the country data CSV file. 
        subregion (str): The user-selected UN sub-region.

    Returns:
        list: A list of unique country records belonging to selected sub-region.
    """
    countries = []

    for row in country_data:
        if row[2] == chosen_subregion:
            countries.append(row)
    return countries

def get_countries(countries_in_subregion):

    """
    Displays numbered list of countries in sub-region and prompts user to select one.

    Parameters: 
        countries_in_subregion (list): A list of country records in selected sub-region.

    Returns:
        list: The selected country's data record.
    """
    while True:
        print("Countries in selected sub-region:")

        for i in range(len(countries_in_subregion)):
            print(f"{i+1}. {countries_in_subregion[i][0]}")

        user_choice = input("Enter country number: ")

        if user_choice.isdigit():
            index = int(user_choice) - 1
            
            if 0 <= index < len(countries_in_subregion):
                return countries_in_subregion[index]

        print("Input invalid. Please try again.")
        
def get_population(pop_data, country_name):

    """
    Searches for population data corresponding to selected country.

    Parameters: 
        population_data (list): Population data read from the population data CSV file.
        country_name (str): The name of the user-selected country. 

    Returns:
        list or None: The population data row for the selected country, or None if no data is found.
    """
    for row in pop_data:
        if row[0] == country_name:
            return row
    return None

def population_stats(pop_row):

    """
    Calculates population change and average population between 2000 and 2020.

    Parameters: 
        pop_row (list): A population data row for selected country.

    Returns:
        float: Population change and average population.
    """
    populations = np.array(pop_row[1:], dtype=float) #describe 
    change = populations[0] - populations[-1]
    average = np.mean(populations)

    return change, average 

def population_density(recent_pop, area):

    """
    Calculates population density for 2020 in the selected country.

    Parameters: 
        recent_pop (float): The population value in 2020 in select country.
        area (float): Land area of country in square kilometers.

    Returns:
        float: Population density (people per square kilometer).
    """
    return recent_pop/area

def species_stats(species_data, countries_in_subregion):

    """
    Calculates average and total number of threatened species for each country in selected sub-region.

    Parameters: 
        species_data (list): Threatened species data from the threatened species CSV file.
        countries_in_subregion (list): Countries belonging to the selected subregion.

    Returns:
        list: A list containing country name, average threatened species, and total threatened species. 
    """
    results = []

    for country_row in countries_in_subregion:
        country = country_row[0]

        for row in species_data[1:]:
            if row[0] == country:
                values = np.array(row[1:], dtype = float)

                avg = np.mean(values)
                total = np.sum(values)

                results.append([country, avg, total]) 
                break
    return results

def species_per_area(total_species, area):
    """
    Calculates threatened species per square kilometer in each country within selected subregion.

    Parameters: 
        total_species (float): The total number of threatened species in a country.
        area (float): Land area of country in square kilometers.

    Returns:
        float: Number of threatened species per sqaure kilometer.
    """
    return total_species/area
