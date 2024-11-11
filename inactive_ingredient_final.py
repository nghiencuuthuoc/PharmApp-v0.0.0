from bs4 import BeautifulSoup as bsoup
import requests
import re
import urllib
from urllib.request import urlopen
import ssl
from itertools import groupby
import pandas as pd
import numpy as np
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

## First Part: Enter Drug Name and Use DailyMeds Search Engigne to Bring Up All Pages in a List##

drug = input("Enter Drug Name:")
base_url = 'https://dailymed.nlm.nih.gov/dailymed/search.cfm?labeltype=all&query=' + drug
r = requests.get(base_url)

soup = bsoup(r.text, 'html.parser')
#finds all the total pages tags#
numpages = soup.find_all('span', re.compile(r".*total-pages.*"))
totpage = list()
for num in numpages:
    num = str(num)
    x = re.findall('>(.*?)<', num)
totalpages = int(x[0])
# Add 1 because Python range.
url_list = ["{}&page={}".format(base_url, str(page)) for page in range(1, totalpages + 1)]
#print(url_list)

## Second Part: Take the list of links and get a list of those links#######

for fff in url_list:
    # For avoid 403-error using User-Agent
    req = urllib.request.Request(fff, headers={'User-Agent' : "Magic Browser"})
    response = urllib.request.urlopen( req )
    html = response.read()
    # Parsing response
    soup = bsoup(html, 'html.parser')
    wwwlist= list()
    tags= soup('a')
    for tag in tags:
        mlink = tag.get('href')
        wwwlist.append(mlink)
    resi = list()
    for x in wwwlist:
        if x == None:
            wwwlist.remove(x)
            continue
    goodlist = list(filter(None, wwwlist)) #this removes Nonetype from the list, this was a problem
    subs = 'dailymed/drugInfo.cfm' #gives  variable to what im looking for
    resi = [i for i in goodlist if subs in i] #finds all the links
    linklist = list()
    for long in resi:
        long = "https://dailymed.nlm.nih.gov" + long #this add to the full website
        linklist.append(long)
        continue

### This takes all the links and adds them to the database####    Note this does not work yet for BRAND and COMBO Drugs

    for bbb in linklist:
        html = urlopen(bbb).read() #note removed , context=ctx from the urlopen (bbb)
        soup = bsoup(html, "html.parser")
        newlist = list()
        tags = soup('td') #this looks through the website and finds tags with "td")
        for tag in tags:
            tag = str(tag)
            if tag == ".":
                tags.remove(tag)
                continue
            ndc = (re.findall("NDC:(.*?)</td>", tag)) #finds all the NDCs
            for num in ndc:
                num = str(num)
                num = (re.findall("([0-9.\-]+)", num))
                for small in num:
                    shortndc = small[:+10] #trims the NDCS to first 7 digits
                    if shortndc not in newlist:
                        newlist.append(shortndc)
                        continue
            ing = (re.findall("<strong>(.*?)</strong>", tag)) #finds all the ingredients
            for lala in ing:
                newlist.append(lala)
                continue
            form = (re.findall('<span class="contentTableReg">(.*?)/span>', tag)) #finds all the formulations
            for newnew in form:
                newlist.append(newnew)
                continue
            strength = (re.findall('<td class="formItem">([0-9].*?)</td>', tag)) #this finds all strentghs and below removes fluff
            for gggg in strength:
                if "BOTTLE" in gggg:
                    continue
                elif "mm" in gggg:
                    strength.remove(gggg)
                    continue
                elif "pieces" in gggg:
                    strength.remove(gggg)
                    continue
                elif "/" in gggg: #this could be a problem for some meds.  dates with slashes showed up in apixiban so added this to remove them
                    strength.remove(gggg)
                    continue
                elif gggg.isdigit(): #this could be a problem.  APixiban had some odd number and this removed it
                    strength.remove(gggg)
                    continue
                newlist.append(gggg + 'stren')
        for period in newlist: #this was for the apixiban url.  For some reason it had a period in the newlist
            if period == ".":
                newlist.remove(period)
                continue
        res = [i[0] for i in groupby(newlist)] #this removes duplicate strings next to each other

        hdlist = list() #this list gives the drug name a handle to split on
        for drug in res:
            if drug == res[2]: #this puts a handle on the third item in the list, which is the main drug
                drug = drug + "111999"
                hdlist.append(drug)
            elif drug.endswith('stren'): #this puts a handle on strength
                drug = drug + 'stren'
                hdlist.append(drug)
            elif drug[0].isdigit(): #this puts a handle on the NDC
                drug = drug + 'happy'
                hdlist.append(drug)
            elif drug.endswith('<'): #this puts a handle on the formulation
                drug = drug + 'mad'
                hdlist.append(drug)
            else:
                drug = drug + "888000" #this puts a handle on the inactive ingredients
                hdlist.append(drug)

        df = pd.DataFrame(hdlist)
        df = df.rename(columns = {0 : 'stuff'}) #gives the column a name "stuff"
        df['MainDrug'] = df['stuff'].apply(lambda x: x.split('111999')[0].strip() if x.count('111999') > 0 else np.NaN).fillna(method='ffill') #this pulls all main drug names into a column
        df['Inactive'] = df['stuff'].apply(lambda x: x.split('888000')[0].strip() if x.count('888000') > 0 else np.NaN).fillna(method="ffill")
        df['NDC'] = df['stuff'].apply(lambda x: x.split('happy')[0].strip() if x.count('happy') > 0 else np.NaN).fillna(method="ffill")
        df['Strength'] = df['stuff'].apply(lambda x: x.split('strenstren')[0].strip() if x.count('strenstren') > 0 else np.NaN).fillna(method="ffill")
        df['Formulation'] = df['stuff'].apply(lambda x: x.split('<mad')[0].strip() if x.count('<mad') > 0 else np.NaN).fillna(method="ffill")
        df = df.dropna().drop('stuff', axis=1).reindex(columns=['MainDrug', 'NDC','Formulation','Inactive', 'Strength']).reset_index(drop=True) #for some reason this line removes all inactive except ndcs
        df['MainDrug'] = df['MainDrug'].str.lower() #need to make lower case to match that in formulation column
        df['Formulation']= df['Formulation'].str.lower()
        df['c'] = [Formulation.replace(MainDrug, '') for Formulation, MainDrug in zip(df['Formulation'], df['MainDrug'])] #this drop the main drug in formulation
        df = df.drop(['Formulation'], axis=1)
        df = df.rename(columns = {'c' : 'Formulation'})
        df = df.reindex(columns=['MainDrug', 'NDC', 'Strength', 'Formulation', 'Inactive']) #this puts the columns in order
        df_prev = df['Inactive'].shift(1) #this removes duplicates
        df = df[df.Inactive != df_prev] #this removes duplicates
        df = df.reset_index().drop_duplicates(subset=['NDC','Inactive'],keep='first').set_index('index') #was getting duplicate inactive, this removes those duplicates
        print(df)
