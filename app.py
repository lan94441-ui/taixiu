import streamlit as st
import streamlit.components.v1 as components
import random

# Cấu hình trang
st.set_page_config(page_title="Sunwin 3D Pro Max", layout="centered")

# Khởi tạo số dư 10 triệu
if 'so_du' not in st.session_state:
    st.session_state.so_du = 10000000

# CSS để làm giao diện đen vàng sang trọng
st.markdown("""
<style>
    .stApp { background-color: #0b0e14; }
    .money-header {
        text-align: center; background: #1a1c23; border: 2px solid gold;
        padding: 15px; border-radius: 20px; color: #00ff00;
        font-size: 30px; font-weight: bold; margin-bottom: 20px;
    }
</style>
<div class="money-header">💰 SỐ DƯ: """ + f"{st.session_state.so_du:,}" + """ VND</div>
""", unsafe_allow_html=True)

# Mã HTML, CSS và JavaScript hoàn chỉnh
html_code = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
    body { background: transparent; color: gold; font-family: 'Segoe UI', sans-serif; text-align: center; overflow: hidden; }
    .table-3d { 
        background: radial-gradient(circle, #333 0%, #000 100%);
        border: 8px solid #ffd700; border-radius: 50%; width: 300px; height: 300px;
        margin: 10px auto; position: relative; display: flex; align-items: center; justify-content: center;
        perspective: 800px; box-shadow: 0 0 30px rgba(255, 215, 0, 0.2);
    }
    .dice-container { display: flex; gap: 10px; z-index: 1; }
    .dice { width: 50px; height: 50px; position: relative; transform-style: preserve-3d; transition: transform 1s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
    .dice div {
        position: absolute; width: 50px; height: 50px; background: #fff;
        border: 1px solid #ccc; border-radius: 8px; display: flex;
        align-items: center; justify-content: center; font-size: 28px; color: #000; font-weight: bold;
    }
    .f1 { transform: translateZ(25px); }
    .f6 { transform: rotateY(180deg) translateZ(25px); }
    .f3 { transform: rotateY(90deg) translateZ(25px); }
    .f4 { transform: rotateY(-90deg) translateZ(25px); }
    .f2 { transform: rotateX(90deg) translateZ(25px); }
    .f5 { transform: rotateX(-90deg) translateZ(25px); }

    .bat {
        position: absolute; width: 270px; height: 270px; 
        background: radial-gradient(circle, #555, #111);
        border-radius: 50%; border: 3px solid #ffd700; z-index: 10;
        cursor: pointer; transition: 0.5s ease-out; font-size: 120px;
        display: flex; align-items: center; justify-content: center;
        box-shadow: 0 15px 35px rgba(0,0,0,0.8);
    }
    .spinning { animation: spin 0.15s infinite linear; }
    @keyframes spin { 0% { transform: rotateX(0) rotateY(0); } 100% { transform: rotateX(360deg) rotateY(360deg); } }
    
    .controls { margin-top: 20px; }
    .btn-main { 
        background: linear-gradient(to bottom, #ffd700, #b8860b); color: black; 
        border: none; padding: 15px 40px; font-size: 22px; font-weight: bold; 
        border-radius: 15px; cursor: pointer; width: 80%; box-shadow: 0 5px 0 #8b6508;
    }
    .btn-main:active { transform: translateY(3px); box-shadow: 0 2px 0 #8b6508; }
</style>
</head>
<body>

    <div class="table-3d">
        <div class="dice-container">
            <div class="dice" id="d1"><div class="f1">⚀</div><div class="f6">⚅</div><div class="f3">⚂</div><div class="f4">⚃</div><div class="f2">⚁</div><div class="f5">⚄</div></div>
            <div class="dice" id="d2"><div class="f1">⚀</div><div class="f6">⚅</div><div class="f3">⚂</div><div class="f4">⚃</div><div class="f2">⚁</div><div class="f5">⚄</div></div>
            <div class="dice" id="d3"><div class="f1">⚀</div><div class="f6">⚅</div><div class="f3">⚂</div><div class="f4">⚃</div><div class="f2">⚁</div><div class="f5">⚄</div></div>
        </div>
        <div class="bat" id="bat" onclick="moBat()">🥣</div>
    </div>

    <div class="controls">
        <button class="btn-main" onclick="lacBat()">🎲 LẮC BÁT</button>
        <p id="msg" style="font-size: 18px; margin-top: 15px;">👉 Bấm Lắc rồi chạm vào bát để Nặn!</p>
    </div>

    <audio id="soundXoc" src="https://www.soundjay.com/misc/sounds/dice-shake-1.mp3"></audio>
    <audio id="soundMo" src="https://www.soundjay.com/misc/sounds/bell-ringing-05.mp3"></audio>

<script>
    let step = 0;
    const bat = document.getElementById('bat');
    const dices = [document.getElementById('d1'), document.getElementById('d2'), document.getElementById('d3')];
    const angles = { 1:[0,0], 2:[-90,0], 3:[0,-90], 4:[0,90], 5:[90,0], 6:[0,180] };

    function lacBat() {
        step = 0;
        bat.style.transform = "translateY(0) rotate(0)";
        document.getElementById('soundXoc').play();
        document.getElementById('msg').innerText = "ĐANG XÓC... 🔥";
        
        dices.forEach(d => d.classList.add('spinning'));
        
        setTimeout(() => {
            dices.forEach(d => {
                d.classList.remove('spinning');
                let res = Math.floor(Math.random() * 6) + 1;
                let a = angles[res];
                d.style.transform = `rotateX(${a[0]}deg) rotateY(${a[1]}deg)`;
            });
            document.getElementById('msg').innerText = "XÓC XONG! CHẠM BÁT ĐỂ NẶN 👆";
        }, 1500);
    }

    function moBat() {
        if(step < 3) {
            step++;
            // Bát nhích lên và nghiêng theo từng lần chạm
            bat.style.transform = `translateY(-${step * 70}px) rotate(${step * 10}deg)`;
            if(step == 3) {
                document.getElementById('soundMo').play();
                document.getElementById('msg').innerText = "MỞ BÁT! CHÚC MỪNG 🎉";
            }
        }
    }
</script>
</body>
</html>
"""

# Hiển thị Game
components.html(html_code, height=550)

# Phần điều khiển tiền cược của Streamlit (nằm dưới game)
st.write("---")
c1, c2 = st.columns(2)
with c1:
    if st.button("🧧 Nhận thêm 1 Triệu"):
        st.session_state.so_du += 1000000
        st.rerun()
with c2:
    if st.button("🗑️ Reset Vốn"):
        st.session_state.so_du = 10000000
        st.rerun()
