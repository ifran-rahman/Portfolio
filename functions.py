from ctypes import alignment
from tkinter import CENTER
from turtle import width
import streamlit as st


#####################
# Custom function for printing text
def homeview(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown('''
    <div>
        <br><br><br><br><br>
        <img src="https://github.com/ifran-rahman/Portfolio/blob/main/dp.png?raw=true" style="width:200px;"">
    </div>''',  unsafe_allow_html  = True)
  with col2:
    st.markdown(b, unsafe_allow_html=True)

def txt(a, b):
  col1, col2 = st.columns([3,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

def txt5(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.image(a)
  with col2:
    st.markdown(b, unsafe_allow_html=True)

def txt6(b):
  st.markdown(b, unsafe_allow_html=True)
#####################
