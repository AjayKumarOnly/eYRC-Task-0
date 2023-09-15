def count_word_lengths(string):
    words = string[1:].split()
    word_lengths = [str(len(word)) for word in words]
    result = ",".join(word_lengths)
    return result
T = int(input())
for _ in range(T):
    input_string = input()
    output = count_word_lengths(input_string)
    print(output)
