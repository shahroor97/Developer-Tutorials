import string
def QuestionsMarks(bonal):
  nums = []
  for i, char in enumerate(bonal):
    if char.isdigit():
      nums.append(int(char))
      for j in range(i-1,-1,-1):
        if bonal[j].isdigit():
          if nums[-1]+int(bonal[j]) == 10:
            if bonal[j:i].count('?') != 3:
              print('False')
            else:
              if bonal[j:i].count('?') == 3:
                print('True')
              
QuestionsMarks('1b3??7')

sentence = 'BEEOP BOOP #$ASJ#%@# BAAPIDYBOOP#@$@#4'

def longestword(sen):
  translator = str.maketrans('','', string.punctuation + string.digits)
  translated_sentence = sen.translate(translator)
  words = translated_sentence.split()
  longest_word = ''
  for word in words:
    if len(word) > len(longest_word):
        longest_word = word
  return longest_word
print(longestword(sentence))


