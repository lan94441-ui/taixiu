import streamlit as st
import random
import time

st.set_page_config(page_title="Casino Úp Bát", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0b1016; color: white; }
    div.stButton > button {
        width: 100%; height: 80px; font-size: 25px; font-weight: bold; 
        border-radius: 20px; border: 2px solid #ffd700; background-color: #1a1c23; color: #ffd700;
    }
    .bat-up { 
        background-color: #3d3d3d; border: 5px solid #ffd700; border-radius: 50%; 
        width: 200px; height: 200px; margin: 0 auto; display: flex; 
        align-items: center; justify-content: center; font-size: 80px;
    }
    .stat-box { padding: 15px; border-radius: 15px; background: #161b22; text-align: center; border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

if 'so_du' not in st.session_state: st.session_state.so_du = 10000
if 'lich_su' not in st.session_state: st.session_state.lich_su = []
if 'dang_lac' not in st.session_state: st.session_state.dang_lac = False
if 'da_lac_xong' not in st.session_state: st.session_state.da_lac_xong = False
if 'ket_qua_tam' not in st.session_state: st.session_state.ket_qua_tam = None

st.markdown("<h1 style='text-align: center; color: #ffd700;'>🎲 CASINO ÚP BÁT 🎲</h1>", unsafe_allow_html=True)

# Thông tin tiền bạc
c1, c2 = st.columns(2)
with c1: st.markdown(f"<div class='stat-box'>💰 Tài khoản<br><span style='font-size: 20px;'>{st.session_state.so_du:,}$</span></div>", unsafe_allow_html=True)
with c2: st.markdown(f"<div class='stat-box'>📊 Số ván chơi<br><span style='font-size: 20px;'>{len(st.session_state.lich_su)}</span></div>", unsafe_allow_html=True)

# Khu vực đặt cược
if st.session_state.so_du < 100:
    st.warning("Bạn hết tiền rồi!")
    if st.button("🧧 Nhận 5000$ cứu trợ"):
        st.session_state.so_du += 5000
        st.rerun()
else:
    cuoc = st.number_input("💵 Tiền đặt cược:", min_value=100, step=500, value=1000)
    col1, col2 = st.columns(2)
    with col1: chon_tai = st.button("🔴 TÀI")
    with col2: chon_xiu = st.button("🔵 XỈU")

    # Xử lý Lắc
    if chon_tai or chon_xiu:
        st.session_state.lua_chon = "Tài" if chon_tai else "Xỉu"
        st.session_state.tien_cuoc = cuoc
        st.session_state.dang_lac = True
        st.session_state.da_lac_xong = False
        
    if st.session_state.dang_lac:
        with st.spinner('🎲 Đang xóc đĩa...'):
            time.sleep(1.5)
            dice = [random.randint(1, 6) for _ in range(3)]
            tong = sum(dice)
            kq = "Xỉu" if 4 <= tong <= 10 else "Tài"
            if dice[0] == dice[1] == dice[2]: kq = "Bão"
            st.session_state.ket_qua_tam = {"dice": dice, "tong": tong, "kq": kq}
            st.session_state.dang_lac = False
            st.session_state.da_lac_xong = True

    # Khu vực Bát Úp
    if st.session_state.da_lac_xong:
        st.markdown("<div class='bat-up'>🥣</div>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center;'><b>Bát đã úp! Đố bạn biết bên trong là gì?</b></p>", unsafe_allow_html=True)
        
        if st.button("✨ MỞ BÁT ✨"):
            res = st.session_state.ket_qua_tam
            st.session_state.lich_su.append(res['kq'][0])
            
            st.markdown(f"<h2 style='text-align:center;'>🎲 {res['dice'][0]} - {res['dice'][1]} - {res['dice'][2]}</h2>", unsafe_allow_html=True)
            st.markdown(f"<h1 style='text-align:center;'>{res['tong']} - {res['kq'].upper()}</h1>", unsafe_allow_html=True)
            
            if res['kq'] == "Bão":
                st.error(f"💀 Bão! Chia buồn -{st.session_state.tien_cuoc:,}$")
                st.session_state.so_du -= st.session_state.tien_cuoc
            elif st.session_state.lua_chon == res['kq']:
                st.balloons()
                st.success(f"🔥 QUÁ ĐỈNH! Bạn đã thắng +{st.session_state.tien_cuoc:,}$")
                st.session_state.so_du += st.session_state.tien_cuoc
            else:
                st.info(f"💸 Tiếc quá! Bạn mất -{st.session_state.tien_cuoc:,}$")
                st.session_state.so_du -= st.session_state.tien_cuoc
            
            st.session_state.da_lac_xong = False # Reset để chơi ván mới

# Lịch sử soi cầu
st.write("---")
cau_html = "".join([f'<span style="background-color:{"#ff4b4b" if x=="T" else "#3b82f6" if x=="X" else "#eab308"}; color:white; padding:8px 12px; border-radius:50%; margin:3px; display:inline-block; font-weight:bold;">{x}</span>' for x in st.session_state.lich_su[-20:]])
st.markdown(f"📊 **Soi cầu:** {cau_html}", unsafe_allow_html=True)
