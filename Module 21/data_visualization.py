import streamlit as st
import pandas as pd
import plotly.express as px

books_df=pd.read_csv('bestsellers with categories.csv')

st.title ("Bestselling Books Analysis")
st.write("This app analyzes the Amazon Top Selling Books.")

st.subheader("Summar Statistics")

total_books=books_df.shape[0]
unique_titles=books_df['Name'].nunique()
average_rating=books_df['User MRating'].mean()
average_price=books_df['Price'].mean()

col1,col2,col3,col4= st.columns(4)
col1.metric("Total Books",total_books)
col2.metric('Unique Titles',unique_titles)
col3.metric('Average Rating of Books',f"{average_rating:,2f}")
col4.metric('Average Price of Books',f"{average_price:,2f}")


st.subheader("Dataset Preview")
st.write(books_df.head(10))

col1, col2 =st.columns(2)

with col1:
    st.subheader("Top 10 book Titles")
    top_titles=books_df['Name'].value_counts().head(10)
    st.bar_chart(top_titles)

with col2:
    st.subheader("Top 10 Authors")
    top_authors=books_df['Author'].value_counts().head(10)
    st.bar_chart(top_authors)

st.subheader("Genre Distribution")
fig=px.pie(books_df,names='Genre',title='Most liked genre',color='Genre',
           color_discrete_sequence=px.colors.sequential.Plasma)
st.plotly_chart(fig)

st.subheader("Number of Fiction vs Non-fiction Books over the Year")
size=books_df.groupby(['Year','Genre']).size().reset_index('Counts')
fig=px.bar(size,x='Year',y='Counts',color='Genre',title='Number of Books over the Years',
           color_discrete_sequence=px.colors.sequential.Plasma,barmode='group')
st.plotly_chart(fig1)


st.subheader("Top 15 Authors by Counts of Books Published")
top_authors=books_df['Author'].value_counts().head(15).reset_index("Count")
fig=px.bar(top_authors,x='Author',y='Count',orientation='h',
           title='Top 15 Authors by Counts of Books Published',
           labels={"Author":"Name of Author","Count":"Number of Books Published"},
           color='Count',color_discrete_sequence=px.colors.sequential.Plasma)
st.plotly_chart(fig2)


st.subheader("Filter Data by Genre")
genre_filter=st.selectbox("Select Genre",books_df['Genre'].umique())
filtered_data=books_df[books_df['Genre']==genre_filter]
st.write(filtered_data)



