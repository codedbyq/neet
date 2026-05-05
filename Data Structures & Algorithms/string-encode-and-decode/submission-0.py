class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            length = len(word)
            delimiter = "#"
            encoded_string += str(length) + delimiter + word
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            start, end = j+1, j+1+length
            decoded_list.append(s[start:end])
            i = end

        return decoded_list
