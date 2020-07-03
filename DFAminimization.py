import json

class DFA:
    def __init__(self, states, sigma, start_state, final_state, transition):
        self.states = states
        self.sigma = sigma
        self.start_state = start_state
        self.final_state = final_state
        self.transition = transition
        self.empty = "-"

        self.print_otomat()

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
            for s in sigma:
                string = "-"
                # print(self.transition[state][s])
                if s not in self.transition[state]:
                    print('{:^10}'.format(self.empty), end="|")
                else:
                    string = ','.join(self.transition[state][s])
                print('{:^10}'.format(string), end="|")
            print("")


            

if __name__ == "__main__":
    with open("test.json", "r") as json_file:
        data = json.load(json_file)

    states = []
    sigma = []
    start_state =[]
    final_state = []
    transition = []

    if data["states"]:
        states = data["states"]
    else:
        print("ERROR: Khong tim thay tap trang thai")
        exit(1)
    
    if data["sigma"]:
        sigma = data["sigma"]
    else:
        print("ERROR: Khong tim thay bang chu cai")
        exit(1)
    
    if data["start"]:
        start_state = data["start"]
    else:
        print("ERROR: Khong tim thay trang thai bat dau")
        exit(1)
        
    if data["final"]:
        final_state = data["final"]
    else:
        print("ERROR: Khong tim thay tap trang thai ket thuc")
        exit(1)
        
    if data["transition"]:
        transition = data["transition"]
    else:
        print("ERROR: Khong tim thay ham chuyen")
        exit(1)

        
    DFA(states, sigma, start_state, final_state, transition)