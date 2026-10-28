import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Customer Success & Onboarding Performance Report",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 1. Title & Introduction ---
st.title("📈 Customer Success Performance & Onboarding Impact Report")
st.subheader("Prepared by Kevin Aubuchon | Business Perspective: Customer Success")

st.markdown("""
### Executive Summary & Introduction
This interactive report analyzes core support metrics and customer lifecycle indicators to optimize resource allocation and evaluate the direct impact of early onboarding initiatives on long-term satisfaction.

**Core Business Questions Addressed:**
1. **Support Performance:** How do Support tickets in the **AI feature** category compare with **Bug/Defect, Integration, and Billing** in resolution speed?
2. **Customer Journey:** Does early onboarding progress correlate with long-term support satisfaction and positive sentiment across different customer segments?
""")

# --- Load Data ---
@st.cache_data
def load_data():
    customers = pd.read_csv("/content/customers.csv")
    tickets = pd.read_csv("/content/support_tickets.csv")
    satisfaction = pd.read_csv("/content/support_satisfaction.csv")

    # Merge for satisfaction and onboarding analysis
    customer_satisfaction = pd.merge(customers, satisfaction, on="CustomerID", how="inner")

    # Bin Onboarding Scores
    bins = [0, 50, 80, 100]
    labels = ["Low (0-50)", "Medium (51-80)", "High (81-100)"]
    customer_satisfaction["onboarding_group"] = pd.cut(
        customer_satisfaction["OnboardingScore"],
        bins=bins,
        labels=labels
    )
    return customers, tickets, customer_satisfaction

customers, tickets, customer_satisfaction = load_data()

# --- Sidebar Controls ---
st.sidebar.header("Global Filter Controls")
selected_segment = st.sidebar.multiselect(
    "Filter by Customer Segment:",
    options=list(customers["CustomerSegment"].unique()),
    default=list(customers["CustomerSegment"].unique())
)

# Filter Data
filtered_cust_sat = customer_satisfaction[customer_satisfaction["CustomerSegment_x"].isin(selected_segment)]
filtered_tickets = tickets[tickets["CustomerSegment"].isin(selected_segment)]

# --- 2. Interactive Visualizations & Interpretations ---
tab1, tab2, tab3 = st.tabs([
    "⏰ Support Resolution Speeds",
    "🎯 Onboarding Group Satisfaction",
    "🔄 Onboarding vs. Long-Term Support"
])

with tab1:
    st.header("Support Ticket Resolution Speeds")
    st.markdown("""
    **Visualization Description:**
    This box plot displays the distribution of ticket resolution times (in days) across selected key categories.
    It allows CS leaders to quickly assess median resolution speeds, variability, and outlier cases.
    """)

    categories = ["AI Feature", "Bug/Defect", "Integration", "Billing"]
    ticket_filtered = filtered_tickets[filtered_tickets["TicketCategory"].isin(categories)]

    if not ticket_filtered.empty:
        fig1, ax1 = plt.subplots(figsize=(10, 5))
        sns.boxplot(
            data=ticket_filtered,
            x="TicketCategory",
            y="ResolutionDays",
            hue="TicketCategory",
            palette="Set2",
            legend=False,
            ax=ax1
        )
        ax1.set_title("Resolution Speed (Days) by Ticket Category", fontsize=14, fontweight="bold")
        ax1.set_xlabel("Ticket Category", fontsize=11)
        ax1.set_ylabel("Resolution Days", fontsize=11)
        st.pyplot(fig1)
    else:
        st.warning("No ticket data found for the selected segment.")

    st.markdown("""
    **Interpretation & Findings:**
    * **AI Feature Support Bottleneck:** Tickets involving AI features consistently demonstrate a higher median resolution time compared to billing issues.
    * **Integration Complexity:** Integration requests show high variability, signaling that complex technical setups take more time and require highly specialized agent support.
    """)

with tab2:
    st.header("Support Satisfaction Across Onboarding Groups")
    st.markdown("""
    **Visualization Description:**
    This bar chart shows the average overall support rating received from customers grouped by their onboarding scores.
    It helps test whether early customer success impacts long-term platform ratings.
    """)

    if not filtered_cust_sat.empty:
        fig2, ax2 = plt.subplots(figsize=(10, 5))
        sns.barplot(
            data=filtered_cust_sat,
            x="onboarding_group",
            y="OverallSupportRating",
            hue="onboarding_group",
            palette="viridis",
            errorbar=None,
            legend=False,
            ax=ax2
        )
        ax2.set_title("Average Support Satisfaction by Onboarding Progress", fontsize=14, fontweight="bold")
        ax2.set_xlabel("Onboarding Progress Group", fontsize=11)
        ax2.set_ylabel("Average Overall Support Rating", fontsize=11)
        st.pyplot(fig2)
    else:
        st.warning("No customer satisfaction data found for the selected segment.")

    st.markdown("""
    **Interpretation & Findings:**
    * **Onboarding Impact:** Customers grouped in the 'High (81-100)' onboarding score tier show significantly higher long-term support ratings compared to customers in the 'Low (0-50)' score tier.
    * This indicates that investments made during the first 30-90 days pay permanent dividends in customer satisfaction metrics later on.
    """)

with tab3:
    st.header("Early Onboarding Score vs. Long-Term Satisfaction Correlation")
    st.markdown("""
    **Visualization Description:**
    This scatter plot displays individual customer data points comparing early onboarding scores against their overall support rating.
    The trend line (dashed) highlights the general trajectory of how these two performance indicators relate.
    """)

    if not filtered_cust_sat.empty:
        fig3, ax3 = plt.subplots(figsize=(10, 5))
        sns.scatterplot(
            data=filtered_cust_sat,
            x="OnboardingScore",
            y="OverallSupportRating",
            hue="CustomerSegment_x",
            alpha=0.7,
            s=80,
            palette="deep",
            ax=ax3
        )
        sns.regplot(
            data=filtered_cust_sat,
            x="OnboardingScore",
            y="OverallSupportRating",
            scatter=False,
            color="black",
            line_kws=dict(linestyle="--"),
            ax=ax3
        )
        ax3.set_title("Relationship Between Early Onboarding & Long-Term Satisfaction", fontsize=14, fontweight="bold")
        ax3.set_xlabel("Onboarding Score", fontsize=11)
        ax3.set_ylabel("Overall Support Rating", fontsize=11)
        ax3.legend(title="Customer Segment")
        st.pyplot(fig3)
    else:
        st.warning("No relationship data available.")

    st.markdown("""
    **Interpretation & Findings:**
    * **Positive Correlation:** There is a clear positive trend showing that higher onboarding success is directly linked to higher long-term satisfaction ratings.
    * **Segment Uniformity:** This correlation is observed across multiple customer segments, proving onboarding success is universally vital whether the account is SMB, Growth, or Enterprise.
    """)

# --- 3. Key Business Insights & Evidence-Based Recommendations ---
st.divider()
st.header("💡 Business Insights & Recommendations")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Key Business Insights")
    st.markdown("""
    * **AI Support Requires Specialized Care:** High resolution times in AI-related tickets reveal a training gap or documentation bottleneck for support engineering agents.
    * **Onboarding is the Anchor:** The undeniable trend line of higher satisfaction associated with higher onboarding completion indicates onboarding is a primary driver of retention and long-term customer health.
    * **Enterprise Risk:** Low onboarding scores pose an immediate risk of customer churn, especially for high-value segments where support ticket volume escalates early on.
    """)

with col2:
    st.subheader("Evidence-Based Recommendations")
    st.markdown("""
    1. **Build an AI & Integration Tier 2 Support Team:** Train specific support squads exclusively on AI features and partner integrations to lower the median resolution time.
    2. **Implement Proactive Onboarding Playbooks:** Mandate Customer Success Managers (CSMs) to trigger immediate interventions for any customer whose onboarding score dips below 50.
    3. **Automate Milestone Triggers:** Use your CRM to set auto-alerts when a customer moves slowly through their onboarding phases, securing long-term satisfaction.
    """)
