import streamlit as st  

# Streamlit App Configuration  
st.set_page_config(page_title="Ultimate Unit Converter", page_icon="📏", layout="centered")  

# Custom Styling for Professional UI  
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(135deg, #f3f4f6, #e3e4e8);
            font-family: 'Arial', sans-serif;
        }
        .main {
            text-align: center;
        }
        .title {
            font-size: 36px;
            font-weight: bold;
            color: #1a1a2e;
        }
        .subheader {
            font-size: 20px;
            color: #333;
            margin-bottom: 20px;
        }
        .input-box {
            background: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            width: 60%;
            margin: auto;
        }
        .stButton>button {
            background: linear-gradient(135deg, #6a11cb, #2575fc);
            color: white;
            font-size: 18px;
            padding: 12px;
            border-radius: 8px;
            border: none;
            transition: 0.3s;
        }
        .stButton>button:hover {
            transform: scale(1.05);
            background: linear-gradient(135deg, #2575fc, #6a11cb);
        }
    </style>
    """, 
    unsafe_allow_html=True
)

# Title and Description  
st.markdown("<div class='title'>📏 Ultimate Unit Converter</div>", unsafe_allow_html=True)  
st.markdown("<div class='subheader'>A Professional & Stylish Unit Conversion Tool</div>", unsafe_allow_html=True)  

# Card-Style Input Box  
# st.markdown("<div class='input-box'>", unsafe_allow_html=True)

# Input Field  
meters = st.number_input("Enter value in meters:", min_value=0.0, format="%.2f")  

# Conversion Selection  
conversion_type = st.selectbox("Convert to:", ["Centimeters", "Kilometers", "Inches", "Feet", "Yards", "Miles"])

# Conversion Logic  
conversion_factors = {
    "Centimeters": 100,
    "Kilometers": 0.001,
    "Inches": 39.3701,
    "Feet": 3.28084,
    "Yards": 1.09361,
    "Miles": 0.000621371
}
result = meters * conversion_factors[conversion_type]

st.markdown("</div>", unsafe_allow_html=True)  # Closing input box

# Convert Button  
if st.button("🚀 Convert Now"):  
    st.success(f"✅ {meters} meters is *{result:.2f} {conversion_type.lower()}*")