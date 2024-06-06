import os
import pandas as pd
from faker import Faker
import random

fake = Faker()

# Sample CV and job requirements
sample_cv = {
    "address": [],
    "certifications": [
        "• IBM Skill Build Data Science – CSR BOX Certificate",
        "• Top 10 position in Hack4Bengal 2023 – District-Level Hackathon",
        "• Top 5 position in Diversion 2k23 – Inter-University Hackathon",
        "• Introduction to Programming in Python – HackerRank Certificate",
        "• Introduction to Programming in Java – HackerRank Certificate",
        "Languages",
        "• English (Advanced), Hindi (Advanced), Bengali (Advanced)"
    ],
    "education": [
        "University of Engineering and Management 2021 - Present",
        "B.Tech(CSIT) Current GPA: 8.4/10",
        "Saint Luke’s Day School 2005 - 2021",
        "ICSE (2019) & ISC (2021) 79% & 85.07%",
        "Courses: Object-Oriented Programming, Data Structures & Algorithms, Cloud Computing & IoT, Database",
        "Management Systems, Deep Learning, Operating Systems, Artificial Intelligence & Machine Learning, Blockchain",
        "Technology, Software Engineering."
    ],
    "email": "priyanshurouth@gmail.com",
    "experience": [
        "IBM Skill Build Micro Internship March 2024 - April 2024",
        "Data Science Intern",
        "• Included Aptitude tests, coding challenges, and AI-based Personal Interview System."
    ],
    "name": [
        "Priyanshu",
        "Routh"
    ],
    "phone": "+91 9875403824",
    "projects": [
        "Venline GitHub",
        "• Developed a web platform using HTML, CSS, and JavaScript, boosting traffic by 30% and conversion rates by 20%.",
        "• Implemented responsive design for mobile and desktop, serving 86% of mobile traffic.",
        "• Integrated user registration, order history, and product favoriting, increasing user sign-ups by 30%.",
        "• Backend with Node.js and Express handling 200 API requests per second.",
        "• Deployed on DigitalOcean with a Nginx server (https://www.venline.co).",
        "Prathamik GitHub",
        "• Created a feature-rich e-learning platform with React for a responsive UI.",
        "• Supported both desktop and mobile usage, covering 33% mobile traffic.",
        "• Used Node.js, Flask, and Express for the backend with MongoDB as the data store.",
        "• Integrated OpenAI’s Chat GPT API for AI-powered learning and Google’s OCR Vision for real-time question-asking.",
        "• Deployed on AWS and Vercel, handling 120 requests per minute.",
        "Skill Studio GitHub",
        "• Built using React and Vite for front-end development.",
        "• Backend powered by Node.js, Flask, and Express, improving scalability by 25%.",
        "• MySQL managed data storage, scalable to 50GB."
    ],
    "skills": [
        "Languages: C, Kotlin, Python, Java, JavaScript/TypeScript, HTML/CSS, SQL, C++, C",
        "Tools: Git/GitHub, Unix Shell, VS Code, IntelliJ, CLion, PyCharm, IDEA, Figma, Firebase, MySQL, MongoDB, DataGrip"
    ]
}

job_requirements = {
    'skills': ['GO', 'aws', 'Rust', 'Augmented Reality', 'Data Science'],
    'education': ['B.Tech', 'M.Tech', 'B.Sc', 'M.Sc'],
    'experience': ['Intern', 'Junior', 'Senior']
}

# Generate synthetic data
num_samples = 5000
data = []
for _ in range(num_samples):
    name = fake.name()
    phone = fake.phone_number()
    email = fake.email()
    skills = "\n".join(fake.random_choices(sample_cv['skills'], length=random.randint(1, 5)))
    education = "\n".join(fake.random_choices(sample_cv['education'], length=random.randint(1, 3)))
    experience = "\n".join(fake.random_choices(sample_cv['experience'], length=random.randint(1, 3)))
    projects = "\n".join(fake.random_choices(sample_cv['projects'], length=random.randint(1, 3)))
    certifications = "\n".join(fake.random_choices(sample_cv['certifications'], length=random.randint(1, 3)))
    
    # Generate CV text
    cv_text = (name, phone, email, skills, education, experience, projects, certifications)
    
    skills_required = "\n".join(fake.random_choices(job_requirements['skills'], length=random.randint(1, 3)))
    education_required = "\n".join(fake.random_choices(job_requirements['education'], length=random.randint(1, 2)))
    experience_required = "\n".join(fake.random_choices(job_requirements['experience'], length=random.randint(1, 2)))
    
    # Generate job description
    job_description = (skills_required, education_required, experience_required)
    
    data.append((name, phone, email, skills, education, experience, projects, certifications, skills_required, education_required, experience_required))

# Create a DataFrame
df = pd.DataFrame(data, columns=['Name', 'Phone', 'Email', 'Skills', 'Education', 'Experience', 'Projects', 'Certifications', 'Skills Required', 'Education Required', 'Experience Required'])

# Specify the path for saving the CSV file
csv_filename = os.path.join("ai_model", "synthetic_data.csv")

# Export DataFrame to CSV
df.to_csv(csv_filename, index=False)

print(f"Synthetic data has been generated and saved to {csv_filename}.")
