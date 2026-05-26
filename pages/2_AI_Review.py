import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="🧠 AI 复盘", page_icon="🧠", layout="wide")
st.title("🧠 AI 智能复盘报告生成器")

with st.sidebar:
    st.header("⚙️ 密钥与配置")
    api_key = st.text_input("🔑 输入你的 DeepSeek API Key", type="password", help="在 platform.deepseek.com 获取")
    
    st.header("📊 复盘参数")
    accounts = st.multiselect("选择账号", ["橘猫大魔王", "布偶小仙女"], default=["橘猫大魔王"])
    dimensions = st.multiselect("分析维度", ["观看数据", "互动分析", "成交转化", "流量来源"], default=["观看数据", "成交转化"])

if st.button("🚀 生成 AI 复盘报告", type="primary", use_container_width=True):
    if not api_key:
        st.error("喵！请在左侧输入 API Key 才能生成报告哦~ 🐾")
    else:
        with st.spinner("🐱 小猫咪正在疯狂分析数据中，请稍候..."):
            try:
                client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
                
                prompt = f"""你是一位资深的直播运营数据分析师，也是团队里的"数据小猫咪"。
                请根据以下虚拟数据生成一份Markdown格式的复盘报告。
                要求：包含核心结论、数据亮点、问题诊断、优化建议。适当使用猫咪emoji 🐱🐾。
                账号：{', '.join(accounts)}，维度：{', '.join(dimensions)}。
                虚拟数据：总观看12.5万，峰值在线3200人，GMV 12.5万，转化率2.1%。流量主要来自直播推荐(60%)。
                """
                
                response = client.chat.completions.create(
                    model="deepseek-chat",
                    messages=[
                        {"role": "system", "content": "你是专业的直播数据分析师，语言风格专业且带点可爱。"},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7
                )
                
                report = response.choices[0].message.content
                st.success("🎉 报告生成完毕！喵~")
                st.divider()
                st.markdown(report)
                
            except Exception as e:
                st.error(f"生成失败，请检查 API Key 是否正确，或余额是否充足：{str(e)}")
else:
    st.info("👈 请在左侧配置好参数和 API Key，然后点击生成按钮喵~")
