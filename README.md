# 📱 Kalkulačka nutnosti MMP

Interaktivní webová aplikace pro mobilní marketéry, která pomáhá rozhodnout, zda potřebujete Mobile Measurement Partner (MMP) nástroj.

## 🚀 Instalace a spuštění

### 1. Nainstalujte závislosti

```bash
pip install -r requirements.txt
```

### 2. Spusťte aplikaci

```bash
streamlit run mmp_calculator.py
```

Aplikace se automaticky otevře v prohlížeči na adrese `http://localhost:8501`

## 📋 Funkce

- **Interaktivní vstupní parametry:**
  - Měsíční media budget (0-500 000 Kč)
  - Počet marketingových kanálů (1-10)
  - Podíl iOS uživatelů (0-100%)
  - Affiliate strategie (ano/ne)

- **Vizualizace:**
  - Interaktivní matice rozhodování s 4 kvadranty
  - Dynamické zobrazení vaší pozice
  - Barevné rozlišení kategorií

- **Doporučení:**
  - Personalizovaný verdikt na základě vašich parametrů
  - Upozornění na iOS specifika
  - Doporučení konkrétních nástrojů

## 🎯 Rozhodovací kategorie

1. **🟢 MMP NEPOTŘEBUJETE** - Nízký budget + 1 kanál
2. **🔵 TECHNICKÁ POTŘEBA** - Multi-channel nebo affiliate
3. **🟠 ŠEDÁ ZÓNA (RIZIKO)** - Vysoký budget + 1 kanál
4. **🔴 MMP JE NUTNOST** - Vysoký budget + multi-channel

## 🛠️ Technologie

- **Streamlit** - Framework pro webové aplikace
- **Plotly** - Interaktivní vizualizace
- **Python 3.8+**

## 📝 Licence

Tento nástroj slouží jako orientační pomůcka pro rozhodování v oblasti mobile marketingu.
