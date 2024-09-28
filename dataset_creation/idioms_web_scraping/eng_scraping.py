import requests
from bs4 import BeautifulSoup
import pandas as pd
# URL of the webpage you want to scrape
url = 'https://byjus.com/english/idioms-in-english/'

# Fetch the content of the webpage
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all <td> elements in the document
table_cells = soup.find_all('td')

data = []

for i in range(3, len(table_cells), 3):  
    if i+2 < len(table_cells):  
        idiom = table_cells[i].text.strip()
        meaning = table_cells[i+1].text.strip()
        sentence_example = table_cells[i+2].text.strip()
        data.append([idiom, meaning, sentence_example])
# Create a DataFrame with the extracted data
df = pd.DataFrame(data, columns=['Idiom', 'Meaning', 'Sentence Example'])

df.to_csv('English_idioms_1.csv', index=False)

#############################################################################################################
url = 'https://leverageedu.com/blog/idioms-with-examples/'

# Fetch the content of the webpage
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')


first_h2 = soup.find('h2', class_='wp-block-heading', id='h-79-idioms-amp-phrases-with-meaning-for-advance-vocabulary')


second_h2 = soup.find('h2', class_='wp-block-heading', id='h-55-best-idioms-amp-phrases-for-competitive-exams')

paragraphs = []

# Find all <p> tags between the two <h2> tags
if first_h2 and second_h2:
    for tag in first_h2.find_next_siblings():
        if tag == second_h2:
            break
        if tag.name == 'p' and 'has-pale-ocean-gradient-background' not in tag.get('class', []):
            paragraphs.append(tag.text)


new_data = []
for i in range(1, len(paragraphs), 2):
    if i + 1 < len(paragraphs):
        # Extract the idiom from the first string
        idiom_part = paragraphs[i].split('. ', 1)[1].strip() if '. ' in paragraphs[i] else paragraphs[i]

        # Extract meaning and example from the second string
        second_part = paragraphs[i + 1]
        meaning_part = second_part.split('Meaning: ')[1].split('Example: ')[0].strip() if 'Meaning: ' in second_part else second_part
        example_part = second_part.split('Example: ')[1].strip() if 'Example: ' in second_part else ''

        # Clean up the example part by removing '\xa0' and other unwanted characters
        example_part = example_part.replace('\xa0', '').strip()

        new_data.append([idiom_part, meaning_part, example_part])

df2 = pd.DataFrame(new_data, columns=['Idiom', 'Meaning', 'Sentence Example'])
df2.to_csv('English_idioms_2.csv', index=False)
#############################################################################################################




url = 'https://leverageedu.com/blog/idioms-with-examples/'

response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

start_h2 = soup.find('h2', id='h-55-best-idioms-amp-phrases-for-competitive-exams')
end_h2 = soup.find('h2', id='h-30-most-popular-idioms-with-examples-for-students')

data = []

if start_h2 and end_h2:
    for tag in start_h2.find_next_siblings():
        if tag == end_h2:
            break
        if tag.name == 'p':
            text = tag.text.strip()
            # Split the text to extract idiom, meaning, and example
            if ' – ' in text and 'Example:' in text:
                idiom_info, example_text = text.split(' – ', 1)
                idiom = idiom_info.split('.')[1].strip()
                meaning, example = example_text.split('Example:', 1)
                data.append([idiom, meaning.strip(), example.strip()])

# Create a DataFrame from the extracted data
df3 = pd.DataFrame(data, columns=['Idiom', 'Meaning', 'Sentence Example'])

df3.to_csv('English_idioms_3.csv', index=False)

#############################################################################################################

url = 'https://leverageedu.com/blog/idioms-with-examples/'

# Fetch the content of the webpage
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

start_h2 = soup.find('h2', id='h-30-most-popular-idioms-with-examples-for-students')
end_h2 = soup.find('h2', id='h-5-best-idioms-with-examples-for-happiness')


paragraphs = []

if start_h2 and end_h2:
    for tag in start_h2.find_next_siblings():
        if tag == end_h2:
            break
        if tag.name == 'p':
            paragraphs.append(tag.text)


data = []

# Parse each paragraph to extract the idiom, its meaning, and the example
for paragraph in paragraphs:
    if 'Meaning:' in paragraph and 'Example:' in paragraph:
        parts = paragraph.split('Meaning:', 1)
        idiom = parts[0].split('.', 1)[1].strip() if '.' in parts[0] else parts[0].strip()
        meaning, example = parts[1].split('Example:', 1)
        data.append([idiom, meaning.strip(), example.strip()])

df4 = pd.DataFrame(data, columns=['Idiom', 'Meaning', 'Sentence Example'])
df4.to_csv('English_idioms_4.csv', index=False)

#############################################################################################################

url = 'https://www.oxfordinternationalenglish.com/dictionary-of-british-slang/'

# Fetch the webpage
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

start_div = soup.find('div', {'id': '1', 'class': 'wysiwyg'})

strong_texts = []
other_texts = []

first_p_tag_skipped = False
for tag in start_div.find_all('p', recursive=True):
    if not first_p_tag_skipped:
        first_p_tag_skipped = True
        continue  # Skip the first <p> tag

    if "We hope you find this dictionary of British slang useful for your time here!" in tag.text:
        break  # Break if the specific text is found

    # Extract and store text from <strong> tags
    strong_text = " ".join([s.get_text() for s in tag.find_all('strong')])
    strong_texts.append(strong_text)

    # Remove <strong> tags from the <p> tag and get the remaining text
    for strong_tag in tag.find_all('strong'):
        strong_tag.decompose()
    other_text = tag.get_text(strip=True)
    other_texts.append(other_text)

# Create a DataFrame with the extracted data
df4 = pd.DataFrame({
    'Strong Text': strong_texts,
    'Other Text': other_texts
})
df4.to_csv('English_idioms_5.csv', index=False)
############################################################################################

data2 = []

urls  = ["https://www.languagerealm.com/english/englishslang.php"]+ [ "https://www.languagerealm.com/english/englishslang_"+ i +".php" for i in 
   ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]]

data2 = []

for url in urls:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')[1:-1]
    current_row = []

    for paragraph in paragraphs:
        text = paragraph.get_text().strip().replace('\n\t\t', ' ')  # Replacing the breaks with a space

        if any(phrase in text for phrase in ["Back to English.", "This dictionary is a comprehensive"]):
            continue  # Skip the iteration if the paragraph contains any specified phrases

        strong_tag = paragraph.find('strong')
        if strong_tag:
            if current_row:
                data2.append(current_row)
            current_row = [strong_tag.get_text().strip()]
   
        if current_row:  # Make sure there's a strong text in the current row
            em_tag = paragraph.find('em')
            if em_tag:
                em_text = em_tag.get_text().strip()
                current_row.append(em_text)
                em_end_index = em_tag.next_sibling
                if em_end_index:
                    text_after_em = str(em_end_index).strip().replace('\n\t\t', ' ')
                    if '1.' in text_after_em:
                        parts = text_after_em.split('1.', 1)
                        current_row.append(parts[0].strip())
                        if len(parts) > 1:
                            current_row.append(parts[1].strip())
                    else:
                        current_row.append(text_after_em)
            else:
                if 'idiom.' in text:
                    parts = text.split('idiom.', 1)
                    current_row.append('idiom.')
                elif 'phr.' in text:
                    parts = text.split('phr.', 1)
                    current_row.append('phr.')
                elif 'inter.' in text:
                    parts = text.split('inter.', 1)
                    current_row.append('inter.')
                elif 'adj;' in text:
                    parts = text.split('adj;', 1)
                    current_row.append('adj;')

                if len(parts) > 1:
                    description = parts[1].strip()
                    if '1.' in description:
                        parts_2 = description.split('1.', 1)
                        current_row.append(parts_2[0].strip())
                        if len(parts_2) > 1:
                            parts_3 = parts_2[1].strip().split('2.', 1)
                            current_row.append(parts_3[0].strip())
                else:
                    current_row.append(text)
    if current_row:
        data2.append(current_row)

# Ensure that all rows have the same number of columns
max_cols = max(len(row) for row in data2)
for row in data2:
    row.extend([''] * (max_cols - len(row)))

column_names = ['Strong Text'] + [f'Column {i}' for i in range(1, max_cols)]
df6 = pd.DataFrame(data2, columns=column_names)
df6.to_csv('English_idioms_6.csv', index=False)