import markovify
import csv

def markov_text(state_to_corpus):
    result = {}
    for item in state_to_corpus:
        result[item] = markovify.Text(''.join(state_to_corpus.get(item)).replace("(", "").replace(")", ""))
    return result

def main():
    with open("corpus.csv", "rb") as f:
        reader = csv.reader(f, delimiter=' ', quotecha='|')
        markov_text([row.replace(",", "|", 1).split("|") for row in f])


if __name__ == "__main__":
    main()
