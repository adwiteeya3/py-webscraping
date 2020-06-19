import requests
import bs4

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)    # To retrieve the HTML data and store it in the object

soup = bs4.BeautifulSoup(page.content, 'html.parser')   # Takes the HTML content from page and convert it into python object

results = soup.find(id='ResultsContainer')  # To find the specific HTML element by its ID
#print(results.prettify())  # To show the output of results in HTML contained within the <div>, use prettify()

jobs_element = results.find_all('section', class_='card-content')   # To find the HTML elements by class name. find_all returns an iterable which displays all the job postings on that page
'''
for i in results:
    print(i, end="")
'''
### The below piece of code filtered the list of jobs along with the location.

for i in jobs_element:
    title_element = i.find('h2', class_='title')
    location_element = i.find('div', class_='location')
    company_element = i.find('div', class_='company')

    if None in (title_element, location_element, company_element):  # This is used for the error None type which is occurring due to advertisements in the page. So this loops skip over all the None values for title
        continue

    print(title_element.text.strip())       # .text extracts the text from HTML tags and .strip() removes extra whitespaces
    print(location_element.text.strip())
    print(company_element.text.strip())
    print()

### The below piece of  code filtered the list of jobs associated only with python and provides the link along with it in order to apply for the job

python_jobs = results.find_all('h2', string= lambda text:'python' in text.lower()) # This piece of code find only those jobs which is related to Python Developer
print(len(python_jobs)) # returns 1

for j in python_jobs:       # To display the link of job.
    link = j.find('a')['href']  # On the page, links are contained inside <a> tag.
    print(j.text.strip())
    print(f"Apply for this job here:{link}")    # by using F-string, the expressions are replaced with their values jus like % and .format
