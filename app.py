import streamlit as st
import random
import time

st.set_page_config(page_title="Casino Pro", layout="centered")

# CSS làm nút bấm to và đẹp
st.markdown("""
    <style>
    div.stButton > button {
        width: 100%; height: 100px; font-size: 30px; font-weight: bold; border-radius: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

if 'so_du' not in st.session_state:
    st.session_state.so_du = 10000
if 'lich_su' not in st.session_state:
    st.session_state.lich_su = []

st.title("🎲 CASINO TÀI XỈU PRO")
st.subheader(f"💰 Số dư: {st.session_state.so_du:,}$")

cuoc = st.number_input("💵 Tiền cược:", min_value=10, step=100, value=500)

col1, col2 = st.columns(2)
with col1:
    tai = st.button("🔴 TÀI")
with col2:
    xiu = st.button("🔵 XỈU")

if tai or xiu:
    chon = "Tài" if tai else "Xỉu"
    if st.session_state.so_du < cuoc:
        st.error("❌ Hết tiền rồi!")
    else:
        with st.spinner('🎲 Đang lắc...'):
            time.sleep(1)
        dice = [random.randint(1, 6) for _ in range(3)]
        tong = sum(dice)
        kq = "Xỉu" if 4 <= tong <= 10 else "Tài"
        if dice[0] == dice[1] == dice[2]: kq = "Bão"
        
        st.session_state.lich_su.append(kq[0])
        st.header(f"Kết quả: {dice[0]}-{dice[1]}-{dice[2]} ({kq})")
        
        if kq == "Bão":
            st.warning("💀 Bão! Nhà cái hốt hết."); st.session_state.so_du -= cuoc
        elif chon == kq:
            st.success(f"🔥 THẮNG! +{cuoc}$"); st.session_state.so_du += cuoc
        else:
            st.error(f"💸 THUA! -{cuoc}$"); st.session_state.so_du -= cuoc

st.write("---")
st.subheader("📊 Lịch sử soi cầu:")
cau = "".join([f'<span style="background-color:{"red" if x=="T" else "blue" if x=="X" else "yellow"}; color:white; padding:8px 12px; border-radius:50%; margin:3px; font-weight:bold;">{x}</span>' for x in st.session_state.lich_su[-15:]])
st.markdown(cau, unsafe_allow_html=True)
