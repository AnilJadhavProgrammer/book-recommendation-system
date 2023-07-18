import pickle
import numpy as np
import pandas as pd 
import streamlit as st

st.header(" Book Recommendation System !!")
with open('C:/Users/DELL/OneDrive/Desktop/python project/Book_Recommendation_System/artifacts/model.pkl', 'rb') as file:
    model = pickle.load(file)
with open('C:/Users/DELL/OneDrive/Desktop/python project/Book_Recommendation_System/artifacts/book_name.pkl', 'rb') as file:
    book_name = pickle.load(file)
final_rating = pd.read_pickle('artifacts/final_rating.pkl')
book_pivot = pd.read_pickle('artifacts/book_pivot.pkl')

def fecth_poster(suggestion):
    book_name=[]
    index_id=[]
    poster_url=[]

    for book_id in suggestion:
        book_name.append(book_pivot.index[book_id])

    for name in book_name[0]:
        ids= np.where(final_rating['Title']== name)[0][0]
        index_id.append(ids)

    for idx in index_id:
        url=final_rating.iloc[idx]['Image-URL']
        poster_url.append(url)

    return poster_url

def fetch_details(suggestion):
    book_details = []

    for book_id in suggestion:
        book_name = book_pivot.index[book_id]
        #ids = np.where(final_rating['Title'].values == book_name)[0][0]
        details = final_rating[final_rating['Title'].isin([book_name])].iloc[0]
        book_details.append({
            'Title': book_name,
            'Author': details['Author'],
            'Publisher': details['Publisher'],
            'Publication Date': details['Publication'],
            'Rating': details['num_of_rating'],
            'Image-URL': details['Image-URL']
        })

    return book_details

def recommend_book(book_name):
    book_list=[]
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance , suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1),n_neighbors=7)


    poster_url = fecth_poster(suggestion)
    book_details = fetch_details(suggestion.flatten())

    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]]
        for j in books:
            book_list.append(j)
    for details in book_details:
        book_list.append(details['Title'])

    return book_list, poster_url, book_details



select_book= st.selectbox(
    "Type or Select your book",
    book_name)

if st.button('Show Recommendation'):
    recommendation_books, poster_url ,book_details= recommend_book(select_book)
    col1,col2,col3,col4,col5,col6 = st.columns(6)

    
    with col1:
        st.text(recommendation_books[1])
        st.image(poster_url[1])
        expander = st.expander(recommendation_books[1])
        expander.image(book_details[1]['Image-URL'])
        expander.write(f"Author: {book_details[1]['Author']}")
        expander.write(f"Publisher: {book_details[1]['Publisher']}")
        expander.write(f"Publication Date: {book_details[1]['Publication Date']}")
        expander.write(f"Rating: {book_details[1]['Rating']}")


    with col2:
        st.text(recommendation_books[2])
        st.image(poster_url[2])
        expander = st.expander(recommendation_books[2])
        expander.image(book_details[2]['Image-URL'])
        expander.write(f"Author: {book_details[2]['Author']}")
        expander.write(f"Publisher: {book_details[2]['Publisher']}")
        expander.write(f"Publication Date: {book_details[2]['Publication Date']}")
        expander.write(f"Rating: {book_details[2]['Rating']}")


    with col3:
        st.text(recommendation_books[3])
        st.image(poster_url[3])
        expander = st.expander(recommendation_books[3])
        expander.image(book_details[3]['Image-URL'])
        expander.write(f"Author: {book_details[3]['Author']}")
        expander.write(f"Publisher: {book_details[3]['Publisher']}")
        expander.write(f"Publication Date: {book_details[3]['Publication Date']}")
        expander.write(f"Rating: {book_details[4]['Rating']}")


    with col4:
        st.text(recommendation_books[4])
        st.image(poster_url[4])
        expander = st.expander(recommendation_books[4])
        expander.image(book_details[4]['Image-URL'])
        expander.write(f"Author: {book_details[4]['Author']}")
        expander.write(f"Publisher: {book_details[4]['Publisher']}")
        expander.write(f"Publication Date: {book_details[4]['Publication Date']}")
        expander.write(f"Rating: {book_details[4]['Rating']}")


    with col4:
        st.text(recommendation_books[5])
        st.image(poster_url[5])
        expander = st.expander(recommendation_books[5])
        expander.image(book_details[5]['Image-URL'])
        expander.write(f"Author: {book_details[5]['Author']}")
        expander.write(f"Publisher: {book_details[5]['Publisher']}")
        expander.write(f"Publication Date: {book_details[5]['Publication Date']}")
        expander.write(f"Rating: {book_details[5]['Rating']}")


    with col6:
        st.text(recommendation_books[6])
        st.image(poster_url[6])
        expander = st.expander(recommendation_books[6])
        expander.image(book_details[6]['Image-URL'])
        expander.write(f"Author: {book_details[6]['Author']}")
        expander.write(f"Publisher: {book_details[6]['Publisher']}")
        expander.write(f"Publication Date: {book_details[6]['Publication Date']}")
        expander.write(f"Rating: {book_details[6]['Rating']}")




