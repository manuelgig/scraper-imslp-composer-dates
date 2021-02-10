# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 16:06:22 2020

@author: Manuel Gigena
"""

from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import pandas as pd
import numpy as np

def composerDates(composer_names,wd,output_file='composer_dates.csv'):
    processed = []
    
    for elem in composer_names:
        try: 
            #elem=data[400]
            comp_name=elem.replace(' ','_')
            print(comp_name)
            
            url_='https://imslp.org/wiki/Category:{}'.format(comp_name)
            url = urllib.parse.quote(url_.encode('utf8'), ':/')
            source = urllib.request.urlopen(url).read() 
    
        except:
            print("Couldn't process {}".format(comp_name))
            processed.append([comp_name,np.NaN,np.NaN,np.NaN,np.NaN,'no'])
            continue
    
        try:
            soup = BeautifulSoup(source,'lxml')
            soup_find=soup.find(class_='cp_firsth').text
            ss=soup_find[soup_find.find("(")+1:soup_find.find(")")].split('—')
            born, death = '',''
            if len(ss)>1:
                born_, death_ =ss[0], ss[1]
                try:
                    string_=ss[0].replace('?','').strip()
                    if string_[:3]=='ca.':
                        born=string_[3:7]                
                    if string_[-3:]=='ca.':
                        born=string_[:5]    
                    elif string_[:3]=='fl.': # 'fl.' is for 'flourished (ca.) xxxx' In a future version I could add a column indicating whether the date was ca/fl/ etc
                        born=string_[3:].replace('s','')
                    else:
                        born = string_[-4:]
                    len_born=len(born)
                except:
                    born=''
                try:
                    string_=ss[1].replace('?','').strip()
                    if string_[:3]=='ca.':
                        death=string_[3:7]                                
                    if string_[-3:]=='ca.':
                        death=string_[:5]
                    if string_[:3]=='fl.': # 'fl.' is for 'flourished (ca.) xxxx' In a future version I could add a column indicating whether the date was ca/fl/ etc
                        death=string_[3:].replace('s','')
                    else:
                        death = string_[-4:]
                    len_death=len(death)
                except:
                    death=''
            else:
                string_=ss[0].replace('?','').strip()
                if string_[:2]=='b.':
                    born = string_[-4:]
                    death=''
                elif string_[:3]=='fl.':    
                    death = string_[-4:]
                else:
                    death = string_[-4:]
                len_born=len(born)
                len_death=len(death)
                
            processed.append([comp_name,born,death,len_born,len_death,'yes'])
          
        except:
            print('hubo algún problema al procesar {}'.format(comp_name))
            processed.append([comp_name,np.NaN,np.NaN,np.NaN,np.NaN,'no'])
            continue
        
    processed = pd.DataFrame(processed,columns=['composer','year_birth','year_death','len_year_birth','len_year_death','retrieved']).replace('_',' ',regex=True)
    processed.to_csv('{}{}'.format(wd,output_file),index=False)
        
    return processed

# Example using composers from a list of IMSLP composer names

path = r'C:/Users/m/Google Drive/27 musica en xml/06_varios/'.replace('\\','/')+'/'
composer_series = pd.read_csv('{}composer_names.csv'.format(path),encoding="utf-8").composer

test = composerDates(composer_series[:10],path)

