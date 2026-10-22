
# Import the libraries needed for the dashboard
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set the dashboard page settings
st.set_page_config(
    page_title="Waste Collection Data Analysis",
    page_icon="♻️",
    layout="wide"
)

# Add the dashboard title and introduction
st.title("Waste Collection Data Analysis: England 2024–2025")
st.write(
    "This dashboard explores recorded recycling tonnage across "
    "reporting periods, local authorities and materials."
)

# Load the cleaned dashboard dataset
@st.cache_data
def load_data():
    return pd.read_csv("cleaned_recycling_dashboard.csv")

dashboard_df = load_data()

# Add filters to the sidebar
st.sidebar.header("Filter the Data")

selected_periods = st.sidebar.multiselect(
    "Select reporting periods",
    options=sorted(dashboard_df["Period"].unique()),
    default=sorted(dashboard_df["Period"].unique())
)

selected_authorities = st.sidebar.multiselect(
    "Select local authorities",
    options=sorted(dashboard_df["Authority"].unique()),
    default=sorted(dashboard_df["Authority"].unique())
)

# Apply the selected filters
filtered_df = dashboard_df[
    dashboard_df["Period"].isin(selected_periods)
    & dashboard_df["Authority"].isin(selected_authorities)
]

# Display key figures
total_tonnage = filtered_df["Recycling_Tonnage"].sum()
authority_count = filtered_df["Authority"].nunique()
material_count = filtered_df["RowText"].nunique()

col1, col2, col3 = st.columns(3)

col1.metric("Recorded Recycling Tonnage", f"{total_tonnage:,.0f} tonnes")
col2.metric("Local Authorities", f"{authority_count:,}")
col3.metric("Material Categories", f"{material_count:,}")

# Summarise recycling tonnage by reporting period
st.subheader("Recorded Recycling Tonnage by Reporting Period")

period_totals = (
    filtered_df.groupby("Period")["Recycling_Tonnage"]
    .sum()
    .reindex([
        "Apr 24 - Jun 24",
        "Jul 24 - Sep 24",
        "Oct 24 - Dec 24",
        "Jan 25 - Mar 25"
    ])
    .dropna()
)

st.bar_chart(period_totals)


# Show the trend in recorded recycling tonnage over time
st.subheader("Recycling Tonnage Trend Over Time")

fig, ax = plt.subplots(figsize=(10, 5))

period_totals.plot(
    kind="line",
    marker="o",
    linewidth=2,
    ax=ax
)

ax.set_xlabel("Reporting Period")
ax.set_ylabel("Recorded Recycling Tonnage (tonnes)")
ax.set_title("Recycling Tonnage Trend Over Time")
ax.grid(True, alpha=0.3)

plt.xticks(rotation=30, ha="right")
fig.tight_layout()

st.pyplot(fig)
plt.close(fig)


# Summarise recycling tonnage by material
st.subheader("Top Five Materials by Recorded Tonnage")

material_totals = (
    filtered_df.groupby("RowText")["Recycling_Tonnage"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

# Create a pie chart for the top five materials
fig, ax = plt.subplots(figsize=(8, 6))

material_totals.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90,
    ax=ax,
    legend=False
)

ax.legend(
    labels=material_totals.index,
    title="Material",
    loc="center left",
    bbox_to_anchor=(1.0, 0.5)
)

ax.set_ylabel("")
ax.set_title("Share of Recorded Tonnage: Top Five Materials")
st.pyplot(fig)
plt.close(fig)





# Third chart: Top 10 Local Authorities
st.subheader("Top 10 Local Authorities by Recorded Recycling Tonnage")

authority_totals = (
    filtered_df.groupby("Authority")["Recycling_Tonnage"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

if authority_totals.empty:
    st.info("No authority data is available for the selected filters.")
else:
    fig, ax = plt.subplots(figsize=(12, 7))

    sorted_authorities = authority_totals.sort_values(ascending=True)

    bar_colours = [
        "#4E79A7", "#F28E2B", "#59A14F", "#E15759", "#B07AA1",
        "#76B7B2", "#EDC948", "#FF9DA7", "#9C755F", "#BAB0AC"
    ]

    sorted_authorities.plot(
        kind="barh",
        ax=ax,
        color=bar_colours[:len(sorted_authorities)]
    )

    # Create a colour key for each local authority
    handles = [
        plt.Rectangle((0, 0), 1, 1, color=bar_colours[i])
        for i in range(len(sorted_authorities))
    ]

    ax.legend(
        handles,
        sorted_authorities.index,
        title="Local Authority — Colour Key",
        loc="upper center",
        bbox_to_anchor=(0.5, -0.15),
        ncol=2,
        frameon=False
    )

    ax.set_xlabel("Recorded recycling tonnage (tonnes)")
    ax.set_ylabel("Local authority")
    ax.set_title("Top 10 Local Authorities by Recorded Recycling Tonnage")

    fig.tight_layout(rect=[0, 0.15, 1, 1])
    st.pyplot(fig)
    plt.close(fig)




st.caption(
    "These figures represent recorded tonnage in the selected dataset. "
    "Differences between authorities may reflect population size, waste generation "
    "and collection arrangements. The figures alone do not measure overall recycling performance."
)

# Show the filtered data without row numbers
with st.expander("View the filtered data"):
    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True
    )

# Explain the limitation of the figures
st.caption(
    "These figures represent recorded tonnage in the selected dataset. "
    "Differences between authorities may reflect population size, "
    "waste generation and collection arrangements. The figures alone "
    "do not measure overall recycling performance."
)
