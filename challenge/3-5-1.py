import pandas as pd
import streamlit as st
exams = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv')


st.title("exam score")

st.write("raw exam scores data")
st.dataframe(exams)
st.write(exams.columns)


options = ['Made_Own_Study_Guide','Did_Exam_Prep Assignment','Studied_In_Groups']
selection = st.selectbox("select a study approach",options)


summary = exams.groupby(selection).agg({'Class_Section':'count','Student_Score':'mean'})
summary = summary.reset_index()
summary = summary.rename(columns={'Class_Section': 'Stident_count','Student_Score':'Average'})

st.write(f"summary of {selection}")
st.dataframe(summary)