# Matching
# Plagiarism Detector & Skill Matcher

Welcome to **Plagiarism Detector & Skill Matcher**, a cutting-edge solution designed to classify text as either human-written or AI-generated, while also providing an intelligent way to match job profiles based on skillsets. This project combines the power of **AI models** with **semantic matching** techniques to streamline talent acquisition and plagiarism detection.

## 🚀 Features

### 1. **Plagiarism Detection (Human vs AI)**
- **AI Model**: Leverages an advanced machine learning model trained to distinguish between human-written text and AI-generated content.
- **Ease of Use**: Simply input any text, and the system will classify it as either human-written or AI-generated with high accuracy.
- **Free & Fast**: Hosted on **Railway** and **Vercel**, this system is designed for high-speed and free access.

### 2. **Skill Matching System**
- **Advanced Skill Matching**: Helps organizations quickly match job profiles with skill requirements.
- **Embeddings-Based Approach**: The system uses **sentence embeddings** to understand and compare job seekers' profiles with job descriptions. It ranks profiles by relevance based on the cosine similarity between the requested skills and those listed in the profiles.
- **Instant Results**: Quickly retrieve matching profiles based on the input job requirements.
  
### 3. **Frontend + Backend Integration**
- **Frontend**: An intuitive **HTML/CSS/JavaScript** interface hosted on **Vercel**. Users can easily input skills and get results in real time.
- **Backend**: The server-side logic is powered by **FastAPI**, which is responsible for processing the skill request and computing the similarity using pre-trained embeddings.

## 🌐 Project Architecture

This project is designed with **scalability** and **efficiency** in mind:

1. **Frontend**: The user interacts with a responsive, simple web interface powered by **HTML**, **CSS**, and **JavaScript**.
2. **Backend**: The backend is built using **FastAPI** with Python, which communicates with an AI model to classify text and a matching algorithm to compare skills.
3. **Hosting**: 
   - The frontend is hosted on **Vercel**.
   - The backend (FastAPI) is deployed on **Railway**, ensuring fast and reliable access to the services.

## 🛠 Tech Stack

- **Frontend**: HTML, CSS, JavaScript (Vercel for hosting)
- **Backend**: Python, FastAPI (Railway for hosting)
- **AI Model**: Hugging Face transformers (for classification tasks)
- **Embeddings**: Sentence-Transformers (for skill matching)
- **Similarity Measure**: Cosine Similarity (via scikit-learn)

## ⚡ How It Works

1. **Plagiarism Detection**:
   - Input text is classified as either **human-written** or **AI-generated** using a pre-trained model.
   - You simply submit a text and the model returns the classification.

2. **Skill Matching**:
   - Users input a list of required skills (e.g., Python, Data Science).
   - The system generates embeddings for both the job profiles and the skills requested.
   - The similarity score between the job profiles and requested skills is calculated using cosine similarity. The profiles are then sorted by relevance.
   
3. **Matching Profiles**:
   - Based on the skills requested, the system returns a list of matching profiles sorted by relevance.

## 🌟 Getting Started
 uvicorn backend_plagia:app
 
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/mounibnasr45/plagia_detector.git
