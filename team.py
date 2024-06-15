class Team(object):
    def __init__(self, team_name, team_subject, team_coach, teaching_week, teaching_time, team_students):
        self.team_name = team_name
        self.team_subject = team_subject
        self.team_coach = team_coach
        self.teaching_week = teaching_week
        self.teaching_time = teaching_time
        self.team_students = team_students

c1_stu = ["符迅"]
c1 = Team("C++2", "C++", "Ward老师", "周五", "14:00~17:00", c1_stu)
