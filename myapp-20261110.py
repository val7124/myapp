import random
import pandas as pd
import streamlit as st

# 設定網頁標題
st.title("📚 我的 TOEIC 單字隨身背 App")


# 從 Excel 自動讀取單字的函式
@st.cache_data
def load_vocabulary():
  try:
    # 讀取同資料夾下的 vocabulary.xlsx
    df = pd.read_excel("vocabulary.xlsx")
    # 將欄位名稱轉成字串並去除前後空白，確保安全
    df.columns = df.columns.str.strip()
    # 轉換成 Streamlit 用的字典清單格式
    return df.to_dict(orient="records")
  except Exception as e:
    st.error(
        f"讀取 Excel 檔案失敗，請確認檔案是否存在或格式是否正確。錯誤訊息: {e}"
    )
    return []


# 載入單字清單
vocabulary_list = load_vocabulary()

# --- 以下是補上的畫面渲染邏輯 ---
if len(vocabulary_list) > 0:
  st.success(f"🎉 成功載入單字！目前共有 {len(vocabulary_list)} 個單字。")

  # 1. 隨機抽考小工具
  st.subheader("🎯 每日單字小測驗")
  if st.button("抽一個單字來背"):
    word_item = random.choice(vocabulary_list)
    st.info(f"**單字 (Word):** {word_item.get('word')}")
    st.write(f"**詞性 (POS):** {word_item.get('pos')}")
    st.write(f"**音標 (Phonetic):** {word_item.get('phonetic')}")
    st.write(f"**意思 (Meaning):** {word_item.get('meaning')}")
    st.write(f"**例句 (Example):** {word_item.get('example')}")

  st.divider()

  # 2. 顯示完整單字列表表格
  st.subheader("📋 完整單字清單表")
  st.dataframe(pd.DataFrame(vocabulary_list), use_container_width=True)

else:
  st.warning("⚠️ 目前讀到的單字清單是空的，請檢查 Excel 檔案內容。")