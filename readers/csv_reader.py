import csv

# Read the entire Csv File
def read_csv(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        data = []
        for row in reader:
            data.append(row)
        return data

# Returns a specfic batch of entries of a CSV file
def read_batch_csv(start, end, filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        data = []
        for row in reader:
            data.append(row)
        if start <= len(data) and end <= len(data):
            return data[start:end+1]


# Function to determine if the CSV file has a header
def has_header(filename):
    with open(filename, newline='') as csvfile:
        return csv.Sniffer().has_header(csvfile.read(1024))


# If the CSV file has a header, the function returns a list with the names of the fields.
# If the CSV file doesn't have a header, the functions throws an exception
def get_header(filename):
    if has_header(filename):
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            return next(reader)
    raise Exception("File has no header")
