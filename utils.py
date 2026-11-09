import pandas as pd



#to match column names case insensitively and return the matched columns using keywords:
def find_columns(columns, keywords):
    
    for col in columns:
        col_lower = str(col).lower()

        for kw in keywords:
            if kw.lower() in col_lower:
                return col
    return None

def load_and_map_contacts(filename):
    """Loads the CSV file and automatically or manually maps Name and Number columns."""

    try:
        df = pd.read_csv(filename)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None, None, None

    print(f"\n[Success] Loaded file with {len(df)} rows.")
    print(f"Available columns found: {list(df.columns)}")

    # Keywords for auto-detection
    name_keywords = [
      "name",
      "full name",
      "customer",
      "first name",
      "client name",
      "client",
    ]
    number_keywords = [
      "number",
      "phone",
      "mobile",
      "whatsapp",
      "contact",
      "cell",
      "tel",
      "telephone",]

    name_col = find_columns(df.columns, name_keywords)
    number_col = find_columns(df.columns, number_keywords)



#if the script logic couldn't auto-detect the columns, prompt the user to select them manually:
    if not name_col:
        print("\nCould not auto-detect the 'Name' column.")
    name_col = input(
        f"Please select the correct Name column from {list(df.columns)}: "
    ).strip()

    if not number_col:
        print("\nCould not auto-detect the 'Number' column.")
        number_col = input(
            f"Please select the correct Number column from {list(df.columns)}: "
        ).strip()

    print(f"\n[Mapping Confirmed] -> Name Column: '{name_col}' | Number Column:"
      f" '{number_col}'")

    return df, name_col, number_col



# a function to check every number must have a default country code prefix, if not then add the default country code prefix to the number:

def format_phone_number(number, default_code):
  """Ensures phone number has a proper country code prefix."""
  cleaned_number = str(number).strip()
  if not cleaned_number.startswith("+"):
    cleaned_number = default_code + cleaned_number
  return cleaned_number