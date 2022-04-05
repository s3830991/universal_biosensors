import csv

'''
trans data in csv to json format (no file output)
'''


def trans_csv():
    with open("Data samples//Transient and associated//transient.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        data = []
        for row in reader:
            data.append({"a": row[0], "b": row[1], "c": row[2]})
    return data
