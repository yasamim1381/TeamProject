#zahra sahamivand
text_dot = input()
text = text_dot.replace("."," ")
text_set = set(text.split())
longest_word = 0 

for j in text_set:
    if len(j) > longest_word: 
        longest_word = len(j)

print("words: " + f"{len(text_set)}")
print("longest: " + f"{longest_word}")
print("chars: " + f"{len(text_dot)}")