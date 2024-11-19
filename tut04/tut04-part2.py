from collections import defaultdict, Counter

def categorize_anagrams(words):
    """Categorize words into groups of anagrams."""
    anagram_dict = defaultdict(list)

    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        anagram_dict[sorted_word].append(word)

    # Reformat dictionary with sorted anagram groups
    result = {k: sorted(v) for k, v in anagram_dict.items()}

    return result

def calculate_frequency(words):
    """Calculate the total frequency of characters in the group of anagrams."""
    frequency = Counter()

    for word in words:
        frequency.update(word.lower())

    return frequency

def find_highest_frequency_group(anagram_dict):
    """Find the group with the highest total character frequency."""
    highest_frequency = 0
    highest_group = None

    for key, words in anagram_dict.items():
        freq = calculate_frequency(words)
        total_frequency = sum(freq.values())

        if total_frequency > highest_frequency:
            highest_frequency = total_frequency
            highest_group = words

    return highest_group

def main():
    # Input from user
    input_words = input("Enter a list of words separated by commas: ").split(',')
    input_words = [word.strip() for word in input_words]

    # Categorize anagrams
    anagram_dict = categorize_anagrams(input_words)

    # Print anagram dictionary
    print("Anagram Dictionary:")
    for key, words in anagram_dict.items():
        print(f"{key}: {words}")

    # Find and print the group with the highest character frequency
    highest_group = find_highest_frequency_group(anagram_dict)

    print("\nGroup with the highest total character frequency:")
    if highest_group:
        print(highest_group)
    else:
        print("No anagram groups found.")

if _name_ == "_main_":
    main()