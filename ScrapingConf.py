from requests import get

url = 'https://tenbound.com/conference/'

response = get(url)

from bs4 import BeautifulSoup

# creates the text to be parsed from web page
html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)

Conference_Speakers = html_soup.find_all('div', class_ = 'uk-width-3-4')


first_speaker = Conference_Speakers[0]
first_speaker
first_speaker.h4.text

title = []

# prints using original container and adjusting the i value
# also appends the person into array called title
i=-1
for titles in Conference_Speakers:
    i += 1
    person = Conference_Speakers[i]
    person
    person.h4.text
    title.append(person.h4.text)
    print(person.text)



# traverses through the array title and then prints the values
j=-1
for person in title:
    j += 1
    print()
    print(title[j])


print()
print("This is the sorted array")
print()

# sorts the array and prints including title
print(sorted(title))


print()
print()

Conference_Sponsors = html_soup.find_all('div', class_ = 'uk-container-center')
first_sponsor = Conference_Sponsors[0]
first_sponsor
first_sponsor.text
print(first_sponsor)




