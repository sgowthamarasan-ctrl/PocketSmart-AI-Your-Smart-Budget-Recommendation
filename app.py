import streamlit as st
from utils.budget_engine import analyze_budget, generate_recommendations

st.set_page_config(page_title="PocketSmart AI", page_icon="💰", layout="wide")

st.title("💰 PocketSmart AI")
st.subheader("Your Smart Budget & Recommendation Assistant")
st.caption("Track your budget, understand your spending, and get practical recommendations.")

with st.sidebar:
    st.header("💵 Monthly Budget")
    income = st.number_input("Monthly income (₹)", min_value=0.0, value=30000.0, step=1000.0)
    savings_goal = st.number_input("Savings goal (₹)", min_value=0.0, value=5000.0, step=500.0)

    st.header("📊 Expenses")
    food = st.number_input("Food & groceries (₹)", min_value=0.0, value=5000.0, step=500.0)
    transport = st.number_input("Transport (₹)", min_value=0.0, value=2500.0, step=500.0)
    rent = st.number_input("Rent / accommodation (₹)", min_value=0.0, value=8000.0, step=500.0)
    bills = st.number_input("Bills & utilities (₹)", min_value=0.0, value=2500.0, step=500.0)
    shopping = st.number_input("Shopping (₹)", min_value=0.0, value=3000.0, step=500.0)
    entertainment = st.number_input("Entertainment (₹)", min_value=0.0, value=1500.0, step=500.0)
    other = st.number_input("Other expenses (₹)", min_value=0.0, value=1500.0, step=500.0)

expenses = {
    "Food & groceries": food,
    "Transport": transport,
    "Rent / accommodation": rent,
    "Bills & utilities": bills,
    "Shopping": shopping,
    "Entertainment": entertainment,
    "Other": other,
}

analysis = analyze_budget(income, savings_goal, expenses)
recommendations = generate_recommendations(analysis)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Income", f"₹{income:,.0f}")
col2.metric("Total expenses", f"₹{analysis['total_expenses']:,.0f}")
col3.metric("Remaining", f"₹{analysis['remaining']:,.0f}")
col4.metric("Savings rate", f"{analysis['savings_rate']:.1f}%")

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("📈 Expense Breakdown")
    chart_data = analysis["category_percentages"]
    st.bar_chart(chart_data)

with right:
    st.subheader("🤖 PocketSmart Recommendations")
    for rec in recommendations:
        st.info(rec)

st.subheader("📋 Budget Summary")
summary = analysis["summary"]
st.dataframe(summary, use_container_width=True, hide_index=True)

if analysis["remaining"] < 0:
    st.error("Your expenses are higher than your income. Consider reducing flexible spending.")
elif analysis["remaining"] < savings_goal:
    st.warning("You are below your savings goal. Review the highest spending categories above.")
else:
    st.success("Your current budget can meet your savings goal. Keep monitoring your spending!")

st.divider()
st.caption("PocketSmart AI • Smart Budget & Recommendation")
