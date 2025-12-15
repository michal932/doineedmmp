# 📱 Do I Need an MMP?

An interactive web application for mobile marketers to determine whether they need a Mobile Measurement Partner (MMP) tool.

## 🚀 Quick Start

### Local Installation

1. **Install dependencies:**

```bash
pip install -r requirements.txt
```

2. **Run the app:**

```bash
streamlit run app.py
```

The app will automatically open in your browser at `http://localhost:8501`

## 🌐 Deploy to the Web

### Option 1: Streamlit Community Cloud (Free & Easy)

1. **Push to GitHub:**
   - Create a new GitHub repository
   - Push this project to your repository

2. **Deploy on Streamlit Cloud:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository, branch, and main file (`app.py`)
   - Click "Deploy"

Your app will be live at `https://[your-app-name].streamlit.app` in minutes!

### Option 2: Other Hosting Platforms

- **Heroku:** Use the included `Procfile` and `setup.sh`
- **AWS/Azure/GCP:** Deploy as a containerized app
- **Railway:** Connect your GitHub repo and deploy

## 📋 Features

- **Interactive Input Parameters:**
  - Monthly media budget ($0-$20,000)
  - Number of marketing channels (1-10)
  - iOS user share percentage (0-100%)
  - Affiliate strategy (yes/no)

- **Visual Decision Matrix:**
  - Interactive 4-quadrant matrix with Plotly
  - Dynamic positioning of your app
  - Color-coded categories

- **Smart Recommendations:**
  - Personalized verdict based on your inputs
  - iOS-specific warnings for SKAdNetwork complexity
  - Budget threshold adjustments
  - Tool recommendations

## 🎯 Decision Categories

1. **🟢 YOU DON'T NEED AN MMP** - Low budget + single channel
2. **🔵 TECHNICAL NEED** - Multi-channel or affiliate marketing
3. **🟠 GRAY ZONE (RISK)** - High budget + single channel
4. **🔴 MMP IS NECESSARY** - High budget + multi-channel

## 🛠️ Technology Stack

- **Streamlit** - Web app framework
- **Plotly** - Interactive visualizations
- **Python 3.8+**

## 📁 Project Structure

```
doineedmmp/
├── app.py              # Main application (English)
├── mmp_calculator.py   # Czech version
├── requirements.txt    # Python dependencies
├── .streamlit/
│   └── config.toml    # Streamlit configuration
├── README.md          # Czech documentation
└── README_EN.md       # This file
```

## 🔧 Configuration

The app uses USD by default. To customize:
- Edit budget ranges in `app.py` (lines 25-31)
- Adjust threshold values (lines 68-73)
- Modify quadrant boundaries (lines 84-127)

## 📝 License

This tool is provided for guidance purposes in mobile marketing decision-making.

## 🤝 Contributing

Feel free to submit issues or pull requests to improve the calculator!

## 🌍 Versions

- **English:** `app.py`
- **Czech (Čeština):** `mmp_calculator.py`
