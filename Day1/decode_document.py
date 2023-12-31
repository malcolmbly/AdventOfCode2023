import re

def format_and_decode(filename):
  print(decode(format_document(filename)))

def decode(filename):
  file = open(filename)
  lines = file.readlines()
  first_number_pattern = re.compile('\\d')
  last_number_pattern = re.compile('\\d(?!\\S*\\d)')
  
  sum = 0
  for line in lines:
    print(line)
    first_number = first_number_pattern.search(line).group()
    if first_number is None:
      continue
    last_number = last_number_pattern.search(line).group()
    print("Numbers are {} and {}".format(first_number, last_number))
    number = first_number + last_number
    sum += int(number)
  return sum

def format_document(filename):
  string_to_number_dict = {
  "one": "o1e",
  "two": "t2o",
  "three": "t3e",
  "four": "f4r",
  "five": "f5e",
  "six": "s6x",
  "seven": "s7n",
  "eight": "e8t",
  "nine": "n9e"
  }
  pattern = re.compile('(one|two|three|four|five|six|seven|eight|nine)')

  unformatted_file = open(filename, 'r')
  formatted_filename = filename + "_formatted"
  formatted_file = open(formatted_filename, 'w')
  lines = unformatted_file.readlines()

  for line in lines:
    while pattern.search(line) is not None:
      number_text_match_value = pattern.search(line).group()
      line = re.sub(number_text_match_value, string_to_number_dict[number_text_match_value], line)
    formatted_file.write(line)

  return formatted_filename

format_and_decode("strings")