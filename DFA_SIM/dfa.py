class Sim_DFA:
    def __init__(self, delta, q0, accp):
        self.delta = delta
        self.q0 = q0
        self.accp = accp
    
    def simulate(self, s):
        state = self.q0
        visited = [state]
        for curr in s:
            state = self.delta[state][curr]
            visited.append(state)
        return state in self.accp, visited

dfa = {
    0:{'0':0, '1':1},
    1:{'0':2, '1':0},
    2:{'0':1, '1':2}
}


my_dfa = Sim_DFA(dfa, 0, {0})

strings = []
for i in range(2):
    tmp_str = input('Enter String: ')
    strings.append(tmp_str)

print('----------------')    

for string in strings:
    print('Running {}'.format(string))
    result, visited_states = my_dfa.simulate(string)

    for i, state in enumerate(visited_states):
        if (i == len(visited_states) - 1):
            print('s_{}'.format(state))
        else:
            print('s_{}'.format(state), '->', end=' ')
    print('Accepted:', result, '\n')
