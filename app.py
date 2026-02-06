import streamlit as st
import random
import time

# Cấu hình phong cách Casino Sunwin
st.set_page_config(page_title="Sunwin Tai Xiu Pro", layout="centered")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(180deg, #1a1a1a 0%, #000000 100%); color: gold; }
    div.stButton > button {
        border: 2px solid #ffd700; background: linear-gradient(to bottom, #444, #111);
        color: white; font-weight: bold; border-radius: 10px; height: 60px;
    }
    .bet-btn { background: linear-gradient(to bottom, #ff4b4b, #8b0000) !important; font-size: 25px !important; height: 100px !important; }
    .xiu-btn { background: linear-gradient(to bottom, #3b82f6, #00008b) !important; font-size: 25px !important; height: 100px !important; }
    .money-box { background: #222; border: 1px solid gold; border-radius: 10px; padding: 10px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

if 'so_du' not in st.session_state: st.session_state.so_du = 100000
if 'cuoc_hien_tai' not in st.session_state: st.session_state.cuoc_hien_tai = 0
if 'lich_su' not in st.session_state: st.session_state.lich_su = []

st.markdown("<h1 style='text-align: center; color: gold;'>🏆 SUNWIN TÀI XỈU MD5 🏆</h1>", unsafe_allow_html=True)

# Hiển thị số dư hiện có
st.markdown(f"<div class='money-box'>💰 SỐ DƯ: <span style='font-size: 25px; color: #00ff00;'>{st.session_state.so_du:,} VND</span></div>", unsafe_allow_html=True)

# Chọn nhanh mức cược như trong hình
st.write("---")
st.write("💵 Chọn mức cược:")
c1, c2, c3, c4, c5 = st.columns(5)
with c1: 
    if st.button("10K"): st.session_state.cuoc_hien_tai += 10000
with c2: 
    if st.button("50K"): st.session_state.cuoc_hien_tai += 50000
with c3: 
    if st.button("100K"): st.session_state.cuoc_hien_tai += 100000
with c4: 
    if st.button("500K"): st.session_state.cuoc_hien_tai += 500000
with c5: 
    if st.button("ALL-IN", type="primary"): st.session_state.cuoc_hien_tai = st.session_state.so_du

st.markdown(f"### Đang cược: <span style='color: yellow;'>{st.session_state.cuoc_hien_tai:,} VND</span>", unsafe_allow_html=True)
if st.button("Xóa cược"): st.session_state.cuoc_hien_tai = 0

# Hai nút đặt cửa khổng lồ
st.write("---")
col_tai, col_xiu = st.columns(2)
with col_tai:
    tai = st.button("🔴 TÀI", key="tai_btn", help="Đặt Tài", use_container_width=True)
with col_xiu:
    xiu = st.button("🔵 XỈU", key="xiu_btn", help="Đặt Xỉu", use_container_width=True)

if tai or xiu:
    if st.session_state.cuoc_hien_tai <= 0:
        st.error("⚠️ Vui lòng chọn tiền cược trước!")
    elif st.session_state.cuoc_hien_tai > st.session_state.so_du:
        st.error("⚠️ Bạn không đủ tiền!")
    else:
        chon = "Tài" if tai else "Xỉu"
        with st.spinner('🎲 Đang xóc...'):
            time.sleep(1.5)
        
        d = [random.randint(1, 6) for _ in range(3)]
        tong = sum(d)
        kq = "Xỉu" if 4 <= tong <= 10 else "Tài"
        if d[0] == d[1] == d[2]: kq = "Bão"
        
        st.session_state.lich_su.append(kq[0])
        
        st.markdown(f"<h2 style='text-align: center;'>🎲 {d[0]} - {d[1]} - {d[2]} ({tong})</h2>", unsafe_allow_html=True)
        
        if kq == "Bão":
            st.error(f"💀 BÃO! Nhà cái thu sạch {st.session_state.cuoc_hien_tai:,} VND")
            st.session_state.so_du -= st.session_state.cuoc_hien_tai
        elif chon == kq:
            st.balloons()
            st.success(f"🎊 THẮNG! +{st.session_state.cuoc_hien_tai:,} VND")
            st.session_state.so_du += st.session_state.cuoc_hien_tai
        else:
            st.error(f"💸 THUA! -{st.session_state.cuoc_hien_tai:,} VND")
            st.session_state.so_du -= st.session_state.cuoc_hien_tai
        
        st.session_state.cuoc_hien_tai = 0 # Reset tiền cược sau ván

# Soi cầu chuyên nghiệp
st.write("---")
st.write("📊 Lịch sử phiên:")
cau_html = "".join([f'<span style="background-color:{"#ff4b4b" if x=="T" else "#3b82f6" if x=="X" else "#eab308"}; color:white; padding:10px 14px; border-radius:50%; margin:4px; display:inline-block; font-weight:bold; border: 1px solid #fff;">{x}</span>' for x in st.session_state.lich_su[-15:]])
st.markdown(cau_html, unsafe_allow_html=True)
