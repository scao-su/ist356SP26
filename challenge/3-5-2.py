import pandas as pd
import streamlit as st
exams = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv')


st.title("exam score")

st.write("raw exam scores data")
st.dataframe(exams)





cols = ['Class_Section', 'Exam_Version', 'Made_Own_Study_Guide', 'Did_Exam_Prep Assignment', 'Studied_In_Groups','Letter_Grade']

measures = ['Completion_Time','Student_Score']

row = st.selectbox('selcct row',cols)
col = st.selectbox('select col',cols)
measure = st.selectbox('select measure',measures)


table = exams.pivot_table(index=row, columns=col, values= measure, aggfunc='mean')
st.write(table)