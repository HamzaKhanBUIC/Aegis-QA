import streamlit as st
from agent_core import AegisSwarm
import time

# 1. PAGE CONFIGURATION (Must be the first Streamlit command)
st.set_page_config(
    page_title="Aegis-QA | Zero-Touch Testing Swarm",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. CUSTOM CSS INJECTION (Hides default Streamlit branding and polishes UI)
st.markdown("""
    <style>
        /* Hide Streamlit header and footer */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Custom Button Styling */
        .stButton>button {
            width: 100%;
            border-radius: 8px;
            background-color: #0f62fe;
            color: white;
            font-weight: bold;
            border: none;
            padding: 0.75rem;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #0353e9;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            transform: translateY(-2px);
            color: white;
        }
        
        /* Text Area Polish */
        .stTextArea textarea {
            border-radius: 8px;
            border: 1px solid #393939;
            font-family: 'Courier New', Courier, monospace;
        }
    </style>
""", unsafe_allow_html=True)

# 3. SIDEBAR ARCHITECTURE
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/IBM_logo.svg/800px-IBM_logo.svg.png", width=100)
    st.title("🛡️ Aegis-QA Swarm")
    st.markdown("### Powered by IBM watsonx.ai & Bob")
    st.markdown("---")
    st.info(
        "**Agentic Nodes Active:**\n"
        "- 🕵️‍♂️ Edge-Case Auditor\n"
        "- 🧪 Test-Weaver Agent\n"
        "- 📚 Doc-Gen Agent"
    )
    st.markdown("---")
    st.caption("v1.0.0-Enterprise | Zero-Leak Protocol Active")

# 4. MAIN STAGE ARCHITECTURE
st.title("⚡ Zero-Touch Security & Testing Swarm")
st.markdown("Drop your raw, untested, or messy code below. The Aegis Antigravity Swarm will instantly audit it for vulnerabilities and generate production-ready PyTest suites.")

# Layout Split: Code Input on Left, Results on Right
col1, col2 = st.columns([1, 1.2], gap="large")

with col1:
    st.subheader("📥 Target Payload (Code)")
    code_input = st.text_area(
        "Paste Python script or function here:", 
        height=350, 
        placeholder="def vulnerable_function(user_input):\n    # Drop code here..."
    )
    
    if st.button("🚀 INITIATE SWARM AUDIT"):
        if not code_input.strip():
            st.warning("⚠️ Please provide a code payload to audit.")
        else:
            with st.spinner("🤖 Orchestrating Watsonx AI Swarm... Analyzing context..."):
                try:
                    # Initialize Swarm and Run Audit
                    swarm = AegisSwarm()
                    results = swarm.run_audit(code_input)
                    
                    # Store results in session state to persist them
                    st.session_state['audit_results'] = results
                    st.session_state['audit_complete'] = True
                    
                    st.toast("✅ Swarm Audit Complete!", icon="🚀")
                    st.balloons() # The Wow Factor for the judges
                except Exception as e:
                    st.error(f"❌ Swarm Failure: {str(e)}")

with col2:
    st.subheader("📊 Swarm Intelligence Output")
    
    # Check if we have results in session state
    if 'audit_complete' in st.session_state and st.session_state['audit_complete']:
        results = st.session_state['audit_results']
        
        # Sleek Tabs for Output
        tab1, tab2 = st.tabs(["🧪 Generated Unit Tests (PyTest)", "🛡️ Security & Doc Report"])
        
        with tab1:
            st.markdown("### Automated Test Suite")
            st.code(results.get('unit_tests', '# No tests generated.'), language='python')
            st.download_button("💾 Download tests.py", results.get('unit_tests', ''), file_name="test_aegis.py")
            
        with tab2:
            st.markdown("### Vulnerability & Documentation Audit")
            st.markdown(results.get('security_docs', '*No documentation generated.*'))
            st.download_button("💾 Download report.md", results.get('security_docs', ''), file_name="aegis_report.md")
    else:
        st.info("👈 Initiate the swarm on the left to see intelligent outputs here. Awaiting payload...")