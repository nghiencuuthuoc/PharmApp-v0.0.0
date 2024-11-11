# Copyright 2021 | Nghiên Cứu Thuốc | RD Pharma Plus

# Email: nghiencuuthuoc@gmail.com | info@nghiencuuthuoc.com

# Web: http://www.nghiencuuthuoc.com

#See more: https://twitter.com/nghiencuuthuoc | https://facebook.com/nghiencuuthuoc

# Note Dev:
# 20210828: update x if no find drug
# 20210829 == pharmapp_v0.8.py: build function:
    # find_drug_on_dailymed 
    # get_inactive_ingredient
    # open_linklist

def find_drug_on_dailymed():
    """
    The Function find_drug_on_dailymed() find drug from DailyMed.
    Example: find_drug_on_dailymed()
    Enter Drug Name:Azithromycin
    """
    from bs4 import BeautifulSoup as bsoup
    import requests
    import re

    ## First Part: Enter Drug Name and Use DailyMeds Search Engigne to Bring Up All Pages in a List##

    drug = input("Enter Drug Name:")
#     drug = 'tocilizumab'
    print(f'{drug}:')
    base_url = 'https://dailymed.nlm.nih.gov/dailymed/search.cfm?labeltype=all&query=' + drug
    r = requests.get(base_url)
    soup = bsoup(r.text, 'html.parser')
    #finds all the total pages tags#
    numpages = soup.find_all('span', re.compile(r".*total-pages.*"))
    x = list()
    for num in numpages:
        num = str(num)
        x = re.findall('>(.*?)<', num)    
    if len(x) == 0:
        print(f"Not find {drug} on DailyMed")
    else:
        print(f"Find {int(x[0])} pages of {drug} on DailyMed")



def get_inactive_ingredient():
    """
    The Function get_inactive_ingredient() get inactive ingredient from DailyMed.
    Save to text file azithromycin.txt and azithromycin_linklist.txt
    Example: get_inactive_ingredient()
    Enter Drug Name:Azithromycin
    """
    
    print("Start import package")
    from bs4 import BeautifulSoup as bsoup
    import requests
    import re
    import urllib
    from urllib.request import urlopen
    # import ssl
    from itertools import groupby
    import pandas as pd
    import numpy as np
    import os
    print("Import package done!")
    # Remove old file
    # os.remove("output.txt")
    
    if os.path.exists('output.txt'):
        os.remove('output.txt')
    else:
        print("Outout file done!")
    if os.path.exists('linklist.txt'):
        os.remove('linklist.txt')
    else:
        print("Link file done!")
        
    if os.path.exists('output1.txt'):
        os.remove('output1.txt')
    else:
        print("Outout1 file done!")
    
    # clear screen
    clear = lambda: os.system('cls')
    clear()
    
    ## First Part: Enter Drug Name and Use DailyMeds Search Engigne to Bring Up All Pages in a List##
    print("#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#")
    print("PharmApp // Copyright 2021 // NGHIEN CUU THUOC // RnD PHARMA PLUS // WWW.NGHIENCUUTHUOC.COM")
    print("Email: nghiencuuthuoc@gmail.com // info@nghiencuuthuoc.com")
    print("https://twitter.com/nghiencuuthuoc // https://facebook.com/nghiencuuthuoc")
    print("#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#")
    print("Drug Discovery Development TopList With Python")
    print("THANKS FOR USING")
    print("#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#")
    drug_raw = input("Enter Drug Name:")
    drug = drug_raw.lower()
    # new_name = input("name for output file: ") # for rename
    new_name =  drug
    base_url = 'https://dailymed.nlm.nih.gov/dailymed/search.cfm?labeltype=all&query=' + drug
    r = requests.get(base_url)
    
    soup = bsoup(r.text, 'html.parser')
    #finds all the total pages tags#
    numpages = soup.find_all('span', re.compile(r".*total-pages.*"))
    # totpage = list()
   
    x = list()
    for num in numpages:
        num = str(num)
        x = re.findall('>(.*?)<', num)
    
    if len(x) == 0:
        print(f"Not find {drug} on DailyMed")
    else:
        print(f"Find {int(x[0])} pages of {drug} on DailyMed")
    
    totalpages = int(x[0])
    
    # Add 1 because Python range.
    url_list = ["{}&page={}".format(base_url, str(page)) for page in range(1, totalpages + 1)]
    # print(url_list)
    
    ## Second Part: Take the lista of links and get a list of those links#######
    
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
            # print(linklist)
            with open("linklist.txt", 'w') as output:
                for row in linklist:
                    output.write(str(row) + '\n')
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
                    drug = drug + "888000" #this puts a handlbetadibee on the inactive ingredients
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
            # print(df)
            # df.to_csv(r'output.csv')
            df.to_csv('output.txt', mode='a', index = False, header=True)
            # writer = pd.ExcelWriter('output.xlsx')
            # df.to_excel(writer)
            # writer.save()
      
            
    # Remove line MainDrug,NDC,Strength,Formulation,Inactive
    with open("output.txt", "r") as f:
        lines = f.readlines()
    with open("output.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != "MainDrug,NDC,Strength,Formulation,Inactive":
                f.write(line)
    
    # Merge file comtain header
    import shutil
    
    with open('output1.txt','wb') as wfd:
        for f in ['header.txt','output.txt']:
            with open(f,'rb') as fd:
                shutil.copyfileobj(fd, wfd)
    
    # rename file output.txt
    old_name = "output1.txt"
    new_name1 = new_name+"_inactive_ingredient_list.txt"
    if os.path.exists(new_name1):
        os.remove(new_name1)
        os.rename(old_name,new_name1)
    else:
        os.rename(old_name,new_name1)
    print(f"Save inactive ingredient of {new_name} on file {new_name1} infolder {os.getcwd()}")
    
    # Rename linklist
    old_name1 = 'linklist.txt'
    name_linklist = new_name+"_linklist" +".txt"
    if os.path.exists(name_linklist):
        os.remove(name_linklist)
        os.rename(old_name1,name_linklist)
    else:
        os.rename(old_name1,name_linklist)
    print(f"Save link DailyMed of {new_name} on file {name_linklist} in folder {os.getcwd()}")
    # round
    # import runpy
    # runpy.run_path(path_name='inactive_ingredient_save_txt_header_final_20210717.py')
    
def open_linklist():
    
    """
    Open linklist text file. The file saved from get_inactive_ingredient().
    The text file sample azithromycin_linklist.txt.
    Example: Enter a name file text: azithromycin_linklist.txt
    """
    
    # get list file txt
    # import subprocess as sp
    import webbrowser
    import time
    # import os
    
    # An input is requested and stored in a variable
    name = input ("Enter a name file text: ")
    number_second_text = input ("Enter a number seconds: ")
    
    # Converts the string into a integer. If you need
    # to convert the user input into decimal format,
    # the float() function is used instead of int()
    number_second = int(number_second_text)
    
    # Prints in the console the variable as requested
    print ("The number you entered is: ", number_second)
    
    f = open(name,'r')
    urls = f.readlines()
    for url in urls:
        # child = sp.Popen(["C:/Program Files (x86)/Google/Chrome/Application/chrome.exe", url ])
        # child = sp.Popen(["C:/Program Files/Google/Chrome/Application/chrome.exe", url ])
        webbrowser.open(url)  # Go to example.com
        time.sleep(number_second)
        print(url)
    
    # clear 
    # clear = lambda: os.system('cls')
    # clear()

