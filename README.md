# 🤖 DataSense AI – Intelligent Data Analyst Agent

> **An AI-powered data analysis platform that transforms raw datasets into meaningful insights, visualizations, statistical analysis, machine learning predictions, SQL queries, Python analysis, and automated reports.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Framework-red.svg)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458.svg)](https://pandas.pydata.org/)
[![Scikit--learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-F7931E.svg)](https://scikit-learn.org/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Multi--Agent-orange.svg)](https://www.langchain.com/langgraph)
[![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-black.svg)](https://ollama.com/)

---

## 📌 Overview

**DataSense AI** is an intelligent data-analysis application designed to act as an **AI Data Analyst**.

Traditional data analysis often requires users to manually:

* Inspect datasets
* Understand column types
* Clean missing and duplicate values
* Detect outliers
* Perform exploratory data analysis
* Create visualizations
* Write SQL queries
* Write Python analysis code
* Build machine-learning models
* Interpret results
* Generate reports

DataSense AI combines these workflows into a single platform.

The user uploads a dataset, and DataSense AI analyzes the data through a combination of **data-processing modules, AI services, machine-learning pipelines, visualization tools, and an LLM-powered conversational interface**.

### 🎯 Main Goal

> **Make data analysis faster, easier, and accessible without requiring the user to manually perform every analytical step.**

---

# ✨ Key Features

## 📂 1. Dataset Upload

Users can upload datasets directly through the Streamlit interface.

### Supported formats

* CSV
* Excel
* Other tabular formats depending on the configured loader

After uploading, the dataset is stored in the application's session state and becomes available to the different analysis modules.

---

## 🔍 2. Automatic Data Profiling

DataSense AI automatically creates a profile of the uploaded dataset.

The profiling process identifies:

* Number of rows
* Number of columns
* Column names
* Data types
* Numerical columns
* Categorical columns
* Missing values
* Duplicate records
* Unique values
* Basic statistics

Example:

```text
Dataset Overview
----------------
Rows: 10,000
Columns: 12

Numerical Columns:
- Age
- Income
- Rating

Categorical Columns:
- Gender
- City
- Category
```

This provides the user with an immediate understanding of the dataset.

---

# 🧹 3. Automated Data Cleaning

DataSense AI provides utilities for common data-cleaning operations.

### Cleaning capabilities include:

* Missing-value detection
* Missing-value handling
* Duplicate detection
* Data-type conversion
* Basic preprocessing
* Outlier detection

The application can identify potential data-quality issues before analysis.

### Example workflow

```text
Raw Dataset
     ↓
Missing Value Detection
     ↓
Duplicate Detection
     ↓
Data Type Validation
     ↓
Outlier Detection
     ↓
Cleaned Dataset
```

---

# 📊 4. Exploratory Data Analysis

The platform performs exploratory analysis to help users understand patterns in their data.

Depending on the dataset, DataSense AI can analyze:

* Distribution of numerical variables
* Categorical frequencies
* Relationships between variables
* Correlations
* Statistical summaries
* Trends and patterns

The objective is to answer questions such as:

> What does this dataset contain?

> Which variables are important?

> Are there correlations between variables?

> Are there unusual observations?

---

# 📈 5. Automatic Data Visualization

DataSense AI generates visualizations based on the dataset and selected analytical requirements.

Possible visualizations include:

* Bar charts
* Line charts
* Histograms
* Scatter plots
* Box plots
* Correlation heatmaps
* Distribution plots
* Categorical comparisons

The visualization layer is designed to make analytical findings easier to understand.

---

# 🧠 6. AI-Powered Insight Generation

One of the major features of DataSense AI is converting analytical results into **human-readable insights**.

Instead of only showing:

```text
Mean Rating = 4.21
Median Rating = 4.30
```

the AI can transform the result into an interpretation such as:

```text
The dataset shows generally high ratings, with the
majority of observations concentrated around the
4–5 range.
```

This makes the system more useful for users who understand business problems but may not have advanced statistical knowledge.

---

# 💬 7. AI Data Analyst Chat

DataSense AI includes a conversational interface where users can interact with their dataset using natural language.

Users can ask questions such as:

```text
What are the most important columns?

Which category has the highest average sales?

Are there any missing values?

What is the correlation between price and rating?

Give me insights from this dataset.

Which factors appear to influence the target variable?
```

The AI analyzes the available dataset context and provides a natural-language response.

---

# 🐍 8. Python Code Execution Agent

DataSense AI can generate and execute Python-based analytical operations.

This allows users to perform custom analysis without manually writing every line of code.

Typical workflow:

```text
User Question
     ↓
AI understands request
     ↓
Python code generation
     ↓
Code execution
     ↓
Result
     ↓
AI interpretation
```

For example, a user may ask:

```text
Find the average sales for each region.
```

The system can generate an appropriate Pandas operation, execute it, and return the result.

---

# 🗄️ 9. SQL Agent

DataSense AI includes an SQL-oriented analysis component.

The objective is to allow users to interact with data using natural-language questions instead of manually constructing SQL queries.

Example:

```text
User:
Show the top 10 products by revenue.
```

The system can translate the request into an SQL-style analytical operation and return the result.

This feature demonstrates the integration of:

* Natural Language Processing
* SQL generation
* Data querying
* AI-assisted analytics

---

# 🤖 10. Automated Machine Learning

DataSense AI includes an AutoML component for basic predictive modelling.

The AutoML pipeline can:

1. Identify the target variable
2. Prepare features
3. Handle preprocessing
4. Select suitable models
5. Train models
6. Evaluate model performance
7. Compare results

Depending on the problem type, models can include algorithms from **Scikit-learn**.

### Example machine-learning workflow

```text
Dataset
   ↓
Target Selection
   ↓
Feature Preparation
   ↓
Preprocessing
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Model Comparison
```

Evaluation metrics can include:

### Regression

* MAE
* MSE
* RMSE
* R²

### Classification

* Accuracy
* Precision
* Recall
* F1-score

---

# 📝 11. Automated Report Generation

DataSense AI is designed to combine analytical outputs into a structured report.

A generated report can include:

* Dataset overview
* Data-quality findings
* Statistical summaries
* EDA findings
* Visualizations
* Machine-learning results
* AI-generated insights
* Recommendations

The objective is to reduce the amount of manual documentation required after completing an analysis.

---

# 🧩 12. Multi-Agent Architecture

DataSense AI is designed around a modular AI-agent architecture.

Different analytical tasks can be handled by specialized components.

Conceptually:

```text
                    ┌───────────────────┐
                    │      User         │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │   Streamlit UI    │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │  AI / Controller  │
                    └─────────┬─────────┘
                              │
            ┌─────────────────┼─────────────────┐
            │                 │                 │
            ▼                 ▼                 ▼
      Data Analysis       SQL Agent       Python Agent
            │                 │                 │
            ▼                 ▼                 ▼
       EDA / Stats       Query Engine      Code Execution
            │                 │                 │
            └─────────────────┼─────────────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Insight Generation│
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │      User         │
                    └───────────────────┘
```

The architecture is designed to make the application easier to extend as new agents and analytical capabilities are added.

---

# 🧠 LLM Integration

DataSense AI uses a configurable LLM layer.

The project is designed so that the LLM provider can be changed without heavily modifying the rest of the application.

The project currently supports a **local Ollama-based setup**.

### Why Ollama?

Using a local LLM provides several advantages:

* No mandatory external API dependency
* Reduced API cost
* Local inference
* Better control over data
* Useful for development and experimentation

Example configuration:

```env
LLM_PROVIDER=ollama
OLLAMA_MODEL=qwen3:4b
```

The exact environment variables may vary depending on the current project configuration.

---

# 🔗 LangGraph

**LangGraph** is used as the foundation for orchestrating AI workflows.

Instead of treating the AI system as one large function, the application can represent different operations as nodes in a graph.

Conceptually:

```text
START
  │
  ▼
Dataset Analysis
  │
  ▼
Determine User Intent
  │
  ├───────────────┐
  ▼               ▼
Python Agent    SQL Agent
  │               │
  └───────┬───────┘
          ▼
   Insight Generation
          │
          ▼
         END
```

This architecture makes it easier to create complex workflows involving multiple specialized AI components.

---

# 🏗️ Project Architecture

The project follows a modular architecture.

```text
DataSense_AI/
│
├── app/
│   ├── Home.py
│   │
│   ├── pages/
│   │   ├── ...
│   │
│   └── components/
│       ├── ...
│
├── ai/
│   ├── llm/
│   │   ├── config.py
│   │   ├── provider.py
│   │   ├── prompts.py
│   │   └── memory.py
│   │
│   └── graph/
│       ├── nodes/
│       └── graph.py
│
├── services/
│   ├── ai_summary.py
│   ├── dataset_profile.py
│   └── ...
│
├── utils/
│   ├── file_loader.py
│   ├── data_profiler.py
│   ├── duplicate.py
│   ├── missing_values.py
│   ├── datatype_converter.py
│   ├── outliers.py
│   └── automl.py
│
├── tests/
│   ├── ...
│
├── .env
├── requirements.txt
├── README.md
└── ...
```

> The exact directory structure may evolve as additional agents and services are implemented.

---

# ⚙️ Technology Stack

| Technology       | Purpose                                           |
| ---------------- | ------------------------------------------------- |
| **Python**       | Core programming language                         |
| **Streamlit**    | Web application and UI                            |
| **Pandas**       | Data manipulation and analysis                    |
| **NumPy**        | Numerical computation                             |
| **Matplotlib**   | Data visualization                                |
| **Plotly**       | Interactive visualization                         |
| **Scikit-learn** | Machine learning and preprocessing                |
| **LangGraph**    | AI workflow orchestration                         |
| **LLM**          | Natural-language reasoning and insight generation |
| **Ollama**       | Local LLM inference                               |
| **Git**          | Version control                                   |
| **GitHub**       | Source-code management                            |

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Vasudevnarvekar/DataSense_AI.git
```

Navigate into the project:

```bash
cd DataSense_AI
```

---

# 🐍 2. Create a Virtual Environment

Create the environment:

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

---

# 📦 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

# 🧠 4. Install Ollama

Download and install Ollama from its official website.

Then verify the installation:

```bash
ollama --version
```

Pull the required model:

```bash
ollama pull qwen3:4b
```

You can verify installed models using:

```bash
ollama list
```

---

# 🔐 5. Configure Environment Variables

Create a `.env` file in the project root.

Example:

```env
LLM_PROVIDER=ollama
OLLAMA_MODEL=qwen3:4b
```

> **Important:** Never commit API keys, passwords, tokens, or other secrets to GitHub.

Add `.env` to `.gitignore`:

```text
.env
venv/
__pycache__/
*.pyc
```

---

# ▶️ 6. Run the Application

Start the Streamlit application:

```bash
streamlit run app/Home.py
```

The application will open in your browser.

---

# 🔄 Application Workflow

The general workflow of DataSense AI is:

```text
                 Upload Dataset
                       │
                       ▼
              Dataset Profiling
                       │
                       ▼
                Data Cleaning
                       │
                       ▼
              Exploratory Analysis
                       │
                       ▼
                Visualization
                       │
                       ▼
             AI Insight Generation
                       │
            ┌──────────┴──────────┐
            ▼                     ▼
       SQL Analysis          Python Analysis
            │                     │
            └──────────┬──────────┘
                       ▼
                     AutoML
                       │
                       ▼
               Report Generation
                       │
                       ▼
                  Final Insights
```

---

# 💡 Example Use Case

Suppose a user uploads a customer-sales dataset containing:

```text
Customer_ID
Age
Gender
City
Product
Quantity
Price
Revenue
Rating
```

DataSense AI can automatically help the user answer:

### Dataset questions

```text
How many customers are present?
What columns are available?
Which columns contain missing values?
```

### Business questions

```text
Which city generates the highest revenue?
Which product is most popular?
What is the average customer rating?
```

### Statistical questions

```text
What is the correlation between price and revenue?
Are there any outliers?
```

### Machine-learning questions

```text
Can revenue be predicted?
Which features are important?
Which model performs best?
```

### AI questions

```text
Summarize the dataset.
Give me the most important business insights.
What actions should a business take based on this data?
```

---

# 🛡️ Data Safety

DataSense AI is designed with local processing in mind.

When using the Ollama configuration, the LLM can run locally rather than requiring the dataset to be sent to an external LLM API.

However, users should still avoid uploading highly sensitive or confidential data unless the deployment environment has been appropriately secured.

---

# 🧪 Testing

The project contains test scripts for validating different components.

Examples:

```bash
python test_llm.py
```

```bash
python test_summary.py
```

```bash
python test_graph.py
```

Testing helps verify:

* LLM connectivity
* AI-generated summaries
* Graph execution
* Individual service functionality
* Integration between components

---

# 📌 Current Development Status

DataSense AI is an actively developed project.

### Implemented / Developed Components

* [x] Project setup
* [x] Dataset upload
* [x] Dataset profiling
* [x] Data cleaning utilities
* [x] Missing-value analysis
* [x] Duplicate detection
* [x] Data-type conversion
* [x] Outlier detection
* [x] Exploratory data analysis
* [x] Data visualization
* [x] AI recommendation/insight components
* [x] Python analysis/code execution
* [x] AutoML pipeline
* [x] LLM integration
* [x] Local Ollama support
* [x] AI summary generation
* [x] AI chat functionality
* [x] LangGraph workflow development
* [ ] Advanced agent orchestration
* [ ] Advanced report generation
* [ ] Production deployment
* [ ] Comprehensive automated testing
* [ ] Performance optimization

---

# 🗺️ Future Roadmap

The long-term roadmap includes:

### Phase 1 — Data Intelligence

* Improved automatic profiling
* Advanced data-quality checks
* Intelligent cleaning recommendations
* Advanced statistical analysis

### Phase 2 — AI Agents

* Specialized EDA Agent
* Visualization Agent
* SQL Agent
* Python Agent
* ML Agent
* Report Agent
* Recommendation Agent

### Phase 3 — Advanced AI

* Improved LangGraph orchestration
* Better conversational memory
* Context-aware analysis
* Multi-step reasoning
* Agent-to-agent communication

### Phase 4 — Reporting

* Automated PDF reports
* Executive summaries
* Business recommendations
* Downloadable analytical reports

### Phase 5 — Production

* Cloud deployment
* Authentication
* User management
* Database integration
* Scalable inference
* Monitoring
* Logging
* CI/CD

---

# 🎯 Project Objectives

The main objectives of DataSense AI are:

1. **Automate repetitive data-analysis tasks**
2. **Reduce the technical barrier to data analysis**
3. **Combine traditional analytics with generative AI**
4. **Provide natural-language interaction with datasets**
5. **Create an extensible multi-agent architecture**
6. **Generate actionable insights instead of only raw statistics**
7. **Explore practical applications of LLMs in data analytics**

---

# 🧠 What This Project Demonstrates

DataSense AI demonstrates practical knowledge of:

### Data Analytics

* Data cleaning
* Exploratory data analysis
* Statistical analysis
* Data visualization
* Data profiling

### Machine Learning

* Feature preprocessing
* Regression
* Classification
* Model evaluation
* Automated model comparison

### Generative AI

* LLM integration
* Prompt engineering
* AI-generated insights
* Conversational analytics
* Local LLM inference

### AI Agents

* Agent architecture
* Tool-based execution
* Workflow orchestration
* LangGraph
* Multi-step AI workflows

### Software Engineering

* Modular architecture
* Git/GitHub
* Virtual environments
* Environment configuration
* Testing
* Error handling

---

# 📊 High-Level Architecture

```text
                         ┌──────────────────────┐
                         │        USER          │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │    STREAMLIT UI      │
                         └──────────┬───────────┘
                                    │
                                    ▼
                    ┌──────────────────────────────┐
                    │       DATA PROCESSING        │
                    │                              │
                    │ Profiling │ Cleaning │ EDA   │
                    └──────────────┬───────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────┐
                    │        AI ORCHESTRATOR       │
                    │          LangGraph            │
                    └──────────────┬───────────────┘
                                   │
             ┌─────────────────────┼─────────────────────┐
             │                     │                     │
             ▼                     ▼                     ▼
      ┌────────────┐       ┌────────────┐       ┌────────────┐
      │ Python     │       │ SQL        │       │ AutoML     │
      │ Agent      │       │ Agent      │       │ Pipeline   │
      └─────┬──────┘       └─────┬──────┘       └─────┬──────┘
            │                    │                    │
            └────────────────────┼────────────────────┘
                                 │
                                 ▼
                      ┌─────────────────────┐
                      │    LLM SERVICE      │
                      │       Ollama        │
                      └──────────┬──────────┘
                                 │
                                 ▼
                      ┌─────────────────────┐
                      │ INSIGHTS / REPORT   │
                      └─────────────────────┘
```

---

# 📷 Screenshots

Add screenshots of the application here.

Example:

```markdown
## Dashboard

![DataSense AI Dashboard](screenshots/dashboard.png)

## Dataset Analysis

![Dataset Analysis](screenshots/analysis.png)

## AI Chat

![AI Chat](screenshots/ai-chat.png)

## AutoML

![AutoML](screenshots/automl.png)
```

Recommended screenshots:

1. Home page
2. Dataset upload
3. Dataset profiling
4. EDA dashboard
5. Visualizations
6. AI insights
7. AI chat
8. AutoML results
9. Final report

---

# 🎥 Demo

Add your project demonstration video here.

```markdown
## 🎥 Demo

[Watch DataSense AI Demo](YOUR_VIDEO_LINK)
```

You can also add a short GIF demonstrating the application.

---

# 📁 Recommended GitHub Repository Structure

```text
DataSense_AI/
│
├── app/
├── ai/
├── services/
├── utils/
├── tests/
│
├── screenshots/
│
├── .gitignore
├── README.md
├── requirements.txt
├── LICENSE
└── .env.example
```

---

# 🔧 Configuration

The application is designed to support configurable AI providers.

A future configuration could look like:

```env
LLM_PROVIDER=ollama
OLLAMA_MODEL=qwen3:4b
```

Potential future providers:

```text
Ollama
OpenAI
Other compatible LLM providers
```

This provider abstraction allows the AI layer to evolve without redesigning the complete application.

---

# ⚠️ Limitations

DataSense AI is currently a development/research project and has several limitations.

### Current limitations include:

* LLM output can occasionally be inaccurate
* Generated Python code requires validation
* AI-generated insights may require human verification
* Large datasets can increase processing time
* Local LLM performance depends on available hardware
* AutoML performance depends on dataset quality
* Production-level security and authentication are not yet implemented

Therefore:

> **AI-generated analysis should be treated as decision support rather than an unquestionable source of truth.**

---

# 🔮 Future Improvements

Potential improvements include:

* RAG-based dataset knowledge retrieval
* Vector database integration
* Better long-term conversational memory
* Advanced anomaly detection
* Feature importance analysis
* Automated feature engineering
* More machine-learning algorithms
* Deep-learning support
* Natural-language SQL execution
* Advanced chart recommendations
* PDF/Excel report export
* User authentication
* Cloud deployment
* Docker containerization
* CI/CD pipeline
* Model monitoring
* Data-drift detection
* Production-grade logging

---

# 👨‍💻 Developer

**Vasudev Narvekar**

Computer Engineering | Data Analytics | AI/ML

Interested in:

* Data Analytics
* Machine Learning
* Generative AI
* AI Agents
* Python
* Data Engineering

---

# ⭐ Why DataSense AI?

DataSense AI is not simply a dashboard for displaying charts.

The project explores how **traditional data analytics can be combined with Generative AI and agent-based workflows** to create an intelligent analytical system.

The core idea is:

```text
Raw Data
   ↓
Data Understanding
   ↓
Data Cleaning
   ↓
Analysis
   ↓
AI Reasoning
   ↓
Insights
   ↓
Business Decisions
```

Instead of requiring users to know exactly **how to perform every analytical operation**, DataSense AI aims to allow users to focus on **what they want to understand from their data**.

---

# 📜 License

This project is intended for educational, research, and portfolio purposes.

Add your preferred license here, for example:

```text
MIT License
```

---

# ⭐ Support

If you find this project interesting:

* ⭐ Star the repository
* 🍴 Fork the project
* 🐛 Report issues
* 💡 Suggest improvements
* 🔀 Submit pull requests

---

## 🚀 DataSense AI

**Turning Data into Decisions with AI.**
