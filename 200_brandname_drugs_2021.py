# -*- coding: utf-8 -*-
"""
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
Copyright 2021 | Nghiên Cứu Thuốc | RD Pharma Plus

Email: nghiencuuthuoc@gmail.com | info@nghiencuuthuoc.com

Web: http://www.nghiencuuthuoc.com

See more: https://twitter.com/nghiencuuthuoc | https://facebook.com/nghiencuuthuoc

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
DEVELOPMENT NOTES

+ 20210828:

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
"""


#


#

drugs_raw = "Accupril Aciphex Actos Adalat Adderall Albuterol Alesse Allegra Allopurinol Alphagan Alprazolam Altace Amaryl Ambien Amitriptyline Amoxicillin Amoxil Amphetamine Amyl nitrite Anabolic Steroids Aricept Atenolol Atenolol (Mylan) Atrovent Augmentin Avandia Avapro Azmacort Bactroban Baycol Biaxin Buspar Cardizem CD Cardura Carisoprodol Ceftin Cefzil Celebrex Celexa Cephalexin Cipro Claritin Claritin Reditabs Claritin-D 12HR Claritin-D 24HR Climara Clonazepam Clonidine HCL Cocaine Combivent Coumadin Cozaar Cyclobenzaprine Depakote Detrol Diazepam Diflucan Dilantin Diovan Diovan HCT Effexor XR Elocon Ery-Tab Evista Flomax Flonase Flovent Folic Acid Fosamax Furosemide Gemfibrozil Glucophage Glucotrol XL Glyburide Hydrochlorothiazide Hydrocodone Hyzaar Ibuprofen Imitrex Isosorbide Mononitrate K-Dur Ketamine Klor-Con 10 Lanoxin Lescol Levaquin Levothroid Levoxyl Lipitor Lo Ovral Loestrin FE Lorazepam Lotensin Lotrel Lotrisone Lysergic Acid Diethylamide Macrobid Marijuana MDMA Medroxyprogesterone Mescaline Methamphetamine Methylphenidate Methylprednisolone Metoprolol Tartrate Miacalcin Monopril Morphine Naproxen Naproxen Sodium Nasonex Neurontin Nicotine Norvasc Ortho Cyclen Ortho Tri-Cyclen Oxycodone OxyContin Paxil Penicillin VK Pepcid Phenergan Plavix Plendil Potassium Chloride Pravachol Prednisone Premarin Prempro Prevacid Prilosec Prinivil Procardia XL Promethazine Propoxyphene Proventil HFA Prozac Psilocybin Ranitidine Relafen Remeron Risperdal Ritalin Rohypnol Roxicet Serevent Serzone Singulair Synthroid Tamoxifen Citrate Temazepam Tiazac Tobradex Toprol-XL Trazodone Triamterene Trimox Triphasil Ultram Valtrex Vasotec Veetids Verapamil Viagra Vicoprofen Vioxx Warfarin Sodium Wellbutrin SR Xalatan Xenical Zestoretic Zestril Ziac Zithromax Zithromax Z-PAK Zocor Zoloft Zyprexa Zyrtec"

#
Drugs A to Z
Top 200 Drugs
This top 200 list is generated using data collected from user searches and survey results.

Accupril
Aciphex
Actos
Adalat CC
Adderall
Albuterol
Alesse-28
Allegra
Allegra-D
Allopurinol
Alphagan
Alprazolam
Altace
Amaryl
Ambien
Amitriptyline HCL
Amoxicillin Trihydrate
Amoxil
Amphetamine
Amyl nitrite
Anabolic Steroids
Aricept
Atenolol
Atenolol (Mylan)
Atrovent
Augmentin
Avandia
Avapro
Azmacort
Bactroban
Baycol
Biaxin
Buspar
Cardizem CD
Cardura
Carisoprodol
Ceftin
Cefzil
Celebrex
Celexa
Cephalexin
Cipro
Claritin
Claritin Reditabs
Claritin-D 12HR
Claritin-D 24HR
Climara
Clonazepam
Clonidine HCL
Cocaine
Combivent
Coumadin
Cozaar
Cyclobenzaprine
Depakote
Detrol
Diazepam
Diflucan
Dilantin
Diovan
Diovan HCT
Effexor XR
Elocon
Ery-Tab
Evista
Flomax
Flonase
Flovent
Folic Acid
Fosamax
Furosemide
Gemfibrozil
Glucophage
Glucotrol XL
Glyburide
Hydrochlorothiazide
Hydrocodone
Hyzaar
Ibuprofen
Imitrex
Isosorbide Mononitrate
K-Dur
Ketamine
Klor-Con 10
Lanoxin
Lescol
Levaquin
Levothroid
Levoxyl
Lipitor
Lo Ovral
Loestrin FE
Lorazepam
Lotensin
Lotrel
Lotrisone
Lysergic Acid Diethylamide
Macrobid
Marijuana
MDMA
Medroxyprogesterone
Mescaline
Methamphetamine
Methylphenidate
Methylprednisolone
Metoprolol Tartrate
Miacalcin
Monopril
Morphine
Naproxen
Naproxen Sodium
Nasonex
Neurontin
Nicotine
Norvasc
Ortho Cyclen
Ortho Tri-Cyclen
Oxycodone
OxyContin
Paxil
Penicillin VK
Pepcid
Phenergan
Plavix
Plendil
Potassium Chloride
Pravachol
Prednisone
Premarin
Prempro
Prevacid
Prilosec
Prinivil
Procardia XL
Promethazine
Propoxyphene
Proventil HFA
Prozac
Psilocybin
Ranitidine
Relafen
Remeron
Risperdal
Ritalin
Rohypnol
Roxicet
Serevent
Serzone
Singulair
Synthroid
Tamoxifen Citrate
Temazepam
Tiazac
Tobradex
Toprol-XL
Trazodone
Triamterene
Trimox
Triphasil
Ultram
Valtrex
Vasotec
Veetids
Verapamil
Viagra
Vicoprofen
Vioxx
Warfarin Sodium
Wellbutrin SR
Xalatan
Xenical
Zestoretic
Zestril
Ziac
Zithromax
Zithromax Z-PAK
Zocor
Zoloft
Zyprexa
Zyrtec