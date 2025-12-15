# ⚡ Quick Start Guide - Deploy in 5 Minutes

## 🎯 Goal
Get your MMP Calculator live on the internet in under 5 minutes (for free!)

## 📦 What You Have

Your project contains:
- ✅ **`app.py`** - English version of the calculator
- ✅ **`mmp_calculator.py`** - Czech version (original)
- ✅ **`requirements.txt`** - All dependencies
- ✅ **`.streamlit/config.toml`** - Streamlit configuration
- ✅ **Deployment files** - Ready for Heroku, Docker, etc.

## 🚀 Fastest Deployment Method

### Streamlit Community Cloud (FREE)

**Step 1:** Create GitHub Repository
```bash
# In your terminal, from the project folder:
git init
git add .
git commit -m "MMP Calculator ready for deployment"
```

**Step 2:** Push to GitHub
- Go to [github.com](https://github.com) and create a new repository
- Follow GitHub's instructions to push your code:
```bash
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
git branch -M main
git push -u origin main
```

**Step 3:** Deploy on Streamlit
1. Visit **[share.streamlit.io](https://share.streamlit.io)**
2. Click "Sign in with GitHub"
3. Click "New app"
4. Select:
   - Repository: `YOUR-USERNAME/YOUR-REPO-NAME`
   - Branch: `main`
   - Main file: `app.py`
5. Click "Deploy!"

**Done!** 🎉 Your app will be live at: `https://[app-name].streamlit.app`

---

## 🧪 Test Locally First

```bash
# Run the English version
streamlit run app.py

# Or run the Czech version
streamlit run mmp_calculator.py
```

Open browser at `http://localhost:8501`

---

## 📝 Customization Tips

### Change Currency or Budget Range

Edit `app.py` around lines 25-31:

```python
# Change max budget from $20,000 to $50,000
monthly_budget = st.sidebar.slider(
    "Monthly Media Budget ($):",
    min_value=0,
    max_value=50000,  # Changed from 20000
    value=5000,
    step=500,
    format="$%d"
)
```

### Change Threshold Values

Edit `app.py` around lines 68-73:

```python
# Default threshold (when iOS < 50%)
budget_threshold = 2000  # Change this value

# iOS-heavy threshold (when iOS > 50%)
if ios_share > 50:
    effective_budget_threshold = 800  # Change this value
```

### Add Your Branding

Edit `app.py` footer section (lines 370-377):

```python
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "MMP Calculator by YourCompany | © 2025"
    "</div>",
    unsafe_allow_html=True
)
```

---

## 🔗 Share Your App

Once deployed, share your link:
```
https://your-app-name.streamlit.app
```

Add it to:
- Your website
- Blog posts
- Social media
- Email signature
- LinkedIn profile

---

## 💡 Pro Tips

1. **Custom Domain:**
   - Streamlit Cloud supports custom domains in settings
   - Example: `calculator.yourdomain.com`

2. **Auto-Updates:**
   - Push changes to GitHub → App updates automatically
   - No manual redeployment needed!

3. **Analytics:**
   - Add Google Analytics code to track visitors
   - See DEPLOYMENT.md for instructions

4. **Mobile Friendly:**
   - App is already responsive
   - Test on phone after deployment

---

## 🆘 Need Help?

1. **App not loading?**
   - Check GitHub repository is public
   - Verify all files are committed
   - Check Streamlit Cloud logs

2. **Chart issues?**
   - Clear browser cache
   - Try different browser
   - Check requirements.txt includes plotly

3. **Want custom features?**
   - See DEPLOYMENT.md for advanced options
   - Edit app.py to customize logic

---

**Ready to deploy?** 🚀 Follow the 3 steps above and you'll be live in minutes!
