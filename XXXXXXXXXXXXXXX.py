import pandas as pd

# Example dataset with symptoms and diseases
data = {
    'anxiety': [1, 0, 1, 0, 1],
    'mood_swings': [1, 0, 1, 1, 0],
    'insomnia': [1, 1, 1, 0, 0],
    'hallucinations': [0, 0, 1, 1, 0],
    'social_withdrawal': [1, 0, 1, 1, 0],
    'panic_attacks': [1, 0, 1, 1, 0],
    'fatigue': [1, 0, 1, 0, 0],
    'memory_loss': [0, 0, 1, 0, 0],
    'confusion': [0, 0, 1, 1, 0],
    'diagnosis': ['bipolar_disorder', 'healthy', 'bipolar_disorder', 'depression', 'anxiety_disorder']
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Saving the dataset
df.to_csv('improved_dataset.csv', index=False)
print("Improved dataset saved successfully.")
