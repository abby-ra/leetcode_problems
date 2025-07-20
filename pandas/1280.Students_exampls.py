import pandas as pd

def students_and_examinations(Students: pd.DataFrame, 
                               Subjects: pd.DataFrame, 
                               Examinations: pd.DataFrame) -> pd.DataFrame:
    
    # Step 1: Cross join Students and Subjects
    students_subjects = Students.merge(Subjects, how='cross')

    # Step 2: Count how many times each student took each subject
    exam_counts = Examinations.groupby(['student_id', 'subject_name']) \
                              .size().reset_index(name='attended_exams')

    # Step 3: Merge and fill missing values
    result = students_subjects.merge(exam_counts, 
                                     on=['student_id', 'subject_name'], 
                                     how='left')
    
    result['attended_exams'] = result['attended_exams'].fillna(0).astype(int)

    # Step 4: Sort the result
    result = result.sort_values(by=['student_id', 'subject_name']).reset_index(drop=True)

    return result
