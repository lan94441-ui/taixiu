import streamlit as st
import random
import time

st.set_page_config(page_title="Tài Xỉu lan94441", page_icon="🎲")
st.title("🎲 Game Tài Xỉu Online")

if 'so_du' not in st.session_state:
    st.session_state.so_du = 1000
if 'lich_su' not in st.session_state:
    st.session_state.lich_su = []

st.sidebar.subheader(f"💰 Số dư: {st.session_state.so_du}$")

cuoc = st.number_input("Tiền cược:", min_value=10, max_value=st.session_state.so_du, value=10)
chon = st.radio("Chọn cửa:", ["Tài", "Xỉu"])

if st.button("🎰 LẮC XÚC XẮC"):
    with st.spinner('Đang lắc...'):
        time.sleep(1)
    xuc_xac = [random.randint(1, 6) for _ in range(3)]
    tong = sum(xuc_xac)
    is_bao = (xuc_xac[0] == xuc_xac[1] == xuc_xac[2])
    
    if is_bao:
        kq = "Bão"; st.session_state.lich_su.append("B")
    elif 4 <= tong <= 10:
        kq = "Xỉu"; st.session_state.lich_su.append("X")
    else:
        kq = "Tài"; st.session_state.lich_su.append("T")
        
    st.subheader(f"Kết quả: {xuc_xac[0]}-{xuc_xac[1]}-{xuc_xac[2]} ({kq})")
    
    if is_bao:
        st.error("💀 BÃO! Nhà cái ăn hết."); st.session_state.so_du -= cuoc
    elif (chon == kq):
        st.success(f"🎉 Thắng! +{cuoc}$"); st.session_state.so_du += cuoc
    else:
        st.error(f"💸 Thua! -{cuoc}$"); st.session_state.so_du -= cuoc

st.divider()
st.write(f"📊 Lịch sử: {' - '.join(st.session_state.lich_su[-10:])}")
