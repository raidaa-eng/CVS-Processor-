# user_csv.py

def read_csv(filename, include_header = True):

    """
    Read a csv file and return contents as a 2D list.

    Parameters:
        filename (str): the name of an existing file to read
        include_header (bool): Indicates whether the CSV file contains a header

    Returns:
        list: a nested list, representing rows from the csv file
    """
    file = open("data_files/" + filename, "r")
    data = [] #nested list

    for line in file:
        line = line.strip()
        row = []
        for index in line.split(","):
            if index.isdigit():
                row.append(float(index))
            else:
                row.append(index)
        data.append(row)

    file.close()
    
    if not include_header:
        return data[1:] #return nested list without headers
    return data #return nested list


def write_csv(filename, data, overwrite = True):

    """
    Writes a 2D list to a new csv file.

    Parameters: 
        filename (str): the name of an existing file to write to
        data (nested list): 2D list containing data
        overwrite (bool):
            (True): overwrite existing file
            (False): append onto existing file

    Returns:
        None
    """
    edit = "w" if overwrite else "a"

    file = open(filename, edit)

    for row in data:
        line = ""
        for i in range(len(row)):
            line += str(row[i])

            if i < (len(row) - 1): #if not last item, add comma
                line += ","
        file.write(line + "\n")
    
    file.close()
