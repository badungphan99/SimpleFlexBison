import json


class DFA:
    def __init__(self, states, sigma, start_state, final_state, transition):
        self.states = sorted(states)
        self.sigma = sigma
        self.start_state = start_state
        self.final_state = final_state
        self.transition = transition
        self.add_state = "aS"
        self.empty = "-"

        print("------------", "Otomat nhap vao", "------------")
        self.print_otomat()
        self.fill()
        self.mDFA()
        print("------------", "Otomat ket qua", "------------")
        self.print_otomat()

    def listToString(self, s):
        str1 = "_"
        return (str1.join(s))

    def print_otomat(self):
        print("Tap trang thai : ", self.states)
        print("Bang chu cai : ", self.sigma)
        print("Trang thai khoi dau : ", self.start_state)
        print("Tap trang thai ket : ", self.final_state)

        print('{:^10}'.format("δ"), end="|")
        for s in self.sigma:
            print('{:^10}'.format(s), end="|")
        print("")
        for state in self.states:
            print('{:^10}'.format(state), end="|")
            for s in self.sigma:
                if s not in self.transition[state]:
                    print('{:^10}'.format(self.empty), end="|")
                else:
                    print('{:^10}'.format(self.transition[state][s]), end="|")
            print("")

    def mDFA(self):

        table = {}
        for i, r in enumerate(self.states):
            table[r] = {}
            for c in self.states[:i]:
                if (r in self.final_state) != (c in self.final_state):
                    table[r][c] = 1
                else:
                    table[r][c] = 0

        # print("A", table["A"])
        # print("B", table["B"])
        # print("C", table["C"])
        # print("D", table["D"])
        # print("E", table["E"])
        # print("F", table["F"])
        # print("--------------")

        flag = True
        while flag:
            flag = False
            for i, r in enumerate(self.states):
                for c in self.states[:i]:
                    if table[r][c] == 1:
                        continue
                    for s in self.sigma:
                        tmp_r = self.transition[r][s]
                        tmp_c = self.transition[c][s]
                        if tmp_c != tmp_r and table[tmp_r] and table[tmp_r][tmp_c] and table[tmp_r][tmp_c] == 1:
                            table[r][c] = 1
                            flag = True

        new_states = list(self.states)
        index = {}

        for i in new_states:
            index[i] = 0

        for i, r in enumerate(self.states):
            for c in self.states[:i]:
                if table[r][c] == 0:
                    if index[r] == 0 and index[c] == 0:
                        new_states.append(sorted([r, c]))
                        index[r] = i
                        index[c] = i
                        new_states.remove(r)
                        new_states.remove(c)
                    elif index[r] != 0 and index[c] == 0:
                        print(r, c)
                        tmp = []
                        for tmpi in index:
                            if index[tmpi] == index[r]:
                                tmp.append(tmpi)
                        new_states.remove(c)
                        new_states.remove(sorted(tmp))
                        tmp.append(c)
                        new_states.append(sorted(tmp))
                        for t in tmp:
                            index[t] = i
                    elif index[r] == 0 and index[c] != 0:
                        tmp = []
                        for tmpi in index:
                            if index[tmpi] == index[c]:
                                tmp.append(tmpi)
                        new_states.remove(r)
                        new_states.remove(sorted(tmp))
                        tmp.append(r)
                        new_states.append(sorted(tmp))
                        for t in tmp:
                            index[t] = i

        new_transition = {}
        for ns in new_states:
            for s in self.sigma:
                nss = self.listToString(ns)
                if nss not in new_transition:
                    new_transition[nss] = {}
                tmp_state = self.transition[ns[0]][s]
                for tmp_ns in new_states:
                    if tmp_state in tmp_ns:
                        new_transition[nss][s] = self.listToString(tmp_ns)
                        break
        new_final = []
        new_states_str = []

        for ns in new_states:
            state = self.listToString(ns)
            new_states_str.append(state)
            for s in ns:
                if s == self.start_state:
                    self.start_state = state
                if s in self.final_state and state not in new_final:
                    new_final.append(state)

        self.states = new_states_str
        self.final_state = new_final
        self.transition = new_transition

    def fill(self):
        flag = False
        for state in self.states:
            if not state in self.transition:
                flag = True
                self.transition[state] = {}
            for s in self.sigma:
                if not s in self.transition[state]:
                    flag = True
                    self.transition[state][s] = self.add_state
        if flag:
            self.states.append(self.add_state)
            self.transition[self.add_state] = {}
            for s in self.sigma:
                self.transition[self.add_state][s] = self.add_state


if __name__ == "__main__":
    with open("test.json", "r") as json_file:
        data = json.load(json_file)

    states = []
    sigma = []
    start_state = []
    final_state = []
    transition = []

    assert data["states"], "ERROR: Khong tim thay tap trang thai"
    assert data["sigma"], "ERROR: Khong tim thay bang chu cai"
    assert data["start"], "ERROR: Khong tim thay bang chu cai"
    assert data["final"], "ERROR: Khong tim thay tap trang thai ket thuc"
    assert data["transition"], "ERROR: Khong tim thay ham chuyen"

    states = data["states"]
    sigma = data["sigma"]
    start_state = data["start"]
    final_state = data["final"]
    transition = data["transition"]

    DFA(states, sigma, start_state, final_state, transition)
