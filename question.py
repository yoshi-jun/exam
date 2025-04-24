import numpy as np

#------------------------------------------------------------------------------
def load_question():
    with open('q.txt', 'r', encoding='utf-8') as file:
        content = file.read()

    contents = content.split("\n\n")
    subs=[]
    for sub in contents:
        subs.append(sub.split("\n"))

    return subs

#------------------------------------------------------------------------------
def load_ans():
    with open('a.txt', 'r', encoding='utf-8') as file:
        content = file.read()

    contents = content.split("\n\n")
    subs=[]
    for sub in contents:
        subs.append(sub.split("\n"))

    return subs

#==============================================================================
def main():
    Qs = load_question()
    As = load_ans()


    for i in range(len(Qs)):
        for j in range(len(Qs[i])):
            input(Qs[i][j])
            input(As[i][j])

if __name__=="__main__":
    main()