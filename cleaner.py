 ###########
## Cleaner ##
 ###########

import re

class Cleaner(object):
    """ Creates an object for building and cleaning sentences """
    def __init__(self):
        self.text = ""
        self.sent_list = []

    def set_text(self, text):
        self.text = text

    def get_sentlist(self):
        return self.sent_list

    def set_sentlist(self, sent_list):
        self.sent_list = sent_list

    # #Generate sentence list from collected text
    # def build_sentlist(self):
    #     print("building sentence list...")
    #     pun_list = [".", "?", "!"]
    #     temp_text = ""
    #     temp_list = []
    #     for char in self.text:
    #         temp_text = temp_text + char

    #         if char in pun_list:
    #             temp_text = " ".join(temp_text.split())
    #             temp_text = re.sub(' +', ' ', temp_text)
    #             temp_list.append(temp_text)
    #             temp_text = ""

    #     self.sent_list = temp_list

    def sort_sentcs(self):
        expression = re.compile(r'([A-Z][^\.!?]*[\.!?])')
        temp_list = re.findall(expression, self.text)
        self.sent_list = temp_list

    #Remove whitespace from sentences
    def remv_wtspace(self):
        print("removing whitespace...")
        temp_list = []
        for sentc in self.sent_list:
            sentc = " ".join(sentc.split())
            temp_list.append(sentc)

        self.sent_list = temp_list

    # #Remove non-alphabetical characters    
    # def remv_noalpha(self):
    #     print("removing non-alphabetical characters...")
    #     pun_list = [".", "?", "!"]
    #     pass_list = [" ", ",", "'"]
    #     temp_list = []
    #     for sentc in self.sent_list:
    #         temp_sent = ""
    #         for char in sentc:
    #             if char.isalpha() or char in pass_list:
    #                 temp_sent = temp_sent + char

    #             elif char in pun_list:
    #                 temp_sent = temp_sent + char
    #                 temp_list.append(temp_sent)
    #                 break

    #     self.sent_list = temp_list
    
    #Keep sentences that contain a keyword
    def check_keywords(self, keywords):
        print("checking for keywords...")
        temp_list = []
        for sentc in self.sent_list:
            for kywrd in keywords:
                if kywrd in sentc:
                    print(sentc)
                    print(kywrd)
                    temp_list.append(sentc)
                    break

        self.sent_list = temp_list

    # #Remove duplicate sentences
    # def remv_duplicates(self):
    #     print("removing duplicate sentences...")
    #     temp_list = []
    #     for sentc in self.sent_list:
    #         if sentc not in temp_list:
    #             temp_list.append(sentc)

    #     self.sent_list = temp_list

    def remv_duplicates(self):
        print("removing duplicates...")
        temp_list = list(set(self.sent_list))
        self.sent_list = temp_list

    #Remove sentences with duplicate words
    def remv_dupwords(self):
        print("removing duplicate words...")
        #List of commonly used conjunctions, articles, and prepositions to ignore
        pass_list = ["is", "for", "and", "or", "are", "the", "a", "an", "at", "of", "to", "in", "on", "they", "there"]
        temp_list = []
        temp_list = temp_list + self.sent_list
        for sentc in self.sent_list:
            temp_sentc = re.sub(r'[^\w\s]', '', sentc)
            check_list = temp_sentc.split()
            word_list = []
            for wrd in check_list:
                if wrd in pass_list:
                    pass
                    
                elif wrd.lower() not in word_list:
                    word_list.append(wrd.lower())

                else:
                    with open("duplicate words.txt", "a") as temp_file:
                        temp_file.write(wrd + "\n")
                        temp_file.close()
                    temp_list.remove(sentc)
                    break

        self.sent_list = temp_list

    #Remove sentences with first-person language
    def remv_firstperson(self):
        print("removing first-person language...")
        word_list = ["I", "me", "Me", "my", "My", "mine", "Mine", "our", "Our", "ours", "Ours", "us", "Us", "we", "We"]
        temp_list = []
        temp_list = temp_list + self.sent_list
        for sentc in self.sent_list:
            temp_sentc = re.sub(r'[^\w\s]', '', sentc)
            check_list = temp_sentc.split()
            for wrd in check_list:
                if wrd not in word_list:
                    pass

                else:
                    temp_list.remove(sentc)
                    break

        self.sent_list = temp_list

    #Remove sentences with second-person language
    def remv_secondperson(self):
        print("removing second-person language...")
        word_list = ["you", "You", "your", "Your", "yours", "Yours"]
        temp_list = []
        temp_list = temp_list + self.sent_list
        for sentc in self.sent_list:
            temp_sentc = re.sub(r'[^\w\s]', '', sentc)
            check_list = temp_sentc.split()
            for wrd in check_list:
                if wrd not in word_list:
                    pass

                else:
                    temp_list.remove(sentc)
                    break

        self.sent_list = temp_list

    #Remove non-declarative sentences from sentence list
    def remv_nodeclare(self):
        print("removing non-declaratives...")
        temp_list = []
        for sentc in self.sent_list:
            try:
                sentc = sentc.strip()
                if sentc[-1] == ".":
                    temp_list.append(sentc)

            except:
                pass
            
        self.sent_list = temp_list

    # #This is done with remv_noalpha
    # #Remove sentences with numbers
    # def remv_exnums(self):
    #     print("removing numbers...")
    #     temp_list = []
    #     temp_list = temp_list + self.sent_list
    #     for sentc in self.sent_list:
    #         for char in sentc:
    #             if char.isdigit():
    #                     temp_list.remove(sentc)
    #                     break

    #     self.sent_list = temp_list

    

    # #Remove sentences that don't begin with uppercase letters
    # def remv_noleadcap(self):
    #     print("removing non-capital leading characters...")
    #     temp_list = []
    #     for sentc in self.sent_list:
    #         sentc = sentc.strip()
    #         if sentc[0].isupper():
    #             temp_list.append(sentc)

    #     self.sent_list = temp_list

    

    # #Remove empty whitespace from before punctuation
    def remv_endspc(self):
        print("removing endspaces...")
        temp_list = []
        for sentc in self.sent_list:  
            try:
                sentc.strip()         
                end_indx = len(sentc) - 1
                if sentc[end_indx - 1] == " ":
                    sentc = sentc[:end_indx - 1:end_indx]

            except:
                pass
            
            temp_list.append(sentc)

        self.sent_list = temp_list

    def remv_punspace(self):
        temp_list = []
        for sentc in self.sent_list:
            sentc = re.sub(r'\s([?.!",](?:\s|$))', r'\1', sentc)
            temp_list.append(sentc)

        self.sent_list = temp_list

    #Remove sentences with single letters
    def remv_exletters(self):
        print("removing extra letters...")
        temp_list = []
        temp_list = temp_list + self.sent_list
        for sentc in self.sent_list:
            temp_sentc = re.sub(r'[^\w\s]', '', sentc)
            check_list = temp_sentc.split()
            for wrd in check_list:
                if len(wrd) == 1 and wrd != "a":
                    temp_list.remove(sentc)
                    break

        self.sent_list = temp_list

    #Remove sentences with extra capital letters
    def remv_excap(self):
        print("removing extra capitals...")
        temp_list = [] 
        temp_list = temp_list + self.sent_list
        for sentc in self.sent_list:
            for char in sentc[1:]:
                if char.isupper():
                    temp_list.remove(sentc)
                    break

        self.sent_list = temp_list

    # def remv_exchars(self):
    #     char_list = ["{", "}", "#", "+", "-", "=", ">", "<" "@", "$", "|", "/", "_", "^"]
    #     temp_list = []
    #     temp_list = temp_list + self.sent_list
    #     for sentc in self.sent_list:
    #         for char in char_list:
    #             if char in sentc:
    #                 temp_list.remove(sentc)
    #                 break

    #     self.sent_list = temp_list

    #Remove sentences in sentence list based on min and max word length
    def trim_sentlist(self, sent_min, sent_max):
        print("trimming sentence list...")
        temp_list = []
        for sentc in self.sent_list:
            if len(sentc.split()) >= sent_min and len(sentc.split()) <= sent_max:
                temp_list.append(sentc)
                
        self.sent_list = temp_list


    #Check words against dictionary
    def remv_misspelled(self, words):
        print("removing misspellings...")
        dict_list = [""]
        words = open(words, 'r')
        wrdlines = words.readlines()
        for wrd in wrdlines:
            dict_list.append(re.sub('\n', '', wrd.lower()))
            
        temp_list = []
        for sentc in self.sent_list:
            word_list = re.sub(r'[^\w\s]', '', sentc.lower()).split()
            check = all(item in dict_list for item in word_list)
            if check == True:
                temp_list.append(sentc)

        self.sent_list = temp_list

    # #Check words against dictionary
    # def remv_misspelled(self, words):
    #     print("removing misspellings...")
    #     dict_list = [""]
    #     words = open(words, 'r')
    #     wrdlines = words.readlines()
    #     for wrd in wrdlines:
    #         dict_list.append(re.sub('\n', '', wrd.lower()))
            
    #     temp_list = []
    #     temp_list = temp_list + self.sent_list
    #     for sentc in self.sent_list:
    #         word_list = re.sub(r'[^\w\s]', '', sentc.lower()).split()
    #         for wrd in word_list:
    #             if wrd not in dict_list:
    #                 temp_list.remove(sentc)
    #                 break

    #     self.sent_list = temp_list

    # #Remove sentences with misspelled words
    # def remv_badspelling(self):
    #     print("checking for spelling errors...")
    #     from spellchecker import SpellChecker
    #     spellchecker = SpellChecker(distance=1)
    #     temp_list = []
    #     temp_list = temp_list + self.sent_list
    #     for sentc in self.sent_list:
    #         word_list = re.sub(r'[^\w\s]', '', sentc).split()
    #         for wrd in word_list:
    #             print(wrd)
                

    #         print("word list: " + str(word_list))
    #         misspelled = spellchecker.unknown(word_list)
    #         print("misspelled: " + str(misspelled))
    #         if len(misspelled) > 0:
    #             print("misspelled tag: " + str(misspelled))
    #             temp_list.remove(sentc)
            
    #     self.sent_list = temp_list

    # #LANGUAGE-TOOL Functions
    # #Fix spelling and grammar errors in sentence list
    # def fix_language(self):
    #     import language_tool_python
    #     print("fixing spelling and grammar errors...")
    #     lang_tool = language_tool_python.LanguageTool('en-US')
    #     temp_list = []
    #     for sentc in self.sent_list:
    #         errors = lang_tool.check(sentc)
    #         if len(errors) > 0:
    #                 sentc = lang_tool.correct(sentc)
                    
    #         temp_list.append(sentc)

    #     self.sent_list = temp_list

    # #Remove sentences with spelling and grammar errors from sentence list
    # def remv_badlanguage(self):
    #     import language_tool_python
    #     print("removing spelling and grammar errors...")
    #     lang_tool = language_tool_python.LanguageTool('en-US')
    #     temp_list = []
    #     for sentc in self.sent_list:
    #         print(sentc)
    #         errors = lang_tool.check(sentc)
    #         print("errors: " + str(errors))
    #         if len(errors) == 0:
    #             temp_list.append(sentc)

    #     self.sent_list = temp_list      
