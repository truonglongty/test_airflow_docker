import csv
import os
from config.connect_db import insert_data

def read_csv_file(file_path):
    if not os.path.exists(file_path):
        print(f'File {file_path} does not exist')
        return None
    
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        # Đọc header (tiêu đề cột)
        header = next(csv_reader)
        
        # Đọc các dòng còn lại
        for row in csv_reader:
            data.append(row)
    
    return header, data

# Header: ['', 'total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size']
# Data:
# ['0', '16.99', '1.01', 'Female', 'No', 'Sun', 'Dinner', '2']
# print("Header:", header)
# print("Data:")
# for row in data:
#     print(row)

def insert_data_to_db(data):
    try:
        for row in data:
            id = int(row[0])
            total_bill = eval(row[1])
            tip = eval(row[2])
            sex = row[3]
            smoker = row[4]
            day = row[5]
            time = row[6]
            size = int(row[7])
            insert_data(id, total_bill, tip, sex, smoker, day, time, size)
    except Exception as e:
        print('Data insertion to db failed')
        print(e)

# file_path = r'data\tips.csv'
# header, data = read_csv_file(file_path)
# insert_data_to_db(data)