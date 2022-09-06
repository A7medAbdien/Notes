import re

# search for a regex pattern at the beginning of a string
pattern = r"\d+"
string = "123aa"
if re.match(pattern, string):
    print("Found at the beginning")

# search for a regex pattern anywhere
string = "Some text. 123"
if re.search(pattern, string):
    print("Found anywhere")

# split a string by the occurrences of a regex pattern
string = "Some text. 123. Some text"
print(re.split(pattern, string))

# replace all occurrences of a regex pattern in a string
string = "Some text. 123. Some text. 321 222"
replacement = "Some text"
print(re.sub(pattern, replacement, string))

# fetch all occurrences of a regex
re_obj = re.compile(pattern)
print(re_obj.findall(string))

print(re.findall(pattern, string))

occurrences = re.finditer(pattern, string)
print([o.group() for o in occurrences])

# how many occurrences of a regex pattern were replaced in a string
result, replaced_count = re.subn(pattern, replacement, string)
print(replaced_count)

# get the part of the string where there was a match, it gets only if it is a first occurrence
# string = "Some text. 123 will result a None"
string = "123Some text. 123"
match_object = re.match(pattern, string)
print(match_object.group())

match_object = re.match(pattern, string)
print(match_object[0])

match_object = re.match(pattern, string)
print(match_object.group(0))
# picked the wrong one


# find the substring that matched the last capturing group of the regex
pattern = r"(\d+) (\d+)?"
string = "000 text"
match_object = re.match(pattern, string)
print(match_object.group(match_object.lastindex))
# wrong solution because I changed the case

# exactly two letters
pattern = r"\\n"
string = "\\n"
match_object = re.match(pattern, string)
print(match_object[0])

# perform case-insensitive matching
string = "HeLlo"
pattern = r"hello"
if re.findall(pattern, string, re.IGNORECASE):
    print("Found")

pattern = r"hello"
re_obj = re.compile(pattern, re.IGNORECASE)
if re_obj.match(string):
    print("Found")

pattern = r"hello"
re_obj = re.compile(pattern, re.I)
if re_obj.search(string):
    print("Found")

# split a string by multiple delimiters
string = "Some text; 123, Some text, 123"
pattern = r"[,;]"
print(re.split(pattern, string))

# shortest possible match, multiple repeat error when uses ?* ** ??
string = "Some text 'a', Some text 'b'"
pattern = r"'(.*?)'"
re_obj = re.compile(pattern)
result = re_obj.findall(string)
print(result)

# . In the default mode, this matches any character except a newline. If the DOTALL flag has been specified, this matches any character including a newline.
string = '''multiline
  string
'''
pattern = r"mul.+ing"
re_obj = re.compile(pattern, re.DOTALL)
result = re_obj.findall(string)
print(result)
