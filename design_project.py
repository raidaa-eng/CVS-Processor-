# design_project.py
# ENDG 233 F24
# STUDENT NAME(S) Raida Alam and Shaimaa Azad
# GROUP NAME 20
# A terminal-based data analysis and visualization program in Python.
# You must follow the specifications provided in the project description.
# Remember to include docstrings and comments throughout your code.

import numpy as np
import math
import user_csv 
import analysis
import matplotlib.pyplot as plt
import plotting

def main():
    while True:
        
        #Read required csv file datasets
        country_data = user_csv.read_csv('Country_Data.csv', False)
        population_data = user_csv.read_csv('Population_Data.csv', False)
        species_data = user_csv.read_csv('Threatened_Species.csv', False)

        #Prompt user to select a sub region
        subregion = analysis.get_subregion(country_data)
        print(f"\nPlease enter a sub-region: {subregion}")

        #Get list of countries in selected sub-region
        countries_in_subregion = analysis.get_countries_in_subregion(country_data,subregion)

        #Exit if no countries found
        if not countries_in_subregion:
            print("No countries found for this sub-region.")
            return

        #Allow the user to select a country from the sub-region list
        selected_country = analysis.get_countries(countries_in_subregion)

        country_name = selected_country[0]
        region_name = selected_country[1]
        area_sq_km = float(selected_country[3])

        print(f"\nSelected country: {country_name}")

        #Get population data row for select country
        pop_row = analysis.get_population(population_data, country_name)

        if pop_row is None:
            print("No population data found for this country.")
            return

        #Calculate population statistics
        pop_change, avg_population = analysis.population_stats(pop_row)
        population_2020 = float(pop_row[1])
        density = analysis.population_density(population_2020, area_sq_km)

        #Display population reults 
        print(f"\nThe change in population from 2000 to 2020 in {country_name} is: {int(pop_change)} people")
        print(f"The average population from 2000 to 2020 in {country_name} is: {int(avg_population)} people")
        print(f"The 2020 population density in {country_name} is: {density:.2f} people per sq km")

        # Calculate average and total threatened species for each country
        species_results = analysis.species_stats(species_data, countries_in_subregion)
        
        # Create a list that will be written to a CSV file for plotting
        plot_data = [["Country", "Total Species", "Species per Sq Km"]]
        
        #Loops through species results 
        for country, _, total in species_results:
            #Match country with area from country data 
            for row in countries_in_subregion:
                #Ensure area value exists
                if row[0] == country and row[3] != "":
                    area = float(row[3])
                    per_area = analysis.species_per_area(total, area) #species/sq km
                    plot_data.append([country, int(total), per_area]) #store values for plotting
                    break
        #Write prepared plotting data to CSV file
        user_csv.write_csv("data_files/species_plot_data.csv", plot_data, overwrite=True)
        plotting.plot_species_data() #Genereate and save plot image

        #DISPLAY RESULTS 
        print("\nThe average number of threatened species in each country of the sub-region:\n")

        print(f"UN Region: {region_name}")
        print(f"UN Sub_Region: {subregion}")
        print("\nCountry")

        for country, avg, _ in species_results:
            print(f"{country:20}{avg:.2f}")

        print("\nThe total number of threatened species in each country of the sub-region:")
        print(f"UN Region: {region_name}")
        print(f"UN Sub_Region: {subregion}")
        print("\nCountry")

        for country, _, total in species_results:
            print(f"{country:20}{int(total)}")

        print("\nThe calculated number of threatened species per sq km of area in each country is:")
        print(f"UN Region: {region_name}")
        print(f"UN Sub_Region: {subregion}")
        print("\nCountry")

        for country, _, total in species_results:
            for row in countries_in_subregion:
                if row[0] == country:
                    if row[3] == "":
                        break
                    area = float(row[3])
                    value = analysis.species_per_area(total, area)
                    print(f"{country:20}{value:.6f}")
                    break
        
        #Loop program
        choice = input("\nRun again? (Yes/No): ").strip().lower()
        if choice != "yes":
            print("Thank you for using our program.")
            break

if __name__ == "__main__":
    main()