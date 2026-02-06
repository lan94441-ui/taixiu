import streamlit as st
import streamlit.components.v1 as components
import random

st.set_page_config(page_title="Sunwin 3D VIP Full Audio", layout="centered")

# Khởi tạo dữ liệu
if 'so_du' not in st.session_state: st.session_state.so_du = 10000000
if 'tien_cuoc' not in st.session_state: st.session_state.tien_cuoc = 0
if 'cua_chon' not in st.session_state: st.session_state.cua_chon = ""
if 'kq_so' not in st.session_state: st.session_state.kq_so = [1, 1, 1]

# Giao diện tiền tệ
st.markdown(f"""
<style>
    .stApp {{ background-color: #0b0e14; }}
    .header-casino {{
        text-align: center; color: gold; border: 2px solid #ffd700;
        padding: 15px; border-radius: 20px; background: linear-gradient(180deg, #1a1c23 0%, #000 100%);
        box-shadow: 0 0 20px rgba(255, 215, 0, 0.2);
    }}
    .money-text {{ color: #4cd137; font-size: 30px; font-weight: bold; }}
</style>
<div class="header-casino">
    <h1 style="margin:0;">🏆 SUNWIN 3D VIP 🏆</h1>
    <div class="money-text">💰 {st.session_state.so_du:,} VND</div>
</div>
""", unsafe_allow_html=True)

# Khu vực đặt cược
st.write("")
c1, c2, c3, c4 = st.columns(4)
with c1: 
    if st.button("100K"): st.session_state.tien_cuoc += 100000
with c2: 
    if st.button("500K"): st.session_state.tien_cuoc += 500000
with c3: 
    if st.button("1M"): st.session_state.tien_cuoc += 1000000
with c4: 
    if st.button("XÓA"): st.session_state.tien_cuoc = 0

st.markdown(f"<h3 style='text-align:center; color:white;'>Cược: <span style='color:yellow;'>{st.session_state.tien_cuoc:,}</span> | Cửa: <span style='color:cyan;'>{st.session_state.cua_chon}</span></h3>", unsafe_allow_html=True)

col_t, col_x = st.columns(2)
with col_t:
    if st.button("🔴 TÀI (11-17)", use_container_width=True): st.session_state.cua_chon = "Tài"
with col_x:
    if st.button("🔵 XỈU (4-10)", use_container_width=True): st.session_state.cua_chon = "Xỉu"

# Tính toán kết quả ngầm trước khi nặn
if st.session_state.tien_cuoc > 0 and st.session_state.cua_chon != "":
    d1, d2, d3 = random.randint(1,6), random.randint(1,6), random.randint(1,6)
    st.session_state.kq_so = [d1, d2, d3]
    tong = sum(st.session_state.kq_so)
    kq_game = "Tài" if 11 <= tong <= 17 else "Xỉu"
    if d1 == d2 == d3: kq_game = "Bão"

# Game HTML 3D tích hợp Âm thanh
html_code = f"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
    body {{ background: transparent; text-align: center; color: gold; font-family: sans-serif; }}
    .table {{ 
        background: radial-gradient(circle, #444 0%, #000 100%);
        border: 6px solid gold; border-radius: 50%; width: 280px; height: 280px;
        margin: 0 auto; position: relative; display: flex; align-items: center; justify-content: center;
        perspective: 1000px; box-shadow: 0 0 30px rgba(0,0,0,1);
    }}
    .dice-box {{ display: flex; gap: 10px; z-index: 1; }}
    .dice {{ width: 50px; height: 50px; position: relative; transform-style: preserve-3d; transition: transform 1s cubic-bezier(0.175, 0.885, 0.32, 1.275); }}
    .dice div {{ position: absolute; width: 50px; height: 50px; background: white; border: 1px solid #ccc; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 30px; color: black; }}
    .f1{{transform:translateZ(25px)}} .f6{{transform:rotateY(180deg) translateZ(25px)}} .f3{{transform:rotateY(90deg) translateZ(25px)}} .f4{{transform:rotateY(-90deg) translateZ(25px)}} .f2{{transform:rotateX(90deg) translateZ(25px)}} .f5{{transform:rotateX(-90deg) translateZ(25px)}}
    
    .bat {{
        position: absolute; width: 260px; height: 260px; background: radial-gradient(circle, #666, #222);
        border-radius: 50%; border: 3px solid #888; z-index: 10; cursor: pointer;
        display: flex; align-items: center; justify-content: center; font-size: 110px;
        transition: 0.6s cubic-bezier(0.5, -0.5, 0.5, 1.5);
    }}
    .spinning {{ animation: spin 0.1s infinite linear; }}
    @keyframes spin {{ 0% {{ transform: rotateX(0) rotateY(0); }} 100% {{ transform: rotateX(360deg) rotateY(360deg); }} }}
    .btn-play {{ background: linear-gradient(to bottom, #ffd700, #b8860b); color: black; border: none; padding: 15px 40px; font-size: 22px; font-weight: bold; border-radius: 15px; cursor: pointer; margin-top: 20px; }}
</style>
</head>
<body>
    <div class="table">
        <div class="dice-box">
            <div class="dice" id="d1"><div class="f1">⚀</div><div class="f6">⚅</div><div class="f3">⚂</div><div class="f4">⚃</div><div class="f2">⚁</div><div class="f5">⚄</div></div>
            <div class="dice" id="d2"><div class="f1">⚀</div><div class="f6">⚅</div><div class="f3">⚂</div><div class="f4">⚃</div><div class="f2">⚁</div><div class="f5">⚄</div></div>
            <div class="dice" id="d3"><div class="f1">⚀</div><div class="f6">⚅</div><div class="f3">⚂</div><div class="f4">⚃</div><div class="f2">⚁</div><div class="f5">⚄</div></div>
        </div>
        <div class="bat" id="bat" onclick="moBat()">🥣</div>
    </div>
    <button class="btn-play" onclick="lacBat()">🎰 LẮC BÁT</button>
    <p id="status">Chạm vào bát để NẶN nhé!</p>

    <audio id="s_xoc" src="https://assets.mixkit.co/active_storage/sfx/2005/2005-preview.mp3"></audio>
    <audio id="s_mo" src="https://assets.mixkit.co/active_storage/sfx/1070/1070-preview.mp3"></audio>

<script>
    let step = 0;
    const bat = document.getElementById('bat');
    const dices = [document.getElementById('d1'), document.getElementById('d2'), document.getElementById('d3')];
    const angles = {{ 1:[0,0], 2:[-90,0], 3:[0,-90], 4:[0,90], 5:[90,0], 6:[0,180] }};
    const final_kq = [{st.session_state.kq_so[0]}, {st.session_state.kq_so[1]}, {st.session_state.kq_so[2]}];

    function lacBat() {{
        step = 0; bat.style.transform = "translateY(0) rotate(0)";
        document.getElementById('s_xoc').play();
        dices.forEach(d => d.classList.add('spinning'));
        setTimeout(() => {{
            dices.forEach((d, i) => {{
                d.classList.remove('spinning');
                let a = angles[final_kq[i]];
                d.style.transform = `rotateX(${{a[0]}}deg) rotateY(${{a[1]}}deg)`;
            }});
            document.getElementById('status').innerText = "ĐÃ XÓC XONG! NẶN ĐI...";
        }}, 1200);
    }}

    function moBat() {{
        if(step < 3) {{
            step++;
            document.getElementById('s_mo').play();
            bat.style.transform = `translateY(-${{step * 80}}px) rotate(${{step * 10}}deg)`;
        }}
    }}
</script>
</body>
</html>
"""
components.html(html_code, height=520)

# Xử lý kết quả trả về Streamlit
if st.button("🧧 XÁC NHẬN KẾT QUẢ & NHẬN THƯỞNG"):
    d1, d2, d3 = st.session_state.kq_so
    tong = d1 + d2 + d3
    kq_game = "Tài" if 11 <= tong <= 17 else "Xỉu"
    if d1 == d2 == d3: kq_game = "Bão"
    
    st.markdown(f"### Kết quả: {d1}-{d2}-{d3} ({tong} - {kq_game.upper()})")
    
    if st.session_state.cua_chon == kq_game:
        st.balloons()
        st.success(f"🔥 THẮNG LỚN! +{st.session_state.tien_cuoc:,} VND")
        st.session_state.so_du += st.session_state.tien_cuoc
    else:
        st.error(f"💸 GÃY CẦU! -{st.session_state.tien_cuoc:,} VND")
        st.session_state.so_du -= st.session_state.tien_cuoc
    
    # Reset ván mới
    st.session_state.tien_cuoc = 0
    st.session_state.cua_chon = ""
