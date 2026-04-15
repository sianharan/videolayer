import streamlit as st
import time

# 1. 페이지 설정
st.set_page_config(layout="wide", page_title="전문가 상담 서비스")

# 2. 사용할 비디오 URL
video_url = "https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-mp4-file.mp4"

# 3. 세련된 미니멀 CSS
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500&display=swap');
        html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
        .block-container { padding-top: 5rem !important; }
        
        /* 팝업 내 카운트다운 스타일 */
        .countdown-text { 
            font-size: 50px; font-weight: 300; color: #444; 
            text-align: center; margin: 20px 0; 
        }
        
        /* 상담 양식 컨테이너 */
        .form-card {
            background-color: #f8f9fa; padding: 40px; border-radius: 16px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.05); margin-top: 20px;
        }
        
        .guide-text { font-size: 15px; color: #888; margin-bottom: 12px; }

        /* 버튼 스타일 */
        div.stButton > button {
            background-color: #1a1a1a; color: white; padding: 14px 40px;
            font-size: 18px; border-radius: 8px; border: none; transition: all 0.3s;
        }
        div.stButton > button:hover { background-color: #333; transform: translateY(-2px); }
    </style>
""", unsafe_allow_html=True)

# --- 팝업창 함수 정의 ---
@st.dialog("학부모 교육 안내")
def show_video_dialog():
    st.write("학부모 교육을 위한 영상을 시청 후 상담을 신청해주세요.")
    
    # 카운트다운 영역
    placeholder = st.empty()
    for i in range(5, 0, -1):
        placeholder.markdown(f"<div class='countdown-text'>{i}</div>", unsafe_allow_html=True)
        time.sleep(1)
    placeholder.empty()
    
    # 영상 재생 (짤림 방지는 Streamlit 기본 기능으로도 충분)
    st.video(video_url, autoplay=True)
    
    if st.button("영상 닫고 상담하기", use_container_width=True):
        st.rerun()

# --- UI 레이아웃 ---
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.write("### 전문가 상담")
    st.write("상담 신청 버튼을 누르면 안내 영상이 시작됩니다.")
    
    # 버튼 클릭 시 팝업 실행
    if st.button("상담 신청"):
        show_video_dialog()

    # 배경에 미리 깔려 있는 상담 양식 (영상 없이도 언제든 작성 가능)
    st.markdown('<div class="form-card">', unsafe_allow_html=True)
    st.write("### 📝 상담 요청")
    st.markdown('<div class="guide-text">상담 내용을 적어주세요</div>', unsafe_allow_html=True)
    
    user_input = st.text_area("", height=150, key="consult_input", label_visibility="collapsed")
    
    if st.button("상담 내용 제출", key="submit_btn", use_container_width=True):
        if user_input:
            st.success("접수되었습니다! 전문가 수연님이 곧 연락드리겠습니다.")
        else:
            st.warning("내용을 입력해주세요.")
    st.markdown('</div>', unsafe_allow_html=True)
