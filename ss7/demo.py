import pandas as pd

myList = [1, 2, 3, 4, 5]

series = pd.Series(myList)
print(series)

# Tạo serires với số tùy chỉnh
seriresCustomIndex = pd.Series(myList, index=['a', 'b', 'c', 'd', 'e'])
print(seriresCustomIndex)

# Tạo serires từ dictionary
seriesDictionary = pd.Series({'name': 'Alice', 'age': 30})
print(seriesDictionary)

# Các thao tác cơ bản với series
# 1. Thao tác lấy dữ liệu thông qua vi trí
print(series[0])  # Lấy phần tử đầu tiên

# 2. Thao tác thêm phần tử vào series
seriresCustomIndex['f'] = 60
seriresCustomIndex['a'] = 100
print(seriresCustomIndex)

# 3. Thao tác xóa phần tử khỏi series
del seriresCustomIndex['f']
print(seriresCustomIndex)

# Xử lý dữ liệu thiếu
s = pd.Series([1, 2, None, 4, None, 6])
print(s)
