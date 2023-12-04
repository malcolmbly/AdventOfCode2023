import re

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
  "one": "1",
  "two": "2",
  "three": "3",
  "four": "4",
  "five": "5",
  "six": "6",
  "seven": "7",
  "eight": "8",
  "nine": "9"
  }
  unformatted_file = open(filename, 'r')
  formatted_filename = filename + "_formatted"
  formatted_file = open(formatted_filename, 'w')
  lines = unformatted_file.readlines()
  pattern = re.compile('(one|two|three|four|five|six|seven|eight|nine)')
  for line in lines:
    # search in line for each of the keys above
    # find the one that has the lowest value for m.start
    while pattern.search(line) is not None:
      number_text_match_value = pattern.search(line).group()
      line = re.sub(number_text_match_value, string_to_number_dict[number_text_match_value], line)
    formatted_file.write(line)

  return formatted_filename

def format_and_decode(filename):
  print(decode(format_document(filename)))

format_and_decode("strings")