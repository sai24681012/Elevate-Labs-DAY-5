import pandas as pd
import os

# Load dataset
df = pd.read_csv(r"C:\Users\PARAPATLA SAI KUMAR\OneDrive\Desktop\Elevate labs internship\DAY-5\titanic.csv")

# Replace 0 -> Died, 1 -> Alive
df['Survived'] = df['Survived'].replace({0: 'Died', 1: 'Alive'})

# Detect Desktop path automatically
desktop_path = os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop")
save_path = os.path.join(desktop_path, "titanic_cleaned.csv")

# Save file
df.to_csv(save_path, index=False)
print(f"✅ File saved at: {save_path}")
