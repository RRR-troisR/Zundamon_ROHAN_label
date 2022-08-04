import os

os.makedirs("phoneme_data", exist_ok=True)
os.makedirs("accent_data", exist_ok=True)

with open("csv_data/phoneme.csv", mode='r') as f:
    lines = f.readlines()
    for line in lines:
        name, phoneme = line.split(",")
        with open("./phoneme_data/" + name + '.ph', mode='w') as f:
            f.write(phoneme.strip('\n'))

with open("csv_data/accent.csv", mode='r') as f:
    lines = f.readlines()
    for line in lines:
        name, accent = line.split(",")
        with open("./accent_data/" + name + '.ac', mode='w') as f:
            f.write(accent.strip('\n'))