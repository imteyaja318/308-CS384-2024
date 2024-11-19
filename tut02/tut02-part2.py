def compressedString(text):
    if not text:
        return ""
    result = ""
    count = 1
    current_char = text[0]

    for i in range(1,len(text)):
        if text[i] == current_char:
            count += 1
        else:
            result += current_char
            if count >= 1:
                result += str(count)
                current_char = text[i]
                count = 1
    result += current_char
    if count >= 1:
        result += str(count)
    return result
input_string = input("Enter the string : ")
compressed_string =  compressedString(input_string)
print(compressed_string)