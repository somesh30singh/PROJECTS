import streamlit as st
import mysql.connector
import pandas as pd

def connect_db():                       # MYSQL USER DETAILS AND DATABASE -------------#
    return mysql.connector.connect(            
        host="localhost",
        user="root",
        password="Somesh@30si@", 
        database="EMPLOYEE_JOINING_FORM"

    )

def Add_Employee(FIRST_NAME,LAST_NAME,PHONE,AGE,EMAIL,ADDRESS,NATIONLITY):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO EMPLOYEE_DETAILS(FIRST_NAME,LAST_NAME,PHONE,AGE,EMAIL,ADDRESS,NATIONALITY) VALUES (%s,%s,%s,%s,%s,%s,%s)",
        (FIRST_NAME,LAST_NAME,PHONE,AGE,EMAIL,ADDRESS,NATIONLITY)
    )
    conn.commit()
    conn.close()

def Update_details(emp_id,first_name,last_name,phone,age,email,address):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """ UPDATE EMPLOYEE_DETAILS SET first_name = %s ,last_name = %s ,phone = %s, age = %s, email = %s, address = %s
        WHERE EMP_id = %s""",
        (emp_id,first_name,last_name,phone,age,email,address)
    )
    conn.commit()
    conn.close()

def View_details():
     conn = connect_db()
     cursor = conn.cursor()

     cursor.execute("SELECT * from EMPLOYEE_DETAILS")
     data = cursor.fetchall()

     conn.close()
     return data

def Delete_details(Emp_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("delete from EMPLOYEE_DETAILS where Emp_id = %s",(Emp_id,))

    conn.commit()
    conn.close()

# MAIN EXECUTION FOR FRONT OF THE WEBSITE ------------------------#
st.title("PYTHON ARILINES INDIA PVT LTD")
st.header("Welcome to Python Airlines")
st.subheader("Employee Joining Form")

MENU = st.sidebar.selectbox("SELECT",["Select","Create","Update","View","Delete"])
if MENU == "Create":
    st.subheader("Add Details")

    First_name = st.text_input("First name")
    Last_name = st.text_input("Last name")
    Phone = st.text_input("Phone")
    Age = st.number_input("age",0,100)
    Email = st.text_input("Email")
    Address = st.text_input("Address")
    Nationality = st.text_input("Nationality")


if st.button("ADD"):
    if len(Phone) != 10:
            st.error("Error: Only 10 digit number should be allowed!")
    else:
        Add_Employee(First_name, Last_name, Phone, Age, Email, Address, Nationality)
        st.success("Details Submitted")
    

# --------------------------------------------------------------#
elif MENU == "Update":
    st.subheader("UPDATE EMPLOYEE DETAILS")

    
    first_name = st.text_input("NAME")
    last_name = st.text_input("LASTNAME")
    phone = st.text_input("ENTER 10 DIGIT MOBILE NUMBER",10)
    age = st.number_input(" AGE")
    email = st. text_input(" EMAIL")
    address = st.text_input("ADDRESS")
    emp_id = st.number_input("Emp_id",1)
    

    if st.button("UPDATE"):
        if len(phone) != 10:
                st.error("Error: Only 10 digit number should be allowed!")
        else:
             Update_details(first_name,last_name,phone,age,email,address,emp_id)
             st.success("Updated Successfully")

elif MENU == "View":
     st.subheader("VIEW DETAILS")
     data = View_details()
     df = pd.DataFrame(data, columns =["EMP_ID","FIRST_NAME","LAST_NAME","PHONE","AGE","EMAIL","ADDRESS","NATIONLITY"])
     st.dataframe(df)

# --------------------------------------------------------------#
if MENU == "Delete":
    st.subheader("DELETE EMPLOYEE DEATILS")
    
    Emp_id = st.number_input("ENTER Emp_id",1)

    if st.button("DELETE"):
        Delete_details(Emp_id)
        st.success("Deleted Successfully")
    




