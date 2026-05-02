import pandas as pd
import streamlit as st
import plotly.express as px


book_df = pd.read_csv('bestsellers_with_categories_2022_03_27.csv')

st.title("Bestselling Book Analysis")
st.write("This app analyzes the Amazon Top Selling books from 2009 to 2022")

st.header("Add New Book Data")

with st.sidebar.form('book_form'):
    new_name = st.text_input('Book Name')
    new_author = st.text_input('Author Name')
    new_user_rating = st.slider("User rating",0.0,5.0,0.0,0.1)
    new_reviews = st.number_input("Reviews", min_value=0,step=1)
    new_price = st.number_input("Price", min_value=0, step=1)
    new_year = st.number_input("Year", min_value=2009,max_value=2022, step=1)
    new_genre = st.selectbox('Genre',book_df['Genre'].unique())
    submit_button = st.form_submit_button(label="Add Book")

if submit_button:
    new_data = {
        'Name': new_name,
        'Author': new_author,
        'User Rating': new_user_rating,
        'Reviews': new_reviews,
        'Price': new_year,
        'Genre': new_genre
    }


    book_df = pd.concat([pd.DataFrame(new_data,index=[0]), book_df], ignore_index=True)
    book_df.to_csv('bestsellers_with_categories_2022_03_27.csv', index= False)
    st.sidebar.success('New book added successfully!')

#Sidebar filters

st.sidebar.header("Filter Options")
selected_author =st.sidebar.selectbox("Select Author", ["All"] + list(book_df['Author'].unique()))
selected_year =st.sidebar.selectbox("Select Year", ["All"] + list(book_df['Year'].unique()))
selected_genre =st.sidebar.selectbox("Select Genre", ["All"] + list(book_df['Genre'].unique()))

min_rating = st.sidebar.slider("Minimum User Rating",0.0,5.0,0.0,0.1)
max_price = st.sidebar.slider("Maximum price",0,book_df['Price'].max(),book_df['Price'].max())

filtered_books_df = book_df.copy()

if selected_author != "All":
    filtered_books_df = filtered_books_df[filtered_books_df["Author"] == selected_author]
if selected_year != "All":
    filtered_books_df = filtered_books_df[filtered_books_df["Year"] == selected_year]
if selected_genre != "All":
    filtered_books_df = filtered_books_df[filtered_books_df["Genre"] == selected_genre]


filtered_books_df = filtered_books_df[
    (filtered_books_df['User Rating'] >=min_rating) & (filtered_books_df['Price'] <= max_price)
]

st.subheader("Summary Statistics")

total_books = book_df.shape[0]
unique_titles = book_df['Name'].nunique()
average_rating = book_df['User Rating'].mean()
average_price = book_df['Price'].mean()

col1,col2,col3,col4 = st.columns(4)
col1.metric("Total Books",total_books)
col2.metric("Unique Titles",unique_titles)
col3.metric("Average Rating",average_rating)
col4.metric("Average Price",average_price)

st.subheader("Dataset Preview")
st.write(book_df.head())

col1, col2 = st.columns(2)

with col1:
    st.subheader("Top 10 Book Titles")
    top_titles = book_df['Name'].value_counts().head(10)
    st.bar_chart(top_titles)

with col2:
    st.subheader("Top 10 Authors")
    top_authors = book_df['Author'].value_counts().head(10)
    st.bar_chart(top_authors)

st.subheader("Genre Distribution")
fig = px.pie(filtered_books_df,names='Genre',title = 'Most Liked Genre (2009-2022)',color='Genre',
             color_discrete_sequence = px.colors.sequential.Plasma)

st.plotly_chart(fig)

#Number of Fiction and Non-fiction books over the year

st.header("Number of Fiction and Non-fiction books over the year")
size = filtered_books_df.groupby(['Year','Genre']).size().reset_index(name='Counts')
fig = px.bar(size, x='Year',y ='Counts',color='Genre',title='Number of Fiction and Non-fiction books over the year from 2009-2022',
             color_discrete_sequence= px.colors.sequential.Plasma,barmode='group')
st.plotly_chart(fig)