import pandas as pd

# Creating a dictionary
d = {
    "Week": [1, 2, 3, 4, 5, 6, 7],
    "Day": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ],
}

# Creating a DataFrame
df = pd.DataFrame(d)

# Display original DataFrame
print("Original DataFrame:\n", df, "\n")

# Adding new column
df.insert(0, "Day_No", range(1, 1 + len(df)))

# Display modified DataFrame
print("MOdified DataFrame:\n", df)
