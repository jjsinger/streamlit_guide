#from typing import Any
#from vega_datasets import data
import streamlit as st
import altair as alt
import pandas as pd
from PIL import Image

def main():
    df = load_data()
    page = st.sidebar.selectbox("Choose a page", ["Homepage", "Exploration"])

    if page == "Homepage":
        st.header("This is your data explorer.")
        st.write("Ignore the dataset for now it is displayed for testing purposes. Please select the Exploration on the left.")
        st.write(df)
    elif page == "Exploration":
        st.title("Dell EMC Edge Infrastructure Solutions")
        #The options need to be a slider and a select box
        #Once the options for the # of cores and Compute Slide are selected

        compute = st.slider('Choose the amount of expected compute (must be greater than 20000, price will change based on compute):', min_value=20000, max_value=130000, value=20000, step=5000)
        #st.write(compute)
        cores = st.selectbox("Choose the number of cores (the image will only change when number of cores is changed)", df['Cores'].unique(), index=2)  # type: This is a CORES select box
        #st.write(cores)
        visualize_data(df, compute, cores) #Visualizes and Image and the corresponding price


@st.cache
def load_data():
    df = pd.read_excel("data\cores_compute.xlsx", index_col='ID')
    return df
#write function that gets the id where compute and core are located
def get_id(df_kw, compute_kw, cores_kw):
    num_id = df_kw[(df_kw['Compute'] == compute_kw) & (df_kw['Cores'] == cores_kw)].index[0] #index[0] is hard coded and needs to be dynamic
    #st.write("Dataframe being passed into get id:", df_kw[(df_kw['Compute'] == compute_kw) & (df_kw['Cores'] == cores_kw)])
    #st.write("NUM_ID: ", num_id)
    return num_id

#Write a function that gets the price based on the ID
def get_price(df_kw, id):
    #returns
    #st.write("ID that was passed to price function: ", id)
    #st.write(type(id))
    price = df_kw.at[id, 'Prices']
    return price

def visualize_data(df, compute_kw, cores_kw):
    # I need to visualize an image of a server here.
    # The inputs are: # of cores, Amount of Compute
    # Output: Image (.png file) and a Price
    #How will I visualize the Price? st.write(df['Prices'])
    #How will I visualize the Image? Use the following: st.image(image, caption='Sunrise by the mountains',
    #use_column_width=True)


    #Write out logic for pricing and images
    #Step 1: Get ID value
    st.write('Compute: ', compute_kw)
    st.write('Cores: ', cores_kw)
    id_f = get_id(df, compute_kw, cores_kw)

    #Step 2: Get price and image where ID is located
    price = get_price(df, id_f)

    #Step 3: Load all images
    image_server_rack = Image.open(r"images\dell_server_rack.png")
    image_server_rack2 = Image.open(r"images\dell_server_rack2.jpg")
    image_server_rack3 = Image.open(r"images\dell_server_rack3.png") #Change images 3, 4, and 5
    image_server_rack4 = Image.open(r"images\dell_server_rack4.jpg")
    image_server_rack5 = Image.open(r"images\dell_server_rack5.png")


    #Step 4: Visualize Price and Image using if logic
    if compute_kw > 20000:
        # this returns a df of ID and Prices: st.dataframe(df[(df['Compute (RAM)'] == compute_kw) & (df['Cores'] & cores_kw)][['ID', 'Prices']])
        if cores_kw == 1:
            # return the price if the compute is 20000 and the number of cores is 1
            st.subheader("PRICE (this is a dummy price for testing purposes): ")
            st.write(price)
            st.image(image_server_rack, caption='Test Title: Dell Server Rack')
            return
        elif cores_kw == 2:
            #return
            st.write("PRICE (this is a dummy price for testing purposes): ", price)
            st.image(image_server_rack2, caption='Test Title: Dell Server Rack 2')
            return
        elif cores_kw == 3:
            #return
            st.write("PRICE (this is a dummy price for testing purposes): ", price)
            st.image(image_server_rack3, caption='Test Title: Dell Server Rack 2')
            return
        elif cores_kw == 4:
            #return
            st.write("PRICE (this is a dummy price for testing purposes): ", price)
            st.image(image_server_rack4, caption='Test Title: Dell Server Rack 2')
            return
        elif cores_kw == 5:
            #return
            st.write("PRICE (this is a dummy price for testing purposes): ", price)
            st.image(image_server_rack5, caption='Test Title: Dell Server Rack 2')
            return
    elif compute_kw > 70000:
        # this returns a df of ID and Prices: st.dataframe(df[(df['Compute (RAM)'] == compute_kw) & (df['Cores'] & cores_kw)][['ID', 'Prices']])
        if cores_kw == 1:
            st.write("PRICE (this is a dummy price for testing purposes): ", price)
            st.image(image_server_rack, caption='Test Title: Dell Server Rack')
            return
            # return the price if the compute is 20000 and the number of cores is 1
        elif cores_kw == 2:
            # return
            st.write("PRICE (this is a dummy price for testing purposes): ", price)
            st.image(image_server_rack2, caption='Test Title: Dell Server Rack 2')
            return
        elif cores_kw == 3:
            #return
            st.write("PRICE (this is a dummy price for testing purposes): ", price)
            st.image(image_server_rack3, caption='Test Title: Dell Server Rack 2')
            return
        elif cores_kw == 4:
            #return
            st.write("PRICE (this is a dummy price for testing purposes): ", price)
            st.image(image_server_rack4, caption='Test Title: Dell Server Rack 2')
            return
        elif cores_kw == 5:
            #return
            st.write("PRICE (this is a dummy price for testing purposes): ", price)
            st.image(image_server_rack5, caption='Test Title: Dell Server Rack 2')
            return

    elif compute_kw > 100000:
        # this returns a df of ID and Prices: st.dataframe(df[(df['Compute (RAM)'] == compute_kw) & (df['Cores'] & cores_kw)][['ID', 'Prices']])
        if cores_kw == 1:
            st.write("PRICE (this is a dummy price for testing purposes): ", price)
            st.markdown("**PRICE** (this is a dummy price for testing purposes): ", price)
            st.image(image_server_rack, caption='Test Title: Dell Server Rack')
            return
            # return the price if the compute is 20000 and the number of cores is 1
        elif cores_kw == 2:
            # return
            st.write("PRICE (this is a dummy price for testing purposes): ", price)
            st.image(image_server_rack2, caption='Test Title: Dell Server Rack 2')
            return
        elif cores_kw == 3:
            # return
            st.write("PRICE (this is a dummy price for testing purposes): ", price)
            st.image(image_server_rack3, caption='Test Title: Dell Server Rack 2')
            return
        elif cores_kw == 4:
            # return
            st.write("PRICE (this is a dummy price for testing purposes): ", price)
            st.image(image_server_rack4, caption='Test Title: Dell Server Rack 2')
            return
        elif cores_kw == 5:
            # return
            st.write("PRICE (this is a dummy price for testing purposes): ", price)
            st.image(image_server_rack5, caption='Test Title: Dell Server Rack 2')
            return

            #remember to change the Compute (RAM) column to just Compute
            #st.dataframe(df[(df['Compute (RAM)'] == compute_kw) & (df['Cores'] & cores_kw)][['ID', 'Prices']])
            #st.image(image_server_rack, caption='Title of Server Rack1', use_column_width=True) #I will need to add a column for this
    #elif compute_kw >= 50000:
    #    st.image(image_full_rack, caption='Title of Server Rack2', use_column_width=True)  # I will need to add a column for this
    #If image = A then show image A and corresponding price


if __name__ == "__main__":
    main()

