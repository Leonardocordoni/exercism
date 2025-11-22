"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    return [round(n) for n in student_scores]


def count_failed_students(student_scores):
    return sum(n<=40 for n in student_scores)


def above_threshold(student_scores, threshold):
    results = []
    for score in student_scores:
        if score >= threshold:
            results.append(score)
    return results


def letter_grades(highest):
    intervalo = round((highest - 40) / 4)
    results = []
    limite = 41
    for _ in range(4):
        results.append(limite)
        limite += intervalo
    return results


def student_ranking(student_scores, student_names):
    results = []
    for rank, (name, score) in enumerate(zip(student_names, student_scores), start=1):
        results.append(f"{rank}. {name}: {score}")
    return results


def perfect_score(student_info):
    for student in student_info:
        if student[1] == 100:
            return student
    return []