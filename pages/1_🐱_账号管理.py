import streamlit as st

st.set_page_config(page_title="账号管理", page_icon="🐱")
st.title("🐱 监测账号管理中心")
st.markdown("在这里添加和管理你需要监测的抖音/视频号账号喵~")

with st.form("add_account_form"):
    st.subheader("➕ 添加新账号")
    platform = st.selectbox("选择平台", ["抖音", "视频号"])
    account_name = st.text_input("账号名称/备注", placeholder="例如：橘猫大魔王")
    account_id = st.text_input("账号主页链接或ID", placeholder="粘贴链接...")
    keywords = st.text_input("监测关键词 (用逗号隔开)", placeholder="美妆, 护肤, 穿搭")
    
    submitted = st.form_submit_button("🐾 确认添加")
    if submitted:
        if account_name and account_id:
            st.success(f"喵！成功添加 {platform} 账号：{account_name} 🎉")
        else:
            st.error("请把账号名称和链接填完整哦~")

st.divider()
st.subheader("📋 当前监测列表")
st.info("当前列表为演示数据，实际使用时会连接数据库读取。")

st.table({
    "账号名称": ["橘猫大魔王", "布偶小仙女"],
    "平台": ["抖音", "视频号"],
    "状态": ["🟢 监测中", "🟢 监测中"],
    "粉丝数": ["12.5w", "8.2w"]
})
