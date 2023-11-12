import re
input_text = """
"""

input_text = input_text.replace(" ", "").replace("\n", "")
input_text = re.sub(r'Rosalind_\d+', '', input_text)
input_text = input_text.replace(">", '",\n"')

input_text = input_text.rstrip(',')

input_text = f'"{input_text}"'

print(input_text)







