import nltk
import re

x = """
I am suffering from jaundice. and I heared 217 people died my cities recently"""
y = nltk.sent_tokenize(x)
l=x.lower()
#z = nltk.word_tokenize(y)
list_pos = ['cholera','typhoid','hiv','malaria','dengue','jaundice','aids','leukemia','adhd','arthritis','asthma','autism spectrum disorder','asd','avian influenza','birth defects','cancer','chlamydia','chronic fatigue syndrome','chronic obstructive pulmonary disease ','copd','chikungunya','diabetes','ebola','ebola virus disease','epilepsy','fetal alcohol spectrum disorders','flu','influenza','genital herpes','herpes simplex virus','giardiasis','gonorrhea','heart disease','hepatitis',' hiv/aids','human papilloma virus','hpv','kidney disease','chronic kidney disease','meningitis','methicillin-resistant staphylococcus aureus','mrsa','microcephaly','middle east respiratory syndrome','mers','overweight and obesity','pollution','parasites – scabies','salmonella','sexually transmitted diseases','stds','stroke','traumatic brain injury ','tbi','trichomonas infection','trichomoniasis','tuberculosis ',' Water-related diseases','zika virus']

for i in range(len(list_pos)):
    if list_pos[i] in l:
        print("Name of the disease = " +list_pos[i] )
        for j in  y:
            a = re.search(r'.*(killing|killed) ([0-9]{0,5}).*',j,re.IGNORECASE)
            b = re.search(r'.*(death|deaths|died) (in|due|of).*',j,re.IGNORECASE) 
            c = re.search(r'.*([0-9]{0,2}) (hundred|thousand|crore|million|billion|people).*',j,re.IGNORECASE)
            d = re.search(r'.*(hundreds|thousands|crores|millions|billions) (of).*',j,re.IGNORECASE)
            e = re.search(r'.*(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|forteen|fifteen|sixteen|seventeen|eihteen|ninteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninty) (of|people) (people).*',j,re.IGNORECASE)
            abc=[a,b,c,d]
            for item in abc:
                if item == None:
                    pass
                else:
                    print(item[0])
                    break
#   
    
        
        
        
    