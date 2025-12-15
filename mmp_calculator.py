"""
MMP Necessity Calculator (Kalkulačka nutnosti MMP)
Interactive Streamlit application for mobile app marketers
"""

import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Kalkulačka nutnosti MMP",
    page_icon="📱",
    layout="wide"
)

# Title
st.title("📱 Kalkulačka nutnosti MMP")
st.markdown("*Potřebuje vaše aplikace Mobile Measurement Partner?*")

# Sidebar with input controls
st.sidebar.header("⚙️ Nastavení parametrů")

# Input 1: Monthly Budget
monthly_budget = st.sidebar.slider(
    "Měsíční Media Budget (CZK):",
    min_value=0,
    max_value=500000,
    value=50000,
    step=5000,
    format="%d Kč"
)

# Input 2: Number of channels
num_channels = st.sidebar.slider(
    "Počet marketingových kanálů:",
    min_value=1,
    max_value=10,
    value=1,
    step=1
)

# Input 3: iOS share
ios_share = st.sidebar.slider(
    "Podíl iOS uživatelů (%):",
    min_value=0,
    max_value=100,
    value=30,
    step=5,
    format="%d%%"
)

# Input 4: Affiliate strategy
uses_affiliate = st.sidebar.checkbox(
    "Využívám Affiliate partnery / Influencery na výkon (CPA)"
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Aktuální hodnoty")
st.sidebar.metric("Budget", f"{monthly_budget:,} Kč".replace(",", " "))
st.sidebar.metric("Kanály", num_channels)
st.sidebar.metric("iOS podíl", f"{ios_share}%")
st.sidebar.metric("Affiliate", "Ano" if uses_affiliate else "Ne")

# Logic: Determine budget threshold based on iOS share
budget_threshold = 50000  # Default threshold
effective_budget_threshold = budget_threshold

if ios_share > 50:
    effective_budget_threshold = 20000  # Lower threshold for iOS-heavy apps

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
# Bottom-Left: Green - "MMP NEPOTŘEBUJETE"
fig.add_shape(
    type="rect",
    x0=0, y0=0,
    x1=x_threshold, y1=y_threshold,
    fillcolor="rgba(76, 175, 80, 0.3)",  # Green
    line=dict(width=0),
    layer="below"
)

# Top-Left: Blue - "TECHNICKÁ POTŘEBA"
fig.add_shape(
    type="rect",
    x0=0, y0=y_threshold,
    x1=x_threshold, y1=10,
    fillcolor="rgba(33, 150, 243, 0.3)",  # Blue
    line=dict(width=0),
    layer="below"
)

# Bottom-Right: Yellow/Orange - "ŠEDÁ ZÓNA (RIZIKO)"
fig.add_shape(
    type="rect",
    x0=x_threshold, y0=0,
    x1=500000, y1=y_threshold,
    fillcolor="rgba(255, 193, 7, 0.3)",  # Yellow/Orange
    line=dict(width=0),
    layer="below"
)

# Top-Right: Red - "MMP JE NUTNOST"
fig.add_shape(
    type="rect",
    x0=x_threshold, y0=y_threshold,
    x1=500000, y1=10,
    fillcolor="rgba(244, 67, 54, 0.3)",  # Red
    line=dict(width=0),
    layer="below"
)

# Add quadrant labels
annotations = [
    dict(
        x=x_threshold / 2, y=y_threshold / 2,
        text="<b>MMP<br>NEPOTŘEBUJETE</b>",
        showarrow=False,
        font=dict(size=14, color="darkgreen"),
        bgcolor="rgba(255, 255, 255, 0.7)",
        borderpad=10
    ),
    dict(
        x=x_threshold / 2, y=(y_threshold + 10) / 2,
        text="<b>TECHNICKÁ<br>POTŘEBA</b>",
        showarrow=False,
        font=dict(size=14, color="darkblue"),
        bgcolor="rgba(255, 255, 255, 0.7)",
        borderpad=10
    ),
    dict(
        x=(x_threshold + 500000) / 2, y=y_threshold / 2,
        text="<b>ŠEDÁ ZÓNA<br>(RIZIKO)</b>",
        showarrow=False,
        font=dict(size=14, color="darkorange"),
        bgcolor="rgba(255, 255, 255, 0.7)",
        borderpad=10
    ),
    dict(
        x=(x_threshold + 500000) / 2, y=(y_threshold + 10) / 2,
        text="<b>MMP JE<br>NUTNOST</b>",
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
    x1=500000, y1=y_threshold,
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
        text=['VAŠE APLIKACE'],
        textposition='top center',
        textfont=dict(size=12, color='darkblue', family='Arial Black'),
        name='Vaše pozice',
        hovertemplate=(
            '<b>Vaše aplikace</b><br>' +
            'Budget: %{x:,} Kč<br>' +
            'Kanály: ' + str(num_channels) + '<br>' +
            '<extra></extra>'
        )
    )
)

# Update layout
fig.update_layout(
    title=dict(
        text="<b>Matice rozhodování: Potřebujete MMP?</b>",
        x=0.5,
        xanchor='center',
        font=dict(size=20)
    ),
    xaxis=dict(
        title="<b>Měsíční Media Budget (CZK)</b>",
        range=[0, 500000],
        gridcolor='lightgray',
        tickformat=',',
        ticksuffix=' Kč'
    ),
    yaxis=dict(
        title="<b>Komplexita kanálů</b>",
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
st.header("💡 Verdikt pro vaši aplikaci")

# Determine the recommendation category
if is_high_budget and is_high_complexity:
    category = "MMP JE NUTNOST"
    color = "red"
    icon = "🔴"
elif is_high_budget and not is_high_complexity:
    category = "ŠEDÁ ZÓNA (RIZIKO)"
    color = "orange"
    icon = "🟠"
elif not is_high_budget and is_high_complexity:
    category = "TECHNICKÁ POTŘEBA"
    color = "blue"
    icon = "🔵"
else:
    category = "MMP NEPOTŘEBUJETE"
    color = "green"
    icon = "🟢"

st.markdown(f"### {icon} **{category}**")

# Generate detailed recommendation text
recommendation_parts = []

# Main assessment
if category == "MMP JE NUTNOST":
    recommendation_parts.append(
        f"S měsíčním budgetem **{monthly_budget:,} Kč** a **{num_channels} "
        f"marketingovými kanály** jednoznačně potřebujete MMP řešení."
    )
    recommendation_parts.append(
        "**Proč?** Při tomto objemu investic a komplexitě kanálů je profesionální "
        "měření a atribuce kritické pro optimalizaci výkonnosti a prevenci podvodů."
    )

elif category == "ŠEDÁ ZÓNA (RIZIKO)":
    recommendation_parts.append(
        f"Váš budget **{monthly_budget:,} Kč** je dostatečně vysoký na to, aby "
        "ospravedlnil investici do MMP, ale zatím pracujete pouze s **jedním kanálem**."
    )
    recommendation_parts.append(
        "**⚠️ Rizika bez MMP:**\n"
        "- **Vendor lock-in:** Závislost na reportingu jediného reklamního kanálu\n"
        "- **Ad fraud:** Vyšší riziko podvodných instalací bez nezávislého ověření\n"
        "- **Škálovatelnost:** Když přidáte další kanály, budete litovat, že jste nezačali dříve"
    )
    recommendation_parts.append(
        "**Doporučení:** Zvažte MMP pro ochranu investice a přípravu na růst."
    )

elif category == "TECHNICKÁ POTŘEBA":
    recommendation_parts.append(
        f"Pracujete s **{num_channels} marketingovými kanály**"
        + (" a využíváte **affiliate partnery**" if uses_affiliate else "")
        + f", ale váš budget je zatím na úrovni **{monthly_budget:,} Kč**."
    )

    if uses_affiliate:
        recommendation_parts.append(
            "**🔴 Affiliate/Influencer marketing vyžaduje MMP!**\n"
            "Pro výkonové kampaně (CPA) potřebujete posílat postbacky partnerům. "
            "Bez MMP nemáte jak automatizovat komunikaci konverzí."
        )

    recommendation_parts.append(
        "**Technická nutnost:** Multi-channel měření vyžaduje centralizované řešení. "
        "Zvažte **free tier** MMP nástrojů (např. AppsFlyer, Adjust) nebo "
        "levnější alternativy pro malé projekty."
    )

else:  # MMP NEPOTŘEBUJETE
    recommendation_parts.append(
        f"S budgetem **{monthly_budget:,} Kč** a **jediným marketingovým kanálem** "
        "zatím nepotřebujete dedikované MMP řešení."
    )
    recommendation_parts.append(
        "**Doporučení:**\n"
        "- Využijte **Firebase Analytics** nebo **Google Analytics for Firebase** (zdarma)\n"
        "- Spoléhejte na reporting přímo z reklamního kanálu\n"
        "- Sledujte situaci: jakmile přidáte druhý kanál nebo zvýšíte budget, MMP začne dávat smysl"
    )

# iOS-specific warning
if ios_share > 50:
    recommendation_parts.append(
        f"**📱 iOSvarování:** Více než **{ios_share}% vašich uživatelů** je na iOS. "
        "Kvůli **SKAdNetwork** a iOS 14.5+ ATT je měření na iOS extrémně složité. "
        "I při nižším budgetu MMP pomůže zpracovat a normalizovat SKAdNetwork data."
    )

    if monthly_budget >= 20000 and monthly_budget < 50000:
        recommendation_parts.append(
            "⚠️ **Prahová hodnota upravena:** Díky vysokému podílu iOS je doporučená "
            "hranice pro MMP snížena z 50 000 Kč na **20 000 Kč měsíčně**."
        )

# Display recommendation
for part in recommendation_parts:
    st.markdown(part)
    st.markdown("")

# Additional info section
st.markdown("---")
st.markdown("### 📚 Co je MMP?")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **Mobile Measurement Partner (MMP)** je nezávislá platforma pro:
    - 📊 **Atribuci** - přiřazení instalací ke správným kampaním
    - 🔍 **Cross-channel analytics** - jednotný pohled na všechny kanály
    - 🛡️ **Fraud prevention** - detekce podvodných instalací
    - 🔗 **Deep linking** - pokročilá uživatelská navigace
    - 📡 **Postbacky** - automatizace komunikace s partnery
    """)

with col2:
    st.markdown("""
    **Nejznámější MMP nástroje:**
    - AppsFlyer
    - Adjust
    - Branch
    - Singular
    - Kochava

    Většina nabízí **free tier** pro malé projekty.
    """)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "Kalkulačka nutnosti MMP | © 2025 | "
    "Slouží pouze jako orientační nástroj pro rozhodování"
    "</div>",
    unsafe_allow_html=True
)
