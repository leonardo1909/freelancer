from datetime import datetime
from dateutil.parser import parse


def skill_object(experience, skill):
    '''
        Create an object that represents the freelancer's skill on a experience.
    '''
    return {
        'id': skill['id'],
        'name': skill['name'],
        'startDate': experience['startDate'],
        'endDate': experience['endDate']
    }


def compute_total_months(id, name, tec_experience_dates):
    '''
        Calculate the total of months a freelancer have with one technology.
        It receives an id, a name and a list of duration experience with a certain technology.
    '''
    total_months = 0
    for experience in tec_experience_dates:
        total_months += ((experience['endDate'].year - experience['startDate'].year) * 12) + ((experience['endDate'].month - experience['startDate'].month))
    return {
        'id': id,
        'name': name,
        'durationInMonths': total_months
    }


def computedSkills(freelance_data):
    '''
        To compute the total amount of months a trainee have with a certain
        technology it creates a list of skills object with the technology
        and the experience time the trainee had with it.

        To simplify the process, the list is sorted by the technology id and
        the date the trainee started to work with it.

        Based on the previous experiences, it measure if newer experiences
        count more duration time to the trainee.
    '''
    skills_date_list = []
    for experience in freelance_data['freelance']['professionalExperiences']:
        for skill in experience['skills']:
            skills_date_list.append(
                skill_object(
                    experience=experience,
                    skill=skill
                )
            )
    skills_date_list = sorted(skills_date_list, key=lambda obj: (obj['id'], obj['startDate']))

    skill_duration = []
    tec_experience_dates = []
    last_skill = skills_date_list[0]['id']
    last_skill_name = skills_date_list[0]['name']
    while skills_date_list:
        skill_experience = skills_date_list.pop(0)
        start_date = parse(skill_experience['startDate']).date()
        end_date = parse(skill_experience['endDate']).date()

        if skill_experience['id'] != last_skill:
            skill_duration.append(
                compute_total_months(
                    id=last_skill,
                    name=last_skill_name,
                    tec_experience_dates=tec_experience_dates
                )
            )
            last_skill = skill_experience['id']
            last_skill_name = skill_experience['name']
            tec_experience_dates = []

        if not tec_experience_dates:
            tec_experience_dates.append(
                {
                    'startDate': start_date,
                    'endDate': end_date
                }
            )
        else:
            tec_experience = tec_experience_dates[-1]
            if start_date > tec_experience['endDate']:
                tec_experience_dates.append(
                    {
                        'startDate': start_date,
                        'endDate': end_date
                    }
                )
            elif start_date < tec_experience['endDate'] and end_date > tec_experience['endDate']:
                tec_experience_dates.append(
                    {
                        'startDate': tec_experience['endDate'],
                        'endDate': end_date
                    }
                )

    skill_duration.append(
        compute_total_months(
            id=last_skill,
            name=last_skill_name,
            tec_experience_dates=tec_experience_dates
        )
    )

    return {
        'freelance': {
            'id': freelance_data['freelance']['id'],
            'computedSkills': skill_duration
        }
    }
