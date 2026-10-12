import re

text = "Soso Tigishvili: soso.tigishvili@itstep.com, dima123@gmail.com, test_user@yahoo.com"

emails = re.findall(
    r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
    text
)

result = "+".join(emails)

print(result)
