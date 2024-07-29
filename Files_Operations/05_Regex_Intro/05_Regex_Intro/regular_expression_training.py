import re
test='test'
str_list = list()
# print(dir(re)
# help(re)
# print(path)
with open('/home/benz/ENTAUTO/CCNPAUTO/Files_Operations/05_Regex_Intro/05_Regex_Intro/show_version.txt') as data:
    output = data.readlines()

string_test="The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."
    
# string_test = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. \nThe panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."
# print(type(string_test))

# print(type(output))
# print(output)

# regex1 = re.compile(r"(\d{4})")

# ####### re.search()#################################
# ###Show the first occurence that matches the pattern#######
# # result = regex1.search(output)
# result = re.findall(regex1, output)
# # print(output[245:249])
# print(result.group(1))

######## re.match ###########################
###Show pattern  match, only at the beginning at the string#######

# regex1 = re.compile(r"(\w{4})")
# result = regex1.match(output)
# # result = re.findall(regex1, output)
# # print(output[245:249])
# print(result.group(1))

####### re.fullmatch ###########################
###Return pattern full match/ fullmach does not take new line #######

# regex1 = re.compile(r".{2442}")
# result = regex1.fullmatch(output)
# result = re.fullmatch(r".{2442}", output)
# print(type(result))
# print(len(output))
# result = re.findall(regex1, output)
# print(output[245:249])
# print(result)
# print(result.group(1))


####### re.findall ###########################
###Return all the occurence matching the pattern #######


# regex1 = re.compile(r"\d{3}")
# result = regex1.findall(output)
# # result = re.fullmatch(r".{2442}", output)
# print(type(result))
# # result = re.findall(regex1, output)
# # print(output[245:249])
# print(result)
# # print(result.group(1))

####### re.split ###########################
###split the string based on the RE pattern #######

# regex1 = re.compile(r"\s")
# result = regex1.split(output)
# # result = re.fullmatch(r".{2442}", output)
# print(type(result))
# # result = re.findall(regex1, output)
# # print(output[245:249])
# print(result)
# # print(result.group(1))


####### re.sub ###########################
###replace all the occurence of the pattern  with replacement #######

# for str_line in output:
#     stripped_line = str_line.strip("\n")
#     print(stripped_line)
#     print(type(stripped_line))
#     regex1 = re.compile(r"Cisco")
#     result = regex1.sub('cisco', stripped_line)
#     str_list.append(result)
#     # # # result = re.fullmatch(r".{2442}", output)
#     # # print(type(re))
#     # # # result = re.findall(regex1, output)
#     # # # print(output[245:249])
#     # print(result)
#     # # # print(result.group(1))
# print(str_list)

####### GROUP() AND GROUPS()  ###########################
### Allow to parse the result in group #######

# result =  re.search(r".+\s(.+ex).+(\d\d\s.+).", string_test, re.S) 
# # print(result.groups())
# print(result.group(0))
# print(result.group(1))
# print(result.group(2))

# ####### START() , END() AND SPAN()  ###########################
### provide the group index or specific location in the string #######


# result =  re.search(r".+\s(.+ex).+(\d\d\s.+).", string_test) 
# # print(result.groups())
# print(result.group(0))
# print(result.group(1))
# print(result.start(1))
# print(result.end(1))
# print(string_test[19:24])
# print(result.span(1))
# print(result.group(2))
# print(result.start(2))
# print(result.end(2))
# print(string_test[273:284])
# print(result.span(2))

##### REGEX FLAG #######

### I FLAG #####

# result = re.findall(r"the", string_test)
# print(result)
# result = re.findall(r"the", string_test, re.I)
# print(result)

### S FLAG #####

# result =  re.search(r".+\s(.+ex).+(\d\d\s.+).", string_test, re.S) 
# # print(result.groups())
# print(result.group(0))
# print(result.group(1))
# print(result.group(2))

#### VERBOSE, X FLAG

# result = re.search(r""".+\s #Beginning of The string 
#     (.+ex) #Searching for index 
#     .+ #Middle of the string 
#     (\d\d\s.+). #Date at the end""", string_test, re.X) 
# print(result.groups())
# # print(result.group(0))
# # print(result.group(1))
# # print(result.group(2))


##### METACHARACTERS #######

### THE DOT ####

### Any character except new line.
# result = re.search(r"(.+)", string_test) 
# print(result.group(1) )

########## METACHARACTERS - THE CARET ( ^ ) #######
### Pattern maches occurence only at beginning of the string####

# result = re.search(r"^\w{3}", string_test) 
# print(result)

########## METACHARACTERS - THE CARET ( ^ ) WITH MULTILINE #######
### Pattern maches occurence only at beginning of each new line of the string####

# result = re.findall(r"^\w{3}", string_test, re.M) 
# print(result)


##### METACHARACTERS - THE DOLLAR SIGN ( $ ) ######
####$ end the line #####
# result =  result = re.findall(r"\s([\w]+)\W$", string_test, re.M) 

# print(result)

#### METACHARACTERS - THE ASTERISK ( * ) ######
#### Repeat the preceding caracter of the pattern zero or multiple times as much as possible. greedy########

# result1 = re.findall(r"\d\d\d*", string_test) 
# # print(result1)
# result2 = re.findall(r"E.* ", string_test) 
# print(result2)

# result = re.findall(r"E\w*", string_test)
# print(result)

######### METACHARACTERS - THE PLUS SIGN ( + ) #####
#### Repeat the preceding  caracter of the pattern 1 or multiple times in a greedy way. As much as possible.########

# result = re.findall(r"E\w+", string_test)
# print(result)

#######  THE QUESTION MARK ( ? ) #########
#### Repeat the preceding caracter 0 or one time ####

# result = re.findall(r"\d\d\d?", string_test) 
# print(result)

# result = re.findall(r"E.? ", string_test) 
# print(result)

# result = re.findall(r"E\w?", string_test) 
# print(result)

###### METACHARACTERS - GREEDY VS. NON-GREEDY ( *?, +?, ?? ) ########

##  *? : zero repetition of the predecente caracter.
# result = re.findall(r"\d\d\d*?", string_test) 
# print(result)

##  +? :  One repetition of the predecente caracter.

# result = re.findall(r"\d\d\d+?", string_test) 
# print(result)

##  ?? :  One repetition of the predecente caracter.
# result = re.findall(r"\d\d\d??", string_test) 
# print(result)


##### METACHARACTERS - THE BACKSLASH ( \ )  ########

#### To espace special caracter or special sequence. 

# result = re.findall(r"\d", string_test)
# result = re.findall(r"\.", string_test) 
# print(result) 

#### THE SQUARE BRACKETS ( [] )#####
### To define a set of caracter. 

# result = re.findall(r"[wxkq]", string_test) 
# result = re.findall(r"[a-d]", string_test) 
# result = re.findall(r"[S-W]", string_test) 
# result = re.findall(r"[1-5]+", string_test) 
# result = re.findall(r"[a-f][c-w]", string_test) 
# result = re.findall(r"[0-9][a-z]", string_test) 
# result = re.findall(r"[\w^X]", string_test) 
### Special caracter loose their super power inside braket. 
# result = re.findall(r"[.+?]", string_test) 
# print(result)

########  CHARACTER CLASSES

# result = re.findall(r"[0-9]", string_test)
# result = re.findall(r"[A-Za-z]", string_test)
# result = re.findall(r"[^0-9]", string_test)
# result = re.findall(r"[ \n\t\r\f\v]", string_test)
# result = re.findall(r"[^ \n\t\r\f\v]", string_test)
# result = re.findall(r"[^a-zA-Z0-9_]", string_test) 
# print(result)

###### HE CURLY BRACES ({})
number = "12391827172820919011001911"
# result = re.findall(r"\b\w{4}\b", string_test)
# result = re.findall(r"\b\w{3,5}\b", string_test)
# result = re.findall(r"\b\w{3,}\b", string_test)
# result = re.search(r"\d{3,6}", number) ## Greedy behavior
# result = re.search(r"\d{3,6}?", number) ## unGreedy behavior
# print(result)

##### THE PIPE ( | )  #### Equivalent to OR

# result = re.search(r"\d{3}|\d{4}|\b[A-Z]{4}\b", string_test)
# print(result)

##### SPECIAL SEQUENCES #####
##### SPECIAL SEQUENCES - \A AND \Z
### \A Matches the sequence at the beginning of the string regarless the string is multine or not
# result = re.findall(r"^([A-Z].*?)\s", string_test, re.M)
# result = re.findall(r"^([A-Z].*?)\s", string_test, re.M)
# result = re.findall(r"\b\A([A-Z].*?\b)", string_test, re.M)
# print(result)

###### \Z Matches the sequence at the end of the entire string regarless the string is multine or not

# result = re.findall(r"\W\Z", string_test, re.M)
# result = re.findall(r"\W$", string_test, re.M)
# print(result)

##### SPECIAL SEQUENCES - \B AND \B
#### Word Boundary. Pattern is bordered by non alphanumerique caracter as space

# result = re.findall(r"\b\w{10,}\b", string_test)
# result = re.findall(r"\bEuro\b", string_test)
# \B at beginning of the  Pattern, seek for pattern  not at the begining of the word
# result = re.findall(r"\Bcross", string_test)
#  \B at the end of the  Pattern, seek for pattern  not at the end of the word
# result = re.findall(r"cross\B", string_test)
#  \B at the beginning end of the  Pattern, seek for pattern  not at the begining  and the end of the word
# result = re.findall(r"\Bcross\B", string_test) 
# print(result)

###### SPECIAL SEQUENCES - \D AND \D
# result = re.findall(r"(\d)([a-z])", string_test)
#### \D ANY NON DIGIT CARACTER
# result = re.findall(r"\W(\D)\W", string_test)
# print(result)

##### SPECIAL SEQUENCES - \s AND \S

#### \s means space caracter represented by [ \n\t\f\r\v]
# result = re.findall(r"\s", string_test)
###### \S Non white caracter
# result = re.findall(r"\S{8,}", string_test)
# print(result)

#### SPECIAL SEQUENCES - \W AND \W

#### \w Any alphanumeric caracter. 
# result = re.findall(r"\s(\w{3,5})\s", string_test)

#### \W Non Alphanumeric caracter. 
# result = re.findall(r"\W", string_test)
# print(result)


######### EXTENSION NOTATIONS AND NON-CAPTURING GROUPS

# result = re.search(r".+(\b.+ex\b).+(\b[A-Z]{4}\b).+(\d\d\s.+)\.", string_test)
# r".+(\b.+ex\b).+(\b[A-Z]{4}\b).+(\d\d\s.+)\.", string_test, re.M)
# print(result)
# print(result.span(0))
# print(string_test[0:148])
# print(result.groups())

#### ?:  For not capturing group, TO IGNORE A GROUP #####

# result = re.search(r".+(?:\b.+ex\b).+(\b[A-Z]{4}\b).+(\d\d\s.+)\.", string_test)
# print(result)
# print(result.groups())


###### NAMED GROUPS AND GROUPDICT()

### ?P<GROUP NAME> TO NAME A GROUP

# result = re.search(r".+(?P<Wordex>\b.+ex\b).+(?P<Uppercase>\b[A-Z]{4}\b).+(?P<Date>\d\d\s.+)\.", string_test)
# # print(result)
# # print(result.groups())
# # print(result.group("Wordex"))
# # print(result.group("Uppercase"))
# # print(result.group("Date"))
# print(result.groupdict())

###### POSITIVE LOOKAHEAD ASSERTIONS ### SPECIFY A CONDITION TO BE PERFOMED FOR THE MATCH

#### ?= : FOR POSITIVE  LOOKAHEAD ASSERTION. DISPLAY PATTERN IF THE CONDITON IS MET NEXT.ONLY.
result = re.findall(r"[A-Z]{5}\s(?=[0-9]{3})", string_test)
# result = re.findall(r"Euro(?=[a-z]+)", string_test)
print(result)

#### NEGATIVE LOOKAHEAD ASSERTIONS ####

#### ?! : FOR POSITIVE  LOOKAHEAD ASSERTION. DISPLAY PATTERN IF THE CONDITON IS  NOT  MET NEXT.ONLY.

# result = re.findall(r"\d(?![5-9]|\D)", string_test)
# result = re.findall(r"\b\w+\b(?!\s)", string_test)
# print(result)

#### POSITIVE LOOKBEHIND ASSERTIONS #######

#### ?<= IF THE PATTERN PRECEDED BY THE CONDITION IN THE PARENTHESIS
# result = re.findall(r"(?<=\s)\d{1,}", string_test)
# result = re.findall(r"(?<=,\s)\b\w+\b", string_test)
# print(result)

###### NEGATIVE LOOKBEHIND ASSERTIONS

#### ?<? IF THE PATTERN PRECEDED BY THE CONDITION IN THE PARENTHESIS NOT MET
# result = re.findall(r"(?<!\s)\d{1,}", string_test)
# result = re.findall(r"(?<!x)x(?!x)", string_test, re.I)
# print(result)


