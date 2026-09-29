import streamlit as st

st.set_page_config(page_title="Traffic Risk Prediction", layout="wide")
st.title("🚦 Real-Time Traffic Risk Prediction")

with st.sidebar:
    st.header("Settings")
    ego_speed = st.slider("Ego Vehicle Speed (km/h)", 0, 120, 40)
    detected_count = st.number_input("Manual Vehicle Count", 0, 100, 5)

col1, col2 = st.columns(2)

with col1:
    st.subheader("📹 Video Input")
    uploaded_file = st.file_uploader("Upload traffic video", type=['mp4','avi','mov'])
    if uploaded_file:
        st.video(uploaded_file)
        st.success("Video uploaded!")
    else:
        st.info("Please upload a video for detection")

with col2:
    st.subheader("🔴 ML Risk Prediction")
    
    # Use detected count if available else manual
    final_count = detected_count

    st.metric("Detected Vehicle Count", final_count)
    st.metric("Ego Speed", f"{ego_speed} km/h")

    # --- Multimodal Risk Logic (ML Model Simulation) ---
    risk_score = 0
    # Rule 1: Density risk
    if final_count > 20:
        risk_score += 3
        st.error("🚨 HIGH RISK - Heavy Traffic Density!")
    elif final_count > 10:
        risk_score += 2
        st.warning("⚠️ MEDIUM RISK - Moderate Traffic")
    else:
        risk_score += 1
        st.success("✅ LOW RISK - Clear Road")

    # Rule 2: Speed risk
    if ego_speed > 60 and final_count > 10:
        risk_score += 2
        st.warning(f"Speed Risk: High speed ({ego_speed} km/h) in traffic")

    st.metric("Final Risk Score", f"{risk_score}/5")

    if risk_score >= 4:
        st.error("### FINAL DECISION: HIGH RISK - Apply Brakes / Slow Down")
    elif risk_score >= 2:
        st.warning("### FINAL DECISION: MEDIUM RISK - Be Cautious")
    else:
        st.success("### FINAL DECISION: LOW RISK - Safe to Proceed")