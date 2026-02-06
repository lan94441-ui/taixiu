import streamlit as st

st.set_page_config(page_title="Sunwin 3D Real", layout="centered")

# Vốn khởi nghiệp 10 Triệu
if 'so_du' not in st.session_state:
    st.session_state.so_du = 10000000

st.markdown(f"""
<style>
    .stApp {{ background: radial-gradient(circle, #2c3e50, #000); }}
    .casino-container {{
        text-align: center;
        font-family: 'Arial', sans-serif;
        color: gold;
    }}
    /* Hiệu ứng Xúc xắc 3D */
    .dice-area {{
        display: flex;
        justify-content: center;
        gap: 20px;
        perspective: 1000px;
        margin: 50px 0;
    }}
    .cube {{
        width: 60px;
        height: 60px;
        position: relative;
        transform-style: preserve-3d;
        transition: transform 2s ease-out;
    }}
    .cube div {{
        position: absolute;
        width: 60px;
        height: 60px;
        background: white;
        border: 2px solid #ccc;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 30px;
        color: black;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.2);
    }}
    /* Các mặt của xúc xắc */
    .front  {{ transform: translateZ(30px); }}
    .back   {{ transform: rotateY(180deg) translateZ(30px); }}
    .right  {{ transform: rotateY(90deg) translateZ(30px); }}
    .left   {{ transform: rotateY(-90deg) translateZ(30px); }}
    .top    {{ transform: rotateX(90deg) translateZ(30px); }}
    .bottom {{ transform: rotateX(-90deg) translateZ(30px); }}

    /* Hiệu ứng quay */
    .spinning {{
        animation: spin 0.5s infinite linear;
    }}
    @keyframes spin {{
        0% {{ transform: rotateX(0) rotateY(0); }}
        100% {{ transform: rotateX(360deg) rotateY(360deg); }}
    }}

    .bat-container {{
        position: relative;
        width: 250px;
        height: 250px;
        margin: 0 auto;
    }}
    .bat {{
        width: 200px;
        height: 200px;
        background: #444;
        border-radius: 50%;
        border: 5px solid gold;
        position: absolute;
        top: 25px;
        left: 25px;
        z-index: 100;
        transition: transform 1s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 80px;
    }}
</style>

<div class="casino-container">
    <h1>🏆 SUNWIN 3D REAL 🏆</h1>
    <h2 style="color: #00ff00;">Số dư: {st.session_state.so_du:,} VND</h2>
</div>
""", unsafe_allow_html=True)

# Logic game đơn giản để kết nối với hiệu ứng
col1, col2 = st.columns(2)
with col1:
    cuoc = st.number_input("Tiền cược:", min_value=10000, step=50000, value=100000)
with col2:
    cua = st.selectbox("Chọn cửa:", ["Tài", "Xỉu"])

if st.button("🔥 LẮC VÀ NẶN 🔥"):
    # Giả lập lắc
    st.markdown("""
    <div class="dice-area">
        <div class="cube spinning"><div>⚀</div><div class="back">⚅</div><div class="right">⚂</div><div class="left">⚃</div><div class="top">⚁</div><div class="bottom">⚄</div></div>
        <div class="cube spinning"><div>⚀</div><div class="back">⚅</div><div class="right">⚂</div><div class="left">⚃</div><div class="top">⚁</div><div class="bottom">⚄</div></div>
        <div class="cube spinning"><div>⚀</div><div class="back">⚅</div><div class="right">⚂</div><div class="left">⚃</div><div class="top">⚁</div><div class="bottom">⚄</div></div>
    </div>
    """, unsafe_allow_html=True)
    
    # Tính toán kết quả
    d = [random.randint(1, 6) for _ in range(3)]
    tong = sum(d)
    kq = "Xỉu" if 4 <= tong <= 10 else "Tài"
    
    import time
    time.sleep(2) # Đợi 2 giây cho cảm giác quay
    
    st.rerun() # Để cập nhật trạng thái mới (Bạn cần thêm logic lưu kết quả vào session_state ở đây)

st.info("Để làm giống 100% như app, bạn cần học về HTML/CSS/JS nâng cao. Bạn có muốn tôi viết hẳn một file HTML riêng để bạn mở bằng trình duyệt không?")
