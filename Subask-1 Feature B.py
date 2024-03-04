def calculate_effort_hours_capacity():
    num_sprint_days = int(input("Total number of Sprint Days:"))

    num_team_members = int(input("Number of Team Members:"))
    team_members = [input(f"Name of the Team Member {i + 1}:") for i in range(num_team_members)]

    days_off = int(input("number of days off(PTO):"))
    hours_for_ceremonies = int(input("Number of hours committed to Sprint ceremonies per day:"))

    min_hours_per_day = int(input("Minimum hours available for sprint per day:"))
    max_hours_per_day = int(input("Maximum hours available for sprint per day:"))
    hours_per_day_range = [min_hours_per_day, max_hours_per_day]