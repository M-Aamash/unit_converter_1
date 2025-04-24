
import streamlit as st

# Set page configuration
st.set_page_config(page_title="Unit Conversion", layout="wide")
st.title("Unit Conversion")
st.write("Select a category, enter a value, and get the converted result in real time.")

# Select category
category = st.selectbox("Choose a category", ["Length", "Time", "Weight"])

# Define unit conversion function
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Meters to Kilometers":
            return value / 1000
        elif unit == "Kilometers to Meters":
            return value * 1000

    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462

    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24

    return None  # Return None if no valid conversion is found

# Unit selection based on category
if category == "Length":
    unit = st.selectbox("Select conversion", ["Kilometers to Meters", "Meters to Kilometers"])
elif category == "Weight":
    unit = st.selectbox("Select conversion", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("Select conversion", ["Seconds to Minutes", "Minutes to Seconds",
                                              "Minutes to Hours", "Hours to Minutes",
                                              "Hours to Days", "Days to Hours"])

# Get input value
value = st.number_input("Enter the value to convert", min_value=0.0, format="%.2f")

# Perform conversion when button is clicked
if st.button("Convert"):
    result = convert_units(category, value, unit)
    if result is not None:
        st.success(f"The result is {result:.2f}")
    else:
        st.error("Invalid conversion. Please select a valid unit.")
