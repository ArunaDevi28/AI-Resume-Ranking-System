import pandas as pd

# Ranked candidate data
data = {
    "Rank": [1, 2, 3],
    "Candidate Name": ["John Doe", "Alice Smith", "Michael Lee"],
    "Match Score": [92, 87, 79],
    "ATS Score": [88, 82, 75],
    "Skills": [
        "Python, NLP, Machine Learning",
        "SQL, Deep Learning",
        "Java, Spring Boot"
    ],
    "Recommendation": [
        "Highly Recommended",
        "Recommended",
        "Moderately Recommended"
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Export to XLSX
df.to_excel("recommended_candidates.xlsx", index=False)

print("XLSX file created successfully!")
