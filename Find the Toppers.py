def main():
    T = int(input())  
    if 1 <= T <= 25:
        for _ in range(T):
            N = int(input())  
            if 2 <= N <= 100:
                student_scores = {}  
        
                for _ in range(N):
                    name, score = input().split()
                    score = float(score)
                    if 0 <= score <= 100:
                        student_scores[name] = score
            
                max_score_students = find_students_with_max_score(student_scores)
            
                for student in max_score_students:
                    print(student)

def find_students_with_max_score(students):
    max_score = max(students.values())
    max_score_students = [name for name, score in students.items() if score == max_score]
    max_score_students.sort()  
    return max_score_students
    
main()
