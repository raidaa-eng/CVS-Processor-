import matplotlib.pyplot as plt
import user_csv
import numpy as np




def plot_species_data():
	#reads the csv data containing data for species 
    data = user_csv.read_csv("species_plot_data.csv", False)
	
    #separating data into lists
    countries = []
    total_species = []
    species_per_sq_km = []


    for row in data:
        countries.append(row[0])
        total_species.append(float(row[1]))
        species_per_sq_km.append(float(row[2]))


    #converting numpy arrays for easier plotting
    total_species = np.array(total_species)
    species_per_sq_km = np.array(species_per_sq_km)


    #size of image, side by side bar plots
    plt.figure(figsize =(12,6))
    #total species plot
    plt.subplot(1, 2, 1)
    plt.bar(countries, total_species, color = "purple")
    plt.title("Total Threatened Species")
    plt.xlabel("Country")
    plt.ylabel("Number of Species")
    plt.xticks(rotation=45, ha="right")


    #species per sq km plot 
    plt.subplot(1, 2, 2)
    plt.bar(countries, species_per_sq_km, color = "pink")
    plt.title("Threatened Species per Sq Km")
    plt.xlabel("Country")
    plt.ylabel("Species / Sq Km")
    plt.xticks(rotation=45, ha="right")#set x axis tick values


	#adjusting the layout, saving the figure
    plt.tight_layout()


    plt.savefig("final_plots/subregion_analysis.png")


    plt.close()
