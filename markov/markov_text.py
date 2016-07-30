import markovify
import csv

def markov_text(texts):
    markov_dict = {}
    for i in texts:
        # print texts[i][0][0]
        markov_dict[i] = markovify.Text(texts[i][0][0].replace("(", "").replace(")", ""))

    return markov_dict

def main():
    with open("corpus.csv", "rb") as f:
        reader = csv.reader(f, delimiter=' ', quotecha='|')
        markov_text([row.replace(",", "|", 1).split("|") for row in f])


if __name__ == "__main__":
    main()
