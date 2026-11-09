import random
import streamlit as st

# 1. 頁面基本設定：針對手機響應式調整
st.set_page_config(
    page_title="My App",
    page_icon="🎯",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- 請加入這兩行來喚醒左側選單 ---
st.sidebar.header("我的專屬選單")
st.sidebar.write("這裡可以放單字分類或按鈕")
# -----------------------------------

st.write("這裡是右邊的主畫面！")


# 2. 手機介面專屬 CSS 樣式優化（縮減上方留白）
st.markdown(
    """
    <style>
        .block-container {
            padding-top: 1rem;
            padding-left: 1rem !important;
            padding-right: 1rem !important;
            max-width: 100% !important;
        }
        div.stButton > button {
            font-size: 20px !important;
            font-weight: bold !important;
            height: 56px !important;
            border-radius: 10px !important;
            padding: 0.5rem 1rem !important;
        }
        div.stButton > button * {
            font-size: 20px !important;
            font-weight: bold !important;
        }
        .stRadio label, .stRadio div {
            font-size: 18px !important;
        }
        .card-container {
            border: 2px solid #cbd5e1;
            border-radius: 12px;
            padding: 20px;
            background-color: #ffffff;
            box-shadow: 2px 4px 12px rgba(0,0,0,0.08);
            margin-top: 10px;
            margin-bottom: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# 41 個完整生字清單
vocabulary_list = [
    {
        "word": "usage limit",
        "pos": "n.",
        "phonetic": "/ˈjuːsɪdʒ ˈlɪmɪt/",
        "meaning": "使用額度",
        "example": "Upgrading your account will double your daily usage limit.",
    },
    {
        "word": "api key",
        "pos": "n.",
        "phonetic": "/ˌeɪ piː aɪ kiː/",
        "meaning": "API 金鑰",
        "example": "Make sure to keep your API key secure and confidential.",
    },
    {
        "word": "snippet",
        "pos": "n.",
        "phonetic": "/ˈsnɪpɪt/",
        "meaning": "片段、程式碼片段",
        "example": "You can copy this code snippet directly into your project.",
    },
    {
        "word": "skip",
        "pos": "v./n.",
        "phonetic": "/skɪp/",
        "meaning": "跳過、略過",
        "example": "You can skip this tutorial if you are already familiar with the setup.",
    },
    {
        "word": "deploy",
        "pos": "v.",
        "phonetic": "/dɪˈplɔɪ/",
        "meaning": "部署、配置",
        "example": "The engineering team will deploy the new application version tonight.",
    },
    {
        "word": "firewall",
        "pos": "n.",
        "phonetic": "/ˈfaɪərwɔːl/",
        "meaning": "防火牆",
        "example": "Configure the firewall rules to block unauthorized access.",
    },
    {
        "word": "router",
        "pos": "n.",
        "phonetic": "/ˈruːtər/",
        "meaning": "路由器",
        "example": "The network administrator restarted the core router.",
    },
    {
        "word": "switch",
        "pos": "n.",
        "phonetic": "/swɪtʃ/",
        "meaning": "交換器",
        "example": "Connect the office computers to the 24-port switch.",
    },
    {
        "word": "vlan",
        "pos": "n.",
        "phonetic": "/ˌviː el eɪ ˈen/",
        "meaning": "虛擬區域網路",
        "example": "We set up a separate VLAN for guest network traffic.",
    },
    {
        "word": "ip address",
        "pos": "n.",
        "phonetic": "/aɪ piː əˈdres/",
        "meaning": "IP 位址",
        "example": "Assign a static IP address to the server before configuration.",
    },
    {
        "word": "subnet mask",
        "pos": "n.",
        "phonetic": "/ˈsʌbnɛt mæsk/",
        "meaning": "子網路遮罩",
        "example": "Enter the correct subnet mask to define the network range.",
    },
    {
        "word": "gateway",
        "pos": "n.",
        "phonetic": "/ˈɡeɪtweɪ/",
        "meaning": "通訊閘、閘道器",
        "example": "Check the default gateway settings if internet access fails.",
    },
    {
        "word": "ssh",
        "pos": "n.",
        "phonetic": "/ˌes es ˈeɪtʃ/",
        "meaning": "安全殼協定",
        "example": "Use SSH to securely connect to the remote Linux server.",
    },
    {
        "word": "scp",
        "pos": "n.",
        "phonetic": "/ˌes siː ˈpiː/",
        "meaning": "安全複製",
        "example": "You can use scp to transfer files between servers securely.",
    },
    {
        "word": "ansible",
        "pos": "n.",
        "phonetic": "/ˈænsɪbəl/",
        "meaning": "自動化設定管理工具",
        "example": "Ansible playbooks automate the software deployment process.",
    },
    {
        "word": "playbook",
        "pos": "n.",
        "phonetic": "/ˈpleɪbʊk/",
        "meaning": "劇本、自動化腳本",
        "example": "Write an Ansible playbook to configure multiple virtual machines.",
    },
    {
        "word": "virtual machine",
        "pos": "n.",
        "phonetic": "/ˈvɜːrtʃuəl məˈshiːn/",
        "meaning": "虛擬機器",
        "example": "Deploy a new Ubuntu virtual machine using VMware Workstation.",
    },
    {
        "word": "hypervisor",
        "pos": "n.",
        "phonetic": "/ˈhaɪpərvɑɪzər/",
        "meaning": "虛擬機器監控程式",
        "example": "The hypervisor manages multiple guest operating systems.",
    },
    {
        "word": "docker",
        "pos": "n.",
        "phonetic": "/ˈdɑːkər/",
        "meaning": "容器化平台",
        "example": "Package your web application into a Docker container.",
    },
    {
        "word": "kubernetes",
        "pos": "n.",
        "phonetic": "/ˌkuːbərˈnɛtiːz/",
        "meaning": "容器編排系統",
        "example": "Kubernetes orchestrates containerized applications across clusters.",
    },
    {
        "word": "repository",
        "pos": "n.",
        "phonetic": "/rɪˈpɑːzətɔːri/",
        "meaning": "儲存庫",
        "example": "Clone the git repository to your local machine.",
    },
    {
        "word": "commit",
        "pos": "v./n.",
        "phonetic": "/kəˈmɪt/",
        "meaning": "提交",
        "example": "Remember to commit your code changes with a clear message.",
    },
    {
        "word": "merge",
        "pos": "v.",
        "phonetic": "/mɜːrdʒ/",
        "meaning": "合併",
        "example": "Merge the feature branch into the main branch.",
    },
    {
        "word": "conflict",
        "pos": "n./v.",
        "phonetic": "/ˈkɑːnflɪkt/",
        "meaning": "衝突",
        "example": "Resolve the merge conflict before pushing to GitHub.",
    },
    {
        "word": "branch",
        "pos": "n.",
        "phonetic": "/bræntʃ/",
        "meaning": "分支",
        "example": "Create a new branch for your upcoming feature development.",
    },
    {
        "word": "pipeline",
        "pos": "n.",
        "phonetic": "/ˈpaɪplaɪn/",
        "meaning": "管線、自動化流程",
        "example": "The CI/CD pipeline automates testing and deployment.",
    },
    {
        "word": "bandwidth",
        "pos": "n.",
        "phonetic": "/ˈbændwɪdθ/",
        "meaning": "頻寬",
        "example": "High-resolution video streaming requires sufficient network bandwidth.",
    },
    {
        "word": "latency",
        "pos": "n.",
        "phonetic": "/ˈleɪtənsi/",
        "meaning": "延遲",
        "example": "Lower network latency improves real-time server response.",
    },
    {
        "word": "throughput",
        "pos": "n.",
        "phonetic": "/ˈθruːpʊt/",
        "meaning": "吞吐量",
        "example": "Network throughput measures the amount of data transferred successfully.",
    },
    {
        "word": "certificate",
        "pos": "n.",
        "phonetic": "/sərˈtɪfɪkət/",
        "meaning": "憑證",
        "example": "Install the SSL certificate to enable secure HTTPS connections.",
    },
    {
        "word": "authentication",
        "pos": "n.",
        "phonetic": "/ɔːˌθentɪˈkeɪʃn/",
        "meaning": "身份驗證",
        "example": "Two-factor authentication adds an extra layer of security.",
    },
    {
        "word": "authorization",
        "pos": "n.",
        "phonetic": "/ˌɔːθərəˈzeɪʃn/",
        "meaning": "授權",
        "example": "Check user permissions and authorization before granting access.",
    },
    {
        "word": "encryption",
        "pos": "n.",
        "phonetic": "/ɪnˈkrɪpʃn/",
        "meaning": "加密",
        "example": "Data encryption protects sensitive files from unauthorized viewing.",
    },
    {
        "word": "decryption",
        "pos": "n.",
        "phonetic": "/diːˈkrɪpʃn/",
        "meaning": "解密",
        "example": "The system performs automatic decryption upon secure login.",
    },
    {
        "word": "backup",
        "pos": "n./v.",
        "phonetic": "/ˈbækʌp/",
        "meaning": "備份",
        "example": "Perform a daily system backup to prevent data loss.",
    },
    {
        "word": "restore",
        "pos": "v.",
        "phonetic": "/rɪˈstɔːr/",
        "meaning": "還原",
        "example": "Restore the database from the latest secure backup file.",
    },
    {
        "word": "recovery",
        "pos": "n.",
        "phonetic": "/rɪˈkʌvəri/",
        "meaning": "復原、恢復",
        "example": "Disaster recovery plans ensure business continuity after system failures.",
    },
    {
        "word": "log",
        "pos": "n./v.",
        "phonetic": "/lɔːɡ/",
        "meaning": "日誌、記錄",
        "example": "Check the system error log to diagnose the network issue.",
    },
    {
        "word": "troubleshooting",
        "pos": "n.",
        "phonetic": "/ˈtrʌbəlʃuːtɪŋ/",
        "meaning": "故障排除",
        "example": "Effective troubleshooting skills are essential for network administrators.",
    },
    {
        "word": "syntax",
        "pos": "n.",
        "phonetic": "/ˈsɪntæks/",
        "meaning": "語法",
        "example": "Check your YAML configuration file for any syntax errors.",
    },
    {
        "word": "permission",
        "pos": "n.",
        "phonetic": "/pərˈmɪʃn/",
        "meaning": "權限",
        "example": "Change file permissions using the chmod command in Linux.",
    },
]

# 側邊欄選單
st.sidebar.title("🎛️ Navigation")
app_mode = st.sidebar.radio(
    "Select Mode", ["📇 Flashcards", "📝 Quiz"]
)

# ==================== 模式一：單字卡瀏覽 ====================
if app_mode == "📇 Flashcards":
    st.markdown("## 📇 Flashcards")

    if "index" not in st.session_state:
        st.session_state.index = 0

    total_words = len(vocabulary_list)
    current_word = vocabulary_list[st.session_state.index]

    st.markdown(f"**{st.session_state.index + 1} / {total_words}**")

    # 手機自適應單字卡介面
    card_html = f"""
    <div class="card-container">
        <div style="font-size: 28px; font-weight: bold; color: #1e293b; margin-bottom: 6px;">
            {current_word['word']} <span style="font-size: 18px; color: #0d9488; font-weight: normal;">({current_word['pos']})</span>
        </div>
        <div style="font-size: 15px; color: #475569; margin-bottom: 8px;">
            <b>Phonetic:</b> {current_word['phonetic']}
        </div>
        <div style="font-size: 22px; font-weight: bold; color: #1d4ed8; margin-bottom: 12px;">
            Meaning: {current_word['meaning']}
        </div>
        <hr style="border: 0; border-top: 1px solid #e2e8f0; margin: 12px 0;">
        <div style="font-size: 16px; color: #334155;">
            💡 <b>Example:</b><br>
            <span style="line-height: 1.4; color: #0f172a;">{current_word['example']}</span>
        </div>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)

    # 左右切換按鈕
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Prev", use_container_width=True):
            if st.session_state.index > 0:
                st.session_state.index -= 1
                st.rerun()

    with col2:
        if st.button("Next ➡️", use_container_width=True):
            if st.session_state.index < total_words - 1:
                st.session_state.index += 1
                st.rerun()

# ==================== 模式二：隨堂小測驗 ====================
elif app_mode == "📝 Quiz":
    st.markdown("## 📝 Vocabulary Quiz")

    if "quiz_item" not in st.session_state:
        st.session_state.quiz_item = None
    if "quiz_options" not in st.session_state:
        st.session_state.quiz_options = []
    if "quiz_answered" not in st.session_state:
        st.session_state.quiz_answered = False

    if st.button("🔄 Next Question", use_container_width=True):
        correct = random.choice(vocabulary_list)
        wrong_pool = [
            w["meaning"] for w in vocabulary_list if w["word"] != correct["word"]
        ]
        wrong_choices = random.sample(wrong_pool, min(3, len(wrong_pool)))
        options = wrong_choices + [correct["meaning"]]
        random.shuffle(options)

        st.session_state.quiz_item = correct
        st.session_state.quiz_options = options
        st.session_state.quiz_answered = False
        st.rerun()

    if st.session_state.quiz_item:
        current_q = st.session_state.quiz_item

        quiz_card_html = f"""
        <div class="card-container">
            <div style="font-size: 18px; font-weight: bold; color: #475569; margin-bottom: 8px;">
                What is the meaning of:
            </div>
            <div style="font-size: 30px; font-weight: bold; color: #1e293b;">
                {current_q['word']} <span style="font-size: 18px; color: #0d9488; font-weight: normal;">({current_q['pos']})</span>
            </div>
        </div>
        """
        st.markdown(quiz_card_html, unsafe_allow_html=True)

        user_choice = st.radio(
            "Select the correct meaning:",
            st.session_state.quiz_options,
            key="current_answer_radio",
        )

        if st.button("Submit Answer", use_container_width=True):
            st.session_state.quiz_answered = True

        if st.session_state.quiz_answered:
            if user_choice == current_q["meaning"]:
                st.success("🎉 Correct!")
            else:
                st.error(
                    f"❌ Incorrect! Correct answer: **{current_q['meaning']}**"
                )
            st.info(f"💡 **Example:** {current_q['example']}")
    else:
        st.info("👆 Click the button above to start!")