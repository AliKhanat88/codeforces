from collections import defaultdict


def print_max_result(questions, students, answers, weightage):
    sum = 0
    for i in  range(questions):
        ans_dict = defaultdict(int)
        for j in range(students):
            ans_dict[answers[j][i]] += 1
        sum += max(ans_dict.values()) * weightage[i]
    print(sum)




def main():
    students, questions = map(int , input().split())
    answers = []
    for i in range(students):
        answers.append(input())
    weightage = [int(num) for num in input().split()]
    print_max_result(questions, students, answers, weightage)

main()