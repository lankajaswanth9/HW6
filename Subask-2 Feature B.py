total_work_days = num_sprint_days - days_off
    available_hours_per_person = (sum(hours_per_day_range) / 2) 

    effort_hours_per_person = (available_hours_per_person - hours_for_ceremonies) * total_work_days  

 
    total_effort_hours_for_team = effort_hours_per_person * num_team_members

    
    print("Effort-Hours/Person:", effort_hours_per_person)
    print("Effort-Hours for Team:", total_effort_hours_for_team)


calculate_effort_hours_capacity()