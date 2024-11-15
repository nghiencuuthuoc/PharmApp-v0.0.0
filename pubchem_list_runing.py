"""
Copyright 2021 | Nghiên Cứu Thuốc | RD Pharma Plus

Email: nghiencuuthuoc@gmail.com | info@nghiencuuthuoc.com

Web: http://www.nghiencuuthuoc.com

See more: https://twitter.com/nghiencuuthuoc | https://facebook.com/nghiencuuthuoc

"""



drugs = ["Acyclovir", "Adalimumab", "Adapalene", "Adefovir dipivoxil", "Adenosine", "Afatinib", "Aflibercept", "Agomelatine", "Albendazole", "Alectinib", "Alemtuzumab", "Alfaxalone", "Alirocumab", "Aliskiren", "Alitretinoin", "Allopurinol", "Alogliptin", "Alprazolam", "Alteplase", "Aluminum chloride", "Aluminum hydroxide", "Aluminum oxide", "Amantadine", "Ambrisentan", "Ambroxol", "Amifostine", "Amikacin", "Amiloride", "Aminobenzoic", "Aminocaproic", "Aminolevulinic", "Aminophylline", "Aminosalicylic", "Amiodarone", "Amisulpride", "Amitriptyline", "Amlodipine", "Ammonium chloride", "Amodiaquine", "Amoxicillin", "Amphetamine", "Amphotericin B", "Ampicillin", "Anakinra", "Anastrozole", "Angiotensin II", "Anidulafungin", "Apixaban", "Apomorphine", "Apremilast", "Aprepitant", "Aprotinin", "Argatroban", "Aripiprazole", "Arsenic trioxide", "Artemether", "Artesunate", "Articaine", "Ascorbic", "Asenapine", "Asunaprevir", "Atazanavir", "Atenolol", "Atezolizumab", "Atomoxetine", "Atorvastatin", "Atovaquone", "Atropine", "Attapulgite", "Auranofin", "Avelumab", "Axitinib", "Azacitidine", "Azathioprine", "Azithromycin", "Aztreonam", "Bacitracin", "Baclofen", "Baricitinib", "Basiliximab", "Bazedoxifene", "Bedaquiline", "Belatacept", "Belimumab", "Bendamustine", "Benralizumab", "Benzalkonium", "Benznidazole", "Benzocaine", "Benzoic", "Benzoyl peroxide", "Benzyl alcohol", "Beta carotene", "Betahistine", "Betamethasone", "Bevacizumab", "Bexarotene", "Bezafibrate", "Bicalutamide", "Bimatoprost", "Biotin", "Bisoprolol", "Bivalirudin", "Bleomycin", "Blinatumomab", "Boceprevir", "Boric", "Bortezomib", "Bosentan", "Bosutinib", "Botulinum toxin type A", "Brentuximab vedotin", "Brexpiprazole", "Brimonidine", "Brinzolamide", "Brivaracetam", "Brodalumab", "Bromocriptine", "Budesonide", "Bumetanide", "Bupivacaine", "Buprenorphine", "Bupropion", "Buspirone", "Busulfan", "Butorphanol", "Cabazitaxel", "Cabergoline", "Cabozantinib", "Caffeine", "Calcipotriol", "Calcitriol", "Calcium alginate", "Calcium carbonate", "Calcium chloride", "Calcium Phosphate", "Camphor", "Canagliflozin", "Canakinumab", "Cangrelor", "Cannabidiol", "Capecitabine", "Capsaicin", "Captopril", "Carbamazepine", "Carbetocin", "Carbon dioxide", "Carbon monoxide", "Carboplatin", "Carfilzomib", "Cariprazine", "Carmustine", "Carvedilol", "Caspofungin", "Castor", "Cefazolin", "Cefepime", "Cefixime", "Cefoperazone", "Cefotaxime", "Ceftaroline fosamil", "Ceftazidime", "Ceftriaxone", "Cefuroxime", "Celecoxib", "Cephalexin", "Ceritinib", "Certolizumab pegol", "Cetirizine", "Cetuximab", "Cetylpyridinium", "Chloral hydrate", "Chlorambucil", "Chloramphenicol", "Chlorhexidine", "Chloroform", "Chloroquine", "Chlorpromazine", "Chlortetracycline", "Chlorthalidone", "Cholecalciferol", "Cholecystokinin", "Cholic", "Chondroitin sulfate", "Chymotrypsin", "Cidofovir", "Cilostazol", "Cimetidine", "Cinacalcet", "Ciprofloxacin", "Cisatracurium", "Cisplatin", "Citalopram", "Citicoline", "Citric", "Cladribine", "Clarithromycin", "Clenbuterol", "Clindamycin", "Clobazam", "Clobetasol", "Clofarabine", "Clofazimine", "Clomipramine", "Clonazepam", "Clonidine", "Clopidogrel", "Clotrimazole", "Clozapine", "Cobicistat", "Cobimetinib", "Cocaine", "Codeine", "Colchicine", "Colistin", "Collagenase clostridium histolyticum", "Corticotropin", "Crizotinib", "Cyclophosphamide", "Cycloserine", "Cyclosporine", "Cysteamine", "Cytarabine", "Dabigatran etexilate", "Dabrafenib", "Dacarbazine", "Daclatasvir", "Dacomitinib", "Dalbavancin", "Dalteparin", "Dantrolene", "Dapagliflozin", "Dapsone", "Daptomycin", "Daratumumab", "Darbepoetin alfa", "Darunavir", "Dasabuvir", "Dasatinib", "Daunorubicin", "Decitabine", "Deferasirox", "Deferiprone", "Deferoxamine", "Delamanid", "Denosumab", "Deoxycholic", "Dermatophagoides farinae", "Dermatophagoides pteronyssinus", "Desflurane", "Desipramine", "Desmopressin", "Desvenlafaxine", "Dexamethasone", "Dexketoprofen", "Dexmedetomidine", "Dexrazoxane", "Dextran", "Dextromethorphan", "Diacerein", "Diazepam", "Diazoxide", "Diclofenac", "Dienogest", "Diethylstilbestrol", "Digoxin", "Diltiazem", "Dimethyl fumarate", "Dimethyl sulfoxide", "Dinoprostone", "Diosmin", "Diphenhydramine", "Dipyridamole", "Disulfiram", "Dobutamine", "Docetaxel", "Dolutegravir", "Domperidone", "Donepezil", "Dopamine", "Doripenem", "Dorzolamide", "Doxazosin", "Doxorubicin", "Doxycycline", "Dronedarone", "Droperidol", "Drospirenone", "Dulaglutide", "Duloxetine", "Dupilumab", "Durvalumab", "Dutasteride", "Eculizumab", "Edaravone", "Edoxaban", "Efavirenz", "Elbasvir", "Elotuzumab", "Eltrombopag", "Elvitegravir", "Emicizumab", "Empagliflozin", "Emtricitabine", "Enalapril", "Enoxaparin", "Entecavir", "Enzalutamide", "Ephedrine", "Epinephrine", "Epirubicin", "Eplerenone", "Epoprostenol", "Eptifibatide", "Erenumab", "Eribulin", "Erlotinib", "Ertapenem", "Erythromycin", "Erythropoietin", "Escitalopram", "Esketamine", "Eslicarbazepine", "Esmolol", "Esomeprazole", "Estradiol", "Estriol", "Estrone", "Etanercept", "Ethambutol", "Ethanol", "Ethinylestradiol", "Etomidate", "Etonogestrel", "Etoposide", "Etoricoxib", "Etravirine", "Everolimus", "Evolocumab", "Exemestane", "Exenatide", "Ezetimibe", "Famotidine", "Favipiravir", "Febuxostat", "Felodipine", "Fenofibrate", "Fentanyl", "Fesoterodine", "Fexofenadine", "Fidaxomicin", "Filgrastim", "Finasteride", "Fingolimod", "Flecainide", "Flibanserin", "Fluconazole", "Fludarabine", "Flumazenil", "Fluocinolone acetonide", "Fluorescein", "Fluorouracil", "Fluoxetine", "Flurbiprofen", "Flutamide", "Fluticasone furoate", "Fluticasone", "Fluvastatin", "Fluvoxamine", "Folic", "Fondaparinux", "Formoterol", "Fosfomycin", "Fructose", "Fulvestrant", "Furosemide", "Fusidic", "Gabapentin", "Gadobutrol", "Gadoxetic", "Galactose", "Galantamine", "Ganciclovir", "Gatifloxacin", "Gefitinib", "Gemcitabine", "Gemfibrozil", "Gemtuzumab ozogamicin", "Gentamicin", "Ginkgo biloba", "Glatiramer", "Glecaprevir", "Gliclazide", "Glimepiride", "Glipizide", "Glucagon", "Glucosamine", "Glutamic", "Glutathione", "Glyburide", "Glycerin", "Glycine betaine", "Glycine", "Glycopyrronium", "Glycyrrhizic", "Golimumab", "Granisetron", "Grazoprevir", "Griseofulvin", "Guanfacine", "Guselkumab", "Haloperidol", "Halothane", "Helium", "Hemin", "Heparin", "Histamine", "Hyaluronic", "Hyaluronidase", "Hydralazine", "Hydrochlorothiazide", "Hydrocodone", "Hydrocortisone", "Hydrogen peroxide", "Hydromorphone", "Hydroquinone", "Hydrotalcite", "Hydroxocobalamin", "Hydroxychloroquine", "Hydroxyethyl Starch", "Hydroxyurea", "Hypochlorite", "Ibandronate", "Ibritumomab tiuxetan", "Ibrutinib", "Ibuprofen", "Icatibant", "Idarubicin", "Idarucizumab", "Idebenone", "Idelalisib", "Ifosfamide", "Iloprost", "Imatinib", "Imipenem", "Imipramine", "Imiquimod", "Indacaterol", "Indapamide", "Indigotindisulfonic", "Indomethacin", "Infliximab", "Ingenol mebutate", "Inositol", "Inotuzumab ozogamicin", "Insulin aspart", "Insulin beef", "Insulin degludec", "Insulin detemir", "Insulin glargine", "Insulin lispro", "Interferon beta-1a", "Interferon beta-1b", "Inulin", "Iodine", "Iodixanol", "Iohexol", "Ipilimumab", "Irbesartan", "Irinotecan", "Iron sucrose", "Iron", "Isavuconazole", "Isoflurane", "Isoniazid", "Isoprenaline", "Isotretinoin", "Itraconazole", "Ivabradine", "Ivacaftor", "Ivermectin", "Ixazomib", "Ixekizumab", "Kanamycin", "Kaolin", "Ketamine", "Ketoconazole", "Ketoprofen", "Ketorolac", "L-Glutamine", "L-Lysine", "Labetalol", "Lacosamide", "Lactic", "Lactulose", "Lamivudine", "Lamotrigine", "Lanreotide", "Lansoprazole", "Lanthanum carbonate", "Lapatinib", "Latanoprost", "Ledipasvir", "Leflunomide", "Lenalidomide", "Lenvatinib", "Lercanidipine", "Letermovir", "Letrozole", "Leucovorin", "Leuprolide", "Levamisole", "Levetiracetam", "Levobupivacaine", "Levodopa", "Levofloxacin", "Levonorgestrel", "Levosimendan", "Levothyroxine", "Lidocaine", "Linaclotide", "Linagliptin", "Lincomycin", "Lindane", "Linezolid", "Lipoic", "Liraglutide", "Lisdexamfetamine", "Lisinopril", "Lixisenatide", "Lomustine", "Loperamide", "Lopinavir", "Loratadine", "Lorazepam", "Lorcaserin", "Lornoxicam", "Losartan", "Lovastatin", "Lumacaftor", "Lumefantrine", "Lurasidone", "Macitentan", "Magnesium oxide", "Magnesium sulfate", "Malathion", "Mandelic", "Mannitol", "Maraviroc", "Mebendazole", "Medroxyprogesterone acetate", "Mefenamic", "Mefloquine", "Melatonin", "Meloxicam", "Melphalan", "Memantine", "Menadione", "Meperidine", "Mepivacaine", "Mepolizumab", "Mercaptopurine", "Meropenem", "Mesalazine", "Metamizole", "Metformin", "Methacholine", "Methadone", "Methimazole", "Methionine", "Methotrexate", "Methylcellulose", "Methylene blue", "Methylphenidate", "Methylprednisolone", "Meticillin", "Metoclopramide", "Metoprolol", "Metronidazole", "Mexiletine", "Micafungin", "Miconazole", "Midazolam", "Midodrine", "Midostaurin", "Mifepristone", "Milnacipran", "Milrinone", "Miltefosine", "Mineral", "Minocycline", "Minoxidil", "Mirabegron", "Mirtazapine", "Misoprostol", "Mitomycin", "Mitotane", "Mitoxantrone", "Modafinil", "Mogamulizumab", "Mometasone furoate", "Montelukast", "Morphine", "Moxidectin", "Moxifloxacin", "Mupirocin", "Mycophenolic", "Nalbuphine", "Nalmefene", "Naloxone", "Naltrexone", "Naproxen", "Natalizumab", "Natamycin", "Nebivolol", "Nelfinavir", "Neomycin", "Neostigmine", "Nepafenac", "Neratinib", "Nevirapine", "Niacin", "Nicardipine", "Niclosamide", "Nicorandil", "Nicotinamide", "Nicotine", "Nifedipine", "Nilotinib", "Nimesulide", "Nimodipine", "Nintedanib", "Nitazoxanide", "Nitric Oxide", "Nitrofurantoin", "Nitrogen", "Nitroglycerin", "Nitroprusside", "Nitrous", "Nitrous oxide", "Nivolumab", "Norepinephrine", "Norfloxacin", "Nortriptyline", "Noscapine", "Nusinersen", "Nystatin", "Obeticholic", "Obinutuzumab", "Ocrelizumab", "Ocriplasmin", "Octreotide", "Ofatumumab", "Ofloxacin", "Olanzapine", "Olaparib", "Olmesartan", "Olodaterol", "Omadacycline", "Omalizumab", "Ombitasvir", "Omeprazole", "Ondansetron", "Opium", "Oritavancin", "Orlistat", "Ornithine", "Oseltamivir", "Osimertinib", "Ouabain", "Oxacillin", "Oxaliplatin", "Oxcarbazepine", "Oxybutynin", "Oxycodone", "Oxygen", "Oxytetracycline", "Oxytocin", "Paclitaxel", "Palbociclib", "Paliperidone", "Palivizumab", "Palonosetron", "Panitumumab", "Panobinostat", "Pantoprazole", "Papaverine", "Parathyroid hormone", "Parecoxib", "Paricalcitol", "Paritaprevir", "Paromomycin", "Paroxetine", "Pasireotide", "Pazopanib", "Pectin", "Pegfilgrastim", "Peginterferon alfa-2a", "Pembrolizumab", "Pemetrexed", "Penicillamine", "Pentamidine", "Pentobarbital", "Pentoxifylline", "Pepsin", "Peramivir", "Perampanel", "Perindopril", "Permethrin", "Pertuzumab", "Phenobarbital", "Phenol", "Phentermine", "Phenylephrine", "Phenytoin", "Pibrentasvir", "Picosulfuric", "Pilocarpine", "Pioglitazone", "Piperacillin", "Piperazine", "Piracetam", "Pirfenidone", "Piroxicam", "Pitavastatin", "Plerixafor", "Polidocanol", "Polyethylene glycol", "Polymyxin B", "Pomalidomide", "Ponatinib", "Posaconazole", "Potassium chloride", "Potassium Iodide", "Potassium", "Povidone-iodine", "Pramipexole", "Prasugrel", "Pravastatin", "Praziquantel", "Prazosin", "Prednisolone", "Prednisone", "Pregabalin", "Prilocaine", "Primaquine", "Probenecid", "Probucol", "Progesterone", "Promethazine", "Propafenone", "Propofol", "Propranolol", "Propylthiouracil", "Protein C", "Prucalopride", "Prussian blue", "Pseudoephedrine", "Pyrazinamide", "Pyridostigmine", "Pyridoxine", "Pyrimethamine", "Quetiapine", "Quinidine", "Quinine", "Rabeprazole", "Raloxifene", "Raltegravir", "Ramelteon", "Ramipril", "Ramucirumab", "Ranibizumab", "Ranitidine", "Ranolazine", "Rasagiline", "Rasburicase", "Rebamipide", "Regadenoson", "Regorafenib", "Remifentanil", "Repaglinide", "Reserpine", "Resorcinol", "Ribavirin", "Ribociclib", "Riboflavin", "Rifabutin", "Rifampicin", "Rifamycin", "Rifapentine", "Rifaximin", "Rilpivirine", "Riluzole", "Rimonabant", "Riociguat", "Risperidone", "Ritonavir", "Rituximab", "Rivaroxaban", "Rivastigmine", "Rocuronium", "Roflumilast", "Romidepsin", "Romiplostim", "Romosozumab", "Ropinirole", "Ropivacaine", "Rose bengal", "Rosiglitazone", "Rosuvastatin", "Rotavirus vaccine", "Rotigotine", "Rutin", "Ruxolitinib", "Sacubitril", "Salbutamol", "Salicylic", "Salmeterol", "Salmon calcitonin", "Saxagliptin", "Scopolamine", "Secukinumab", "Selegiline", "Selexipag", "Semaglutide", "Sertraline", "Sevelamer", "Sevoflurane", "Sibutramine", "Sildenafil", "Silodosin", "Silver nitrate", "Silver sulfadiazine", "Silver", "Simeprevir", "Simvastatin", "Sirolimus", "Sitagliptin", "Sodium bicarbonate", "Sodium chloride", "Sodium citrate", "Sodium fluoride", "Sodium oxybate", "Sodium sulfate", "Sofosbuvir", "Solifenacin", "Somatostatin", "Sorafenib", "Sorbitol", "Sotalol", "Spironolactone", "St. John's Wort", "Stavudine", "Streptokinase", "Streptomycin", "Streptozocin", "Strontium ranelate", "Succinylcholine", "Sufentanil", "Sugammadex", "Sulbactam", "Sulfadiazine", "Sulfadoxine", "Sulfamethazine", "Sulfamethoxazole", "Sulfasalazine", "Sulindac", "Sulodexide", "Sumatriptan", "Sunitinib", "Suvorexant", "Tacrine", "Tacrolimus", "Tadalafil", "Tafamidis", "Tafluprost", "Talimogene laherparepvec", "Tamoxifen", "Tamsulosin", "Tapentadol", "Tazarotene", "Tazobactam", "Tedizolid", "Teduglutide", "Tegafur", "Teicoplanin", "Telaprevir", "Telavancin", "Telbivudine", "Telmisartan", "Temozolomide", "Temsirolimus", "Tenecteplase", "Tenofovir alafenamide", "Tenofovir disoproxil", "Terbinafine", "Terbutaline", "Teriflunomide", "Teriparatide", "Terlipressin", "Testosterone", "Tetracaine", "Tetracycline", "Thalidomide", "Theophylline", "Thiamine", "Thimerosal", "Thiopental", "Thioridazine", "Thiotepa", "Thiram", "Thrombin", "Ticagrelor", "Tigecycline", "Timolol", "Tiotropium", "Tirofiban", "Tobramycin", "Tocilizumab", "Tocopherol", "Tofacitinib", "Tolterodine", "Tolvaptan", "Topiramate", "Topotecan", "Trabectedin", "Tramadol", "Trametinib", "Tranexamic", "Trastuzumab emtansine", "Trastuzumab", "Travoprost", "Trazodone", "Treosulfan", "Treprostinil", "Tretinoin", "Triamcinolone", "Trichloroethylene", "Triclabendazole", "Triclosan", "Trifluridine", "Trimetazidine", "Trimethoprim", "Triptorelin", "Tromethamine", "Trypsin", "Tryptophan", "txt", "txt_list_file", "Ulipristal", "Umeclidinium", "Urea", "Urokinase", "Ursodeoxycholic", "Ustekinumab", "Valganciclovir", "Valproic", "Valsartan", "Vancomycin", "Vandetanib", "Vardenafil", "Varenicline", "Vedolizumab", "Velpatasvir", "Vemurafenib", "Venetoclax", "Venlafaxine", "Verapamil", "Verteporfin", "Vigabatrin", "Vilanterol", "Vilazodone", "Vildagliptin", "Vinblastine", "Vincristine", "Vinorelbine", "Vismodegib", "Vitamin A", "Vorapaxar", "Voriconazole", "Vorinostat", "Vortioxetine", "Warfarin", "Yellow Fever Vaccine", "Yohimbine", "Zanamivir", "Zidovudine", "Zinc chloride", "Zinc oxide", "Zinc sulfate", "Zinc", "Ziprasidone", "Zoledronic", "Zolpidem", "Zonisamide"]


import pharmapp as pa

for drug in drugs:
    print(drug)
    pa.get_inactive_ingredient(name_drug=drug)
    print(f'{drug} done!')






Abacavir
Abatacept
Abciximab
Abemaciclib
Abiraterone
Acarbose
Aceclofenac
Acenocoumarol
Acetaminophen
Acetazolamide
Acetic acid
Acetylcholine
Acetylcysteine
Acetylsalicylic acid
Acitretin
Aclidinium
Activated charcoal
Acyclovir
Adalimumab
Adapalene
Adefovir dipivoxil
Adenosine
Afatinib
Aflibercept
Agomelatine
Albendazole
Alectinib
Alemtuzumab
Alfaxalone
Alirocumab
Aliskiren
Alitretinoin
Allopurinol
Alogliptin
Alprazolam
Alteplase
Aluminum chloride
Aluminum hydroxide
Aluminum oxide
Amantadine
Ambrisentan
Ambroxol
Amifostine
Amikacin
Amiloride
Aminobenzoic acid
Aminocaproic acid
Aminolevulinic acid
Aminophylline
Aminosalicylic acid
Amiodarone
Amisulpride
Amitriptyline
Amlodipine
Ammonium chloride
Amodiaquine
Amoxicillin
Amphetamine
Amphotericin B
Ampicillin
Anakinra
Anastrozole
Angiotensin II
Anidulafungin
Apixaban
Apomorphine
Apremilast
Aprepitant
Aprotinin
Argatroban
Aripiprazole
Arsenic trioxide
Artemether
Artesunate
Articaine
Ascorbic acid
Asenapine
Asunaprevir
Atazanavir
Atenolol
Atezolizumab
Atomoxetine
Atorvastatin
Atovaquone
Atropine
Attapulgite
Auranofin
Avelumab
Axitinib
Azacitidine
Azathioprine
Azithromycin
Aztreonam
Bacitracin
Baclofen
Baricitinib
Basiliximab
Bazedoxifene
Bedaquiline
Belatacept
Belimumab
Bendamustine
Benralizumab
Benzalkonium
Benznidazole
Benzocaine
Benzoic acid
Benzoyl peroxide
Benzyl alcohol
Beta carotene
Betahistine
Betamethasone
Bevacizumab
Bexarotene
Bezafibrate
Bicalutamide
Bimatoprost
Biotin
Bisoprolol
Bivalirudin
Bleomycin
Blinatumomab
Boceprevir
Boric acid
Bortezomib
Bosentan
Bosutinib
Botulinum toxin type A
Brentuximab vedotin
Brexpiprazole
Brimonidine
Brinzolamide
Brivaracetam
Brodalumab
Bromocriptine
Budesonide
Bumetanide
Bupivacaine
Buprenorphine
Bupropion
Buspirone
Busulfan
Butorphanol
Cabazitaxel
Cabergoline
Cabozantinib
Caffeine
Calcipotriol
Calcitriol
Calcium alginate
Calcium carbonate
Calcium chloride
Calcium Phosphate
Camphor
Canagliflozin
Canakinumab
Cangrelor
Cannabidiol
Capecitabine
Capsaicin
Captopril
Carbamazepine
Carbetocin
Carbon dioxide
Carbon monoxide
Carboplatin
Carfilzomib
Cariprazine
Carmustine
Carvedilol
Caspofungin
Castor oil
Cefazolin
Cefepime
Cefixime
Cefoperazone
Cefotaxime
Ceftaroline fosamil
Ceftazidime
Ceftriaxone
Cefuroxime
Celecoxib
Cephalexin
Ceritinib
Certolizumab pegol
Cetirizine
Cetuximab
Cetylpyridinium
Chloral hydrate
Chlorambucil
Chloramphenicol
Chlorhexidine
Chloroform
Chloroquine
Chlorpromazine
Chlortetracycline
Chlorthalidone
Cholecalciferol
Cholecystokinin
Cholic Acid
Chondroitin sulfate
Chymotrypsin
Cidofovir
Cilostazol
Cimetidine
Cinacalcet
Ciprofloxacin
Cisatracurium
Cisplatin
Citalopram
Citicoline
Citric acid
Cladribine
Clarithromycin
Clenbuterol
Clindamycin
Clobazam
Clobetasol
Clofarabine
Clofazimine
Clomipramine
Clonazepam
Clonidine
Clopidogrel
Clotrimazole
Clozapine
Cobicistat
Cobimetinib
Cocaine
Codeine
Colchicine
Colistin
Collagenase clostridium histolyticum
Corticotropin
Crizotinib
Cyclophosphamide
Cycloserine
Cyclosporine
Cysteamine
Cytarabine
Dabigatran etexilate
Dabrafenib
Dacarbazine
Daclatasvir
Dacomitinib
Dalbavancin
Dalteparin
Dantrolene
Dapagliflozin
Dapsone
Daptomycin
Daratumumab
Darbepoetin alfa
Darunavir
Dasabuvir
Dasatinib
Daunorubicin
Decitabine
Deferasirox
Deferiprone
Deferoxamine
Delamanid
Denosumab
Deoxycholic acid
Dermatophagoides farinae
Dermatophagoides pteronyssinus
Desflurane
Desipramine
Desmopressin
Desvenlafaxine
Dexamethasone
Dexketoprofen
Dexmedetomidine
Dexrazoxane
Dextran
Dextromethorphan
Diacerein
Diazepam
Diazoxide
Diclofenac
Dienogest
Diethylstilbestrol
Digoxin
Diltiazem
Dimethyl fumarate
Dimethyl sulfoxide
Dinoprostone
Diosmin
Diphenhydramine
Dipyridamole
Disulfiram
Dobutamine
Docetaxel
Dolutegravir
Domperidone
Donepezil
Dopamine
Doripenem
Dorzolamide
Doxazosin
Doxorubicin
Doxycycline
Dronedarone
Droperidol
Drospirenone
Dulaglutide
Duloxetine
Dupilumab
Durvalumab
Dutasteride
Eculizumab
Edaravone
Edoxaban
Efavirenz
Elbasvir
Elotuzumab
Eltrombopag
Elvitegravir
Emicizumab
Empagliflozin
Emtricitabine
Enalapril
Enoxaparin
Entecavir
Enzalutamide
Ephedrine
Epinephrine
Epirubicin
Eplerenone
Epoprostenol
Eptifibatide
Erenumab
Eribulin
Erlotinib
Ertapenem
Erythromycin
Erythropoietin
Escitalopram
Esketamine
Eslicarbazepine
Esmolol
Esomeprazole
Estradiol
Estriol
Estrone
Etanercept
Ethambutol
Ethanol
Ethinylestradiol
Etomidate
Etonogestrel
Etoposide
Etoricoxib
Etravirine
Everolimus
Evolocumab
Exemestane
Exenatide
Ezetimibe
Famotidine
Favipiravir
Febuxostat
Felodipine
Fenofibrate
Fentanyl
Fesoterodine
Fexofenadine
Fidaxomicin
Filgrastim
Finasteride
Fingolimod
Flecainide
Flibanserin
Fluconazole
Fludarabine
Flumazenil
Fluocinolone acetonide
Fluorescein
Fluorouracil
Fluoxetine
Flurbiprofen
Flutamide
Fluticasone furoate
Fluticasone
Fluvastatin
Fluvoxamine
Folic acid
Fondaparinux
Formoterol
Fosfomycin
Fructose
Fulvestrant
Furosemide
Fusidic acid
Gabapentin
Gadobutrol
Gadoxetic acid
Galactose
Galantamine
Ganciclovir
Gatifloxacin
Gefitinib
Gemcitabine
Gemfibrozil
Gemtuzumab ozogamicin
Gentamicin
Ginkgo biloba
Glatiramer
Glecaprevir
Gliclazide
Glimepiride
Glipizide
Glucagon
Glucosamine
Glutamic acid
Glutathione
Glyburide
Glycerin
Glycine betaine
Glycine
Glycopyrronium
Glycyrrhizic acid
Golimumab
Granisetron
Grazoprevir
Griseofulvin
Guanfacine
Guselkumab
Haloperidol
Halothane
Helium
Hemin
Heparin
Histamine
Hyaluronic acid
Hyaluronidase
Hydralazine
Hydrochlorothiazide
Hydrocodone
Hydrocortisone
Hydrogen peroxide
Hydromorphone
Hydroquinone
Hydrotalcite
Hydroxocobalamin
Hydroxychloroquine
Hydroxyethyl Starch
Hydroxyurea
Hypochlorite
Ibandronate
Ibritumomab tiuxetan
Ibrutinib
Ibuprofen
Icatibant
Idarubicin
Idarucizumab
Idebenone
Idelalisib
Ifosfamide
Iloprost
Imatinib
Imipenem
Imipramine
Imiquimod
Indacaterol
Indapamide
Indigotindisulfonic acid
Indomethacin
Infliximab
Ingenol mebutate
Inositol
Inotuzumab ozogamicin
Insulin aspart
Insulin beef
Insulin degludec
Insulin detemir
Insulin glargine
Insulin lispro
Interferon beta-1a
Interferon beta-1b
Inulin
Iodine
Iodixanol
Iohexol
Ipilimumab
Irbesartan
Irinotecan
Iron sucrose
Iron
Isavuconazole
Isoflurane
Isoniazid
Isoprenaline
Isotretinoin
Itraconazole
Ivabradine
Ivacaftor
Ivermectin
Ixazomib
Ixekizumab
Kanamycin
Kaolin
Ketamine
Ketoconazole
Ketoprofen
Ketorolac
L-Glutamine
L-Lysine
Labetalol
Lacosamide
Lactic acid
Lactulose
Lamivudine
Lamotrigine
Lanreotide
Lansoprazole
Lanthanum carbonate
Lapatinib
Latanoprost
Ledipasvir
Leflunomide
Lenalidomide
Lenvatinib
Lercanidipine
Letermovir
Letrozole
Leucovorin
Leuprolide
Levamisole
Levetiracetam
Levobupivacaine
Levodopa
Levofloxacin
Levonorgestrel
Levosimendan
Levothyroxine
Lidocaine
Linaclotide
Linagliptin
Lincomycin
Lindane
Linezolid
Lipoic acid
Liraglutide
Lisdexamfetamine
Lisinopril
Lixisenatide
Lomustine
Loperamide
Lopinavir
Loratadine
Lorazepam
Lorcaserin
Lornoxicam
Losartan
Lovastatin
Lumacaftor
Lumefantrine
Lurasidone
Macitentan
Magnesium oxide
Magnesium sulfate
Malathion
Mandelic acid
Mannitol
Maraviroc
Mebendazole
Medroxyprogesterone acetate
Mefenamic acid
Mefloquine
Melatonin
Meloxicam
Melphalan
Memantine
Menadione
Meperidine
Mepivacaine
Mepolizumab
Mercaptopurine
Meropenem
Mesalazine
Metamizole
Metformin
Methacholine
Methadone
Methimazole
Methionine
Methotrexate
Methylcellulose
Methylene blue
Methylphenidate
Methylprednisolone
Meticillin
Metoclopramide
Metoprolol
Metronidazole
Mexiletine
Micafungin
Miconazole
Midazolam
Midodrine
Midostaurin
Mifepristone
Milnacipran
Milrinone
Miltefosine
Mineral oil
Minocycline
Minoxidil
Mirabegron
Mirtazapine
Misoprostol
Mitomycin
Mitotane
Mitoxantrone
Modafinil
Mogamulizumab
Mometasone furoate
Montelukast
Morphine
Moxidectin
Moxifloxacin
Mupirocin
Mycophenolic acid
Nalbuphine
Nalmefene
Naloxone
Naltrexone
Naproxen
Natalizumab
Natamycin
Nebivolol
Nelfinavir
Neomycin
Neostigmine
Nepafenac
Neratinib
Nevirapine
Niacin
Nicardipine
Niclosamide
Nicorandil
Nicotinamide
Nicotine
Nifedipine
Nilotinib
Nimesulide
Nimodipine
Nintedanib
Nitazoxanide
Nitric Oxide
Nitrofurantoin
Nitrogen
Nitroglycerin
Nitroprusside
Nitrous acid
Nitrous oxide
Nivolumab
Norepinephrine
Norfloxacin
Nortriptyline
Noscapine
Nusinersen
Nystatin
Obeticholic acid
Obinutuzumab
Ocrelizumab
Ocriplasmin
Octreotide
Ofatumumab
Ofloxacin
Olanzapine
Olaparib
Olmesartan
Olodaterol
Omadacycline
Omalizumab
Ombitasvir
Omeprazole
Ondansetron
Opium
Oritavancin
Orlistat
Ornithine
Oseltamivir
Osimertinib
Ouabain
Oxacillin
Oxaliplatin
Oxcarbazepine
Oxybutynin
Oxycodone
Oxygen
Oxytetracycline
Oxytocin
Paclitaxel
Palbociclib
Paliperidone
Palivizumab
Palonosetron
Panitumumab
Panobinostat
Pantoprazole
Papaverine
Parathyroid hormone
Parecoxib
Paricalcitol
Paritaprevir
Paromomycin
Paroxetine
Pasireotide
Pazopanib
Pectin
Pegfilgrastim
Peginterferon alfa-2a
Pembrolizumab
Pemetrexed
Penicillamine
Pentamidine
Pentobarbital
Pentoxifylline
Pepsin
Peramivir
Perampanel
Perindopril
Permethrin
Pertuzumab
Phenobarbital
Phenol
Phentermine
Phenylephrine
Phenytoin
Pibrentasvir
Picosulfuric acid
Pilocarpine
Pioglitazone
Piperacillin
Piperazine
Piracetam
Pirfenidone
Piroxicam
Pitavastatin
Plerixafor
Polidocanol
Polyethylene glycol
Polymyxin B
Pomalidomide
Ponatinib
Posaconazole
Potassium chloride
Potassium Iodide
Potassium
Povidone-iodine
Pramipexole
Prasugrel
Pravastatin
Praziquantel
Prazosin
Prednisolone
Prednisone
Pregabalin
Prilocaine
Primaquine
Probenecid
Probucol
Progesterone
Promethazine
Propafenone
Propofol
Propranolol
Propylthiouracil
Protein C
Prucalopride
Prussian blue
Pseudoephedrine
Pyrazinamide
Pyridostigmine
Pyridoxine
Pyrimethamine
Quetiapine
Quinidine
Quinine
Rabeprazole
Raloxifene
Raltegravir
Ramelteon
Ramipril
Ramucirumab
Ranibizumab
Ranitidine
Ranolazine
Rasagiline
Rasburicase
Rebamipide
Regadenoson
Regorafenib
Remifentanil
Repaglinide
Reserpine
Resorcinol
Ribavirin
Ribociclib
Riboflavin
Rifabutin
Rifampicin
Rifamycin
Rifapentine
Rifaximin
Rilpivirine
Riluzole
Rimonabant
Riociguat
Risperidone
Ritonavir
Rituximab
Rivaroxaban
Rivastigmine
Rocuronium
Roflumilast
Romidepsin
Romiplostim
Romosozumab
Ropinirole
Ropivacaine
Rose bengal
Rosiglitazone
Rosuvastatin
Rotavirus vaccine
Rotigotine
Rutin
Ruxolitinib
Sacubitril
Salbutamol
Salicylic acid
Salmeterol
Salmon calcitonin
Saxagliptin
Scopolamine
Secukinumab
Selegiline
Selexipag
Semaglutide
Sertraline
Sevelamer
Sevoflurane
Sibutramine
Sildenafil
Silodosin
Silver nitrate
Silver sulfadiazine
Silver
Simeprevir
Simvastatin
Sirolimus
Sitagliptin
Sodium bicarbonate
Sodium chloride
Sodium citrate
Sodium fluoride
Sodium oxybate
Sodium sulfate
Sofosbuvir
Solifenacin
Somatostatin
Sorafenib
Sorbitol
Sotalol
Spironolactone
St. John's Wort
Stavudine
Streptokinase
Streptomycin
Streptozocin
Strontium ranelate
Succinylcholine
Sufentanil
Sugammadex
Sulbactam
Sulfadiazine
Sulfadoxine
Sulfamethazine
Sulfamethoxazole
Sulfasalazine
Sulindac
Sulodexide
Sumatriptan
Sunitinib
Suvorexant
Tacrine
Tacrolimus
Tadalafil
Tafamidis
Tafluprost
Talimogene laherparepvec
Tamoxifen
Tamsulosin
Tapentadol
Tazarotene
Tazobactam
Tedizolid
Teduglutide
Tegafur
Teicoplanin
Telaprevir
Telavancin
Telbivudine
Telmisartan
Temozolomide
Temsirolimus
Tenecteplase
Tenofovir alafenamide
Tenofovir disoproxil
Terbinafine
Terbutaline
Teriflunomide
Teriparatide
Terlipressin
Testosterone
Tetracaine
Tetracycline
Thalidomide
Theophylline
Thiamine
Thimerosal
Thiopental
Thioridazine
Thiotepa
Thiram
Thrombin
Ticagrelor
Tigecycline
Timolol
Tiotropium
Tirofiban
Tobramycin
Tocilizumab
Tocopherol
Tofacitinib
Tolterodine
Tolvaptan
Topiramate
Topotecan
Trabectedin
Tramadol
Trametinib
Tranexamic acid
Trastuzumab emtansine
Trastuzumab
Travoprost
Trazodone
Treosulfan
Treprostinil
Tretinoin
Triamcinolone
Trichloroethylene
Triclabendazole
Triclosan
Trifluridine
Trimetazidine
Trimethoprim
Triptorelin
Tromethamine
Trypsin
Tryptophan
Ulipristal
Umeclidinium
Urea
Urokinase
Ursodeoxycholic acid
Ustekinumab
Valganciclovir
Valproic acid
Valsartan
Vancomycin
Vandetanib
Vardenafil
Varenicline
Vedolizumab
Velpatasvir
Vemurafenib
Venetoclax
Venlafaxine
Verapamil
Verteporfin
Vigabatrin
Vilanterol
Vilazodone
Vildagliptin
Vinblastine
Vincristine
Vinorelbine
Vismodegib
Vitamin A
Vorapaxar
Voriconazole
Vorinostat
Vortioxetine
Warfarin
Yellow Fever Vaccine
Yohimbine
Zanamivir
Zidovudine
Zinc chloride
Zinc oxide
Zinc sulfate
Zinc
Ziprasidone
Zoledronic acid
Zolpidem
Zonisamide
