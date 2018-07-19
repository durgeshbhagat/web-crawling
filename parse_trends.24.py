import os
import sys
import bs4
import json


ip_dir = 'trends24_india'
op_dir= 'parsed_trends24_india'
try:
    os.mkdir(op_dir)
except:
    print('%s dir exists' %(op_dir))
    
file_list = os.listdir(ip_dir)
trending_word = {}
for fname in file_list:
    fname_total = '%s/%s' %(ip_dir, fname)
    fin = open(fname_total,'r')
    s = fin.read()
    fin.close()
    soup = bs4.BeautifulSoup(s, 'html.parser')
    soup_trend = soup.find('div' , attrs= {'id' :'trend-list'})
    soup_trend_list = soup_trend.findAll('div', attrs= { 'class' : 'trend-card'})
    for i,soup in enumerate(soup_trend_list,1):
        
        time_stamp = soup.find('h5').get_text() 
        print(i, soup, time_stamp)
        if time_stamp not in trending_word:
            top_word_list = soup.findAll('li')
            trending_word[time_stamp]= []
            for j,word in enumerate(top_word_list,1):
                link = word.find('a')
                trending_word[time_stamp].append((j, link.get_text(), link['href']))
                

                
    #print(len(soup_trend_list))
    #print(soup_trend_list[0])
    
fout_name = 'trends24.json'
fout_name_total = '%s/%s' %(op_dir, fout_name)
fout = open(fout_name_total, 'w')
json.dump(trending_word, fout, indent =4)
fout.close()
