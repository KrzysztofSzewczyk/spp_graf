import csv
import matplotlib.pyplot as plt

# You can replace the 'data' variable with the actual CSV file name if you want to read from a file.

# Define the file path
csv_file = "D:\python\spp\data.csv"

parsed_data = []

with open(csv_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        parsed_data.append(row)
#print(parsed_data)

for record in parsed_data:
    record['Dátum odpočtu'] = record['Dátum odpočtu'].split()[0]

cleaned_data =[]

vt_data = []
vt_data_spotreba = []
nt_data = []
nt_data_spotreba = []




    
for i in parsed_data:
    if i['Druh registra (kód)'] == 'VT':
        vt_data.append([i['Dátum odpočtu'], i['Hodnota odpočtu']])
    else:
        nt_data.append([i['Dátum odpočtu'], i['Hodnota odpočtu']])

nt_data.sort()
vt_data.sort()

vt_sportreba_start = int(vt_data[0][1])
for i in vt_data:
    vt_data_spotreba.append([i[0], int(i[1]) - int(vt_sportreba_start)])
    vt_sportreba_start = int(i[1])




nt_sportreba_start = int(nt_data[0][1])
for i in nt_data:
    nt_data_spotreba.append([i[0], int(i[1]) - int(nt_sportreba_start)])
    nt_sportreba_start = int(i[1])


def save_graph(data, jpg_name):
# Extract the dates and values from the data
    dates = [row[0] for row in data]
    values = [int(row[1]) for row in data]

    # Convert dates to datetime objects
    from datetime import datetime
    dates = [datetime.strptime(date, '%Y-%m-%d') for date in dates]

    # Create a line plot
    plt.figure(figsize=(10, 6))
    plt.plot(dates, values, marker='o', linestyle='-')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title('Spotreba kWh')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Display the plot
    plt.savefig(jpg_name+'.png')
    
    
save_graph(nt_data_spotreba, 'nt')
save_graph(vt_data_spotreba, 'vt')