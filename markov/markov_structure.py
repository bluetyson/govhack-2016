import pykov

def markov_chain(states):
    T = pykov.Matrix()
    markov_states = []
    for i in xrange(0, len(states)-1):
        markov_states.append((states[i], states[i+1],))

    for i in xrange(len(markov_states)):
        total = len([j for j in markov_states if j[0] == markov_states[i][0]]),
        amount = markov_states.count(markov_states[i])
        markov_states[i] += (amount/float(total[0]),)
    for i in markov_states:
        if (i[0], i[1]) not in T:
            T[(i[0], i[1])] = i[2]

    return pykov.Chain(T)


def main():
    s1 = state.State("n")
    s2 = state.State("a")
    s3 = state.State("m")
    for i in markov_chain([s1, s2, s3, s2, s1, s3, s2, s1, s3, s2, s1]).walk(10):
        print i.name

if __name__ == "__main__":
    main()
