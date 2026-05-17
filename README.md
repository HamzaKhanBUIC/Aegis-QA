# 🛡️ Aegis-QA: Zero-Touch Security & Testing Swarm

> **Automated Unit Testing & Security Auditing powered by Multi-Agent AI**

[![Built with IBM watsonx.ai](https://img.shields.io/badge/Built%20with-IBM%20watsonx.ai-0f62fe?style=for-the-badge&logo=ibm)](https://www.ibm.com/watsonx)
[![Powered by IBM Bob](https://img.shields.io/badge/Powered%20by-IBM%20Bob-0f62fe?style=for-the-badge)](https://www.ibm.com/bob)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Streamlit Live](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://aegis-app1.streamlit.app/)

---

## 🚨 The Problem

Modern software development faces a critical bottleneck:

- **Manual Unit Testing** consumes 30-40% of development time
- **Security Audits** require specialized expertise and are often delayed until late in the cycle
- **Code Coverage** gaps lead to production bugs and vulnerabilities
- **Documentation** of security findings is tedious and inconsistent

**Result:** Developers spend more time writing tests than building features, and security issues slip through the cracks.

---

## ✨ The Solution

**Aegis-QA** revolutionizes the testing and security workflow with a **Multi-Agent Swarm Architecture** that:

🤖 **Analyzes your codebase** using IBM watsonx.ai's Granite-3-8b model  
🧪 **Generates comprehensive PyTest suites** with edge cases and mocks  
🔒 **Performs automated security audits** identifying vulnerabilities (SQL injection, XSS, auth flaws)  
📄 **Creates professional documentation** for all findings  
⚡ **Delivers results in minutes**, not hours or days

Built entirely with **IBM Bob** during the IBM Bob Hackathon, Aegis-QA demonstrates the power of AI-assisted development and multi-agent orchestration.

---

## 🎯 Key Features

### 🎨 **Intuitive Streamlit UI**
- Clean, modern interface for uploading Python files
- Real-time progress tracking with agent status updates
- Downloadable test files and security reports

### 🧠 **Powered by IBM watsonx.ai**
- **Granite-3-8b-Instruct** model for intelligent code analysis
- Context-aware test generation with realistic edge cases
- Security vulnerability detection using industry best practices

### 🤝 **Multi-Agent Swarm Architecture**
- **Test Generator Agent**: Creates comprehensive PyTest suites
- **Security Auditor Agent**: Identifies OWASP Top 10 vulnerabilities
- **Coordinator Agent**: Orchestrates workflow and ensures quality

### 📊 **Comprehensive Output**
- **Unit Tests**: Production-ready PyTest files with fixtures and mocks
- **Security Reports**: Detailed vulnerability assessments with severity ratings
- **Code Coverage**: Recommendations for improving test coverage

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- IBM watsonx.ai API credentials
- Git (for cloning the repository)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Aegis-QA.git
   cd Aegis-QA
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure IBM watsonx.ai credentials**
   
   Create a `.env` file in the root directory:
   ```env
   WATSONX_API_KEY=your_api_key_here
   WATSONX_PROJECT_ID=your_project_id_here
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Access the UI**
   
   Open your browser and navigate to `http://localhost:8501`

### Usage

1. **Upload** your Python file using the file uploader
2. **Click** "🚀 Analyze & Generate Tests" to start the swarm
3. **Watch** as agents analyze your code in real-time
4. **Download** generated test files and security reports
5. **Review** findings and integrate into your workflow

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Streamlit UI                         │
│              (User Interface Layer)                     │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              Agent Coordinator                          │
│         (Orchestration & Workflow)                      │
└─────┬───────────────────────────────────────────┬───────┘
      │                                           │
      ▼                                           ▼
┌─────────────────────┐              ┌─────────────────────┐
│  Test Generator     │              │  Security Auditor   │
│      Agent          │              │       Agent         │
│                     │              │                     │
│ • PyTest Creation   │              │ • OWASP Analysis    │
│ • Edge Cases        │              │ • Vulnerability     │
│ • Mock Generation   │              │   Detection         │
└──────────┬──────────┘              └──────────┬──────────┘
           │                                    │
           └────────────────┬───────────────────┘
                            ▼
                ┌───────────────────────┐
                │   IBM watsonx.ai      │
                │   Granite-3-8b Model  │
                └───────────────────────┘
```

---

## 🎓 Hackathon Compliance

### IBM Bob Hackathon Submission

**Project Name:** Aegis-QA: Zero-Touch Security & Testing Swarm

**Category:** Developer Tools & Productivity

**Built With:**
- IBM Bob (AI-assisted development)
- IBM watsonx.ai (Granite-3-8b-Instruct model)
- Python, Streamlit, PyTest

**Key Innovation:** Multi-agent swarm architecture for automated testing and security auditing

### 📹 Demo & Links

- **Live Demo:** [https://aegis-app1.streamlit.app/]
- **Hackathon Submission:** [https://lablab.ai/ai-hackathons/ibm-bob-hackathon/agentic-innovation-node/aegis-qa-zero-touch-security-and-testing-swarm]

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| **AI Model** | IBM watsonx.ai Granite-3-8b-Instruct |
| **Frontend** | Streamlit |
| **Backend** | Python 3.8+ |
| **Testing Framework** | PyTest |
| **Agent Framework** | Custom Multi-Agent System |
| **Development** | IBM Bob AI Assistant |

---

## 📈 Future Enhancements

- [ ] Support for additional programming languages (JavaScript, Java, Go)
- [ ] Integration with CI/CD pipelines (GitHub Actions, Jenkins)
- [ ] Real-time collaboration features for team workflows
- [ ] Advanced security scanning (dependency vulnerabilities, license compliance)
- [ ] Performance testing and load analysis agents
- [ ] VS Code extension for in-editor testing

---

## 🤝 Contributing

We welcome contributions! This project was built during the IBM Bob Hackathon, and we're excited to continue improving it with the community.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **IBM watsonx.ai** for providing the powerful Granite-3-8b model
- **IBM Bob** for revolutionizing the development experience
- **IBM Bob Hackathon** organizers for this incredible opportunity
- The open-source community for inspiration and tools

---

## 📧 Contact

**Project Maintainer:** Hamza Imran

**Email:** hamza135252@gmail.com

**GitHub:** [@HamzaKhanBUIC](https://github.com/HamzaKhanBUIC)

**LinkedIn:** [@Hamza Imran](www.linkedin.com/in/hamza-imran-17569b383)

---

<div align="center">

### ⭐ If you find Aegis-QA useful, please star this repository! ⭐

**Built with ❤️ using IBM Bob and IBM watsonx.ai**

</div>
