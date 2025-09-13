import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import operator as op

ops = {
        '==': op.eq,
        '!=': op.ne,
        '>': op.gt,
        '<': op.lt,
        '>=': op.ge,
        '<=': op.le
    }


st.title("CSV ANALYZER")
st.write("")
uploads = st.file_uploader("Upload your CSV file")
if uploads is not None:
    df = pd.read_csv(uploads)
    st.subheader("Data Preview")
    st.dataframe(df.head(5))


    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter DataFrame")

    column_options=df.columns
    selected_column=st.selectbox("Select Column",column_options)

    column_datatype=df[selected_column].dtype
    if column_datatype == 'int64':
        input = st.number_input("Enter Number", 0)
    elif column_datatype == 'float64':
        input = st.number_input("Enter Number", 0.0)
    elif column_datatype == 'bool':
        boolean = [True, False]
        input = st.selectbox("Enter Boolean", boolean)
    elif column_datatype == 'object':
        input = st.text_input("Enter Text")

    if column_datatype == 'object':
        operations_options = ['==', 'contains']
        selected_operation = st.selectbox("Select Operation", operations_options)
    else:
        operations_options=['==','>','<','>=','<=','contains']
        selected_operation = st.selectbox("Select Operation", operations_options)
    if selected_operation == 'contains':
        filter=df[selected_column].str.contains(input, case=False, na=False)
    else:
        filter = ops[selected_operation](df[selected_column], input)
    if st.button("Filter"):
        filtered_data=df[filter]
        st.write(filtered_data)

    st.subheader("Data Visualization")
    x_label=st.selectbox("Select X- Label ",df.select_dtypes(include=['float64','int64','int32','float32']).columns)
    y_label=st.selectbox("Select Y- Label ",df.select_dtypes(include=['float64','int64','int32','float32']).columns)
    vis_option=['Line Plot','Scatter Plot','Bar Graph','Histogram']
    selected_vis_option=st.selectbox("Select Visualization Type", vis_option)

    if st.button("Visualize"):
        if(selected_vis_option == 'Line Plot'):
            plt.plot(df[x_label],df[y_label])
            plt.xlabel(df[x_label])
            plt.ylabel(df[y_label])

        elif selected_vis_option == 'Scatter Plot':
            plt.scatter(df[x_label], df[y_label])
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.title(f"{y_label} vs {x_label}")

        elif selected_vis_option == 'Bar Graph':
            plt.bar(df[x_label], df[y_label])
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.title(f"{y_label} by {x_label}")

        elif selected_vis_option == 'Histogram':
            plt.hist(df[x_label], bins=20, color='skyblue', edgecolor='black')
            plt.xlabel(x_label)
            plt.title(f"Histogram of {x_label}")
        st.pyplot(plt)









