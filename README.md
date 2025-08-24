# 💊 MedScanAI

## 📌 Overview  
**MedScanAI** is an AI-powered healthcare platform designed to assist users in detecting medical issues from scans, identifying medicines, finding nearby doctors and pharmacies, and assessing mental health. It leverages deep learning, computer vision, NLP, and secure backend architecture to provide intelligent and accessible healthcare assistance.

---

## 🚀 Key Features  

### 🧠 Medical Scan Analysis  
- Upload X-ray or scan images to detect abnormalities.  
- Powered by CNN-based deep learning models.  
- Provides instant diagnostic insights for early detection.

### 💊 Medicine Recognition & Information  
- Upload images of medicines for instant identification.  
- Displays drug name, use cases, dosage, and side effects.  
- Uses OpenCV and TensorFlow for image-based detection.

### 📍 Doctor & Pharmacy Locator  
- Locates nearby doctors and pharmacies using Google Maps API.  
- Provides directions, contact info, and operating hours.  
- Essential for emergencies and unfamiliar areas.

### 💬 Health Query Analyzer  
- Users can type in symptoms or health-related questions.  
- NLP models (GPT/BERT) analyze and suggest medical advice.  
- Helps avoid unnecessary doctor visits.

### 🧠 Mental Health Check  
- Anonymous mental health evaluation using standard tools (GAD-7/PHQ-9).  
- Analyzes responses and suggests helpful actions or professionals.  
- Encourages mental wellness and early detection of stress/anxiety.

### 🤖 AI Chatbot Assistant  
- Smart chatbot integrated with OpenAI GPT API or Dialogflow.  
- Responds to general health queries and navigational help.  
- Always accessible through floating chat icon on all pages.

### 🔐 Authentication System  
- JWT-based secure login and signup system.  
- Built using Node.js, Express, and MongoDB.  
- Middleware-protected routes to safeguard personal health data.

### 🖥️ User-Friendly UI  
- Built using HTML, CSS, and JavaScript.  
- Clean, responsive design with intuitive navigation.  
- Real-time results and minimal learning curve.

---

## 📂 Tech Stack  

| Layer        | Technologies Used                              |
|--------------|------------------------------------------------|
| Frontend     | HTML, CSS, JavaScript                          |
| Backend      | Flask / Django (AI modules), Node.js (Auth)    |
| Database     | MongoDB (Auth), Firebase/PostgreSQL (optional) |
| ML/DL Models | TensorFlow, PyTorch, OpenCV                    |
| APIs         | Google Maps API, OpenAI GPT/Dialogflow         |
| Auth         | JWT, Node.js, Express                          |

---


## 📂 Tech Stack
- **Machine Learning & Deep Learning** – TensorFlow, PyTorch, OpenCV
- **Frontend** – HTML, CSS, JavaScript
- **Backend** – Flask / Django (for AI models), Node.js (for authentication)
- **Database** – MongoDB (for user login system), Firebase / PostgreSQL (optional for other features)
- **APIs** – Google Maps API
- **Chatbot** – OpenAI GPT / Dialogflow (custom integration)

---

## 🔐 Authentication Module
- Built using **Node.js**, **Express**, and **MongoDB**
- Supports **JWT-based login/signup**
- User credentials are stored securely in **MongoDB**
- Middleware to protect medical prediction routes for authenticated users

---

## 🧠 AI Chatbot
- Integrated an AI chatbot using **OpenAI GPT API**
- Responds to common medical queries and guides users through the platform
- Available on every page via a chat icon popup

---

# Backend – Auth System (Node.js)
- Navigate to auth directory
cd auth

- Install Node.js dependencies
npm install

 -Start the server
node index.js



## 🔧 Installation & Setup

### Backend – AI Models (Python)
```sh
# Clone the repository
git clone https://github.com/ayush07mishra/MedScanAI.git
cd MedScanAI

# Install Python dependencies
pip install -r requirements.txt

# Run Flask App
python app.py
