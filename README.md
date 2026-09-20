# 🚀 AI Career Skill Gap Analyzer

An AI-powered career guidance web application built with **Streamlit** and **Google Gemini**. The application analyzes a user's current skills against their target career role and generates a personalized skill-gap analysis, learning roadmap, and project suggestions.

## 🌐 Live Website

The project is deployed using **Streamlit Community Cloud**.

👉 **Visit the AI Career Skill Gap Analyzer:**
[https://ai-career-skill-gap-analyzer-b7kayyhldtypbddf65u3nc.streamlit.app](https://ai-career-skill-gap-analyzer-b7kayyhldtypbddf65u3nc.streamlit.app)

You can enter your target role, experience level, and current skills to receive an AI-generated career roadmap.

---

## 📌 Table of Contents

1. Overview
2. Project Architecture & Workflow
3. Key Features
4. Tech Stack
5. Local Installation & Setup
6. Deployment
7. Project Structure
8. Future Improvements
9. License

---

## 🔍 Overview

Breaking into specialized fields such as **AI Engineering** can be challenging because of rapidly evolving technologies and constantly changing industry requirements.

The **AI Career Skill Gap Analyzer** helps users understand what they need to learn to move from their current skill level toward their desired career role.

The application takes the following inputs:

* 🎯 Target Career Role
* 📊 Experience Level
* 🧠 Current Skills

Using Google's Gemini AI, the application analyzes these inputs and generates:

* Missing skills and competencies
* Personalized learning phases
* A structured learning roadmap
* Portfolio project suggestions
* Practical next steps

The goal is to turn an unclear career path into a structured and actionable learning journey.

---

## 🏗️ Project Architecture & Workflow

**User Input**

Target Role → Experience Level → Current Skills

↓

**Streamlit Interface**

Processes the user's inputs and handles interaction with the application.

↓

**Google Gemini**

The AI model analyzes the user's current profile against the requirements of their target career role.

↓

**AI Skill Analysis**

The application identifies:

* Skill gaps
* Learning phases
* Recommended projects

↓

**Personalized Roadmap**

The generated recommendations are displayed to the user through the Streamlit interface.

---

## ✨ Key Features

### 🎯 AI-Powered Skill Gap Analysis

Analyzes the user's current skills against their target career role and identifies important skills and competencies that may need to be developed.

### 🧠 Personalized Learning Roadmap

Generates a structured, phase-by-phase roadmap based on the user's current experience and desired career path.

### 📚 Chronological Learning Phases

Organizes recommended topics into logical learning stages, helping users understand what to focus on first and what to learn next.

### 💡 Portfolio Project Suggestions

Suggests practical projects that can help users apply their skills and build a stronger technical portfolio.

### ⚡ Dynamic Skill Processing

Allows users to enter multiple existing skills and generates an analysis based on their individual profile.

### 🛡️ Error Handling

Includes exception handling to provide a smoother experience when API requests or other operations encounter errors.

### 🌐 Interactive Web Interface

Built with Streamlit, allowing users to interact with the application directly through a simple web interface.

---

## 🛠️ Tech Stack

**Python** — Core programming language

**Streamlit** — Web application and user interface

**Google GenAI SDK** — Integration with Google's generative AI models

**Gemini** — AI-powered career analysis and roadmap generation

**Python-Dotenv** — Environment variable management

**Git & GitHub** — Version control and project hosting

**Streamlit Community Cloud** — Application deployment

---

## 💻 Local Installation & Setup

Follow the steps below to run the project locally.

### 1. Clone the Repository

Clone the repository from GitHub and navigate into the project folder.

Repository:
[https://github.com/shivisrivastava0212/AI-Career-Skill-Gap-Analyzer](https://github.com/shivisrivastava0212/AI-Career-Skill-Gap-Analyzer)

### 2. Install Dependencies

Install the required Python packages using the project's `requirements.txt` file.

### 3. Configure Environment Variables

Create a `.env` file in the root directory and add your Gemini API key.

### 4. Run the Application

Run the Streamlit application locally using:

`streamlit run app.py`

Once the command runs successfully, Streamlit will provide a local URL where you can access the application.

---

## ☁️ Deployment

The application is deployed using **Streamlit Community Cloud**.

### Deployment Configuration

* **Branch:** `main`
* **Main File:** `app.py`
* **Python Version:** `3.12`
* **Deployment Platform:** Streamlit Community Cloud
* **Required Secret:** `GEMINI_API_KEY`

---

## 📂 Project Structure

The project follows a simple structure:

**AI-Career-Skill-Gap-Analyzer/**

* `app.py` — Main Streamlit application
* `requirements.txt` — Required Python dependencies
* `.gitignore` — Files and folders excluded from Git
* `README.md` — Project documentation
* `LICENSE` — Project license

---

## 🔮 Future Improvements

Potential improvements for future versions include:

* 📄 Resume upload and automatic skill extraction
* 🎯 Job-description-based skill gap analysis
* 📊 Visual representation of skill gaps
* 📅 Personalized weekly learning plans
* 🔗 Integration with online learning platforms
* 💼 Internship and job recommendation features
* 📈 Learning progress tracking
* 🤖 More advanced AI-powered career guidance

---

## 📄 License

This project is distributed under the **MIT License**.

See the `LICENSE` file for more information.

---

## 👩‍💻 Author

**Shivi Srivastava**

* B.Tech Computer Science Engineering
* Machine Learning & AI Enthusiast

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ **Star** on GitHub!

You can also try the live application here:

👉 **AI Career Skill Gap Analyzer – Live Website**
[https://ai-career-skill-gap-analyzer-b7kayyhldtypbddf65u3nc.streamlit.app/](https://ai-career-skill-gap-analyzer-b7kayyhldtypbddf65u3nc.streamlit.app/)
