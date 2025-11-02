def num_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    character_count = {}
    for character in text:
        character = character.lower()
        if 'a' <= character <= 'z':
            if character in character_count:
                character_count[character] += 1
            else:
                character_count[character] = 1
    return character_count

def sort_on(dict_to_sort):
    def sort_key(dict_item):
        return dict_item["num"]
    
    sorted_list = []
    for char, num in dict_to_sort.items():
        sorted_list.append({"char": char, "num": num})
    
    sorted_list.sort(key=sort_key, reverse=True)
    return sorted_list
