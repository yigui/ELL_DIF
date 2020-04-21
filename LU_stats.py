#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 14:02:12 2020

@author: yigui
"""
import os
os.chdir('Z:/Special Projects/ISASP/2019/DIF/DIF EL/Transcription/Python_code')
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import string
import sys
import os
import misc
import wordDict
import sentimentanal
import similarity
nltk.download('wordnet')
import re
import compound
from compound import Compound
compo=Compound()
import spellchecker
from spellchecker import SpellChecker
spell = SpellChecker()
from textstat.textstat import textstat
from sentimentanal import Posscore,Negscore
import os
import syllapy

ConTract={"ain't": True, "aren't": True, "can't": True, "can't've": True, "'cause": True, "could've": True, "couldn't": True, "couldn't've": True, "didn't": True, "doesn't": True, "don't": True, "hadn't": True, "hadn't've": True, "hasn't": True, "haven't": True, "he'd": True, "he'd've": True, "he'll": True, "he'll've": True, "he's": True, "how'd": True, "how'd'y": True, "how'll": True, "how's": True, "I'd": True, "I'd've": True, "I'll": True, "I'll've": True, "I'm": True, "I've": True, "isn't": True, "it'd": True, "it'd've": True, "it'll": True, "it'll've": True, "it's": True, "let's": True, "ma'am": True, "mayn't": True, "might've": True, "mightn't": True, "mightn't've": True, "must've": True, "mustn't": True, "mustn't've": True, "needn't": True, "needn't've": True, "o'clock": True, "oughtn't": True, "oughtn't've": True, "shan't": True, "sha'n't": True, "shan't've": True, "she'd": True, "she'd've": True, "she'll": True, "she'll've": True, "she's": True, "should've": True, "shouldn't": True, "shouldn't've": True, "so've": True, "so's": True, "that'd": True, "that'd've": True, "that's": True, "there'd": True, "there'd've": True, "there's": True, "they'd": True, "they'd've": True, "they'll": True, "they'll've": True, "they're": True, "they've": True, "to've": True, "wasn't": True, "we'd": True, "we'd've": True, "we'll": True, "we'll've": True, "we're": True, "we've": True, "weren't": True, "what'll": True, "what'll've": True, "what're": True, "what's": True, "what've": True, "when's": True, "when've": True, "where'd": True, "where's": True, "where've": True, "who'll": True, "who'll've": True, "who's": True, "who've": True, "why's": True, "why've": True, "will've": True, "won't": True, "won't've": True, "would've": True, "wouldn't": True, "wouldn't've": True, "y'all": True, "y'all'd": True, "y'all'd've": True, "y'all're": True, "y'all've": True, "you'd": True, "you'd've": True, "you'll": True, "you'll've": True, "you're": True, "you've": True}
wrong={'aint': False, 'arent': False, 'cant': False, 'cantve': False,  'couldve': False, 'couldnt': False, 'couldntve': False, 'didnt': False, 'doesnt': False, 'dont': False, 'hadnt': False, 'hadntve': False, 'hasnt': False, 'havent': False, 'hed': False, 'hedve': False,  'hellve': False, 'hes': False, 'howd': False, 'howdy': False, 'howll': False, 'hows': False, 'Id': False, 'Idve': False, 'Ill': False, 'Illve': False, 'Im': False, 'Ive': False, 'isnt': False, 'itd': False, 'itdve': False, 'itll': False, 'itllve': False, 'its': False, 'lets': False, 'maam': False, 'maynt': False, 'mightve': False, 'mightnt': False, 'mightntve': False, 'mustve': False, 'mustnt': False, 'mustntve': False, 'neednt': False, 'needntve': False, 'oclock': False, 'oughtnt': False, 'oughtntve': False, 'shant': False, 'shantve': False,  'shedve': False, 'shellve': False, 'shes': False, 'shouldve': False, 'shouldnt': False, 'shouldntve': False, 'sove': False, 'sos': False, 'thatd': False, 'thatdve': False, 'thats': False, 'thered': False, 'theredve': False, 'theres': False, 'theyd': False, 'theydve': False, 'theyll': False, 'theyllve': False, 'theyre': False, 'theyve': False, 'tove': False, 'wasnt': False, 'wed': False, 'wedve': False,  'wellve': False,  'weve': False, 'werent': False, 'whatll': False, 'whatllve': False, 'whatre': False, 'whats': False, 'whatve': False, 'whens': False, 'whenve': False, 'whered': False, 'wheres': False, 'whereve': False, 'wholl': False, 'whollve': False, 'whos': False, 'whove': False, 'whys': False, 'whyve': False, 'willve': False, 'wont': False, 'wontve': False, 'wouldve': False, 'wouldnt': False, 'wouldntve': False, 'yall': False, 'yalld': False, 'yalldve': False, 'yallre': False, 'yallve': False, 'youd': False, 'youdve': False, 'youll': False, 'youllve': False, 'youre': False, 'youve': False}


IDlist=list()

for file in os.listdir("Z:/Special Projects/ISASP/2019/DIF/DIF EL/Transcription/Yi_AI_6WR"):
    #namelist=list()
    if file.endswith(".txt"):
        #print('"'+file[ :len(file)-4]+'"',end=",")
        IDlist.append(file)
        
IDlist
with open('Z:/Special Projects/ISASP/2019/DIF/DIF EL/Crosswalk for Python/Prompts/Prom6.txt', 'r', encoding="ISO-8859-1") as file:
   prom6 = file.read()#raw text of Prompt6


global stop
stop = set(stopwords.words('english'))

#all_stops = stop | set(string.punctuation)


def noft_text(t):    
    return t[:t.rfind('\n')]

from misc import getUniqWords
global Prom_words

#Prom_words=getUniqWords(Prwords)#this is the list of all unique words in prompt

def pulloid(t):# pull out the student ID
    if t.startswith('Doc'):
        return (t[7:27])
#list of words in the essay that are appeared in prompt


import language_check
tool = language_check.LanguageTool('en-US')
from similarity import Similarity

def LLink():
    with open('Z:/Special Projects/ISASP/2019/DIF/DIF EL/Transcription/Lexicon_dict/Lexi_Dict.txt', 'r') as f:
        LLink= f.readlines()
    LLink= [x.strip() for x in LLink] 
    return LLink

global L
L=LLink()


def main():
    #f=open('0418TestOnlineG6.csv', 'w')
    for e in IDlist:
        dataresult={}
        '''
        with open('Z:/Special Projects/ISASP/2019/DIF/DIF EL/Transcription/Yi_AI_6WR/'+e, encoding="ISO-8859-1" ) as file:
            essay= file.read()
            
        ''' 
        with open('Z:/Special Projects/ISASP/2019/DIF/DIF EL/Transcription/Yi_AI_6WR/AAAVLP13819000473707.txt', encoding="ISO-8859-1" ) as file:
            essay= file.read()
            
         # remove the footer in txt
        id_num=pulloid(essay) 
        print(id_num)
        
        essay=noft_text(essay)
        essay=essay[30:]
        dataresult['id_num']=id_num
        
        #process Prompt,remove stopwords and number and punctuations
        Promwdstxt=cleanPromt(prom6)
        validwdsinProm=getUniqWords(Promwdstxt)#Here the list only contains unique words in prompt except stopwords
        

        cleaness_text=cleanPromt(essay)
        cleaness_text=noft_text(cleaness_text)
        
        cleanlst_essay=getWordlist(cleaness_text) 
        
        #Vocab in the essay
        #essay_Uniq=getVocabNum(cleaness_text)
        Vocabnum=getVocabNum(cleaness_text)      
        #l=getVocab(cleaness_text)
        print(getVocab(cleaness_text))
        
        # count how many words in the essay are from the list
        Num_wdsFromProm=wdsAppinProm(validwdsinProm,cleanlst_essay)
        
        #number of words in the essay that are appeared in prompt
        #es_wdsinpm=wdsAppinProm(cleanedess)
        
        #count how many grammar errors
        #No_gram=countGram(gramerror(essay))

        misspelled={}
        misspelled=spell.unknown(cleanlst_essay)
        for e in cleanlst_essay:
            if e in wrong.keys():
                misspelled.add(e)
        c=list()
        for e in misspelled:
            if e in ConTract.keys():                
                c.append(e)
            elif e in compo.keys():
                c.append(e)
        for e in c:
            misspelled.remove(e)
############## removed contractions as misspelled
        print(misspelled)
        Num_Mispell=len(misspelled)
        

        w=re.split("[^-\w]+", cleaness_text)
        w=[string for string in w if string != ""]
        print(w)
        
        wordcount=len(w)
        dataresult['wordcount']=wordcount

        from nltk.tokenize import sent_tokenize, word_tokenize

        sentcount=len(sent_tokenize(essay))
        ASL=(wordcount/sentcount)

        dataresult['sentcount']=sentcount
        dataresult['Avsenlg']=ASL

        ASW=(syllapy.count(cleaness_text))/wordcount
        ASL=(wordcount/sentcount)
        Fre=206.835-(1.015*ASL)-(84.6 * ASW)

        dataresult['Times using words from prompt']=Num_wdsFromProm
        dataresult['Vocab in essay']= Vocabnum
 
        dataresult['Essay percentage using words from Prompt']="{:.2f}".format((Num_wdsFromProm/wordcount)*100)
        
        
        dataresult['No of mispelled words']=Num_Mispell
        dataresult['Percentage of mispelled words'] ="{:.2f}".format((Num_Mispell/wordcount)*100)
        
        
        #dataresult['No of grammar errors']=countGram(gramerror(essay))
        
        dw=countDifficult(cleanlst_essay)
        dataresult['No of Difficult words']=dw
        
        Estimatedlevel=textstat.text_standard(essay)
        dataresult['Estimatedlevel']=Estimatedlevel
        
        ease=Fre
        dataresult['reading_ease']=ease
        '''
        sim=Similarity(cleaness_text,Promwdstxt)
        dataresult['Cosine Similarity with Prompt']="{:.2f}".format(sim[0][1])
        
        posiness=Posscore(cleanlst_essay)
        dataresult['No of Positives in essay']=posiness
        
        PerPos="{:.2f}".format((posiness/wordcount)*100) 
        dataresult['percentage of Positives in essay']=PerPos
        
        negaess=Negscore(cleanlst_essay)
        dataresult['No of Negatives in essay']=negaess


        PerNeg="{:.2f}".format((negaess/wordcount)*100) 
        dataresult['percentage of Negatives in essay']=PerNeg
        
        L=wordDict.LLink()
        
        lk=0
        for word in cleanlst_essay:
            
            if word in L:
                lk+=1
                
                
        dataresult['No of Linking words in essay']=lk
        
        PerLink="{:.2f}".format((lk/wordcount)*100) 
        dataresult['percentage of Linking Words in essay']=PerLink
        '''
        import csv
        for v in dataresult:
            dataresult[v]=str(dataresult[v])
        


        with open('0418TestOnlineG6.csv','a+', newline='') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            writer.writerow(list(dataresult.keys()))
            writer.writerow(list(dataresult.values()))

'''
for e in IDlist:
    with open('X:/Special Projects/ISASP/2019/DIF/DIF EL/Transcription/Yi_AI_6WR/'+e, 'r') as file:
        essay= file.read()
        essay=noft_text(essay) # remove the footer in txt

        nofooter=getWordlist(essay) 
        ess_uniq=getVocab(nofooter)
        countProwds=WdsinProm(nofooter) #number of words in the essay that are appeared in prompt

        es_wdsinpm=wdsAppinProm(nofooter)
        misspelled=spell.unknown(nofooter)
        id_num=pullid(essay)
        freqDist = FreqDist(es_wdsinpm)
        plt.title('Frequency distribution of top 50 in words used from Prompt '+str(id_num))
        fig = freqDist.plot(50)
        plt.tight_layout() 
        fig.figure.set_size_inches(10.5, 8.5)

#The saving part of the solution
        fig.figure.savefig('%s.png' % id_num)
        #print(essay[0:28],'\n')
        sys.stdout = open(e, "w")
        LUvars(essay)
        #sys.stdout.close()
        '''
