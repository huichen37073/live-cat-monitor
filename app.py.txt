import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="喵数据 - 直播监测", page_icon="🐱", layout="wide")

st.markdown("""
<style>
    .stMetric { background-color: #FFF5EB; padding: 15px; border-radius: 15px; border: 2px dashed #FFB347; }
    .cat-welcome { background: linear-gradient(135deg, #FFF5EB, #FFE8D6); padding: 20px; border-radius: 20px; text-align: center; border: 2px solid #FF8C42; margin-bottom: 20px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="cat-welcome"><h1>🐱 喵数据：直播监测与AI复盘</h1><p>喵~ 今天的数据都帮你盯好了！🐾 小猫咪正在努力工作中...</p></div>', unsafe_allow_html=True)

st.subheader("📊 核心数据概览")
col1, col2, col3, col4 = st.columns(4)
col1.metric("👀 总观看人次", "125,430", "+12.5% 📈")
col2.metric("💬 总互动次数", "34,210", "+8.3% 📈")
col3.metric("💰 总 GMV", "¥ 458,900", "+15.7% 📈")
col4.metric("📉 平均互动率", "4.2%", "-1.1% 📉")

st.subheader("📈 近7日直播观看趋势")
df = pd.DataFrame({
    "日期": ["01-01", "01-02", "01-03", "01-04", "01-05", "01-06", "01-07"],
    "观看人数": [12000, 15000, 13500, 18000, 22000, 19500, 25000],
    "互动次数": [3000, 4200, 3800, 5100, 6500, 5800, 7200]
})
fig = px.line(df, x="日期", y=["观看人数", "互动次数"], color_discrete_sequence=["#FF8C42", "#7BC67E"])
fig.update_layout(plot_bgcolor="#FFF9F0", paper_bgcolor="#FFF9F0")
st.plotly_chart(fig, use_container_width=True)

st.subheader("🐾 最近直播记录")
live_data = pd.DataFrame({
    "主播": ["🐱 橘猫大魔王", "🐱 布偶小仙女", "🐱 狸花带货王"],
    "平台": ["抖音", "视频号", "抖音"],
    "观看人数": [45000, 12000, 38000],
    "GMV (¥)": [125000, 34000, 98000],
    "AI评分": ["🌟 92分", "🐾 78分", "🌟 88分"]
})
st.dataframe(live_data, use_container_width=True, hide_index=True)
