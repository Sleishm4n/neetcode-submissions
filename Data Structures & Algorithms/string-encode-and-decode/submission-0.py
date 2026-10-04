class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string = ""
        for string in strs:
            str_len = str(len(string))
            msg = str_len + "~" + string
            encoded_string += msg

        return encoded_string

    def decode(self, s: str) -> List[str]:

        decoded_strs = []
        i = 0
        while i < len(s):
            j = s.find("~", i)
            length = int(s[i:j])

            start = j + 1
            end = start + length

            decoded_strs.append(s[start:end])
            i = end

        return decoded_strs