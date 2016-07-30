import pykov

def markov_chain(states):
    T = pykov.Matrix()
    known_states = []
    for i in xrange(0, len(states)-1):
        state = (states[i], states[i+1])
        T_list = list(T)
        total = len([i for i in T_list if i[0] == state[0]])
        pblty = None
        if state not in T:
            pblty = 1/(float(total) or 1)
        else:
            state_cnt = T_list.count(state)
            pblty = state_cnt/float(total)
        T[state] = pblty
    return pykov.Chain(T)


def main():
    s1 = state.State("n")
    s2 = state.State("a")
    s3 = state.State("m")
    for i in markov_chain([s1, s2, s3, s2, s1, s3, s2, s1, s3, s2, s1]).walk(10):
        print i.name

if __name__ == "__main__":
    main()
