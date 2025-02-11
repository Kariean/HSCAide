import sqlite3 

def create_course_database():
    # Connect to (or create) the database file
    conn = sqlite3.connect("database_course.db")
    cursor = conn.cursor()
   
    # Create the movies table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course TEXT NOT NULL,
            faculty TEXT,
            difficulty TEXT,
            units INTEGER,
            description text
        )
    ''')

    # Insert sample data
    
    hsc_subjects = [
    # English
    ("English Standard", "English", "Standard", 2, "A foundational English course focusing on reading, writing, and analysis."),
    ("English Advanced", "English", "Advanced", 2, "A more in-depth study of literature and analytical skills."),
    ("English Extension 1", "English", "Extension", 1, "An advanced course focusing on literary theory and critical analysis."),
    ("English Extension 2", "English", "Extension", 1, "A creative and independent research-based extension of English studies."),
    ("English as an Additional Language or Dialect (EAL/D)", "English", "Standard", 2, "For students who speak English as an additional language."),
    ("English Studies", "English", "Standard", 2, "Focuses on practical English skills for everyday and professional contexts."),

    # Mathematics
    ("Mathematics Standard 1", "Mathematics", "Standard", 2, "A practical course focusing on real-world applications of math."),
    ("Mathematics Standard 2", "Mathematics", "Standard", 2, "A more technical version of Mathematics Standard, preparing for further study."),
    ("Mathematics Advanced", "Mathematics", "Advanced", 2, "A rigorous math course covering algebra, calculus, and probability."),
    ("Mathematics Extension 1", "Mathematics", "Extension", 1, "An additional challenge for students excelling in Advanced Mathematics."),
    ("Mathematics Extension 2", "Mathematics", "Extension", 1, "The highest level of HSC Mathematics, covering advanced calculus and proof."),

    # Science
    ("Biology", "Science", "Standard", 2, "Explores the structure, function, and evolution of living organisms."),
    ("Chemistry", "Science", "Advanced", 2, "Studies the properties of substances, chemical reactions, and atomic structure."),
    ("Physics", "Science", "Advanced", 2, "Focuses on motion, energy, and the laws governing the universe."),
    ("Earth and Environmental Science", "Science", "Standard", 2, "Examines the Earth's systems, sustainability, and environmental impacts."),
    ("Investigating Science", "Science", "Standard", 2, "Develops skills in scientific inquiry, research, and experimentation."),
    ("Science Extension", "Science", "Extension", 1, "A research-based course exploring advanced scientific inquiry."),

    # Human Society and Its Environment (HSIE)
    ("Ancient History", "HSIE", "Standard", 2, "Studies the societies, cultures, and events of the ancient world."),
    ("Modern History", "HSIE", "Standard", 2, "Focuses on key historical events and movements from the 18th century onwards."),
    ("History Extension", "HSIE", "Extension", 1, "Analyzes historical debates and theories with independent research."),
    ("Legal Studies", "HSIE", "Standard", 2, "Explores the legal system, rights, and responsibilities in society."),
    ("Business Studies", "HSIE", "Standard", 2, "Examines business management, finance, and marketing principles."),
    ("Economics", "HSIE", "Advanced", 2, "Studies economic theories, policies, and their real-world applications."),
    ("Geography", "HSIE", "Standard", 2, "Investigates natural and human environments and global challenges."),
    ("Society and Culture", "HSIE", "Standard", 2, "Explores cultural diversity, identity, and social change."),
    ("Aboriginal Studies", "HSIE", "Standard", 2, "Examines Aboriginal culture, history, and perspectives."),
    ("Studies of Religion I", "HSIE", "Standard", 1, "Explores different religious traditions and their influence."),
    ("Studies of Religion II", "HSIE", "Standard", 2, "A more in-depth analysis of multiple religious traditions."),

    # Technological and Applied Studies (TAS)
    ("Agriculture", "TAS", "Standard", 2, "Covers farming practices, sustainability, and agricultural technology."),
    ("Design and Technology", "TAS", "Standard", 2, "Focuses on designing and creating innovative solutions to real-world problems."),
    ("Engineering Studies", "TAS", "Advanced", 2, "Examines engineering principles, design, and problem-solving."),
    ("Food Technology", "TAS", "Standard", 2, "Explores nutrition, food production, and consumer science."),
    ("Industrial Technology", "TAS", "Standard", 2, "Covers manufacturing and practical applications of industry-based skills."),
    ("Software Design and Development", "TAS", "Advanced", 2, "Focuses on programming, system design, and software engineering."),
    ("Textiles and Design", "TAS", "Standard", 2, "Explores textile production, fashion design, and material technology."),

    # Creative Arts
    ("Dance", "Creative Arts", "Standard", 2, "Develops skills in choreography, performance, and dance analysis."),
    ("Drama", "Creative Arts", "Standard", 2, "Explores acting, performance, and theatre production."),
    ("Music 1", "Creative Arts", "Standard", 2, "A general music course covering performance, composition, and musicology."),
    ("Music 2", "Creative Arts", "Advanced", 2, "A more in-depth study of musical concepts and performance."),
    ("Music Extension", "Creative Arts", "Extension", 1, "For advanced students specializing in performance or composition."),
    ("Visual Arts", "Creative Arts", "Standard", 2, "Covers artistic techniques, theory, and art history."),

    # Personal Development, Health and Physical Education (PDHPE)
    ("Personal Development, Health and Physical Education", "PDHPE", "Standard", 2, "Studies health, fitness, and human development."),
    ("Community and Family Studies", "PDHPE", "Standard", 2, "Explores family dynamics, social structures, and community support."),

    # Languages
    ("Arabic", "Languages", "Standard", 2, "Studies the Arabic language and culture."),
    ("Chinese", "Languages", "Standard", 2, "Covers Chinese language skills and cultural studies."),
    ("French", "Languages", "Standard", 2, "Focuses on French language proficiency and culture."),
    ("German", "Languages", "Standard", 2, "Covers German language and cultural studies."),
    ("Indonesian", "Languages", "Standard", 2, "Studies Indonesian language skills and cultural aspects."),
    ("Italian", "Languages", "Standard", 2, "Focuses on Italian language and cultural appreciation."),
    ("Japanese", "Languages", "Standard", 2, "Covers Japanese language learning and cultural understanding."),
    ("Korean", "Languages", "Standard", 2, "Studies Korean language skills and cultural insights."),
    ("Modern Greek", "Languages", "Standard", 2, "Covers Modern Greek language and culture."),
    ("Spanish", "Languages", "Standard", 2, "Studies Spanish language and cultural elements."),
    ("Vietnamese", "Languages", "Standard", 2, "Covers Vietnamese language and cultural traditions."),
    ("Latin", "Languages", "Standard", 2, "Focuses on Latin language and classical texts."),
    ("Classical Greek", "Languages", "Standard", 2, "Studies Ancient Greek language and literature."),

    # Vocational Education and Training (VET) Courses
    ("Business Services", "VET", "Standard", 2, "Provides practical business and administrative skills."),
    ("Construction", "VET", "Standard", 2, "Covers building, safety, and trade skills."),
    ("Entertainment Industry", "VET", "Standard", 2, "Focuses on event management, audio-visual production, and stagecraft."),
    ("Hospitality", "VET", "Standard", 2, "Provides skills for the food and hospitality industry."),
    ("Information and Digital Technology", "VET", "Standard", 2, "Covers IT systems, networking, and digital tools."),
    ("Primary Industries", "VET", "Standard", 2, "Studies agricultural and farming industry skills."),
    ("Retail Services", "VET", "Standard", 2, "Focuses on customer service and retail management."),
    ("Tourism, Travel and Events", "VET", "Standard", 2, "Provides skills for working in tourism and events management.")
]

    


    cursor.executemany('INSERT INTO courses (course, faculty, difficulty, units, description) VALUES (?, ?, ?, ?, ?)', hsc_subjects)
   
    # Commit and close the connection
    conn.commit()
    conn.close()
    print("Database and table created successfully with sample data.")

# Run the function to create the database
if __name__ == "__main__":
    create_course_database()