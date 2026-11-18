# University Library Book Recommendation System

A rule-based book recommendation system developed using Python. The project helps university students discover relevant books based on their academic requirements, including programme, semester, subject, topic, academic level, and purpose of study.

Unlike machine learning-based recommendation systems, this project uses a simple weighted scoring algorithm to evaluate books and generate personalised recommendations.

## Project Overview

The University Library Book Recommendation System is a menu-driven Python application designed to make book searching and selection easier for university students.

It maintains a catalogue of 25 books across different academic programmes and subjects. Students can search the catalogue, explore subject-wise and topic-wise books, or receive ranked recommendations based on their individual requirements.

The recommendation process is completely rule-based and does not require any AI, machine learning models, external libraries, or database connections.

##  Features

- **Complete Library Catalogue:** Displays all 25 books with their details and availability status.
- **Book Search:** Search books by subject, author, topic, programme, or book type.
- **Personalised Recommendations:** Generates recommendations based on student preferences.
- **Subject-Wise Recommendations:** Finds books belonging to a particular subject.
- **Topic-Wise Search:** Identifies books covering a specific topic.
- **Weighted Scoring System:** Calculates recommendation scores using predefined criteria.
- **Ranking System:** Sorts recommended books from highest to lowest score.
- **Top-N Recommendations:** Allows students to choose how many recommendations they want.
- **Availability Filter:** Displays all relevant books or only currently available books.
- **Recommendation Summary:** Provides statistics such as average score, highest score, and total relevant books.
- **Input Validation:** Handles invalid menu choices, empty inputs, and incorrect values.

## Recommendation Algorithm

The system uses a weighted scoring mechanism to determine how relevant each book is to a student's requirements.

Each book is evaluated against six criteria:

| Matching Criteria | Score |
|---|---:|
| Exact Subject Match | +5 |
| Topic Match | +4 |
| Programme Match | +2 |
| Academic Level Match | +3 |
| Purpose and Book Type Match | +2 |
| Book Availability | +1 |
| **Maximum Score** | **17** |

### Recommendation Categories

Based on the calculated score, books are classified into the following categories:

| Score Range | Recommendation |
|---|---|
| 14–17 | Highly Recommended |
| 10–13 | Recommended |
| 6–9 | Moderately Relevant |
| 1–5 | Low Relevance |
| 0 | Not Relevant |

Books are sorted by their recommendation scores in descending order. When two books have the same score, their titles are used for alphabetical ordering.

## 📖 Book Catalogue

The project contains 25 sample books covering different academic areas, including:

- Python Programming
- Artificial Intelligence
- Data Structures
- Database Management Systems
- Web Development
- Computer Networks
- Operating Systems
- Software Engineering
- Financial Accounting
- Marketing Management
- Business Statistics
- Research Methodology
- Cyber Security
- Cloud Computing
- Mathematics for Computing

Supported academic programmes:

- BCA
- B.Com
- BBA
- BA
- B.Sc
- B.Tech

##  Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| datetime | Displaying execution date and time |
| Lists | Storing the book catalogue and recommendations |
| Dictionaries | Managing book information and student requirements |
| Tuples | Storing fixed programme and category options |
| Functions | Organising the application into reusable modules |
| Conditional Statements | Implementing search and recommendation logic |
| Loops | Iterating through books and handling user input |
| String Methods | Performing case-insensitive searches |
| Sorting | Ranking books based on recommendation scores |

**External Dependencies:** None. The project uses only Python's built-in standard library.

## 📂 Project Structure

```text
University-Library-Book-Recommendation/
│
├── main.py
└── README.md
```

*Note: `main.py` is the suggested filename for the Python source code.*

## ⚙️ Installation and Execution

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/University-Library-Book-Recommendation.git
```

### 2. Navigate to the Project Directory

```bash
cd University-Library-Book-Recommendation
```

### 3. Run the Application

```bash
python main.py
```

Make sure Python 3 is installed on your system.

## 🖥️ Application Menu

When the program starts, users are presented with the following menu:

```text
UNIVERSITY LIBRARY BOOK RECOMMENDATION SYSTEM
Subject-based rules | No AI/ML | Standard library only

MAIN MENU

1. Display complete library catalogue
2. Search books
3. Get personalised recommendations
4. Subject-wise recommendation
5. Topic-wise search
6. Exit

Choose an option (1-6):
```

Users can select an option and follow the instructions displayed in the terminal.

##  Learning Objectives

This project demonstrates the practical implementation of fundamental Python programming concepts:

- Variables and data types
- Lists, tuples, and dictionaries
- Functions and modular programming
- Loops and conditional statements
- String manipulation and normalisation
- Searching and sorting techniques
- User input validation
- Basic algorithm design and weighted scoring
- Working with Python's standard library


## Project Information

**Project Name:** University Library Book Recommendation System  
**Programming Language:** Python 3  
**Project Type:** Academic / Mini Project  
**Recommendation Approach:** Rule-Based Weighted Scoring  
**Dependencies:** Python Standard Library Only

---

*Developed as a Python programming project to demonstrate the practical use of fundamental programming concepts through a real-world university library application.*
