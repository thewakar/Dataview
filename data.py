import streamlit as st
from streamlit_lightweight_charts import renderLightweightCharts

chartOptions = {
    "layout": {
        "textColor": 'black',
        "background": {
            "type": 'solid',
            "color": 'white'
        }
    }
}

import requests
r = requests.get('https://docs.google.com/spreadsheets/d/1Vdw5xnB_WfduSsZOEbF-ZltwT2yxAxTSaPH2saX5o5A/edit#gid=0&output=csv')
data = r.content

seriesLineChart = [{
    "type": 'Line',
    "data": data,
    "options": {}
}]

st.subheader("Line Chart with Watermark")

renderLightweightCharts([
    {
        "chart": chartOptions,
        "series": seriesLineChart
    }
], 'line')
