import markovify
import csv

def markov_text(texts):
    markov_dict = {}
    for i in texts:
        print i
        model = markovify.Text(i[1].strip())
        markov_dict[i[0]] = model.make_sentence()
    return markov_dict


def main():
    with open("corpus.csv", "rb") as f:
        reader = csv.reader(f, delimiter=' ', quotechar='|')
        markov_text([row.replace(",", "|", 1).split("|") for row in f])


if __name__ == "__main__":
    main()
