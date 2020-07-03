import json

if __name__ == "__main__":
    with open("test.json", "r") as json_file:
        data = json.load(json_file)

    print(data["states"])