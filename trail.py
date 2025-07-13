import pandas as pd

# Simulated main dataframe (starts empty)
main_df = pd.DataFrame()

# Simulated batch data
batch_1_data = [
    ["TATA Motors", 1000, 10.5, 250],
    ["IRFC", 800, 12.0, 180]
]
batch_1_params = ["Sales", "OPM", "Profit after tax"]

batch_2_data = [
    ["TATA Motors", 15.2, 30],
    ["IRFC", 14.0, 10],
    ["RELIANCE", 18.0, 40]  # New company
]
batch_2_params = ["Return on capital employed", "EPS"]

# Convert each batch to DataFrame
df1 = pd.DataFrame(batch_1_data, columns=["Company"] + batch_1_params)
df2 = pd.DataFrame(batch_2_data, columns=["Company"] + batch_2_params)

# Set 'Company' as index for easier alignment and merging
df1.set_index("Company", inplace=True)
df2.set_index("Company", inplace=True)

# Merge into main_df incrementally
main_df = main_df.combine_first(df1)
main_df = main_df.combine_first(df2)

main_df.reset_index(inplace=True)
print(main_df.head())
