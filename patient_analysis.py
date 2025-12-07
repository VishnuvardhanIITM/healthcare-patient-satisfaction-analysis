import matplotlib.pyplot as plt

# Quarterly performance data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
scores = [2.65, 0.24, 8.27, 7.15]
industry_target = 4.5

# Calculate average
average = sum(scores) / len(scores)
print("Average Satisfaction Score:", round(average, 2))

# Plot
plt.figure()
plt.plot(quarters, scores, marker='o', label='Patient Satisfaction Score')
plt.axhline(industry_target, linestyle='--', label='Industry Target (4.5)')
plt.xlabel('Quarters - 2024')
plt.ylabel('Satisfaction Score')
plt.title('Quarterly Patient Satisfaction Trend - 2024')
plt.legend()
plt.savefig('patient_satisfaction_trend.png')
plt.close()
