import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Set page config for a premium feel
st.set_page_config(
    page_title="Sales Performance Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stMetric {
        background-color: #1e2130;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    div[data-testid="stMetricValue"] {
        color: #00d4ff;
    }
    </style>
    """, unsafe_allow_html=True)

@st.cache_data
def load_data():
    df = pd.read_csv('data/cleaned_sales_data.csv')
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    return df

def main():
    df = load_data()

    # Sidebar Filters
    st.sidebar.title("🛠️ Dashboard Filters")
    region = st.sidebar.multiselect("Select Region", options=df['Region'].unique(), default=df['Region'].unique())
    category = st.sidebar.multiselect("Select Category", options=df['Category'].unique(), default=df['Category'].unique())
    
    # Filter data
    filtered_df = df[(df['Region'].isin(region)) & (df['Category'].isin(category))]

    # Header
    st.title("📊 Sales Performance Executive Dashboard")
    st.markdown("### Strategic Overview & Performance Metrics")
    
    # Top KPI Cards
    col1, col2, col3, col4 = st.columns(4)
    
    total_revenue = filtered_df['Revenue'].sum()
    total_profit = filtered_df['Profit'].sum()
    total_orders = filtered_df['Order ID'].nunique()
    avg_margin = (total_profit / total_revenue * 100) if total_revenue != 0 else 0
    
    col1.metric("Total Revenue", f"${total_revenue:,.0f}", "+12%")
    col2.metric("Total Profit", f"${total_profit:,.0f}", "+8%")
    col3.metric("Total Orders", f"{total_orders:,}", "+5%")
    col4.metric("Profit Margin", f"{avg_margin:.1f}%", "-2%")

    st.markdown("---")

    # Main Visuals
    left_col, right_col = st.columns([2, 1])

    with left_col:
        # Revenue Trend
        st.subheader("📈 Monthly Revenue Trend")
        df_trend = filtered_df.groupby(filtered_df['Order Date'].dt.to_period('M'))['Revenue'].sum().reset_index()
        df_trend['Order Date'] = df_trend['Order Date'].astype(str)
        fig_trend = px.area(df_trend, x='Order Date', y='Revenue', 
                            color_discrete_sequence=['#00d4ff'],
                            template="plotly_dark")
        fig_trend.update_layout(margin=dict(l=0, r=0, t=30, b=0))
        st.plotly_chart(fig_trend, use_container_width=True)

    with right_col:
        # Category Breakdown
        st.subheader("📦 Sales by Category")
        fig_pie = px.pie(filtered_df, values='Revenue', names='Category', 
                         hole=0.5, template="plotly_dark",
                         color_discrete_sequence=px.colors.sequential.RdBu)
        fig_pie.update_layout(margin=dict(l=0, r=0, t=30, b=0))
        st.plotly_chart(fig_pie, use_container_width=True)

    # Second Row
    st.markdown("---")
    col_a, col_b = st.columns(2)

    with col_a:
        st.subheader("🌍 Regional Performance")
        df_region = filtered_df.groupby('Region')['Revenue'].sum().reset_index().sort_values('Revenue', ascending=False)
        fig_region = px.bar(df_region, x='Region', y='Revenue', 
                            color='Revenue', color_continuous_scale='Blues',
                            template="plotly_dark")
        st.plotly_chart(fig_region, use_container_width=True)

    with col_b:
        st.subheader("🔝 Top 10 Products by Profit")
        df_prod = filtered_df.groupby('Product Name')['Profit'].sum().nlargest(10).reset_index()
        fig_prod = px.bar(df_prod, y='Product Name', x='Profit', 
                          orientation='h', color='Profit',
                          color_continuous_scale='Viridis',
                          template="plotly_dark")
        fig_prod.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig_prod, use_container_width=True)

    # Data Table Preview
    with st.expander("🔍 View Raw Cleaned Data"):
        st.dataframe(filtered_df.head(100), use_container_width=True)

if __name__ == "__main__":
    main()
