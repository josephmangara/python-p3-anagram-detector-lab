# your code goes here!

class Anagram:
    def __init__(self, anagram):
        self.anagram = anagram

    def match(self, words):
        matching_anagrams = [word for word in words if sorted(word) == sorted(self.anagram)]
        
        return matching_anagrams
    
listen = Anagram("acers")
result = listen.match(["enlists", "google", "inlets", "races"])
print(result)