
import pandas as pd
pd.set_option("display.max_columns",None)

# Read the CSV file
data_df = pd.read_csv("PD 2024 Wk 1 Input.csv")

# Extracting all information from "Flight Details" feature
data_df[["Date","Flight Number","From To","Class","Price"]] = data_df["Flight Details"].str.split("//",expand = True)
data_df[["From","To"]] = data_df["From To"].str.split("-",expand = True)

data_df.drop(columns = ["Flight Details","From To"],axis = 1, inplace = True)

# Show the first few rows for validation
print(data_df.head())

# Show the data types to check them
print(data_df.info())

# converting Date from Object data type to datetime format
data_df["Date"] = pd.to_datetime(data_df["Date"])

# Convert "Price" to a float type
data_df["Price"] = data_df["Price"].astype("float")

# Show the first few rows after the conversion
print(data_df.head())

# Recode "Flow Card?" from 1/0 to "Yes"/"No"
data_df.loc[data_df["Flow Card?"] == 1, "Flow Card?"] = "Yes"
data_df.loc[data_df["Flow Card?"] == 0, "Flow Card?"] = "No"

data_df.head()

# Split DataFrames based on "Flow Card?" values (Yes/No)
flow_card_holder = data_df.loc[data_df["Flow Card?"]=="Yes"][["Date","Flight Number", "From", "To","Class", "Price","Flow Card?","Bags Checked", "Meal Type"]]
flow_card_not_holder = data_df.loc[data_df["Flow Card?"]=="No"][["Date","Flight Number", "From", "To","Class", "Price","Flow Card?","Bags Checked", "Meal Type"]]

print(flow_card_holder.head())
print(flow_card_not_holder.head())



