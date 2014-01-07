import sys, urllib2, csv
from bs4 import BeautifulSoup

def scrape_pr():
   
   #initialize source url and set maximum count
   src_url = 'http://qa.governor.state.nc.us/NewsItems/PressReleaseDetail.aspx?newsItemID='
   url_count = 1
   max_count = 10
   
   #load data from pages
   
   #initialize csv file with headers
   writer = csv.writer(open('pr_database.csv', 'wb'))
   writer.writerow(['uid','date','hed','text'])
   text_data = ""   
   
   while url_count <= max_count:
      try:
         print src_url + str(url_count)
         html_file = urllib2.urlopen(src_url + str(url_count)).read()
         soup = BeautifulSoup(html_file)
         
         date = soup.find(id="ctl00_ContentPlaceHolder1_FormView1_ReleaseDateLabel").string
         print date
         
         hed = soup.h2.string
         print hed
         
         #print soup.find(id="ctl00_ContentPlaceHolder1_FormView1_Label1").string
         
         #for string in soup.find(id="ctl00_ContentPlaceHolder1_FormView1_Label1").stripped_strings:
            #print(repr(string))
         
         for string in soup.find(id="ctl00_ContentPlaceHolder1_FormView1_Label1").stripped_strings:
            text_data += repr(string)
         print text_data
         
         writer.writerow([url_count, date, hed, text_data])

      except:
         print 'ERROR: '
         print url_count
      url_count += 1

   #print '...wrapping up'

if __name__ == '__main__':
   
   scrape_pr()
   #print '...done'