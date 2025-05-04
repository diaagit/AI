def evaluate_performance(punctuality, task_completion, teamwork, innovation):
    score = 0
    details = {}

    # Rule-based scoring
    if punctuality >= 90:
        score += 25
        details['Punctuality'] = 25
    elif punctuality >= 75:
        score += 15
        details['Punctuality'] = 15
    else:
        score += 5
        details['Punctuality'] = 5

    if task_completion >= 90:
        score += 30
        details['Task Completion'] = 30
    elif task_completion >= 75:
        score += 20
        details['Task Completion'] = 20
    else:
        score += 10
        details['Task Completion'] = 10

    if teamwork == 'excellent':
        score += 20
        details['Teamwork'] = 20
    elif teamwork == 'average':
        score += 10
        details['Teamwork'] = 10
    else:
        score += 5
        details['Teamwork'] = 5

    if innovation == 'high':
        score += 25
        details['Innovation'] = 25
    elif innovation == 'medium':
        score += 15
        details['Innovation'] = 15
    else:
        score += 5
        details['Innovation'] = 5

    # Final Evaluation
    if score >= 80:
        evaluation = "Outstanding Performance"
    elif score >= 60:
        evaluation = "Good Performance"
    elif score >= 40:
        evaluation = "Needs Improvement"
    else:
        evaluation = "Poor Performance"

    return score, details, evaluation

# Example usage
punctuality = int(input("Enter punctuality percentage: "))
task_completion = int(input("Enter task completion rate: "))
teamwork = input("Enter teamwork (excellent/average/poor): ").lower()
innovation = input("Enter innovation level (high/medium/low): ").lower()

score, details, result = evaluate_performance(punctuality, task_completion, teamwork, innovation)

print("\n--- Score Breakdown ---")
for category, points in details.items():
    print(f"{category}: {points} points")

print(f"\nTotal Score: {score}")
print(f"Performance Evaluation: {result}")
