def student_marks(marks): return {'total': sum(marks), 'percentage': sum(marks) / (len(marks) * 100) * 100 if marks else 0}
