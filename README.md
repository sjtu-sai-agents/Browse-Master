# 🚀 BrowseMaster: Scalable Web Browsing via Tool-Augmented Programmatic Agent Pair

**BrowseMaster** is a next-generation LLM-based web browsing agent that addresses the shortcomings of traditional search and existing agents by uniting **broad, code-driven search** with **deep, strategic reasoning**.  
Its **Planner–Executor** framework delivers scalable, coherent, and efficient information seeking, achieving strong results on both BrowseComp and BrowseComp-ZH benchmarks.

[![arXiv](https://img.shields.io/badge/arXiv-2508.09129-b31b1b.svg)](https://arxiv.org/abs/2508.09129)

![BrowseMaster Results](./assets/result.PNG)

## 🛠️ Framework

![BrowseMaster Framework](./assets/fig1.png)

## 🔑 Key Features

- 🧠 **Planner–Executor Framework** – Separates large-scale, code-driven search from high-level reasoning for cleaner context and deeper thinking.  
- 📜 **Code-Based Search Primitives** – Execute `batch_search`, `check_condition`, `generate_keywords` operations over thousands of pages with minimal context overhead.  
- 🎯 **Confidence-Guided Replanning** – Dynamically reset strategy when confidence is low to avoid premature convergence.  

## 📖 Documentation

### Prompts and Examples
- Detailed prompts for both planner and executor components are available in the `prompts/` directory
- Sample responses from BrowseComp evaluations can be found in `logs/example.jsonl`

### Getting Started

#### Prerequisites
- For sandbox setup and code execution environment, please refer to [mcp_sandbox](https://github.com/sjtu-sai-agents/mcp_sandbox)
- Note that we use locally deployed DeepSeek-R1-0528 model, instead of api.

#### Configuration
1. Configure model endpoints in `configs/model_config.yaml`:
   - DeepSeek-R1-0528 model URL
   - DeepSeek-R1 model URL
   - ToolBox URL

#### Running BrowseMaster
1. Ensure all prerequisites are met (environment, toolbox, and configuration)
2. For single query inference, execute:
```bash
python agent.py
```

## 📊 Experiments

### 🚀 Scaling Search Calls & Computation Efficiency
<p align="center">
  <img src="./assets/scalling.PNG" alt="Scaling" width="80%" />
</p>

### 🌐 Breadth of Domains Explored
<p align="center">
  <img src="./assets/domains.PNG" alt="Domains" width="80%" />
</p>