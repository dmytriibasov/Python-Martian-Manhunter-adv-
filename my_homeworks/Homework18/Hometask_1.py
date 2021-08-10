import re

data = r'[XX/XXX/XXXX XX:XX:XX]'
hidden_route = r'/anything_else/'

pattern_data = re.compile(r"(\[\d{2}\/[a-zA-Z]{3}\/\d{4}\s((\:?\d{2}){3}\]))")
pattern_route = re.compile(r'(\/admin\/)')

with open('django_success(2).log') as log_file:
    logfile = ''.join(log_file.readlines())

with open('regex_file.log', 'w') as new_file:
    updated_file = re.sub(pattern_route, hidden_route, logfile)
    new_file.writelines(re.sub(pattern_data, data, updated_file))
