'''
problem states :
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

we need to replace the word from dictionary in sentence. 
step 1: split the word in words using split method  and convert the dictionary into set for better accessing the element and
it is not complsory
step 2: define a replace_word funtion and it is a helper function to fid the matches between word and rootset 
def replace_word(word):
            for i in range(len(word)):
                if word[:i] in root_set:
                    return word[:i]
            return word 
if all the character present in the rootset it will retrun the word[:i} substring other wise normal word only 
step 3: and all the replace_word function for each word present in the words and finnaly retrun the joined string using join method 
'''
class Solution(object):
    def replaceWords(self, dictionary, sentence):
     
        words = sentence.split()
        root_set = set(dictionary)

        def replace_word(word):
            for i in range(len(word)):
                if word[:i] in root_set:
                    return word[:i]
            return word 
        
        replace_word = [replace_word(word) for word in words]
        return ' '.join(replace_word)
