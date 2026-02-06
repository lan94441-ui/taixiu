import streamlit as st
import random
import time

st.set_page_config(page_title="Sunwin 3D - Nặn Bát", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: #ffd700; }
    /* Hiệu ứng đĩa và bát */
    .plate {
        background: radial-gradient(circle, #444, #000);
        border: 5px solid #ffd700; border-radius: 50%;
        width: 300px; height: 300px; margin: 0 auto;
        position: relative; display: flex; align-items: center; justify-content: center;
        overflow: hidden;
    }
    .bat-up {
        position: absolute; width: 100%; height: 100%;
        background: radial-gradient(circle, #666, #222); border-radius: 50%;
        border: 2px solid #888; z-index: 10;
        display: flex; align-items: center; justify-content: center;
        font-size: 100px; transition: 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    .dice-gif { width: 200px; }
    .dice-final { font-size: 80px; }
    div.stButton > button {
        border-radius: 12px; border: 2px solid #ffd700; background: #1a1a1a; color: gold; height: 60px; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

if 'so_du' not in st.session_state: st.session_state.so_du = 10000000
if 'trang_thai' not in st.session_state: st.session_state.trang_thai = "CUOC"
if 'cuoc' not in st.session_state: st.session_state.cuoc = 0

st.markdown("<h1 style='text-align: center; color: gold;'>🏆 CASINO 3D LUXURY 🏆</h1>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center; color: #00ff00;'>💰 {st.session_state.so_du:,} VND</h3>", unsafe_allow_html=True)

# 1. ĐẶT CƯỢC
if st.session_state.trang_thai == "CUOC":
    c1, c2, c3, c4 = st.columns(4)
    with c1: 
        if st.button("100K"): st.session_state.cuoc += 100000
    with c2: 
        if st.button("500K"): st.session_state.cuoc += 500000
    with c3: 
        if st.button("1M"): st.session_state.cuoc += 1000000
    with c4: 
        if st.button("XÓA"): st.session_state.cuoc = 0
    
    st.markdown(f"<h4 style='text-align:center;'>Đang đặt: {st.session_state.cuoc:,}</h4>", unsafe_allow_html=True)
    col_t, col_x = st.columns(2)
    with col_t:
        if st.button("🔴 TÀI", use_container_width=True):
            if 0 < st.session_state.cuoc <= st.session_state.so_du:
                st.session_state.chon = "Tài"; st.session_state.trang_thai = "XOC"; st.rerun()
    with col_x:
        if st.button("🔵 XỈU", use_container_width=True):
            if 0 < st.session_state.cuoc <= st.session_state.so_du:
                st.session_state.chon = "Xỉu"; st.session_state.trang_thai = "XOC"; st.rerun()

# 2. HIỆU ỨNG XÓC ĐĨA (DÙNG ẢNH ĐỘNG)
elif st.session_state.trang_thai == "XOC":
    st.markdown("<h2 style='text-align: center;'>🎲 ĐANG LẮC...</h2>", unsafe_allow_html=True)
    # Hiển thị ảnh xúc xắc đang quay (dùng emoji tạm thời kết hợp hiệu ứng CSS)
    st.markdown("""
        <div class="plate">
            <div style="font-size: 100px; animation: spin 0.2s infinite linear;">🎲</div>
        </div>
        <style> @keyframes spin { 100% { transform: rotate(360deg); } } </style>
    """, unsafe_allow_html=True)
    
    time.sleep(2) # Đợi 2 giây cho cảm giác xóc thật
    st.session_state.kq = [random.randint(1, 6) for _ in range(3)]
    st.session_state.trang_thai = "NAN"
    st.rerun()

# 3. NẶN BÁT
elif st.session_state.trang_thai == "NAN":
    st.markdown(f"<p style='text-align:center;'>Cược {st.session_state.chon}: {st.session_state.cuoc:,}</p>", unsafe_allow_html=True)
    
    # Bấm để nặn
    if 'mo' not in st.session_state: st.session_state.mo = 0
    
    offset = st.session_state.mo * -100
    icons = {1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"}
    d = st.session_state.kq
    
    st.markdown(f"""
        <div class="plate">
            <div class="dice-final">
                {icons[d[0]] if st.session_state.mo >= 1 else ""} 
                {icons[d[1]] if st.session_state.mo >= 2 else ""} 
                {icons[d[2]] if st.session_state.mo >= 3 else ""}
            </div>
            <div class="bat-up" style="transform: translateY({offset}px);">🥣</div>
        </div>
    """, unsafe_allow_html=True)

    if st.session_state.mo < 3:
        if st.button("👉 CHẠM ĐỂ NẶN BÁT 👈"):
            st.session_state.mo += 1
            st.rerun()
    else:
        if st.button("XEM KẾT QUẢ"):
            st.session_state.trang_thai = "KET_QUA"
            st.rerun()

# 4. KẾT QUẢ
elif st.session_state.trang_thai == "KET_QUA":
    d = st.session_state.kq
    tong = sum(d)
    kq_chu = "Xỉu" if 4 <= tong <= 10 else "Tài"
    if d[0] == d[1] == d[2]: kq_chu = "Bão"
    
    st.markdown(f"<h1 style='text-align: center;'>{tong} - {kq_chu.upper()}</h1>", unsafe_allow_html=True)
    
    if st.session_state.chon == kq_chu:
        st.balloons(); st.success(f"THẮNG! +{st.session_state.cuoc:,}")
        st.session_state.so_du += st.session_state.cuoc
    else:
        st.error(f"THUA! -{st.session_state.cuoc:,}")
        st.session_state.so_du -= st.session_state.cuoc

    if st.button("CHƠI TIẾP"):
        st.session_state.trang_thai = "CUOC"; st.session_state.mo = 0; st.session_state.cuoc = 0; st.rerun()
