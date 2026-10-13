count = {}

def text()->str:
    text = input(str("Zadej text:"))
    return text

def spliter(text:str)->list:
    text_lower = text.lower()
    slova = text_lower.split()
    return slova

def words_num(slova:list)->int:
    return len(slova)

def words_counter(count:dict, slova)->dict:
    for slovo in slova:
        if slovo in count:
            count[slovo] += 1
        else:
            count[slovo] = 1
    return count

def main():
    text_input = text()
    slova = spliter(text_input)
    word_number = words_num(slova)
    words_count = words_counter(count, slova)

    print(f"{slova}")
    print(f"počet slov: {word_number}")
    print(f"počet stejných slov: {words_count}")

if __name__ == "__main__":
    main()
