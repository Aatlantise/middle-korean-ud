

def main():
    sents = []
    tokens = []
    with open("hunmin-tokens.txt", encoding='utf-8') as f:
        for line in f:
            if line.strip():
                tokens.append(line.strip())
            else:
                sents.append(tokens)
                tokens = []

    i = 1

    f = open("okm_Hunmin-ud-test.conllu", 'w', encoding='utf-8')
    for sent in sents:
        j = 1
        sent_str = " ".join(sent)
        f.write(f"# sent_id = {i}\n")
        f.write(f"# sent = {sent_str}\n")
        for token in sent:
            _fields = '\t'.join(['_'] + ["NOUN"] + ['_'] * 2 + ["0"] + ['root'] + ['_'] * 2)
            f.write(f"{j}\t{token}\t{_fields}\n")
            j += 1
        i += 1
        f.write('\n')
    f.write('\n')
    f.close()

if __name__ == '__main__':
    main()