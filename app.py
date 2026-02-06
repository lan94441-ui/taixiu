import streamlit as st
import random
import time

# Cấu hình phong cách Casino Sunwin Thượng Lưu
st.set_page_config(page_title="Sunwin 10 Triệu - Nặn Bát", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: #ffd700; }
    .dice-plate {
        background: radial-gradient(circle, #444, #000);
        border: 5px solid #ffd700; border-radius: 50%;
        width: 300px; height: 300px; margin: 0 auto;
        position: relative; display: flex; align-items: center; justify-content: center;
        box-shadow: 0 0 30px rgba(255, 215, 0, 0.3);
    }
    .bat-up {
        position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background: linear-gradient(145deg, #666, #333); border-radius: 50%; border: 3px solid #888;
        display: flex; align-items: center; justify-content: center;
        font-size: 150px; cursor: pointer; transition: 0.6s ease-out; z-index: 10;
    }
    .dice-img { font-size: 70px; margin: 5px; filter: drop-shadow(0 0 10px gold); }
    div.stButton > button {
        width: 100%; height: 65px; font-weight: bold; border-radius: 12px; 
        border: 2px solid #ffd700; background: #1a1a1a; color: gold;
    }
    .money-display { 
        text-align: center; background: #161b22; border: 1px solid #30363d;
        padding: 10px; border-radius: 15px; color: #00ff00; font-size: 28px; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Khởi tạo vốn 10 TRIỆU VND
if 'so_du' not in st.session_state: st.session_state.so_du = 10000000
if 'cuoc' not in st.session_state: st.session_state.cuoc = 0
if 'trang_thai' not in st.session_state: st.session_state.trang_thai = "DAT_CUOC"
if 'step_nan' not in st.session_state: st.session_state.step_nan = 0 

def get_dice_icon(n):
    icons = {1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"}
    return icons.get(n, "❓")

st.markdown("<h1 style='text-align: center; color: gold;'>🏆 SUNWIN 10 TRIỆU 🏆</h1>", unsafe_allow_html=True)

# 1. MÀN HÌNH ĐẶT CƯỢC
if st.session_state.trang_thai == "DAT_CUOC":
    st.markdown(f"<div class='money-display'>💰 SỐ DƯ: {st.session_state.so_du:,} VND</div>", unsafe_allow_html=True)
    
    st.write("")
    c1, c2, c3, c4 = st.columns(4)
    with c1: 
        if st.button("100K"): st.session_state.cuoc += 100000
    with c2: 
        if st.button("500K"): st.session_state.cuoc += 500000
    with c3: 
        if st.button("1M"): st.session_state.cuoc += 1000000
    with c4: 
        if st.button("XÓA"): st.session_state.cuoc = 0

    st.markdown(f"<h3 style='text-align: center;'>Đang cược: <span style='color:white;'>{st.session_state.cuoc:,}</span></h3>", unsafe_allow_html=True)
    
    col_t, col_x = st.columns(2)
    with col_t:
        if st.button("🔴 TÀI", use_container_width=True):
            if st.session_state.cuoc > 0 and st.session_state.cuoc <= st.session_state.so_du:
                st.session_state.chon = "Tài"; st.session_state.trang_thai = "LAC"; st.rerun()
            else: st.error("Tiền cược không hợp lệ!")
    with col_x:
        if st.button("🔵 XỈU", use_container_width=True):
            if st.session_state.cuoc > 0 and st.session_state.cuoc <= st.session_state.so_du:
                st.session_state.chon = "Xỉu"; st.session_state.trang_thai = "LAC"; st.rerun()

# 2. HIỆU ỨNG LẮC XÚC XẮC
elif st.session_state.trang_thai == "LAC":
    st.markdown("<h2 style='text-align: center;'>🎲 ĐANG XÓC ĐĨA...</h2>", unsafe_allow_html=True)
    with st.empty():
        for _ in range(12):
            st.markdown(f"<div style='font-size: 80px; text-align: center;'>{' '.join([get_dice_icon(random.randint(1,6)) for _ in range(3)])}</div>", unsafe_allow_html=True)
            time.sleep(0.1)
    st.session_state.kq = [random.randint(1, 6) for _ in range(3)]
    st.session_state.trang_thai = "NAN_BAT"
    st.rerun()

# 3. TỰ TAY NẶN BÁT
elif st.session_state.trang_thai == "NAN_BAT":
    st.markdown(f"<p style='text-align: center;'>Đặt: <b>{st.session_state.chon}</b> | Cược: <b>{st.session_state.cuoc:,}</b></p>", unsafe_allow_html=True)
    
    # Bát nhích dần lên
    offset = st.session_state.step_nan * -70 
    
    st.markdown(f"""
        <div class="dice-plate">
            <div class="dice-img">{' '.join([get_dice_icon(st.session_state.kq[i]) if st.session_state.step_nan > i else "" for i in range(3)])}</div>
            <div class="bat-up" style="transform: translateY({offset}px);">🥣</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    if st.session_state.step_nan < 4:
        if st.button("👉 BẤM ĐỂ MỞ BÁT TỪ TỪ 👈"):
            st.session_state.step_nan += 1
            st.rerun()
    else:
        if st.button("XEM KẾT QUẢ"):
            st.session_state.trang_thai = "KET_QUA"
            st.rerun()

# 4. KẾT QUẢ CUỐI CÙNG
elif st.session_state.trang_thai == "KET_QUA":
    d = st.session_state.kq
    tong = sum(d)
    kq_chu = "Xỉu" if 4 <= tong <= 10 else "Tài"
    if d[0] == d[1] == d[2]: kq_chu = "Bão"

    st.markdown(f"<h1 style='text-align: center;'>{get_dice_icon(d[0])} {get_dice_icon(d[1])} {get_dice_icon(d[2])}</h1>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align: center; color: gold;'>{tong} - {kq_chu.upper()}</h1>", unsafe_allow_html=True)

    if st.session_state.chon == kq_chu:
        st.balloons(); st.success(f"🔥 HÚP LỚN! +{st.session_state.cuoc:,}"); st.session_state.so_du += st.session_state.cuoc
    else:
        st.error(f"💸 GÃY CẦU! -{st.session_state.cuoc:,}"); st.session_state.so_du -= st.session_state.cuoc

    if st.button("LÀM VÁN MỚI"):
        st.session_state.trang_thai = "DAT_CUOC"; st.session_state.step_nan = 0; st.session_state.cuoc = 0; st.rerun()
