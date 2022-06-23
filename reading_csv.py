import csv, numpy as np

# file = open("quotes_data.csv")
#
# csvreader = csv.reader(file)
#
# header = []
# header = next(csvreader)
# print(header)

with open(
    "quotes_data.txt",
    "r",
) as file:
    reader = csv.reader(file, delimiter="|")#, escapechar='\\')
    header = []
    header = next(reader)
    header = np.append(header, next(reader))
    print(header)
    print(header[0].replace(r'\n', '\n'))

    # for row in reader:
    #     print(row)
string = "When you arise in the morning, think of what a precious privilege it is to be alive - to breathe, to think, to enjoy, to love. \n- Marcus Aurelius"
print((string))
