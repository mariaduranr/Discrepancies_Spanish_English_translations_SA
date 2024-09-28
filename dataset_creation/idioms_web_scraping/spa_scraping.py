import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

url = 'https://www.spanishdict.com/guide/spanish-idioms'

# Fetch the content of the webpage
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')
data = []

# Loop through each table row
for row in soup.find_all('tr'):
    # Initialize a dictionary to store the texts for this row
    row_data = {'Idiom': None, 'literal_translation': None, 'Meaning': None}
    
    # Find all strong tags within the row
    strong_tags = row.find_all('strong')
    if strong_tags:
        # Add the first strong tag's text if it exists
        row_data['Idiom'] = strong_tags[0].get_text(strip=True)
        # Add the last strong tag's text if there is more than one
        if len(strong_tags) > 1:
            row_data['Meaning'] = strong_tags[-1].get_text(strip=True)
    
    # Find the em tag within the row and add its text
    em_tag = row.find('em')
    if em_tag:
        row_data['literal_translation'] = em_tag.get_text(strip=True)
    
    # Add the dictionary to the data list
    data.append(row_data)

# Create a DataFrame with the extracted data
df = pd.DataFrame(data)
df.to_csv('Spanish_idioms_1.csv', index=False)
#################################################################################################
urls = [
    "https://www.speakinglatino.com/spanish-idioms-t/",
    "https://www.speakinglatino.com/spanish-sayings-u/",
    "https://www.speakinglatino.com/spanish-expressions-a/",
    "https://www.speakinglatino.com/spanish-expressions-b/",
    "https://www.speakinglatino.com/spanish-expressions-c/",
    "https://www.speakinglatino.com/spanish-expressions-d/",
    "https://www.speakinglatino.com/puerto-rican-sayings-in-spanish-e/",
    "https://www.speakinglatino.com/spanish-expressions-g/",
    "https://www.speakinglatino.com/spanish-sayings-h/",
    "https://www.speakinglatino.com/spanish-idioms-i/",
    "https://www.speakinglatino.com/spanish-sayings-j/",
    "https://www.speakinglatino.com/spanish-idioms-m/",
    "https://www.speakinglatino.com/spanish-idioms-n/",
    "https://www.speakinglatino.com/puerto-rican-sayings-in-spanish-o/",
    "https://www.speakinglatino.com/spanish-sayings-r/",
    "https://www.speakinglatino.com/english-sayings-in-spanish-y/"
]

data = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

for url in urls:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Adjust the range as needed based on the content of the pages
    if url == "https://www.speakinglatino.com/spanish-idioms-t/" or url == "https://www.speakinglatino.com/spanish-sayings-u/":
        paragraphs = soup.find_all('p')[1:-2]

        current_row = []
        for paragraph in paragraphs:
            text = paragraph.get_text().strip()
            if any(phrase in text for phrase in ["Next Letter", "« Previous Letter", "Check out these other",
                                                "Navigation", "The following is the Speaking Latino",
                                                "Browse English Sayings starting with",
                                                "You can find this list and much more in my book"]):
                continue

            if paragraph.find('strong'):
                if current_row:
                    data.append(current_row)
                current_row = [text]  # start a new row with the idiom
            else:
                text = paragraph.get_text().strip()
                if text.startswith('-'):
                    current_row.append(text[1:].strip())  # append the meaning to the current row

        if current_row:
            data.append(current_row)
    else:
        # Find all paragraphs and skip the first five
        paragraphs = soup.find_all('p')[6:-2]

        for paragraph in paragraphs:
            text = paragraph.get_text().strip()
            if any(phrase in text for phrase in ["Next Letter", "« Previous Letter", "Check out these other","Navigation"]):
                    continue  # Skip this iteration if the paragraph contains any of the specified phrases

            if paragraph.find('strong'):
                    if current_row:
                        # Finish the current row and append it to data
                        data.append(current_row)
                    # Start a new row with the text from the <strong> tag
                    current_row = [paragraph.get_text().strip()]
            else:
                    text = paragraph.get_text().strip()
                    if text.startswith('-'):
                        # Append the text without the dash to the current row
                        current_row.append(text[1:].strip())
            if current_row:
                data.append(current_row)

# Create a DataFrame from the accumulated data
max_cols = max(len(row) for row in data)
column_names = ['Idiom'] + [f'Meaning {i}' for i in range(1, max_cols)]

df = pd.DataFrame(data, columns=column_names)
df.to_csv('Spanish_idioms_2.csv', index=False)


#################################################################################################

urls = ["https://www.languagerealm.com/spanish/spanishidioms.php"]+\
    ["https://www.languagerealm.com/spanish/spanishidioms_" + i + ".php" for i in 
    "bcdefghijklmnopqrstuvwxyz"]

data1 = []

for url in urls:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')[1:-1]
    for paragraph in paragraphs:
    # Check for unwanted phrases and skip if they are found
        if any(phrase in paragraph.get_text() for phrase in ["Back to Spanish.", "Spanish idioms are essential to understanding and communicating","Translation prices"]):
            continue
        # Append the text of the paragraph to data1, stripping any leading/trailing whitespace
        if paragraph != '':
            data1.append(paragraph.get_text().strip())

# Process the data to fit into the DataFrame structure
processed_data = []
for item in data1[:-1]:
    parts = item.split('\n\t\t')
    if '\n' in item:
        parts = item.split('\n')
    if len(parts) != 1:
        before_tab = parts[0]
        after_tab = parts[1]
        
        # Check if '1.' exists in the part after '\n\t\t' and split further if it does
        example_sentence = None
        if '1.' in after_tab:
            after_tab_parts = after_tab.split('1.', 1)
            after_tab = after_tab_parts[0].strip()
            example_sentence = '1.' + after_tab_parts[1]

    processed_data.append([before_tab, after_tab, example_sentence])

# Create a DataFrame
df3 = pd.DataFrame(processed_data, columns=['Phrase', 'Meaning', 'Example'])

# Save the DataFrame to a CSV file
df3.to_csv('Spanish_idioms_3.csv', index=False)
