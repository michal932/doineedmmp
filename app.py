"""
MMP Necessity Calculator
Interactive Streamlit application for mobile app marketers
"""

import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Do I Need an MMP?",
    page_icon="📱",
    layout="wide"
)

# Title
st.title("📱 Do I Need an MMP?")
st.markdown("*Mobile Measurement Partner & SKAdNetwork Decision Tool*")

# Sidebar with input controls
st.sidebar.header("⚙️ Input Parameters")

# Input 1: Monthly Budget (EUR)
monthly_budget = st.sidebar.slider(
    "Monthly Media Budget (€):",
    min_value=0,
    max_value=20000,
    value=2000,
    step=200,
    format="€%d"
)

# Input 2: Number of channels
num_channels = st.sidebar.slider(
    "Number of Marketing Channels:",
    min_value=1,
    max_value=10,
    value=1,
    step=1
)

# Input 3: iOS share
ios_share = st.sidebar.slider(
    "iOS User Share (%):",
    min_value=0,
    max_value=100,
    value=30,
    step=5,
    format="%d%%"
)

# Input 4: Affiliate strategy
uses_affiliate = st.sidebar.checkbox(
    "I use Affiliate partners / Performance-based Influencers (CPA)",
    help="Affiliate marketing requires MMP for postback automation"
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 💰 iOS Budget")

# Input 5: Checkbox for separate iOS budget
use_separate_ios_budget = st.sidebar.checkbox(
    "I have a separate iOS budget",
    help="Check this if you allocate a specific budget for iOS campaigns separately from your total budget"
)

# Calculate iOS-specific budget
if use_separate_ios_budget:
    # Input 6: Separate iOS Budget slider
    monthly_ios_budget = st.sidebar.slider(
        "Monthly iOS Budget (€):",
        min_value=0,
        max_value=20000,
        value=int(monthly_budget * ios_share / 100),
        step=100,
        format="€%d",
        help="Your dedicated iOS marketing budget per month"
    )
else:
    # Calculate from total budget and iOS share
    monthly_ios_budget = monthly_budget * (ios_share / 100)

st.sidebar.markdown("---")

# Collapsible App Details section
with st.sidebar.expander("🎯 App Details (Optional for SKAN)"):
    st.markdown("*These details help optimize SKAN recommendations*")

    # Input 7: App Category
    app_category = st.selectbox(
        "App Category:",
        ["Gaming", "Finance", "E-commerce", "Education", "Health & Fitness",
         "Lifestyle", "Utilities", "Media", "Other"]
    )

    # Input 8: Monetization Model
    monetization_model = st.selectbox(
        "Monetization Model:",
        ["Subscription", "Subscription with trial", "In-app purchases",
         "Hybrid", "Ad-based", "No monetization"]
    )

    # Input 9: Primary Goal
    primary_goal = st.selectbox(
        "Primary Acquisition Goal:",
        ["Install", "Registration", "Trial Start", "Purchase", "Retention/Engagement"]
    )

st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Current Values")
st.sidebar.metric("Total Budget", f"€{monthly_budget:,}")
st.sidebar.metric("iOS Budget", f"€{int(monthly_ios_budget):,}")
st.sidebar.metric("Channels", num_channels)
st.sidebar.metric("iOS Share", f"{ios_share}%")

# ============================================================================
# SKAN RELEVANCE EVALUATION
# ============================================================================

# Base SKAN relevance on iOS budget
if monthly_ios_budget < 500:
    skan_relevance = "low"
    skan_level = "❌ SKAN doesn't make sense"
    skan_color = "red"
elif 500 <= monthly_ios_budget < 1000:
    skan_relevance = "medium"
    skan_level = "🟡 SKAN makes limited sense"
    skan_color = "orange"
else:
    skan_relevance = "high"
    skan_level = "✅ SKAN makes sense"
    skan_color = "green"

# Adjust based on monetization model
monetization_skan_boost = False
if monetization_model in ["Subscription", "Subscription with trial"]:
    monetization_skan_boost = True
    # Trial and subscription models benefit heavily from SKAN conversion values
    if skan_relevance == "low" and monthly_ios_budget >= 300:
        skan_relevance = "medium"
        skan_level = "🟡 SKAN makes limited sense"

# Adjust based on primary goal
if primary_goal in ["Purchase", "Trial Start"] and monthly_ios_budget >= 400:
    if skan_relevance == "low":
        skan_relevance = "medium"
        skan_level = "🟡 SKAN makes limited sense"

# Adjust based on app category
high_ltv_categories = ["Finance", "E-commerce", "Gaming"]
if app_category in high_ltv_categories and monthly_ios_budget >= 400:
    if skan_relevance == "low":
        skan_relevance = "medium"
        skan_level = "🟡 SKAN makes limited sense"

# ============================================================================
# MMP NECESSITY EVALUATION
# ============================================================================

# Logic: Determine budget threshold based on iOS share
budget_threshold = 2000  # Default threshold (€2,000 EUR ~ 50,000 CZK)
effective_budget_threshold = budget_threshold

if ios_share > 50:
    effective_budget_threshold = 800  # Lower threshold for iOS-heavy apps (€800 EUR ~ 20,000 CZK)

# Determine quadrant
is_high_budget = monthly_budget >= effective_budget_threshold
is_high_complexity = num_channels > 1 or uses_affiliate

# For visualization: adjust Y-value if affiliate is used
visual_channels = num_channels
if uses_affiliate and num_channels == 1:
    visual_channels = 2.5  # Push into technical necessity zone visually

# Create the Plotly chart
fig = go.Figure()

# Define quadrant boundaries
x_threshold = effective_budget_threshold
y_threshold = 1.5  # Visual threshold between single and multi-channel

# Add colored quadrant shapes (as rectangles)
# Bottom-Left: Green - "YOU DON'T NEED AN MMP"
fig.add_shape(
    type="rect",
    x0=0, y0=0,
    x1=x_threshold, y1=y_threshold,
    fillcolor="rgba(76, 175, 80, 0.3)",  # Green
    line=dict(width=0),
    layer="below"
)

# Top-Left: Blue - "TECHNICAL NEED"
fig.add_shape(
    type="rect",
    x0=0, y0=y_threshold,
    x1=x_threshold, y1=10,
    fillcolor="rgba(33, 150, 243, 0.3)",  # Blue
    line=dict(width=0),
    layer="below"
)

# Bottom-Right: Yellow/Orange - "GRAY ZONE (RISK)"
fig.add_shape(
    type="rect",
    x0=x_threshold, y0=0,
    x1=20000, y1=y_threshold,
    fillcolor="rgba(255, 193, 7, 0.3)",  # Yellow/Orange
    line=dict(width=0),
    layer="below"
)

# Top-Right: Red - "MMP IS NECESSARY"
fig.add_shape(
    type="rect",
    x0=x_threshold, y0=y_threshold,
    x1=20000, y1=10,
    fillcolor="rgba(244, 67, 54, 0.3)",  # Red
    line=dict(width=0),
    layer="below"
)

# Add quadrant labels
annotations = [
    dict(
        x=x_threshold / 2, y=y_threshold / 2,
        text="<b>YOU DON'T<br>NEED AN MMP</b>",
        showarrow=False,
        font=dict(size=14, color="darkgreen"),
        bgcolor="rgba(255, 255, 255, 0.7)",
        borderpad=10
    ),
    dict(
        x=x_threshold / 2, y=(y_threshold + 10) / 2,
        text="<b>TECHNICAL<br>NEED</b>",
        showarrow=False,
        font=dict(size=14, color="darkblue"),
        bgcolor="rgba(255, 255, 255, 0.7)",
        borderpad=10
    ),
    dict(
        x=(x_threshold + 20000) / 2, y=y_threshold / 2,
        text="<b>GRAY ZONE<br>(RISK)</b>",
        showarrow=False,
        font=dict(size=14, color="darkorange"),
        bgcolor="rgba(255, 255, 255, 0.7)",
        borderpad=10
    ),
    dict(
        x=(x_threshold + 20000) / 2, y=(y_threshold + 10) / 2,
        text="<b>MMP IS<br>NECESSARY</b>",
        showarrow=False,
        font=dict(size=14, color="darkred"),
        bgcolor="rgba(255, 255, 255, 0.7)",
        borderpad=10
    )
]

# Add threshold lines
fig.add_shape(
    type="line",
    x0=x_threshold, y0=0,
    x1=x_threshold, y1=10,
    line=dict(color="gray", width=2, dash="dash")
)

fig.add_shape(
    type="line",
    x0=0, y0=y_threshold,
    x1=20000, y1=y_threshold,
    line=dict(color="gray", width=2, dash="dash")
)

# Add user's position as a prominent dot
fig.add_trace(
    go.Scatter(
        x=[monthly_budget],
        y=[visual_channels],
        mode='markers+text',
        marker=dict(
            size=25,
            color='darkblue',
            symbol='circle',
            line=dict(width=3, color='white')
        ),
        text=['YOUR APP'],
        textposition='top center',
        textfont=dict(size=12, color='darkblue', family='Arial Black'),
        name='Your position',
        hovertemplate=(
            '<b>Your app</b><br>' +
            'Budget: €%{x:,}<br>' +
            'Channels: ' + str(num_channels) + '<br>' +
            '<extra></extra>'
        )
    )
)

# Update layout
fig.update_layout(
    title=dict(
        text="<b>Decision Matrix: Do You Need an MMP?</b>",
        x=0.5,
        xanchor='center',
        font=dict(size=20)
    ),
    xaxis=dict(
        title="<b>Monthly Media Budget (EUR)</b>",
        range=[0, 20000],
        gridcolor='lightgray',
        tickformat=',',
        tickprefix='€'
    ),
    yaxis=dict(
        title="<b>Channel Complexity</b>",
        range=[0, 10],
        gridcolor='lightgray',
        dtick=1
    ),
    annotations=annotations,
    hovermode='closest',
    showlegend=False,
    height=600,
    plot_bgcolor='white',
    paper_bgcolor='white'
)

# Display the chart
st.plotly_chart(fig, use_container_width=True)

# Dynamic recommendation section
st.markdown("---")
st.header("💡 Recommendations for Your App")

# ============================================================================
# MMP RECOMMENDATION (Primary)
# ============================================================================
st.subheader("🔧 Mobile Measurement Partner")

# Determine the recommendation category
if is_high_budget and is_high_complexity:
    category = "MMP IS NECESSARY"
    color = "red"
    icon = "🔴"
elif is_high_budget and not is_high_complexity:
    category = "GRAY ZONE (RISK)"
    color = "orange"
    icon = "🟠"
elif not is_high_budget and is_high_complexity:
    category = "TECHNICAL NEED"
    color = "blue"
    icon = "🔵"
else:
    category = "YOU DON'T NEED AN MMP"
    color = "green"
    icon = "🟢"

st.markdown(f"### {icon} **{category}**")

# Generate detailed recommendation text
recommendation_parts = []

# Main assessment
if category == "MMP IS NECESSARY":
    recommendation_parts.append(
        f"With a monthly budget of **€{monthly_budget:,}** and **{num_channels} "
        f"marketing channel{'s' if num_channels > 1 else ''}**, you definitely need an MMP solution."
    )
    recommendation_parts.append(
        "**Why?** At this investment level and channel complexity, professional "
        "measurement and attribution are critical for performance optimization and fraud prevention."
    )

elif category == "GRAY ZONE (RISK)":
    recommendation_parts.append(
        f"Your budget of **€{monthly_budget:,}** is high enough to justify an MMP investment, "
        "but you're currently working with only **one channel**."
    )
    recommendation_parts.append(
        "**⚠️ Risks without MMP:**\n"
        "- **Vendor lock-in:** Dependence on a single ad channel's reporting\n"
        "- **Ad fraud:** Higher risk of fraudulent installs without independent verification\n"
        "- **Scalability:** When you add more channels, you'll regret not starting earlier"
    )
    recommendation_parts.append(
        "**Recommendation:** Consider an MMP to protect your investment and prepare for growth."
    )

elif category == "TECHNICAL NEED":
    recommendation_parts.append(
        f"You're working with **{num_channels} marketing channels**"
        + (" and using **affiliate partners**" if uses_affiliate else "")
        + f", but your budget is currently at **€{monthly_budget:,}**."
    )

    if uses_affiliate:
        recommendation_parts.append(
            "**🔴 Affiliate/Influencer marketing requires an MMP!**\n"
            "For performance-based campaigns (CPA), you need to send postbacks to partners. "
            "Without an MMP, you have no way to automate conversion communication."
        )

    recommendation_parts.append(
        "**Technical necessity:** Multi-channel measurement requires a centralized solution. "
        "Consider **free tier** MMP tools (e.g., AppsFlyer, Adjust) or "
        "cheaper alternatives for small projects."
    )

else:  # YOU DON'T NEED AN MMP
    recommendation_parts.append(
        f"With a budget of **€{monthly_budget:,}** and **a single marketing channel**, "
        "you don't yet need a dedicated MMP solution."
    )
    recommendation_parts.append(
        "**Recommendation:**\n"
        "- Use **Firebase Analytics** or **Google Analytics for Firebase** (free)\n"
        "- Rely on reporting directly from your ad channel\n"
        "- Monitor the situation: once you add a second channel or increase your budget, an MMP will make sense"
    )

# iOS-specific warning
if ios_share > 50:
    recommendation_parts.append(
        f"**📱 iOS Warning:** More than **{ios_share}% of your users** are on iOS. "
        "Due to **SKAdNetwork** and iOS 14.5+ ATT, measurement on iOS is extremely complex. "
        "Even with a lower budget, an MMP helps process and normalize SKAdNetwork data."
    )

    if monthly_budget >= 800 and monthly_budget < 2000:
        recommendation_parts.append(
            "⚠️ **Threshold adjusted:** Due to high iOS share, the recommended "
            "MMP threshold is lowered from €2,000 to **€800 per month**."
        )

# Display recommendation
for part in recommendation_parts:
    st.markdown(part)
    st.markdown("")

# ============================================================================
# SKAN RECOMMENDATION (Secondary)
# ============================================================================
st.markdown("---")
st.subheader("📱 SKAdNetwork (SKAN)")
st.markdown(f"### {skan_level}")

# Generate SKAN explanation
skan_explanation = []

if use_separate_ios_budget:
    skan_explanation.append(
        f"Your **dedicated iOS budget is €{int(monthly_ios_budget):,}/month**."
    )
else:
    skan_explanation.append(
        f"Your **iOS budget is €{int(monthly_ios_budget):,}/month** "
        f"({ios_share}% of total €{monthly_budget:,} budget)."
    )

if skan_relevance == "high":
    skan_explanation.append(
        "**Why SKAN makes sense:**\n"
        "- Budget is sufficient to optimize SKAN campaigns\n"
        "- You can measure post-install events and revenue\n"
        "- SKAN conversion values will improve campaign performance"
    )

    if monetization_skan_boost:
        skan_explanation.append(
            f"**{monetization_model}** models benefit significantly from SKAN "
            "revenue tracking and conversion value optimization."
        )

elif skan_relevance == "medium":
    skan_explanation.append(
        "**Limited SKAN value:**\n"
        "- Budget is modest but can support basic SKAN setup\n"
        "- Focus on high-value conversion events only\n"
        "- ROI may be marginal at this spend level"
    )

    if monetization_skan_boost:
        skan_explanation.append(
            f"Your **{monetization_model}** model increases SKAN priority. "
            "Proper setup can help optimize for high-LTV users."
        )

    if primary_goal in ["Purchase", "Trial Start"]:
        skan_explanation.append(
            f"Your goal (**{primary_goal}**) aligns well with SKAN conversion tracking."
        )

else:  # low relevance
    skan_explanation.append(
        "**Why SKAN doesn't make sense yet:**\n"
        "- iOS budget is too low for meaningful SKAN optimization\n"
        "- Setup complexity outweighs potential benefits\n"
        "- Focus on increasing budget or iOS share first"
    )

    if ios_share < 30:
        skan_explanation.append(
            f"Your iOS share is only {ios_share}%. SKAN becomes valuable when "
            "iOS represents a larger portion of your user base."
        )

# Special case: No monetization
if monetization_model == "No monetization":
    skan_explanation.append(
        "**⚠️ Note:** Without monetization, SKAN revenue signals won't apply. "
        "Focus on event-based conversion values instead."
    )

for part in skan_explanation:
    st.markdown(part)
    st.markdown("")

# Additional info section
st.markdown("---")
st.markdown("### 📚 Learn More")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### What is an MMP?")
    st.markdown("""
    **Mobile Measurement Partner (MMP)** is an independent platform for:
    - 📊 **Attribution** - assigning installs to the right campaigns
    - 🔍 **Cross-channel analytics** - unified view across all channels
    - 🛡️ **Fraud prevention** - detecting fraudulent installs
    - 🔗 **Deep linking** - advanced user navigation
    - 📡 **Postbacks** - automated communication with partners
    """)

with col2:
    st.markdown("#### What is SKAdNetwork?")
    st.markdown("""
    **SKAdNetwork (SKAN)** is Apple's privacy-focused attribution framework:
    - 🍎 **iOS 14.5+** - required for iOS attribution
    - 🔒 **Privacy-first** - no device-level tracking
    - 📊 **Conversion values** - measure post-install events
    - ⏱️ **Delayed reporting** - 24-72 hour attribution windows
    - 🎯 **Campaign optimization** - limited but valuable data

    **Note:** MMPs like AppsFlyer and Adjust help you set up and optimize SKAN campaigns.
    """)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "MMP Necessity Calculator | © 2025 | "
    "For guidance purposes only"
    "</div>",
    unsafe_allow_html=True
)
