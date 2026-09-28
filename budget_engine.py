import pandas as pd

def analyze_budget(income, savings_goal, expenses):
    total = sum(expenses.values())
    remaining = income - total
    savings_rate = (remaining / income * 100) if income else 0

    percentages = {}
    for category, amount in expenses.items():
        percentages[category] = (amount / total * 100) if total else 0

    category_percentages = pd.DataFrame(
        {"Percentage": percentages}
    ).sort_values("Percentage", ascending=False)

    summary = pd.DataFrame([
        {"Category": k, "Amount (₹)": v, "Share (%)": round(percentages[k], 1)}
        for k, v in sorted(expenses.items(), key=lambda x: x[1], reverse=True)
    ])

    return {
        "income": income,
        "savings_goal": savings_goal,
        "total_expenses": total,
        "remaining": remaining,
        "savings_rate": savings_rate,
        "category_percentages": category_percentages,
        "summary": summary,
        "expenses": expenses,
    }

def generate_recommendations(analysis):
    expenses = analysis["expenses"]
    income = analysis["income"]
    total = analysis["total_expenses"]
    remaining = analysis["remaining"]
    savings_goal = analysis["savings_goal"]

    if not income:
        return ["Enter your monthly income to receive personalized budget recommendations."]

    recs = []
    highest = max(expenses, key=expenses.get) if expenses else None

    if remaining < 0:
        recs.append("⚠️ You are overspending. Reduce flexible categories such as shopping, entertainment, and food first.")
    elif remaining < savings_goal:
        gap = savings_goal - remaining
        recs.append(f"🎯 You are about ₹{gap:,.0f} short of your savings goal. Look for expenses you can reduce.")
    else:
        recs.append("✅ Your budget currently supports your savings goal. Consider moving the surplus into savings.")

    if highest and total and expenses[highest] / total > 0.30:
        recs.append(f"🔎 {highest} is your largest expense category. Review this category for possible savings.")

    if expenses.get("Shopping", 0) > income * 0.10:
        recs.append("🛍️ Shopping is above 10% of income. Consider a monthly shopping limit.")

    if expenses.get("Entertainment", 0) > income * 0.08:
        recs.append("🎬 Entertainment is relatively high. Set a fixed entertainment allowance.")

    if expenses.get("Food & groceries", 0) > income * 0.20:
        recs.append("🍱 Food & groceries are taking a large share of income. Planning meals and comparing prices may help.")

    if analysis["savings_rate"] >= 20:
        recs.append("💎 Your current surplus is at least 20% of income. Building an emergency fund can be a useful next step.")

    return recs
