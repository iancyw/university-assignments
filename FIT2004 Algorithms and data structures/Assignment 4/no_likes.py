def main():
    lst = S.strip().split("\n")
    person1 = [char for char in lst[0]]
    person2 = [char for char in lst[1]]

    same = 0
    for i in range(len(person1)):
        if person1[i] == person2[i]:
            same += 1
    return same

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        S = input()

        out_ = main()
        print(out_)