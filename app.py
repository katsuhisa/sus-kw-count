# app.py
import streamlit as st
from page import batch_process, batch_process_graph

# ページを追加するための辞書
PAGES = {
    # "分類CSVアップロード": upload_csv,
    "単語出現回数カウント": batch_process,
    "グラフ描写": batch_process_graph
}

def main():
    st.sidebar.title("📜集計表サステナ単語カウントアプリ")
    
    st.sidebar.markdown("### :orange[処理のレベルを選択]")  # サイドバーに分類の選択を追加
    selection = st.sidebar.selectbox("", list(PAGES.keys()))
    page = PAGES[selection]
    page.app()

if __name__ == "__main__":
    main()
