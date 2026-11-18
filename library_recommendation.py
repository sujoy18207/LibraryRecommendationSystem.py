"""  University Library Book Recommendation System """

from datetime import datetime
PROGRAMMES = ("BCA", "B.Com", "BBA", "BA", "B.Sc", "B.Tech")
SEMESTERS = ("Semester 1", "Semester 2", "Semester 3", "Semester 4",
             "Semester 5", "Semester 6", "Semester 7", "Semester 8")
LEVELS = ("Beginner", "Intermediate", "Advanced")
PURPOSES = ("Textbook", "Reference", "Research", "Exam Preparation", "Supplementary")
BOOK_TYPES = ("Textbook", "Reference", "Research", "Exam Preparation", "Supplementary")

LIBRARY = [
    {"id": "B001", "title": "Python Programming for Beginners", "author": "A. Sharma",
     "subject": "Python Programming", "topics": ["variables", "loops", "functions", "strings"],
     "programmes": ["BCA", "B.Sc", "B.Tech"], "level": "Beginner", "type": "Textbook",
     "year": 2023, "available": True},
    {"id": "B002", "title": "Python: Data Structures and Problem Solving", "author": "R. Das",
     "subject": "Python Programming", "topics": ["lists", "tuples", "dictionaries", "functions"],
     "programmes": ["BCA", "B.Sc", "B.Tech"], "level": "Intermediate", "type": "Reference",
     "year": 2024, "available": True},
    {"id": "B003", "title": "Introduction to Artificial Intelligence", "author": "P. Mukherjee",
     "subject": "Artificial Intelligence", "topics": ["search", "knowledge representation", "expert systems"],
     "programmes": ["BCA", "B.Tech", "B.Sc"], "level": "Beginner", "type": "Textbook",
     "year": 2022, "available": True},
    {"id": "B004", "title": "Machine Learning Fundamentals", "author": "S. Banerjee",
     "subject": "Artificial Intelligence", "topics": ["classification", "regression", "model evaluation"],
     "programmes": ["BCA", "B.Tech", "B.Sc"], "level": "Advanced", "type": "Research",
     "year": 2024, "available": False},
    {"id": "B005", "title": "Data Structures Using C", "author": "N. Chatterjee",
     "subject": "Data Structures", "topics": ["arrays", "linked lists", "stacks", "queues"],
     "programmes": ["BCA", "B.Tech", "B.Sc"], "level": "Intermediate", "type": "Textbook",
     "year": 2021, "available": True},
    {"id": "B006", "title": "Algorithms and Complexity", "author": "M. Roy",
     "subject": "Data Structures", "topics": ["sorting", "searching", "big o", "recursion"],
     "programmes": ["BCA", "B.Tech", "B.Sc"], "level": "Advanced", "type": "Reference",
     "year": 2023, "available": True},
    {"id": "B007", "title": "Database Management Systems", "author": "K. Sen",
     "subject": "Database Management Systems", "topics": ["sql", "normalization", "transactions"],
     "programmes": ["BCA", "B.Tech", "BBA"], "level": "Intermediate", "type": "Textbook",
     "year": 2022, "available": True},
    {"id": "B008", "title": "Web Development with HTML and CSS", "author": "D. Paul",
     "subject": "Internet and Web Technology", "topics": ["html", "css", "responsive design"],
     "programmes": ["BCA", "B.Tech"], "level": "Beginner", "type": "Supplementary",
     "year": 2024, "available": True},
    {"id": "B009", "title": "JavaScript and Modern Web Applications", "author": "T. Ghosh",
     "subject": "Internet and Web Technology", "topics": ["javascript", "dom", "events", "fetch"],
     "programmes": ["BCA", "B.Tech"], "level": "Intermediate", "type": "Reference",
     "year": 2024, "available": False},
    {"id": "B010", "title": "Computer Networks: An Introduction", "author": "B. Dutta",
     "subject": "Computer Networks", "topics": ["osi model", "tcp/ip", "routing"],
     "programmes": ["BCA", "B.Tech", "B.Sc"], "level": "Beginner", "type": "Textbook",
     "year": 2020, "available": True},
    {"id": "B011", "title": "Operating Systems Concepts", "author": "A. Nair",
     "subject": "Operating Systems", "topics": ["processes", "deadlocks", "memory management"],
     "programmes": ["BCA", "B.Tech"], "level": "Intermediate", "type": "Textbook",
     "year": 2023, "available": True},
    {"id": "B012", "title": "Software Engineering Principles", "author": "S. Mitra",
     "subject": "Software Engineering", "topics": ["sdlc", "testing", "requirements"],
     "programmes": ["BCA", "B.Tech"], "level": "Intermediate", "type": "Reference",
     "year": 2022, "available": True},
    {"id": "B013", "title": "Business Communication Skills", "author": "R. Kapoor",
     "subject": "Business Communication", "topics": ["presentations", "reports", "interviews"],
     "programmes": ["BBA", "B.Com", "BA"], "level": "Beginner", "type": "Supplementary",
     "year": 2021, "available": True},
    {"id": "B014", "title": "Financial Accounting Essentials", "author": "P. Gupta",
     "subject": "Financial Accounting", "topics": ["journal", "ledger", "trial balance"],
     "programmes": ["B.Com", "BBA"], "level": "Beginner", "type": "Textbook",
     "year": 2022, "available": True},
    {"id": "B015", "title": "Advanced Corporate Accounting", "author": "R. L. Gupta",
     "subject": "Advanced Corporate Accounting", "topics": ["consolidation of accounts", "financial statements"],
     "programmes": ["B.Com"], "level": "Advanced", "type": "Reference",
     "year": 2023, "available": True},
    {"id": "B016", "title": "Cost and Management Accounting", "author": "M. Jain",
     "subject": "Cost Accounting", "topics": ["marginal costing", "budgeting", "variance analysis"],
     "programmes": ["B.Com", "BBA"], "level": "Intermediate", "type": "Textbook",
     "year": 2020, "available": False},
    {"id": "B017", "title": "Principles of Marketing", "author": "A. Verma",
     "subject": "Marketing Management", "topics": ["segmentation", "branding", "consumer behaviour"],
     "programmes": ["BBA", "B.Com"], "level": "Beginner", "type": "Textbook",
     "year": 2022, "available": True},
    {"id": "B018", "title": "Human Resource Management", "author": "N. Bose",
     "subject": "Human Resource Management", "topics": ["recruitment", "training", "performance appraisal"],
     "programmes": ["BBA", "BA"], "level": "Intermediate", "type": "Reference",
     "year": 2023, "available": True},
    {"id": "B019", "title": "Business Statistics", "author": "S. Choudhury",
     "subject": "Business Statistics", "topics": ["probability", "correlation", "regression"],
     "programmes": ["B.Com", "BBA", "B.Sc"], "level": "Intermediate", "type": "Textbook",
     "year": 2021, "available": True},
    {"id": "B020", "title": "Research Methodology", "author": "K. Malhotra",
     "subject": "Research Methodology", "topics": ["sampling", "hypothesis testing", "questionnaire"],
     "programmes": ["BBA", "B.Com", "BA", "B.Sc"], "level": "Advanced", "type": "Research",
     "year": 2024, "available": True},
    {"id": "B021", "title": "Environmental Studies", "author": "M. Saha",
     "subject": "Environmental Studies", "topics": ["ecosystems", "pollution", "sustainability"],
     "programmes": ["BA", "B.Sc", "BCA", "B.Com"], "level": "Beginner", "type": "Supplementary",
     "year": 2020, "available": True},
    {"id": "B022", "title": "Mathematics for Computing", "author": "P. Roy",
     "subject": "Discrete Mathematics", "topics": ["sets", "logic", "graphs"],
     "programmes": ["BCA", "B.Tech", "B.Sc"], "level": "Intermediate", "type": "Reference",
     "year": 2023, "available": True},
    {"id": "B023", "title": "Cyber Security Basics", "author": "I. Ahmed",
     "subject": "Cyber Security", "topics": ["encryption", "authentication", "network security"],
     "programmes": ["BCA", "B.Tech"], "level": "Beginner", "type": "Textbook",
     "year": 2024, "available": False},
    {"id": "B024", "title": "Cloud Computing Concepts", "author": "V. Iyer",
     "subject": "Cloud Computing", "topics": ["virtualization", "saas", "paas", "iaas"],
     "programmes": ["BCA", "B.Tech"], "level": "Advanced", "type": "Research",
     "year": 2024, "available": True},
    {"id": "B025", "title": "Exam Preparation: Computer Fundamentals", "author": "L. Das",
     "subject": "Computer Fundamentals", "topics": ["number systems", "input output", "memory"],
     "programmes": ["BCA", "B.Tech", "B.Sc"], "level": "Beginner", "type": "Exam Preparation",
     "year": 2022, "available": True},
]


def normalise(value):
    """Return trimmed lowercase text for case-insensitive comparisons."""
    return value.strip().lower()


def display_library():
    """Display every book in the catalogue."""
    print("\n" + "=" * 90)
    print("UNIVERSITY LIBRARY CATALOGUE")
    print("=" * 90)
    for book in LIBRARY:
        status = "Available" if book["available"] else "Not available"
        print(f'{book["id"]} | {book["title"]} | {book["author"]} | '
              f'{book["subject"]} | {book["level"]} | {book["type"]} | {status}')
    print(f"\nTotal books in catalogue: {len(LIBRARY)}")


def search_books():
    """Search by subject, author, topic, programme or book type."""
    fields = {
        "1": ("subject", "Subject"),
        "2": ("author", "Author"),
        "3": ("topic", "Topic"),
        "4": ("programme", "Programme"),
        "5": ("type", "Book type"),
    }
    print("\nSearch books by:")
    for key, value in fields.items():
        print(f"{key}. {value[1]}")
    choice = input("Choose search field (1-5): ").strip()
    if choice not in fields:
        print("Invalid choice. Please choose a number from 1 to 5.")
        return

    term = input(f'Enter {fields[choice][1].lower()} to search: ').strip()
    if not term:
        print("Search term cannot be empty.")
        return

    field = fields[choice][0]
    matches = []
    for book in LIBRARY:
        if field == "topic":
            searchable = " ".join(book["topics"]).lower()
        elif field == "programme":
            searchable = " ".join(book["programmes"]).lower()
        else:
            searchable = str(book[field]).lower()
        if normalise(term) in searchable:
            matches.append(book)

    if matches:
        print(f"\nFound {len(matches)} matching book(s):")
        for book in matches:
            show_book(book)
    else:
        print("No books matched that search.")


def show_book(book, rank=None, score=None, reasons=None):
    """Display book information, with optional recommendation details."""
    if rank is not None:
        print("\n" + "-" * 70)
        print(f"Rank: {rank}")
    print(f'Book ID: {book["id"]}')
    print(f'Title: {book["title"]}')
    print(f'Author: {book["author"]}')
    print(f'Subject: {book["subject"]}')
    print(f'Topics: {", ".join(book["topics"])}')
    print(f'Programme(s): {", ".join(book["programmes"])}')
    print(f'Academic level: {book["level"]}')
    print(f'Book type: {book["type"]}')
    print(f'Publication year: {book["year"]}')
    print(f'Availability: {"Available" if book["available"] else "Not available"}')
    if score is not None:
        print(f"Recommendation score: {score}/17")
        print(f"Category: {classify_score(score)}")
        print("Reason for recommendation:")
        if reasons:
            for reason in reasons:
                print(f"  - {reason}")
        else:
            print("  - No criteria matched; shown for completeness.")


def calculate_score(book, student_requirements):
    """
    Calculate score using the exact weights in the assignment:
    subject +5, topic +4, programme +2, level +3,
    purpose/type +2, available +1.
    Returns (score, reasons).
    """
    score = 0
    reasons = []

    if normalise(book["subject"]) == normalise(student_requirements["subject"]):
        score += 5
        reasons.append("Exact subject match (+5)")

    requested_topic = normalise(student_requirements["topic"])
    if requested_topic and any(requested_topic in normalise(topic) for topic in book["topics"]):
        score += 4
        reasons.append("Topic match (+4)")

    if student_requirements["programme"] in book["programmes"]:
        score += 2
        reasons.append("Programme match (+2)")

    if book["level"] == student_requirements["level"]:
        score += 3
        reasons.append("Academic level match (+3)")

    if book["type"] == student_requirements["purpose"]:
        score += 2
        reasons.append("Purpose and book type match (+2)")

    if book["available"]:
        score += 1
        reasons.append("Currently available (+1)")

    return score, reasons


def classify_score(score):
    """Classify recommendation relevance using if/elif/else."""
    if 14 <= score <= 17:
        return "Highly Recommended"
    elif 10 <= score <= 13:
        return "Recommended"
    elif 6 <= score <= 9:
        return "Moderately Relevant"
    elif 1 <= score <= 5:
        return "Low Relevance"
    else:
        return "Not Relevant"


def get_student_requirements():
    """Collect and validate student requirements."""
    print("\nEnter your academic requirements.")
    print("Available programmes:", ", ".join(PROGRAMMES))
    programme_lookup = {normalise(item): item for item in PROGRAMMES}
    while True:
        programme = input("Programme: ").strip()
        if normalise(programme) in programme_lookup:
            programme = programme_lookup[normalise(programme)]
            break
        print("Please enter one of the listed programmes.")

    semester_lookup = {normalise(item): item for item in SEMESTERS}
    while True:
        semester = input("Semester (e.g. Semester 3): ").strip()
        if normalise(semester) in semester_lookup:
            semester = semester_lookup[normalise(semester)]
            break
        print("Please enter a semester from Semester 1 to Semester 8.")

    while True:
        subject = input("Subject: ").strip()
        if subject:
            break
        print("Subject cannot be empty.")

    topic = input("Topic (press Enter if no specific topic): ").strip()

    level_lookup = {normalise(item): item for item in LEVELS}
    while True:
        level = input("Academic level (Beginner/Intermediate/Advanced): ").strip()
        if normalise(level) in level_lookup:
            level = level_lookup[normalise(level)]
            break
        print("Please enter Beginner, Intermediate or Advanced.")

    purpose_lookup = {normalise(item): item for item in PURPOSES}
    while True:
        purpose = input("Purpose (Textbook/Reference/Research/Exam Preparation/Supplementary): ").strip()
        if normalise(purpose) in purpose_lookup:
            purpose = purpose_lookup[normalise(purpose)]
            break
        print("Please enter one of the listed purposes.")

    return {
        "programme": programme,
        "semester": semester,
        "subject": subject,
        "topic": topic,
        "level": level,
        "purpose": purpose,
    }


def recommend_books(student_requirements, top_recomendation=None, available_only=False):
    """Evaluate the complete catalogue and display ranked recommendations."""
    recommendations = []
    for book in LIBRARY:
        score, reasons = calculate_score(book, student_requirements)
        if score > 0:
            # Store a new dictionary so the original catalogue is not modified.
            recommendations.append({
                "book": book,
                "score": score,
                "reasons": reasons,
            })

    # Sort descending by score
    recommendations.sort(key=lambda item: (-item["score"], item["book"]["title"].lower()))

    if available_only:
        recommendations = [
            item for item in recommendations if item["book"]["available"]
        ]

    relevant_count = len(recommendations)

    # Calculate summary statistics from the full filtered recommendation set
    summary_scores = [item["score"] for item in recommendations]
    summary_highly_recommended = sum(1 for item in recommendations if item["score"] >= 14)
    summary_available = sum(1 for item in recommendations if item["book"]["available"])
    summary_highest_score = max(summary_scores) if summary_scores else 0
    summary_average_score = sum(summary_scores) / len(summary_scores) if summary_scores else 0.0

    if top_recomendation is not None:
        recommendations = recommendations[:top_recomendation]  

    print("\n" + "=" * 90)
    print("RANKED BOOK RECOMMENDATIONS")
    print("=" * 90)
    if not recommendations:
        print("No relevant books found with the current requirements and filters.")
    else:
        for rank, item in enumerate(recommendations, start=1):
            show_book(item["book"], rank, item["score"], item["reasons"])

    print("\n" + "=" * 60)
    print("RECOMMENDATION SUMMARY")
    print("=" * 60)
    print(f"Total books examined: {len(LIBRARY)}")
    print(f"Total relevant books after availability filter: {relevant_count}")
    print(f"Books displayed: {len(recommendations)}")
    print(f"Highly recommended books in filtered results: {summary_highly_recommended}")
    print(f"Currently available books in filtered results: {summary_available}")
    print(f"Highest recommendation score in filtered results: {summary_highest_score}/17")
    print(f"Average recommendation score in filtered results: {summary_average_score:.2f}/17")
    print(f"Execution date and time: {datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')}")
    print("=" * 60)
    return recommendations


def subject_wise_recommendation():
    #Display books that match a subject entered by the user.
    subject = input("Enter subject: ").strip()
    if not subject:
        print("Subject cannot be empty.")
        return
    req = {
        "programme": "",
        "semester": "",
        "subject": subject,
        "topic": "",
        "level": "",
        "purpose": "",
    }
    matches = []
    for book in LIBRARY:
        if normalise(book["subject"]) == normalise(subject):
            matches.append(book)
    if not matches:
        print("No exact subject match found.")
    else:
        print(f"\nBooks for subject: {subject}")
        for book in matches:
            show_book(book)


def topic_wise_search():
    topic = input("Enter topic to search: ").strip()
    if not topic:
        print("Topic cannot be empty.")
        return
    matches = []
    for book in LIBRARY:
        if any(normalise(topic) in normalise(item) for item in book["topics"]):
            matches.append(book)
    if not matches:
        print("No books found for that topic.")
    else:
        print(f"\nBooks covering '{topic}':")
        for book in matches:
            show_book(book)


def get_recommendation():
    """Ask for a positive number of recommendations."""
    while True:
        value = input("How many recommendations do you want? (e.g. 5): ").strip()
        try:
            number = int(value)
            if number > 0:
                return number
            print("Enter a number greater than zero.")
        except ValueError:
            print("Please enter a whole number, such as 5.")


def main():
    """Main menu; loops until the user chooses Exit."""
    print("=" * 90)
    print("UNIVERSITY LIBRARY BOOK RECOMMENDATION SYSTEM")
    print("=" * 90)

    while True:
        print("\nMAIN MENU")
        print("1. Display complete library catalogue")
        print("2. Search books")
        print("3. Get personalised recommendations")
        print("4. Subject-wise recommendation")
        print("5. Topic-wise search")
        print("6. Exit")
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            display_library()
        elif choice == "2":
            search_books()
        elif choice == "3":
            requirements = get_student_requirements()
            top_recomendation = get_recommendation()
            while True:
                availability_choice = input(
                    "Availability filter: 1. All relevant books  2. Available books only: "
                ).strip()
                if availability_choice in ("1", "2"):
                    break
                print("Choose 1 or 2.")
            recommend_books(
                requirements,
                top_recomendation=top_recomendation,
                available_only=(availability_choice == "2"),
            )
        elif choice == "4":
            subject_wise_recommendation()
        elif choice == "5":
            topic_wise_search()
        elif choice == "6":
            print("Thank you for using the University Library Book Recommendation System.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
