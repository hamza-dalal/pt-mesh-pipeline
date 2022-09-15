# ============================================================================= 
 # This code is at initial stage and has to be worked on several aspects.  
 # It includes data only from first page.  
 # Due to time restriction, was not able to work on multiple sites data scraping. Will work on this later if possible.  
 # ============================================================================= 
  
  
 #%% Installing and importing modules 
  
 from bs4 import BeautifulSoup 
 import requests 
 import csv 
  
  
 #%% Main code for Web Scraping 
  
 #url = "https://www.contractsfinder.service.gov.uk/Search/Results" 
 class Scraper:  
     def __init__(self, aurl): 
         self.url = aurl 
         html = requests.get(aurl) 
         soup = BeautifulSoup(html.content) 
         tendors = soup.find_all("div", class_ = "search-result") 
         file = "scraper.csv" 
         f = open(file,'w',newline = '') 
         g = csv.writer(f) 
         header = ["Title", "Organization"] 
         g.writerow(header) 
         for tendor in tendors: 
             title = tendor.find("div", class_ = "search-result-header").a.text 
             l=[title] 
             g.writerow(l) 
         f.close() 
  
  
         # lists = soup.findall("a", class_ = "get-started group") 
         # print(lists) 
         # file = "scraper.csv" 
         # f = open(file,'w',newline = '') 
         # g = csv.writer(f) 
  
 # This will generate a csv file named Scraper in the working directory containing data 
 Scraper("https://www.contractsfinder.service.gov.uk/Search/Results") 
  
  
  
  
 #%% Url parser 
  
 url = "https://www.contractsfinder.service.gov.uk/Search/Results" 
 html = requests.get(url) 
 # soup = BeautifulSoup(html.text,'html.parser') 
 soup = BeautifulSoup(html.content) 
  
 #%% Creating and opening csv file 
  
 file = "scraper.csv" 
 f = open(file,'w',newline = '') 
 g = csv.writer(f) 
 header = ["Title", "Organization"] 
 g.writerow(header) 
 # f.close() 
  
 #%% Scraper 
 tendors = soup.find_all("div", class_ = "search-result") 
 for tendor in tendors: 
     title = tendor.find("div", class_ = "search-result-header").a.text 
     l=[title] 
     g.writerow(l) 
  
 f.close() 
  
  
 #%% Function to go to next page | not completed 
 def getnextpage(soup): 
     page = soup.find("ul", class_ = "gadget-footer-paginate") 
     if page.find("li", class_ = "standard-paginate-next-box standard-paginate-next-icon"): 
         url1 = page.find_all("li", class_ = "standard-paginate").find("a").get(["href"]) 
         print(url) 
     else: 
         print("FALSE") 
          
 print(getnextpage(soup)) 
          
 page = soup.find("ul", class_ = "gadget-footer-paginate")     
 print(page)     
 
