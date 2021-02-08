# Web Scraping Script - Academic Performance - Big Data Challenge 2021

import requests
import csv
from bs4 import BeautifulSoup as bs

def extract_item(raw):
    item = raw.text
    item = item.strip()
    item.replace("\"", "")
    return item

def extract_year(raw):
    td = tr.find("td")
    item_year = raw.text
    item_year = rd.item.strip()
    item_year.replace("\"", "")
    return item_year

def extract_state_code(raw):
    item_state_code = raw.text
    item_state_code = item.strip()
    item_state_code.replace("\"", "")
    tr = soup.find("tr")
    td = tr.find("td")
    return item_state_code

def extract_state_name(raw):
    td = tr.find("td")
    item_state_name = raw.text
    item_state_name = td.item.strip()
    item_state_name.replace("\"", "")
    return item_state_name

def extract_gpa(raw):
    item_gpa = raw.text
    item_gpa = item.strip()
    item_gpa.replace("\"", "")
    return item_gpa

def extract_math_gpa(base_url, tag):
    url_data_tags = requests.get(base_url+tag)
    soup = bs(url_data_tags.content, 'html.parser')

    tr = soup.find("tr")
    td = tr.find("td")
    Math_GPA = td.find(id="literarcy-rates")

    if Math_GPA:
        m_gpa = extract_item(Math_GPA)
        m_gpa = m_gpa[m_gpa.find('\n'):]
        return m_gpa.strip()

    return 

def extract_english_gpa(base_url, tag):
    url_data_tags = requests.get(base_url+tag)
    soup = bs(url_data_tags.content, 'html.parser')

    tr = soup.find("tr")
    td = tr.find("td")
    English_GPA = td.find(id="literarcy-rates")

    if English_GPA:
        e_gpa = extract_item(English_GPA)
        e_gpa = e_gpa[e_gpa.find('\n'):]
        return e_gpa.strip()

    return ""

def extract_science_gpa(base_url, tag):
    url_data_tags = requests.get(base_url+tag)
    soup = bs(url_data_tags.content, 'html.parser')

    tr = soup.find("tr")
    td = tr.find("td")
    description_raw = td.find(id="literarcy-rates")

    if Science_GPA:
        s_gpa = extract_item(Science_GPA)
        s_gpa = historic[historic.find('Yes\n'):]
        return s_gpa.strip()

    return

# Webiste Information
base_url = "https://"
soup = bs(base_url.content, 'html.parser')

# These next lines push all the data to the csv file:
filename = "data_all.csv"
csv_writer = csv.writer(open(filename, 'w'), lineterminator='\n')

csv_writer.writerow(["Year", "State.Code", "State.Name", "Total.RecordedTests", "English.GPA", "Mathematics.GPA", "Sciences.GPA", 
                    "Income.Under.20k", "Income.20-40k", "Income.40-60k", "Income.60-80k", "Income.80-100k", "Income.Over.100k"])

for tr in soup.find_all("tr"):
    data = []

    body = tr.find_all("td")

    if body:
        Year = body[0]
        State_Code = body[1]
        State_Name = body[2]
        Total_RecordedTests = body[3]
        English_GPA = body[4]
        Math_GPA = body[5]

        # Appends data into the csv:
        data.append(extract_item(Year))
        data.append(extract_item(State_Code))
        data.append(extract_item(Total_RecordedTests))
        data.append(extract_english_gpa(English_GPA))
        data.append(extract_math_gpa(base_url, extract_item(Math_GPA)))
        data.append(extract_science_gpa(base_url, extract_item(Science_GPA)))

        if data:
            print("Inserting data: {} ".format(','.join(data)))
            csv_writer.writerow(data)
