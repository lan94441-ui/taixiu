import streamlit as st
import random
import time

st.set_page_config(page_title="Tự Tay Mở Bát", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    div.stButton > button {
        width: 100%; height: 80px; font-size: 25px; font-weight: bold; 
        border-radius: 20px; border: 2px solid #ffd700; background-color: #1a1c23; color: #ffd700;
    }
    .bat-container {
        text-align: center; padding: 20px; background: #1f2937; border-radius: 20px; border: 2px solid #374151;
    }
    .status-text { font-size: 20px; color: #ffd700; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

if 'so_du' not in st.session_state: st.session_state.so_du = 10000
if 'lich_su' not in st.session_state: st.session_state.lich_su = []
if 'trang_thai' not in st.session_state: st.session_state.trang_thai = "DANG_CUOC" # DANG_CUOC, DA_UP_BAT, DA_MO
if 'kq_phien' not in st.session_state: st.session_state.kq_phien = {}

st.markdown("<h1 style='text-align: center; color: #ffd700;'>🥣 TỰ TAY MỞ BÁT 🎲</h1>", unsafe_allow_html=True)
st.subheader(f"💰 Vốn: {st.session_state.so_du:,}$")

# 1. GIAI ĐOẠN ĐẶT CƯỢC
if st.session_state.trang_thai == "DANG_CUOC":
    cuoc = st.number_input("💵 Tiền cược:", min_value=100, step=500, value=1000)
    col1, col2 = st.columns(2)
    with col1: tai = st.button("🔴 TÀI")
    with col2: xiu = st.button("🔵 XỈU")

    if tai or xiu:
        st.session_state.lua_chon = "Tài" if tai else "Xỉu"
        st.session_state.tien_cuoc = cuoc
        # Lắc xúc xắc ngầm
        dice = [random.randint(1, 6) for _ in range(3)]
        tong = sum(dice)
        kq = "Xỉu" if 4 <= tong <= 10 else "Tài"
        if dice[0] == dice[1] == dice[2]: kq = "Bão"
        st.session_state.kq_phien = {"dice": dice, "tong": tong, "kq": kq}
        
        with st.spinner('🎲 Đang xóc đĩa...'):
            time.sleep(1)
        st.session_state.trang_thai = "DA_UP_BAT"
        st.rerun()

# 2. GIAI ĐOẠN TỰ TAY MỞ BÁT
elif st.session_state.trang_thai == "DA_UP_BAT":
    st.markdown("<div class='bat-container'>", unsafe_allow_html=True)
    st.markdown(f"### Bạn cược: {st.session_state.lua_chon} - {st.session_state.tien_cuoc:,}$")
    st.markdown("<h1 style='font-size: 100px;'>🥣</h1>", unsafe_allow_html=True)
    st.markdown("<p class='status-text'>👇 KÉO THANH NÀY SANG PHẢI ĐỂ MỞ BÁT 👇</p>", unsafe_allow_html=True)
    
    # Thanh trượt mô phỏng việc dùng tay kéo bát
    mo_bat = st.slider("", 0, 100, 0)
    
    if mo_bat > 90: # Khi kéo đến gần hết thanh
        st.session_state.trang_thai = "DA_MO"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# 3. GIAI ĐOẠN KẾT QUẢ
elif st.session_state.trang_thai == "DA_MO":
    res = st.session_state.kq_phien
    st.session_state.lich_su.append(res['kq'][0])
    
    st.markdown(f"<h2 style='text-align:center;'>🎲 {res['dice'][0]} - {res['dice'][1]} - {res['dice'][2]}</h2>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align:center;'>{res['tong']} - {res['kq'].upper()}</h1>", unsafe_allow_html=True)
    
    if st.session_state.lua_chon == res['kq']:
        st.balloons()
        st.success(f"🔥 THẮNG! +{st.session_state.tien_cuoc:,}$")
        st.session_state.so_du += st.session_state.tien_cuoc
    else:
        st.error(f"💸 THUA! -{st.session_state.tien_cuoc:,}$")
        st.session_state.so_du -= st.session_state.tien_cuoc
        
    if st.button("CHƠI VÁN MỚI"):
        st.session_state.trang_thai = "DANG_CUOC"
        st.rerun()

# Soi cầu
st.write("---")
cau_html = "".join([f'<span style="background-color:{"#ff4b4b" if x=="T" else "#3b82f6" if x=="X" else "#eab308"}; color:white; padding:8px 12px; border-radius:50%; margin:3px; display:inline-block; font-weight:bold;">{x}</span>' for x in st.session_state.lich_su[-20:]])
st.markdown(f"📊 **Cầu đang chạy:** {cau_html}", unsafe_allow_html=True)
