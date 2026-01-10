import streamlit as st
import pandas as pd
import modulos.create_entry as create
import modulos.read_data as read
import modulos.update_entry as update
import modulos.delete_entry as delete
from modulos.users_list import usuarios, user_alexandro

st.title("Organizador Financeiro")