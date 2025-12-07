class Solution:
    def compress(self, chars: List[str]) -> int:
        write_index = 0  
        i = 0  
        while i < len(chars):
            current_char = chars[i]
            counter = 0
            while i < len(chars) and chars[i] == current_char:
                i += 1
                counter += 1
            chars[write_index] = current_char
            write_index += 1
            if counter > 1:
                for digit in str(counter):
                    chars[write_index] = digit
                    write_index += 1
        return write_index
