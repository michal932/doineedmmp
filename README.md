# 📱 Do I Need an MMP?

An interactive web application for mobile marketers to determine whether they need a Mobile Measurement Partner (MMP) tool and evaluate SKAdNetwork (SKAN) relevance.

**🌐 Live Demo:** [Coming soon - Deploy to Streamlit Cloud](https://share.streamlit.io)

## ✨ Features

### Dual Recommendation System

**📱 SKAdNetwork (SKAN) Evaluation**
- Smart iOS budget analysis
- Monetization model considerations
- App category and goal alignment
- Three-tier relevance scoring

**🔧 MMP Necessity Assessment**
- Budget and channel complexity analysis
- Interactive 4-quadrant decision matrix
- Risk assessment and recommendations
- Platform mix optimization

### Input Parameters

- **Budget:** Monthly media spend (EUR)
- **Channels:** Number of marketing channels (1-10)
- **iOS Share:** Percentage of iOS users (0-100%)
- **App Category:** Gaming, Finance, E-commerce, Education, Health & Fitness, Lifestyle, Utilities, Media
- **Monetization:** Subscription, Trial, In-app purchases, Hybrid, Ad-based
- **Primary Goal:** Install, Registration, Trial Start, Purchase, Retention
- **Affiliate/CPA:** Performance marketing partnerships

## 🚀 Quick Start

### Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501`

### Deploy to Web

**Option 1: Streamlit Community Cloud (Recommended - FREE)**

1. Fork this repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Click "New app"
5. Select: Repository → Branch: `main` → File: `app.py`
6. Deploy!

**Option 2: Heroku**

```bash
heroku create your-app-name
git push heroku main
```

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

## 📊 How It Works

### SKAN Relevance Levels

- **✅ SKAN makes sense** (iOS budget > €1,000/month)
  - Sufficient budget for optimization
  - Revenue tracking and conversion values
  - Campaign performance improvements

- **🟡 SKAN makes limited sense** (iOS budget €500-€1,000/month)
  - Basic SKAN setup possible
  - Focus on high-value events
  - Marginal ROI at this spend level

- **❌ SKAN doesn't make sense** (iOS budget < €500/month)
  - Budget too low for meaningful optimization
  - Setup complexity outweighs benefits
  - Focus on scaling first

### MMP Decision Categories

1. **🟢 You Don't Need an MMP**
   - Low budget + single channel
   - Use Firebase Analytics (free)

2. **🔵 Technical Need**
   - Multi-channel or affiliate marketing
   - Consider free tier MMP tools

3. **🟠 Gray Zone (Risk)**
   - High budget + single channel
   - Risk of vendor lock-in and ad fraud

4. **🔴 MMP is Necessary**
   - High budget + multi-channel
   - Professional measurement critical

## 🛠️ Technology Stack

- **Streamlit** - Web application framework
- **Plotly** - Interactive visualizations
- **Python 3.8+**
- **NumPy** - Numerical computations

## 📁 Project Structure

```
doineedmmp/
├── app.py              # Main application (English, EUR)
├── mmp_calculator.py   # Czech version (CZK)
├── requirements.txt    # Python dependencies
├── .streamlit/
│   └── config.toml    # Streamlit configuration
├── Procfile           # Heroku deployment
├── setup.sh           # Heroku setup script
└── docs/
    ├── DEPLOYMENT.md  # Deployment guide
    ├── QUICKSTART.md  # Quick start guide
    └── README_EN.md   # English documentation
```

## 🌍 Language Versions

- **English:** `app.py` (EUR currency)
- **Czech:** `mmp_calculator.py` (CZK currency)

## 📚 Documentation

- **[QUICKSTART.md](QUICKSTART.md)** - Deploy in 5 minutes
- **[DEPLOYMENT.md](DEPLOYMENT.md)** - Comprehensive deployment guide
- **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Project overview

## 🤝 Contributing

Issues and pull requests are welcome! Feel free to contribute improvements.

## 📄 License

This tool is provided for guidance purposes in mobile marketing decision-making.

## 🔗 Related Resources

- [AppsFlyer](https://www.appsflyer.com) - Leading MMP platform
- [Adjust](https://www.adjust.com) - Mobile measurement solution
- [Apple SKAdNetwork Documentation](https://developer.apple.com/documentation/storekit/skadnetwork)

---

**Made with ❤️ for mobile marketers**

**Questions?** Open an issue or contribute to the project!
