data = '''(dog:42,cat:33);
cat dog

((dog:4,cat:3):74,robot:98,elephant:58);
dog elephant'''

formatted_data = [f"{line.strip().replace(',', '')}" if ',' in line else line.strip() for line in data.split(';')]
formatted_data = [line for line in formatted_data if line]
print(formatted_data)
