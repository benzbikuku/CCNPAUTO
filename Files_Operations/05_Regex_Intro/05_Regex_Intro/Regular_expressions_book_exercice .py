import re
# import pprint from pprint
event = dict()
event_list = []

book_year_list = list()
with open(file="/home/benz/ENTAUTO/CCNPAUTO/Files_Operations/05_Regex_Intro/05_Regex_Intro/bookshelf.txt") as bookshelf:
    # books = bookshelf.readlines()
    books = bookshelf.read()
    
###### BOOKSHELF EXERCICE.
    
# print(books)

# for book in books:
#     result=re.search(r"(?P<Author>.+);(?P<Title>.+);(?P<year>\d{4})", book)
#     if len(result["Title"]) <= 25:
#         # print(result["Author"])
#         # print(type(result["Author"]))
        
#         # print(result["Title"])
#         # print(result["year"])
#         title_year = "{0} : {1}".format(result["Author"],result["year"])
#         book_year_list.append(title_year)
#         #print(title_year)
#         # f"{result["Title"]} "
# print(book_year_list)

### Book Solution ######

#### Print Title with lengh less than 25
# result = re.findall(r".+?;(.{1,25});.+?", books)
# result = re.findall(r"(.+?;.+?);20[0-9][0-9]", books)

# print(result)

# pattern = re.compile(r".+?;(.+?);19[8-9]\d?")
# result = pattern.findall(books)
# print(result)


 ##### PHONE LIST SOLUTION
 
# with open(file="/home/benz/ENTAUTO/CCNPAUTO/Files_Operations/05_Regex_Intro/05_Regex_Intro/phone.txt") as bookshelf:
#     # books = bookshelf.readlines()
#     phone_dictory = bookshelf.read()
#     # print(phone_dictory)
    
# # result = re.findall(r".+ (.+)\t\(\d\d0\)\s(.+)", phone_dictory)
# # result = re.findall(r".+?(.+)\t\([1-2][0-9][0-9]\)\s.+", phone_dictory)
# result = re.findall(r"(.+)? .+[aeiou]\t\(\d\d\d\)\s.+-\d\d\d[079]", phone_dictory)
# print(result)

#### DATE AND TIME ####

# with open(file="/home/benz/ENTAUTO/CCNPAUTO/Files_Operations/05_Regex_Intro/05_Regex_Intro/logs.txt") as logs:
#     logs_journal = logs.read()
#     # print(logs_journal)
    
# # critical_events = re.findall(r".+ \d\/\d{2}\/\d{4} [12|1-3]:[0-9][0-9]:[0-9][0-9] PM (\w+)", logs_journal)
# # critical_events = re.findall(r".+ (\d\/\d{2}\/\d{4}) .+ PM TPM", logs_journal)
# critical_events = re.findall(r".+ (1\/[24567]{2}\/2020 8:[0-9][0-9]:[0-9][0-9])", logs_journal)


# print(critical_events)

# # print(critical_events)
# for critical_event in critical_events:
#     event["severity"] = critical_event[0]
#     event["event_date"] = critical_event[1]
#     event["event_source"] = critical_event[2]
#     event_list.append(event)
# print(event_list)


##### WEB ADDRESSES

# with open(file="/home/benz/ENTAUTO/CCNPAUTO/Files_Operations/05_Regex_Intro/05_Regex_Intro/web.txt") as web:
#     web_journal = web.read()
#     print(web_journal)
    
# result = re.findall(r"\w+\t(https:\/\/.+)?\t\d{1,} .+?\t.+?\tOnline shopping\t.+", web_journal)

### Find the site names of all the websites in the file that are based  in China and have 3-letter URL extensions

# result = re.findall(r"(.+)\thttps:\/\/\w+\.\w+\t\d{1,} .+?\t.+?\t.+\t.+\s+China", web_journal)
#### URL and country of all Social networking websites in the file whose domain name(exclusding the extension) is less than 5 caracters long. 
# result = re.findall(r"(.+)\thttps:\/\/\w{5,}\..+\tSocial networking\t.+?\s.+?\s(.+)", web_journal)

# Site name and web protocol of all the websites whose URLs contain subdomains(e.g. https://something.website.abc)

# result = re.findall(r"(.+)\thttps:\/\/\w{5,}\..+\tSocial networking\t.+?\s.+?\s(.+)", web_journal)
# result = re.findall(r"(.+)\t(https):\/\/\w+\.\w+\.\w+", web_journal)

# print(result)

# print(web_split)
    
# print(web_journal)

### STOCK

with open(file="/home/benz/ENTAUTO/CCNPAUTO/Files_Operations/05_Regex_Intro/05_Regex_Intro/stocks.txt") as stocks:
    stock_string = stocks.read()
print(stock_string)
    
    
#### Company for which the revenue is more than 50 billion. 

# result = re.findall(r"(.+)?\t.+M\s+([5-9]\d.+)B\s+.+",stock_string)

#### Comapany name for which the revenue is under 50 billion

# result = re.findall(r"(.+)?\s+\d+\.\d+M\s+[0-4]\d\.\d+B\s+.+",stock_string)

#### Company name whose revenue is between 10B and 30B and P/E is betweeen 10 and 15

# result = re.findall(r"(.+)?\s+\d+\.\d+M\s+[0-4]\d\.\d+B\s+.+",stock_string)

#### Company whose avearage volume is under 10M

# result = re.findall(r"(.+)?\s+[1-9]\.\d\dM\s+",stock_string)

#### Company whose Average volume starts with an even digit and P/E ratio ends with an odd digit

result = re.findall(r"(.+)?\s+[2468].+M.+B.+\d+.\d[13567]",stock_string)



print(result)
     
 
