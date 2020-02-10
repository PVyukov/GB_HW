study = {}
with open('5_6_in_data', encoding='utf-8') as f:
    for subject in f:
        subject = subject.strip()
        lessons_cnt = 0
        subject_list = subject.split(': ')
        lessons_list = subject_list[1].split(' ')
        for lesson in lessons_list:
            if lesson == '—':
                continue
            lessons_cnt += int(lesson.split('(')[0])
        study[subject_list[0]] = lessons_cnt
print(study)