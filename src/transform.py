def compute_final_grade(student: dict, weights: dict) -> None:
    """
    Calculates the final weighted score for a student.
    Weights used: Quizzes (20, Midterm (30%), Final (40%)
    """
    quizzes = [
        student['quiz1'] or 0,
        student['quiz2'] or 0,
        student['quiz3'] or 0,
        student['quiz4'] or 0,
        student['quiz5'] or 0
    ]
    quiz_ave = sum(quizzes) / len(quizzes)

    midterm = student['midterm'] or 0
    final = student['final'] or 0
    attendance = student['attendance_percent'] or 0

    score = (
        quiz_ave * weights['quizzes'] + 
        midterm * weights['midterm'] + 
        final * weights['final'] +
        attendance * weights['attendance']
    )

    student['final_grade'] = round(score, 2)

def assign_letter_grade(student: dict) -> None:
    """
    Assigns a letter grade based on the final score.
    Standard 10-point scale: A(90+), B(80-89), C(70-79), D(60-69), F(<60).
    """
    grade = student['final_grade']

    if grade >= 90:  letter = "A"
    elif grade >= 85: letter = "B+"
    elif grade >= 80: letter = "B"
    elif grade >= 75: letter = "C"
    else: letter = "F"

    student['letter_grade'] = letter