import random
import pandas as pd
import streamlit as st


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