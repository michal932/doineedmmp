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

# Input 3: Affiliate strategy
uses_affiliate = st.sidebar.checkbox(
    "I use Affiliate partners / Performance-based Influencers (CPA)",
    help="Affiliate marketing requires MMP for postback automation"
)

# ============================================================================
# MMP NECESSITY EVALUATION
# ============================================================================

# Logic: Determine budget threshold
budget_threshold = 2000  # Default threshold (€2,000 EUR ~ 50,000 CZK)
effective_budget_threshold = budget_threshold

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
# Bottom: Green - "YOU DON'T NEED AN MMP" (full width)
fig.add_shape(
    type="rect",
    x0=0, y0=0,
    x1=20000, y1=y_threshold,
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
        x=10000, y=y_threshold / 2,
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
        title="<b>Number of Marketing Channels</b>",
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
if is_high_complexity and is_high_budget:
    category = "MMP IS NECESSARY"
    color = "red"
    icon = "🔴"
elif is_high_complexity and not is_high_budget:
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
        "**Why MMP makes sense in 2025:**\n"
        "- **Cross-channel deduplication:** Essential when users see ads on multiple channels before installing\n"
        "- **Centralized reporting:** Single source of truth for attribution across all campaigns\n"
        "- **Programmatic network support:** Critical for AppLovin, Unity Ads, and similar networks\n"
        "- **Reduced engineering burden:** Avoid costly custom development and ongoing maintenance"
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

# Display recommendation
for part in recommendation_parts:
    st.markdown(part)
    st.markdown("")

# Additional info section
st.markdown("---")
st.markdown("### 📚 What is an MMP?")
st.markdown("""
**Mobile Measurement Partner (MMP)** is an independent platform for:
- 📊 **Attribution** - assigning installs to the right campaigns
- 🔍 **Cross-channel analytics** - unified view across all channels
- 🛡️ **Fraud prevention** - detecting fraudulent installs
- 🔗 **Deep linking** - advanced user navigation
- 📡 **Postbacks** - automated communication with partners
""")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "MMP Necessity Calculator | "
    "For guidance purposes only"
    "</div>",
    unsafe_allow_html=True
)
