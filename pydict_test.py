just_the_text = "This is an Apple string of words. I want to visit the Grand Canyon at Willow Tree Park."
normal_words = ['Jim', 'you', 'Pam', 'my', 'Sam', 'Brian', 'grape', 'Sink', 'Apple', 'Beetle', 'dork']
# strip all the other stuff off just_the_text
just_the_text = just_the_text.strip()
# identify all capitalized words over 3 chars and adds to cap_words

#print(normal_words)
li = list(just_the_text.split(" "))

print("starting li list:")
print(li)

cap_words = []
for i, element in enumerate(li):
    previous_element = li[i-1] if i > 0 else None
    current_element = element
    next_element = li[i+1] if i < len(li)-1 else None
    if i > 0 and i < len(li)-1:
        if current_element.istitle() and len(current_element) > 2:
            if previous_element.istitle() and current_element.istitle() and next_element.istitle():
                print(previous_element, current_element, next_element)
                three_together = previous_element + str(" ") + current_element + str(" ") + next_element
                cap_words.append(three_together)
                #print("deleting from 3:" + )
                del previous_element
                del current_element
                del next_element
            elif current_element.istitle() and next_element.istitle():
                print(current_element, next_element)
                two_together = current_element + str(" ") + next_element
                cap_words.append(two_together)
                del current_element
                del next_element
            else:
                print(current_element)
                one_together = current_element
                cap_words.append(one_together)
                del li[i]
        else:
            pass
    else:
        pass
print("")
print("here are the cap words list:")
print(cap_words)
print("")
print("ending li list:")
print(li)

#print(li)

##next_word = cap_words[1]

#cap_words[1] = current_word
#print("current_word: ")
#print(current_word)

#print("next_word: ")
#print(next_word)

#cap_words[0] = current_word + str(" ") + next_word
#del cap_words[2]



"""
for word in just_the_text.split():
    if word.istitle() and len(word) > 3 and next(word).istitle:
        cap_words.append(word)
        cap_words[word] = next(word)
    else:
        if word.istitle() and len(word) > 3:
            cap_words.append(word)
        else:
            pass
"""

