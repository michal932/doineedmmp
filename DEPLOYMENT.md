# 🚀 Deployment Guide - MMP Necessity Calculator

This guide will help you deploy your MMP Calculator to the web so anyone can access it.

## 📌 Recommended: Streamlit Community Cloud (100% Free)

**Pros:** Free, automatic updates, easy setup, SSL included
**Hosting:** Streamlit's official platform

### Step-by-Step Instructions:

#### 1. Prepare Your GitHub Repository

```bash
# Initialize git repository (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - MMP Calculator"

# Create a new repository on GitHub (via web interface)
# Then push your code:
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
git branch -M main
git push -u origin main
```

#### 2. Deploy on Streamlit Cloud

1. Go to **[share.streamlit.io](https://share.streamlit.io)**
2. Click **"Sign in with GitHub"**
3. Click **"New app"**
4. Fill in the deployment form:
   - **Repository:** Select your repository
   - **Branch:** `main`
   - **Main file path:** `app.py`
5. Click **"Deploy!"**

**Done!** Your app will be live in 2-3 minutes at:
```
https://[your-app-name].streamlit.app
```

#### 3. Configure Custom Domain (Optional)

In your Streamlit Cloud dashboard:
- Go to App Settings → General
- Add your custom domain
- Update your DNS records as instructed

---

## 🌐 Alternative: Heroku

**Pros:** More control, custom domains easy
**Cost:** Free tier available (with limitations)

### Files Needed (Already Included):

1. **`requirements.txt`** - Python dependencies
2. **`Procfile`** - Tells Heroku how to run the app
3. **`setup.sh`** - Configuration script

### Create Missing Files:

```bash
# Create Procfile
echo "web: sh setup.sh && streamlit run app.py" > Procfile

# Create setup.sh
cat > setup.sh << 'EOF'
mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
[browser]\n\
gatherUsageStats = false\n\
" > ~/.streamlit/config.toml
EOF

chmod +x setup.sh
```

### Deploy to Heroku:

```bash
# Install Heroku CLI first: https://devcenter.heroku.com/articles/heroku-cli

# Login
heroku login

# Create app
heroku create your-mmp-calculator

# Push code
git push heroku main

# Open app
heroku open
```

---

## 🐳 Docker Deployment (Advanced)

For AWS, Google Cloud, Azure, or your own server.

### Create Dockerfile:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Build and Run:

```bash
# Build image
docker build -t mmp-calculator .

# Run locally
docker run -p 8501:8501 mmp-calculator

# Deploy to cloud (example for Google Cloud Run)
gcloud run deploy mmp-calculator --source . --platform managed --region us-central1 --allow-unauthenticated
```

---

## 🔧 Configuration for Production

### Update `app.py` for Production (Optional):

Add analytics, custom CSS, or meta tags:

```python
# Add at the top of app.py after imports
import streamlit as st

# Add custom CSS
st.markdown("""
    <style>
    /* Your custom CSS */
    </style>
""", unsafe_allow_html=True)

# Add Google Analytics (optional)
st.markdown("""
    <!-- Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=YOUR-GA-ID"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'YOUR-GA-ID');
    </script>
""", unsafe_allow_html=True)
```

---

## 📊 Post-Deployment Checklist

- [ ] App loads without errors
- [ ] All sliders and inputs work correctly
- [ ] Chart displays properly
- [ ] Recommendations update dynamically
- [ ] Mobile responsive (test on phone)
- [ ] Share link with colleagues for testing
- [ ] Set up custom domain (optional)
- [ ] Add Google Analytics (optional)
- [ ] Star the repository on GitHub 😊

---

## 🆘 Troubleshooting

### App won't deploy:
- Check `requirements.txt` has all dependencies
- Verify Python version compatibility (3.8+)
- Check Streamlit Cloud logs for errors

### Chart not displaying:
- Ensure Plotly is in `requirements.txt`
- Clear browser cache
- Check browser console for JavaScript errors

### Slow loading:
- Optimize imports (lazy loading)
- Reduce chart complexity
- Use Streamlit caching where applicable

---

## 🔄 Updating Your Deployed App

### Streamlit Cloud:
Simply push changes to GitHub:
```bash
git add .
git commit -m "Update feature"
git push origin main
```
Streamlit Cloud auto-deploys in ~2 minutes!

### Heroku:
```bash
git push heroku main
```

---

## 📞 Support

- **Streamlit Docs:** [docs.streamlit.io](https://docs.streamlit.io)
- **Community Forum:** [discuss.streamlit.io](https://discuss.streamlit.io)
- **Issues:** Open an issue on your GitHub repository

---

**Congratulations!** 🎉 Your MMP Calculator is now live and accessible to the world!
