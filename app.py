import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("🎓 Student Performance Analyzer")

# Upload Excel File
uploaded_file = st.file_uploader(
    "Upload Excel File",
    type=["xlsx"]
)

if uploaded_file is not None:
    # Read Excel File
    df = pd.read_excel(uploaded_file)

    # Total Marks
    df["Total"] = df["T1"] + df["MidSem"] + df["T2"]

    # Percentage Calculation
    df["Percentage"] = (
    (df["Total"] / 55) * 100
).round(2)

    df["Current_CGPA"] = (
    df["Percentage"] / 9.5
).round(2)

    def cgpa_status(cgpa):
        if cgpa >= 8.5:
            return "Bright Learner"
        elif cgpa < 6.5:
            return "Slow Learner"
        else:
            return "Average Learner"

    df["CGPA_Status"] = df["Current_CGPA"].apply(cgpa_status)

    st.subheader("📄 Uploaded Data")
    st.dataframe(df)

    # Bright learner dataframe
    bright_students = df[df["CGPA_Status"] == "Bright Learner"]

    # Slow learner dataframe
    slow_students = df[df["CGPA_Status"] == "Slow Learner"]

    # Counts
    st.write("Total Bright Learners:", len(bright_students))
    st.write("Total Slow Learners:", len(slow_students))

    # Bright report
    st.subheader("🌟 Bright Learner Report")
    st.dataframe(bright_students)

    # Slow report
    st.subheader("📉 Slow Learner Report")
    st.dataframe(slow_students)

    

    # -----------------------------
    # GRAPHS SECTION
    # -----------------------------

    st.header("📊 Analytics Dashboard")

    # Learner Distribution Chart
    status_count = df["CGPA_Status"].value_counts()

    fig, ax = plt.subplots()

    ax.bar(
        status_count.index,
        status_count.values
    )

    ax.set_title(
        "Learner Distribution"
    )

    st.pyplot(fig)

    # Percentage Histogram
    fig, ax = plt.subplots()

    ax.hist(
        df["Percentage"],
        bins=5
    )

    ax.set_title(
        "Percentage Distribution"
    )

    st.pyplot(fig)

    # CGPA Comparison Graph
    fig, ax = plt.subplots()

    ax.plot(
        df["Name"],
        df["Previous_CGPA"],
        marker='o',
        label='Previous'
    )

    ax.plot(
        df["Name"],
        df["Current_CGPA"],
        marker='o',
        label='Current'
    )

    ax.legend()

    ax.set_title(
        "Previous vs Current CGPA"
    )

    st.pyplot(fig)

    def compare_cgpa(row):
        previous = row["Previous_CGPA"]
        current = row["Current_CGPA"]
        if current > previous:
            return "Improved Performance"
        elif current < previous:
            return "Performance Declined"
        else:
            return "Consistent Performance"

    df["CGPA_Report"] = df.apply(compare_cgpa, axis=1)

    def remarks(row):
        if row["CGPA_Report"] == "Improved Performance":
            return "Excellent Improvement"
        elif row["CGPA_Report"] == "Performance Declined":
            return "Needs Academic Support"
        else:
            return "Maintaining Consistency"

    df["Remarks"] = df.apply(remarks, axis=1)

    st.subheader("📊 Student Progress Report")
    st.dataframe(df)

    def t1_status(mark):
        if mark >= 15:
            return "Bright"
        elif mark < 10:
            return "Slow"
        else:
            return "Average"


    df["T1_Status"] = df["T1"].apply(t1_status)


    def midsem_status(mark):
        if mark >= 11:
            return "Bright"
        elif mark < 7:
            return "Slow"
        else:
            return "Average"


    df["MidSem_Status"] = df["MidSem"].apply(midsem_status)


    def t2_status(mark):
        if mark >= 15:
            return "Bright"
        elif mark < 10:
            return "Slow"
        else:
            return "Average"


    df["T2_Status"] = df["T2"].apply(t2_status)


    def final_status(percentage):
        if percentage >= 75:
            return "Bright Learner"
        elif percentage < 50:
            return "Slow Learner"
        else:
            return "Average Learner"


    df["Final_Status"] = df["Percentage"].apply(final_status)


    st.subheader("📊 Complete Student Report")
    st.dataframe(df)


    def classify_student(percentage):
        if percentage >= 75:
            return "Bright Learner"
        elif percentage < 50:
            return "Slow Learner"
        else:
            return "Average Learner"


    df["Category"] = df["Percentage"].apply(classify_student)


    st.subheader("📊 Processed Data")
    st.dataframe(df)

    # Category Count
    category_count = df["Category"].value_counts()

    st.subheader("📈 Student Categories")
    fig, ax = plt.subplots()
    ax.bar(category_count.index, category_count.values)
    ax.set_xlabel("Category")
    ax.set_ylabel("Number of Students")
    st.pyplot(fig)

else:
    st.write("Please upload an Excel file")

