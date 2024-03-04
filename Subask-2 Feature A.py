def calculate_velocity(previous_sprint_points):
    total_points = sum(previous_sprint_points)
    average_velocity = total_points / len(previous_sprint_points)
    return average_velocity

average_velocity = calculate_velocity(previous_sprint_points)
print(f"Output: Average Velocity: {average_velocity:.2f} points per sprint")