import math

def clean_text(txt):
    """
    takes a string of text txt as a parameter and returns a list containing the words 
    in txt after it has been “cleaned”
    """
    lower = txt.lower()
    for symbol in """.,?"'!;:""":
        lower = lower.replace(symbol, ' ')
        
    lower_split = lower.split()
    return lower_split

def sample_file_write(filename):
    """
    A function that demonstrates how to write a
    Python dictionary to an easily-readable file.
    """
    d = {'test': 1, 'foo': 42}   
    f = open(filename, 'w')      
    f.write(str(d))              
    f.close()

def sample_file_read(filename):
    """
    A function that demonstrates how to read a
    Python dictionary from a file.
    """
    f = open(filename, 'r')    
    d_str = f.read()          
    f.close()

    d = dict(eval(d_str))     

    print("Inside the newly-read dictionary, d, we have:")
    print(d)   

def stem(s):
    """
    accepts a string as a parameter and returns the stem of the string
    """
    if s[-3:] == 'ing':
        if s[-4] == s[-5]:
            s = s[:-4]
        else:
            s = s[:-3]
    elif s[-2:] == 'er':
        s = s[:-2]
    elif s[-2:] == 'es':
        s = s[:-2]
    elif s[-2:] == 'ly':
        s = s[:-2]
    elif s[-4:] == 'ment':
        s = s[:-4]
    elif s[-2:] == 'ed':
        s = s[:-2]
    elif s[-3:] == 'ers':
        s = s[:-3]
    elif s[-1:] == 'y':
        s = s[:-1] + 'i'
    elif s[-1:] == 'e':
        s = s[:-1]
    elif s[-1:] == 's':
        s = s[:-1]
        
    return s

def compare_dictionaries(d1, d2):
    """
    takes two feature dictionaries d1 and d2 as inputs and computes and 
    return their log similarity score
    """
    total = 0
    log_score = 0
    if d1 == {}:
        return -50
    for x in d1:
        total += d1[x]
    if total == 0:
        return -50
    for y in d2:
        if y in d1:
            log_score += math.log(d1[y]/total)*d2[y]
        else:
            log_score += math.log(0.5/total)*d2[y]
    
    return log_score
        

class TextModel:
    """
    serves as a blueprint for objects that model a body of text
    """
    
    def __init__(self, model_name):
        """
        constructs a new TextModel object by accepting a string model_name as a parameter
        """
        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.punc = {}
        
    def __repr__(self):
       """
       returns a string that includes the name of the model as well as the sizes of 
       the dictionaries for each feature of the text
       """
       s = 'text model name: ' + self.name + '\n'
       s += '  number of words: ' + str(len(self.words)) + '\n'
       s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
       s += '  number of stems: ' + str(len(self.stems)) + '\n'
       s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
       s += '  number of punctuations: ' + str(len(self.punc)) + '\n'
       return s
   
    def add_string(self, s):
        """
        adds a string of text s to the model by augmenting the feature dictionaries 
        defined in the constructor
        """
        
        """cleans the text by removing punctuation and updates the words dictionary"""        
        new = clean_text(s)
        for x in new:
            if x in self.words:
                self.words[x] += 1
            else:
                self.words[x] = 1
            
        """cleans the text by removing punctuation and adds to the word_lengths dictionary"""
        for x in new:
            length = len(x)
            if length in self.word_lengths:
                self.word_lengths[length] += 1
            else:
                self.word_lengths[length] = 1
                    
        """cleans the text by removing punctuation and adds to the stems dictionary"""
        for x in new:
            new2 = stem(x)    
            if new2 in self.stems:
                self.stems[new2] += 1
            else:
                self.stems[new2] = 1
        
        """splits the text into a list of words and updates the sentence_lengths dictionary"""
        sentence = 0
        for x in s.split():
            if x[-1] not in '.!?':
                sentence += 1
            else:
                sentence += 1
                if sentence in self.sentence_lengths:
                    self.sentence_lengths[sentence] += 1
                else:
                    self.sentence_lengths[sentence] = 1
                sentence = 0
                
        """splits the text into a list of words and updates the punc dictionary"""
        for x in s.split():
            if x[-1] in '.!?':
                a = x[-1]  
                if a in self.punc:
                    self.punc[a] += 1
                else:
                    self.punc[a] = 1
    
    def add_file(self, filename):
        """
        adds all of the text in the file identified by filename to the model
        """
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        text = f.read()
        self.add_string(text)
        
    def save_model(self):
        """
        saves the TextModel object self by writing its various feature dictionaries to files
        """
        words = self.words
        x = open(self.name + '_' + 'words', 'w')
        x.write(str(words))
        x.close()
        
        word_lengths = self.word_lengths
        y = open(self.name + '_' + 'word_lengths', 'w')
        y.write(str(word_lengths))
        y.close()
        
        stems = self.stems
        s = open(self.name + '_' + 'stems', 'w')
        s.write(str(stems))
        s.close()
        
        sentence_lengths = self.sentence_lengths
        n = open(self.name + '_' + 'sentence_lengths', 'w')
        n.write(str(sentence_lengths))
        n.close()
        
        punctuation = self.punc
        p = open(self.name + '_' + 'punc', 'w')
        p.write(str(punctuation))
        p.close()
        
    def read_model(self):
        """
        reads the stored dictionaries for the called TextModel object from their files 
        and assigns them to the attributes of the called TextModel
        """
        x = open(self.name + '_' + 'words', 'r')    
        d_str1 = x.read()          
        x.close()
        self.words = dict(eval(d_str1))     
        
        y = open(self.name + '_' + 'word_lengths', 'r')    
        d_str2 = y.read()          
        y.close()
        self.word_lengths = dict(eval(d_str2))
        
        s = open(self.name + '_' + 'stems', 'r')
        d_str3 = s.read()          
        s.close()
        self.stems = dict(eval(d_str3))
        
        n = open(self.name + '_' + 'sentence_lengths', 'r')
        d_str4 = n.read()          
        n.close()
        self.sentence_lengths = dict(eval(d_str4))

        p = open(self.name + '_' + 'punc', 'r')
        d_str5 = p.read()          
        p.close()
        self.punc = dict(eval(d_str5))
        
        
    def similarity_scores(self, other):
        """
        computes and returns a list of log similarity scores measuring the similarity 
        of self and other – one score for each type of feature
        """
        word_score = compare_dictionaries(other.words, self.words)
        word_lengths_score = compare_dictionaries(other.word_lengths, self.word_lengths)
        stems_score = compare_dictionaries(other.stems, self.stems)
        sentence_lengths_score = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
        punctuation_score = compare_dictionaries(other.punc, self.punc)
        
        result = [word_score, word_lengths_score, stems_score, sentence_lengths_score, punctuation_score]
        
        return result
    
    def classify(self, source1, source2):
        """
        compares the called TextModel object (self) to two other “source” TextModel objects 
        (source1 and source2) and determines which of these other TextModels is the more likely 
        source of the called TextModel
        """
        
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        print('scores for', source1.name + ':', scores1)
        print('scores for', source2.name + ':', scores2)
        
        count1 = 0
        count2 = 0
        for x in range(len(scores1)):
            if scores1[x] > scores2[x]:
                count1 += 1
            elif scores2[x] > scores1[x]:
                count2 += 1
            
        if count1 > count2:
            print(self.name, 'is more likely to have come from', source1.name)
        elif count2 > count1:
            print(self.name, 'is more likely to have come from', source2.name)


def test():
    """tests the TextModel implementation"""
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')

    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)
    
def run_tests():
    """compares source models to four new text documents and computes similarity scores
    to determine which source model is the more likely source"""
    source1 = TextModel('new york times')
    source1.add_file('NY Times Article 1.txt')
    source1.add_file('NY Times Article 2.txt')
    source1.add_file('NY Times Article 3.txt')
    
    source2 = TextModel('boston globe')
    source2.add_file('Boston Globe Article 1.txt')
    source2.add_file('Boston Globe Article 2.txt')
    source2.add_file('Boston Globe Article 3.txt')
    
    new1 = TextModel('lowell sun')
    new1.add_file('Lowell Sun Article.txt')
    new1.classify(source1, source2)

    new2 = TextModel('westford cat')
    new2.add_file('Westford Cat Article.txt')
    new2.classify(source1, source2)

    new3 = TextModel('washington post')
    new3.add_file('Washington Post Article.txt')
    new3.classify(source1, source2)
    
    new4 = TextModel('cnn')
    new4.add_file('CNN Article.txt')
    new4.classify(source1, source2)

        


        
    
       
        