import nltk
import re
#x="""The was 2nd raped on  october of the same year by a  boy for many days continuosly"""


x = """ Two men raped an unconscious 30-year-old woman on a Harlem sidewalk in the middle of the day, police said Tuesday.

The woman had apparently been drinking, and the suspects took advantage, a police source said.

The shocking attack happened last Friday at about 4 p.m. on E. 126th St. between Park and Madison Aves.

A witness saw Victor Lopez, 54, rape the woman while holding her against a gate, according to the criminal complaint.  His alleged accomplice, Angel Feliciano, 35, fondled the woman’s genitals during the rape, the complaint said.

When police got there the woman “was unable to form complete sentences and she was unable to stand on her own,” the complaint said.

Lopez, who is 5 feet 9 inches and 230 pounds, is being held on $50,000 bail. He has 29 prior arrests, including for burglary and drug possession, police sources said.

His lawyer did not respond to a request for comment.  Feliciano, who is 5 feet 11 inches tall and weighs 280 pounds, is being held on $7,500 bail. He has 32 prior arrests, including for drug possession with intent to sell, burglary and menacing with a weapon, sources said. His lawyer had no comment.

Residents on the block were stunned at the brazen nature of the attack.

“It's unnerving because I live down the block and take this route a lot," said stay-at-home mom Felicia Buchanan, 50. “I feel bad for the person. I'm glad the men got caught.

“Maybe they need more police presence here, even just during the day. """
# Any piece of article
w1 = nltk.sent_tokenize(x) #Sentence Tockenizer
from nltk.corpus import stopwords # Excludes Stopwords
text = ' '.join([word for word in x.split() if word not in (stopwords.words('english'))]) # Excludes Stopwords and split
list_pos = ['raped','rape','rapes','raping','molest','molested','sexual harassment','sexually abussed','ravish','raping','abduction']
                        # List of words generally used in Rape-news-article 
for i in range(len(list_pos)):
    if list_pos[i] in x:
        print("This News is about Rape")
        for i in  w1:
            m = re.search(r'.*(I|He|She) (is|am|woman|man|girl|boy|teenager|minor) ([0-9]{1,2}).*',i,re.IGNORECASE)
            n = re.search(r'.*(I|He|She) (is|am) in (my|his|her) (late|mid|early)? ?(tens|twenties|thirties|forties|fifties|sixties|seventies|eighties|nineties|hundreds).*',i,re.IGNORECASE)
            o = re.search(r'.*(I|He|She) (is|am|the|was) (twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen) ?(one|two|three|four|five|six|seven|eight|nine)?.*',i,re.IGNORECASE)
            p = re.search(r'.*(age|is|@|was|of|about) ([0-9]{1,2}).*',i,re.IGNORECASE)
            q = re.search(r'.*(age|is|@|was) (twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen) ?(one|two|three|four|five|six|seven|eight|nine)?.*',i,re.IGNORECASE)
            r = re.search(r'.*([0-9]{2}) (yrs|years|year).*',i,re.IGNORECASE)
            s = re.search(r'.*(twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen) ?(one|two|three|four|five|six|seven|eight|nine)? (yrs|years).*',i,re.IGNORECASE)
            t = re.search(r'.*(early|late) ([0-9]{2}).*',i,re.IGNORECASE)
            u = re.search(r'.*(victim|sufferer|wounded person) ([0-9]{2}).*',i,re.IGNORECASE)
            v = re.search(r'.*([0-9]{2})([-])(yrs|years|year)([-]).*',i,re.IGNORECASE) 
            w = re.search(r'.*(woman|man|girl|boy|teenager|minor)(,)([0-9]{1,2}).*',i,re.IGNORECASE)
            x1 = re.search(r'.*(0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])[- /.](19|20).*',i,re.IGNORECASE)
            y = re.search(r'.*(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20).*',i,re.IGNORECASE)
            z = re.search(r'.*${jan:+January}${feb:+February}${mar:+March}${apr:+April}${may:+May}${jun:+June}${jul:+July}${aug:+August}${sep:+September}${oct:+October}${nov:+November}${dec:+December} ${1st:+${1st}st}${2nd:+${2nd}nd}${3rd:+${3rd}rd}${nth:+${nth}th}, ${19xx:+19${19xx}}${20xx:+20${20xx}}.*',i,re.IGNORECASE)
            abc=[m,n,o,p,q,r,s,t,u,v,w,x1,y,z]# Pattern matching re
            for item in abc:
                if item == None:
                    pass
                else:
                    print(item[0])
                    break
                    # takes the sentence contain above pattern
    else:
        print("This News is Not about Rape")
    break


