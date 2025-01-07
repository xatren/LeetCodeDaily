class Solution(object):
    def stringMatching(self, words):
        result = []

        # Compare each word with all other words
        for i in range(len(words)):
            for j in range(len(words)):
                # Skip comparing word with itself
                if i != j:
                    # If current word is a substring of another word
                    if words[i] in words[j]:
                        result.append(words[i])
                        # Break inner loop once we find a match
                        break

        return result
        