import streamlit as st
import pandas as pd
import plotly.express as px
from numerize.numerize import numerize
import query  
from streamlit_option_menu import option_menu
import plotly.graph_objs as go



import time 

st.set_page_config(page_title="Dashboard", page_icon="🌍", layout="wide")
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)


st.subheader("🔔 Insurance Descriptive Analysis")
st.markdown("##")

# Get data from the database
result = query.view_all_data()

if result:
    # Convert result to a pandas DataFrame
    df = pd.DataFrame(result, columns=["Policy", "Expiry", "Location", "State", "Region", "Investment", "Construction", "BusinessType", "Earthquake", "Flood", "Rating", "id"])
else:
    st.error("Nessun dato trovato.")

# Sidebar filter options
#st.sidebar.image("data/logo.png", caption="Online Analytics")
st.sidebar.header("Please filter")

# Filters for Region, Location, and Construction
region = st.sidebar.multiselect("Select Region", options=df["Region"].unique(), default=df["Region"].unique(), key="region_filter")
location = st.sidebar.multiselect("Select Location", options=df["Location"].unique(), default=df["Location"].unique(), key="location_filter")
construction = st.sidebar.multiselect("Select Construction", options=df["Construction"].unique(), default=df["Construction"].unique(), key="construction_filter")

# Filter the dataframe based on selected values
df_selection = df.query(
    "Region in @region and Location in @location and Construction in @construction"
)

# Tabular Data Display
def Home():
    with st.expander("Tabular"):
        # Show only selected columns
        showData = st.multiselect('Filter columns to display:', df_selection.columns.tolist(), default=df_selection.columns.tolist(), key="show_data_columns")
        if showData:
            st.write(df_selection[showData])
        else:
            st.write(df_selection)



# Calculations for metrics
total_investment = df_selection["Investment"].sum()
investment_mode_series = df_selection["Investment"].mode()
investment_mode = investment_mode_series[0] if not investment_mode_series.empty else "No Mode"
investment_mean = df_selection["Investment"].mean()
investment_median = df_selection["Investment"].median()
rating = df_selection["Rating"].sum()

# Display metrics in columns
total1, total2, total3, total4, total5 = st.columns(5, gap='large')

with total1:
    st.info('Total Investment', icon="📌")
    st.metric(label="sum TZS", value=f"{total_investment:,.0f}")

with total2:
    st.info('Most Frequent', icon="📌")
    st.metric(label="mode TZS", value=f"{investment_mode if isinstance(investment_mode, str) else f'{investment_mode:,.0f}'}")

with total3:
    st.info('Average', icon="📌")
    st.metric(label="Average TZS", value=f"{investment_mean:,.0f}")

with total4:
    st.info('Central Earning', icon="📌")
    st.metric(label="median TZS", value=f"{investment_median:,.0f}")

with total5:
    st.info('Rating', icon="📌")
    st.metric(label="Rating", value=numerize(rating), help=f""" Total Rating: {rating} """)

st.markdown(""" ___ """)



# Graphs Function
def graphs():
    investment_by_business_type = df_selection.groupby(by=["BusinessType"]).count()[["Investment"]].sort_values(by="Investment")
    fig_investment = px.bar(
        investment_by_business_type,
        x="Investment",
        y=investment_by_business_type.index,
        orientation="h",
        title="<b> Investment by Business Type </b>",
        color_discrete_sequence=["#ea662e"] * len(investment_by_business_type),
        template="plotly_white",
    )
    fig_investment.update_layout(
        plot_bgcolor="white",
        xaxis=dict(showgrid=False)
    )

    investment_state = df_selection.groupby(by=["State"]).count()[["Investment"]]
    fig_state = px.line(
        investment_state,
        x=investment_state.index,
        y="Investment",
        orientation="h",
        title="<b> Investment by State </b>",
        color_discrete_sequence=["#ea662e"] * len(investment_state),
        template="plotly_white",
    )
    fig_state.update_layout(
        xaxis=dict(tickmode="linear"),
        plot_bgcolor="white",
        yaxis=dict(showgrid=False)
    )

    left, right = st.columns(2)
    left.plotly_chart(fig_state, use_container_width=True)
    right.plotly_chart(fig_investment, use_container_width=True)


def Progressbar():
    st.markdown("""<style>.stProgress > div > div > div > div { background-image: linear-gradient(to right, #99ff99 , #FFFF00)}</style>""",unsafe_allow_html=True,)
    target=3000000000
    current=df_selection["Investment"].sum()
    percent=round((current/target*100))
    mybar=st.progress(0)

    if percent>100:
        st.subheader("Target done !")
    else:
     st.write("you have ",percent, "% " ,"of ", (format(target, 'd')), "TZS")
     for percent_complete in range(percent):
        time.sleep(0.1)
        mybar.progress(percent_complete+1,text=" Target Percentage")


def sideBar():
 with st.sidebar:
    selected=option_menu(
        menu_title="Main Menu",
        options=["Home","Progress"],
        icons=["house","eye"],
        menu_icon="cast",
        default_index=0,
        orientation="h"
    )
 if selected=="Home":
    st.subheader(f"Page: {selected}")
    Home()
    graphs()
 if selected=="Progress":
    st.subheader(f"Page: {selected}")
    Progressbar()
    graphs()

sideBar()

st.subheader('PICK FEATURES TO EXPLORE DISTRIBUTIONS TRENDS BY QUARTILES',)
#feature_x = st.selectbox('Select feature for x Qualitative data', df_selection.select_dtypes("object").columns)
feature_y = st.selectbox('Select feature for y Quantitative Data', df_selection.select_dtypes("number").columns)
fig2 = go.Figure(
    data=[go.Box(x=df['BusinessType'], y=df[feature_y])],
    layout=go.Layout(
        title=go.layout.Title(text="BUSINESS TYPE BY QUARTILES OF INVESTMENT"),
        plot_bgcolor='rgba(0, 0, 0, 0)', 
        paper_bgcolor='rgba(0, 0, 0, 0)',  
        xaxis=dict(showgrid=True, gridcolor="#ea662e"),  
        yaxis=dict(showgrid=True, gridcolor="#ea662e"),  
        font=dict(color="#ea662e"),  # Set text color to black
    )
)
# Display the Plotly figure using Streamlit
st.plotly_chart(fig2,use_container_width=True)



hide_st_style=""" 

<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
"""

