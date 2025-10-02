import requests
from bs4 import BeautifulSoup

linkedin_SoftwareEngineer = requests.get("https://www.linkedin.com/jobs/search/?currentJobId=3609026700&geoId=100737633&keywords=Software%20Engineer&location=San%20Diego%20County%2C%20California%2C%20United%20States&refresh=true")
linkedin_GameDevelopment = requests.get("https://www.linkedin.com/jobs/search/?currentJobId=3607431293&geoId=100737633&keywords=game%20developer&location=San%20Diego%20County%2C%20California%2C%20United%20States&refresh=true")
linkedin_CommunityManager = requests.get("https://www.linkedin.com/jobs/search/?currentJobId=3607319067&f_WT=2&keywords=Community%20Manager")
linkedin_SocialMedia = requests.get("https://www.linkedin.com/jobs/search/?currentJobId=3603310787&f_JT=F&f_WT=2&geoId=103644278&keywords=social%20media&location=United%20States&refresh=true")

#default globals
soup = BeautifulSoup(linkedin_SoftwareEngineer.text, 'lxml')
jobs = soup.find_all('div', class_='base-card')

def grabListings(type=None): #modify globals for the searching
  global soup, jobs
  if(type == "SoftwareEngineer"):
    soup = BeautifulSoup(linkedin_SoftwareEngineer.text, 'lxml')
    jobs = soup.find_all('div', class_='base-card')
  elif(type == "GameDeveloper"):
    soup = BeautifulSoup(linkedin_GameDevelopment.text, 'lxml')
    jobs = soup.find_all('div', class_='base-card')
  elif(type == "SocialMedia"):
    soup = BeautifulSoup(linkedin_SocialMedia.text, 'lxml')
    jobs = soup.find_all('div', class_='base-card')
  else:
    soup = BeautifulSoup(linkedin_CommunityManager.text, 'lxml')
    jobs = soup.find_all('div', class_='base-card')


def job_info(j_card):
  job_title = j_card.find('h3', class_='base-search-card__title').text
  job_company = j_card.find('h4', class_='base-search-card__subtitle').text
  job_location = j_card.find('span', class_='job-search-card__location').text
  job_link = j_card.find('a', class_='base-card__full-link')['href']

  # formatting
  job_title = job_title.strip()
  job_company = job_company.strip()
  job_location = job_location.strip()
  job = {
    'title': job_title,
    'company': job_company,
    'location': job_location,
    'link': job_link
  }
  return job


def get_jobs(type):
  grabListings(type)
  jList = []
  global jobs

  for job in jobs:
    j = job_info(job)
    jList.append(j)
  return jList


Get_Jobs = get_jobs(type)
