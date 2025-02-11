import sqlite3 

def create_course_database():
    # Connect to (or create) the database file
    conn = sqlite3.connect("database_course_info.db")
    cursor = conn.cursor()
   
    # Create the movies table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses_extended (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course TEXT NOT NULL,
            description TEXT,
            difficulty TEXT,
            scaling TEXT
        )
    ''')

    # Insert sample data
    
    hsc_subjects_info = [
    # English
    ("English Standard",  
        "Focuses on reading, writing, and text analysis with both practical and academic applications. Students engage with a variety of texts, including novels, poetry, media, and film, developing essential literacy and communication skills. Writing tasks range from creative responses to structured essays, fostering clarity and coherence in expression. The course also helps students develop strong comprehension skills by analyzing themes, context, and language techniques in texts.",  
        "Moderate; suitable for students of varying abilities but requires consistent effort in writing, comprehension, and critical thinking. While not as demanding as English Advanced, students must be able to form well-structured arguments and engage with complex ideas in a clear and logical manner.",  
        "Lower scaling compared to Advanced and Extension courses, but strong performance can still contribute well to ATAR outcomes. Success in this course depends on strong essay-writing skills and the ability to critically engage with various forms of media and literature."  
    ),  
    
    ("English Advanced",  
        "Provides an in-depth study of literature, analytical writing, and critical interpretation. Students analyze complex texts, including Shakespeare, contemporary fiction, and non-fiction, while refining their essay-writing skills. The course encourages students to think critically about human experiences, values, and societal issues through literature. Mastery of textual analysis, argument development, and sophisticated writing is essential for high achievement.",  
        "Higher difficulty; requires strong essay writing, textual analysis, and critical thinking abilities. Students are expected to write with a high level of sophistication, engaging with abstract themes, intertextuality, and diverse perspectives.",  
        "Scales significantly higher than Standard due to its academic rigor and complexity. Those who excel in this subject often demonstrate advanced interpretative skills and strong command of language, which contribute to better ATAR outcomes."  
    ),  
    
    ("English Extension 1",  
        "Explores literary theory, independent research, and advanced textual analysis. Students engage with sophisticated concepts such as postmodernism, feminism, and existentialism while developing high-level writing skills. The subject demands originality, independence, and the ability to evaluate and apply different critical perspectives to texts. Readings often include complex and philosophical literature that challenges students to form nuanced arguments.",  
        "Challenging; requires independent reading, analytical depth, and theoretical engagement. A high level of self-motivation is necessary, as students must conduct extensive research and develop original arguments beyond standard literary analysis.",  
        "Scales highly due to its advanced nature and the level of analytical skill required. Top-performing students often use their knowledge to enhance their performance in Advanced English, strengthening their overall ATAR score."  
    ),  
    
    ("English Extension 2",  
        "A self-directed course where students produce a major work in critical or creative writing. It emphasizes originality, extensive research, and high-level textual engagement. The major work requires an extensive process of drafting, editing, and reflection, culminating in a sophisticated final piece. Students must also submit a reflection statement that demonstrates their creative process, research, and understanding of literary conventions.",  
        "Very demanding; requires creativity, critical thinking, and strong time management for producing an independent major work. Students must be prepared to work autonomously, engaging with literary theory and receiving feedback to refine their work throughout the year.",  
        "Scales extremely well, as it is one of the most selective and academically rigorous English courses. Success in this course can demonstrate advanced skills in research, writing, and independent learning, which are highly valued in university admissions."  
    ),  
    
    ("English as an Additional Language or Dialect (EAL/D)",  
        "Designed for students who speak English as an additional language, focusing on communication, comprehension, and academic writing. It helps students adapt to an English-speaking environment and prepares them for further study or work. Emphasis is placed on improving fluency in spoken and written English while developing confidence in academic settings. The course includes structured listening, reading, and writing activities tailored to support second-language learners.",  
        "Moderate; requires improvement in listening, speaking, reading, and writing skills, with an emphasis on practical and academic English. Students who engage with the material and seek additional language practice will benefit most from this course.",  
        "Scales similarly to Standard but provides targeted support for non-native speakers to develop fluency and confidence. Those who perform well can achieve strong ATAR contributions, especially if they develop high proficiency in written English."  
    ),  
    
    ("English Studies",  
        "A practical course designed for students who want to improve their functional English skills. Focuses on everyday language use, workplace communication, and media literacy rather than deep literary analysis. Topics may include writing for employment, interpreting news and advertisements, and understanding workplace communication. The course is ideal for students who want to develop their English skills for professional and vocational contexts.",  
        "Easier than Standard; ideal for students who prefer a more vocational approach to English rather than an academic one. Assessments focus on practical application rather than theoretical analysis, making it accessible to a broader range of students.",  
        "Lower scaling than other English courses, as it prioritizes real-world applications over complex analytical skills. However, students who engage with coursework and develop strong communication skills can still achieve solid results."  
    ),  
        
    # Mathematics Subjects
    ("Mathematics Standard 1", 
        "A practical course focusing on real-world applications of math. Topics include finance, statistics, and measurement, providing a foundation for students aiming for a career in business or trades.", 
        "Less demanding; emphasizes practical math skills that students can apply to everyday situations. It requires basic problem-solving and data interpretation abilities.", 
        "Low scaling, due to its practical nature and focus on less abstract mathematical concepts. However, it is highly beneficial for students pursuing vocational studies or business-oriented careers."
    ),
    ("Mathematics Standard 2", 
        "A more technical version of Mathematics Standard, preparing for further study. It covers algebra, probability, and introductory calculus, bridging the gap between practical and more abstract mathematics.", 
        "Moderate difficulty; students will develop stronger algebraic and statistical skills and prepare for subjects requiring a deeper understanding of mathematical concepts.", 
        "Scales slightly better than Standard 1, as it prepares students for higher education courses in business, economics, and science, offering more theoretical content."
    ),
    ("Mathematics Advanced", 
        "A rigorous math course covering algebra, calculus, and probability. It provides the essential mathematical foundation for students pursuing university-level STEM courses in fields such as engineering, physics, and economics.", 
        "Challenging; students need to have strong problem-solving skills, a solid understanding of abstract concepts, and the ability to apply mathematical methods to real-world situations.", 
        "Scales well due to its academic difficulty, making it a highly regarded subject for university entrance, particularly in STEM-related degrees."
    ),
    ("Mathematics Extension 1", 
        "An additional challenge for students excelling in Advanced Mathematics. This course delves deeper into calculus, algebra, and mathematical proofs, building upon the content learned in Mathematics Advanced.", 
        "Very challenging; students will encounter advanced problem-solving techniques, abstract concepts, and an increased level of theoretical mathematics.", 
        "Scales extremely well, offering a high ATAR contribution. It is ideal for students pursuing highly competitive university courses in mathematics, physics, or engineering."
    ),
    ("Mathematics Extension 2", 
        "The highest level of HSC Mathematics, covering advanced calculus, mathematical proofs, and the theory behind complex mathematical models. This course is designed for top-tier students who wish to specialize in pure mathematics.", 
        "Extremely demanding; requires exceptional logical thinking, high-level problem-solving abilities, and the ability to tackle the most abstract and complex mathematical concepts.", 
        "Scales among the highest of all HSC subjects. It is particularly valuable for students pursuing elite mathematics or physics degrees, and is regarded as one of the most challenging HSC courses."
    ),
    
    # Science Subjects
    ("Biology", 
        "A study of the structure, function, and evolution of living organisms. Students explore topics like cellular biology, genetics, ecology, and evolution.", 
        "Moderate difficulty; requires understanding of biological concepts, memorization, and application in real-world contexts. It also involves laboratory work and practical investigations.", 
        "Scales moderately; while not as high as Chemistry or Physics, it’s still a solid choice for students pursuing careers in health, medicine, or environmental science."
    ),
    ("Chemistry", 
        "Explores the properties of substances, chemical reactions, and atomic structure. Topics include organic chemistry, inorganic chemistry, and thermodynamics.", 
        "Challenging; requires a deep understanding of chemical principles, problem-solving abilities, and experimental skills. This course also involves extensive lab work and application of theoretical knowledge.", 
        "Scales well; a difficult but rewarding subject, essential for students pursuing careers in STEM fields, particularly those aiming for university courses in chemistry, medicine, and engineering."
    ),
    ("Physics", 
        "Focuses on the fundamental principles of motion, energy, forces, and the laws of the universe. Topics include mechanics, electricity, magnetism, and wave theory.", 
        "Challenging; requires strong mathematical and conceptual problem-solving skills. Physics also involves theoretical applications, experiments, and critical thinking.", 
        "Scales highly; a demanding course, but it offers excellent scaling for students excelling in both Physics and Mathematics, and it’s crucial for those pursuing engineering or physics-based university courses."
    ),
    ("Earth and Environmental Science", 
        "Studies the Earth’s systems, environmental sustainability, and the impact of human activity on natural resources. Topics include geology, weather patterns, and ecosystems.", 
        "Moderate; involves a combination of theoretical learning and practical investigation. Students learn about environmental issues and solutions while exploring scientific methods.", 
        "Scales lower than Chemistry and Physics, but it’s still an excellent option for students interested in environmental science, sustainability, or natural resource management."
    ),
    ("Investigating Science", 
        "A hands-on course that emphasizes scientific inquiry and experimentation. Students learn how to design experiments, collect data, and analyze results.", 
        "Easier than traditional sciences; focuses on practical investigations and the scientific method. Ideal for students who enjoy working in labs and applying their scientific knowledge to real-world problems.", 
        "Lower scaling; this course focuses more on practical skills and understanding scientific processes rather than academic theory, making it less competitive in ATAR rankings."
    ),
    ("Science Extension", 
        "A research-based course designed for students interested in scientific inquiry at an advanced level. Students undertake independent research projects and present their findings.", 
        "Very challenging; requires a high level of independent thinking, research skills, and scientific analysis. This course is suitable for students who enjoy exploring scientific topics in depth and conducting experiments.", 
        "Scales highly; as one of the most academically rigorous science courses, it’s ideal for students aiming to pursue science-based degrees in university, particularly in research and development fields."
    ),
    
    
    ("Ancient History", 
    "A study of the societies, cultures, and events of the ancient world, including Ancient Egypt, Greece, Rome, and other early civilizations.", 
    "Moderate; involves the analysis of historical sources, writing essays, and understanding the development of ancient societies. It requires a strong interest in history and research skills.", 
    "Scales moderately; while it’s not as academically rigorous as some other subjects, it’s an excellent choice for students interested in history, archaeology, and cultural studies."
    ),
    ("Modern History", 
        "Focuses on key historical events and movements from the 18th century onwards, such as the French Revolution, World Wars, and modern political movements.", 
        "Moderate to challenging; requires the ability to analyze historical events, examine primary sources, and develop critical thinking skills.", 
        "Scales well; a popular subject for students pursuing university courses in law, politics, and history, with good ATAR scaling for those who perform well in essays and exams."
    ),
    ("History Extension", 
        "Provides an in-depth analysis of historical debates, theories, and methodologies. Students engage in independent research and critical analysis of historical sources.", 
        "Challenging; requires strong research, writing, and analytical skills. It’s ideal for students who are passionate about history and enjoy deep intellectual engagement with historical topics.", 
        "Scales highly; as a research-focused course, it’s highly regarded by universities, particularly for students pursuing higher education in history, political science, or law."
    ),
    ("Legal Studies", 
        "Explores the Australian legal system, rights, and responsibilities, focusing on topics like criminal law, civil law, and international law.", 
        "Moderate; involves understanding legal concepts, case studies, and applying legal principles. It requires logical thinking, writing skills, and an interest in societal issues.", 
        "Scales well; a valuable subject for students pursuing careers in law, criminology, and politics, with good scaling based on performance in exams and assignments."
    ),
    ("Business Studies", 
        "Examines the key principles of business management, finance, marketing, and business ethics. Topics include business operations, human resources, and economic factors.", 
        "Moderate; requires an understanding of business concepts, financial analysis, and decision-making processes. It’s suited to students with an interest in entrepreneurship, marketing, and management.", 
        "Scales moderately; while it doesn’t scale as highly as more technical subjects, it’s still a solid choice for students considering a career in business, management, or marketing."
    ),
    ("Economics", 
        "Studies economic theories, policies, and their real-world applications. Topics include supply and demand, market structures, economic systems, and global economic issues.", 
        "Challenging; requires critical thinking, mathematical skills, and the ability to analyze complex economic models. A strong foundation in mathematics is helpful.", 
        "Scales highly; it’s a sought-after subject for students pursuing university degrees in economics, business, and finance, with strong scaling for top performers."
    ),
    ("Geography", 
        "Investigates natural and human environments, including topics like population studies, climate change, urbanization, and global challenges such as sustainability.", 
        "Moderate; involves research, fieldwork, and the analysis of geographical patterns. It requires a good understanding of environmental and social issues.", 
        "Scales moderately; while it’s not as competitive as some other subjects, it’s a valuable course for students interested in environmental science, urban planning, or international development."
    ),
    ("Society and Culture", 
        "Explores cultural diversity, identity, and social change, with a focus on global and local issues such as migration, gender, and technology’s impact on society.", 
        "Moderate; requires an understanding of social issues, cultural perspectives, and the ability to engage with complex social concepts. It involves essay writing and research.", 
        "Scales moderately; it’s ideal for students pursuing careers in sociology, psychology, or social work, with solid scaling based on performance in assignments and exams."
    ),
    ("Aboriginal Studies", 
        "Examines Aboriginal culture, history, and perspectives, with a focus on the impact of colonization, Indigenous rights, and the preservation of cultural heritage.", 
        "Moderate; requires understanding the history and cultural practices of Aboriginal Australians and analyzing social issues related to Indigenous communities.", 
        "Scales moderately; while it may not have high scaling compared to other HSIE subjects, it’s an important course for students interested in Indigenous studies, social justice, and cultural heritage."
    ),
    ("Studies of Religion I", 
        "Explores different religious traditions, their beliefs, rituals, and influence on societies, focusing on major world religions such as Christianity, Islam, Hinduism, and Buddhism.", 
        "Moderate; requires an understanding of religious teachings, cultural practices, and the ability to critically analyze religious texts and beliefs.", 
        "Scales moderately; a valuable subject for students pursuing studies in theology, philosophy, or anthropology, though it’s less competitive for ATAR purposes."
    ),
    ("Studies of Religion II", 
        "A more in-depth analysis of multiple religious traditions, with a focus on their development, key concepts, and their impact on modern society and culture.", 
        "Moderate to challenging; requires deep critical thinking, research skills, and the ability to compare and contrast different religious beliefs and practices.", 
        "Scales moderately; this course is ideal for students interested in religious studies, philosophy, and cultural analysis, though it doesn’t scale as highly as other advanced subjects."
    ),
    

    ("Agriculture", 
    "Covers farming practices, sustainability, and agricultural technology. Students study plant growth, animal husbandry, and environmental management within the agricultural sector.", 
    "Moderate; requires an interest in environmental sustainability, biology, and practical agricultural skills. Involves fieldwork and hands-on tasks.", 
    "Scales moderately; while it’s not as academically rigorous as other advanced subjects, it’s beneficial for students considering careers in agriculture, environmental science, or sustainability."
    ),
    ("Design and Technology", 
        "Focuses on designing and creating innovative solutions to real-world problems. Students explore product design, prototyping, and technical drawing.", 
        "Moderate; requires creativity, problem-solving skills, and practical knowledge in materials and design processes. Involves hands-on project work.", 
        "Scales moderately; suitable for students interested in design, engineering, and innovation, with potential pathways into industrial design, architecture, and engineering."
    ),
    ("Engineering Studies", 
        "Examines engineering principles, design, and problem-solving. Topics include mechanical, civil, and electrical engineering, as well as design and manufacturing processes.", 
        "Challenging; requires a solid understanding of physics, mathematics, and technical problem-solving. It’s ideal for students pursuing a career in engineering or technical fields.", 
        "Scales well; highly regarded for students interested in engineering disciplines, with strong ATAR scaling for top performers."
    ),
    ("Food Technology", 
        "Explores nutrition, food production, and consumer science. Students study food safety, preservation techniques, and the impact of food on health.", 
        "Moderate; involves practical cooking tasks, research, and analysis of the food industry. Requires an interest in health, nutrition, and culinary practices.", 
        "Scales moderately; a good option for students interested in the food industry, nutrition, or health sciences, though it doesn’t scale as highly as more academically rigorous subjects."
    ),
    ("Industrial Technology", 
        "Covers manufacturing and practical applications of industry-based skills, including woodworking, metalworking, and electronics.", 
        "Moderate; involves hands-on skills in fabrication, design, and understanding industrial processes. It’s ideal for students with an interest in working with tools and machinery.", 
        "Scales moderately; suitable for students aiming for careers in trades, engineering, or manufacturing industries, with solid scaling based on performance in practical projects."
    ),
    ("Software Design and Development", 
        "Focuses on programming, system design, and software engineering. Students develop software applications and learn about algorithms, coding languages, and systems architecture.", 
        "Challenging; requires strong problem-solving skills, logical thinking, and a solid understanding of computer programming and system design principles.", 
        "Scales well; excellent for students pursuing careers in software development, information technology, or computer engineering, with good scaling for top performers."
    ),
    ("Textiles and Design", 
        "Explores textile production, fashion design, and material technology. Students learn about fabric types, garment construction, and design principles.", 
        "Moderate; requires creativity, attention to detail, and practical skills in sewing, pattern making, and fabric manipulation. Involves hands-on design and project work.", 
        "Scales moderately; a valuable course for students interested in fashion, design, or textiles industries, with solid scaling based on design projects and assessments."
    ),
    
    
    # Creative Arts Subjects
    ("Dance", 
        "Develops skills in choreography, performance, and dance analysis. Students study different dance styles, techniques, and the history of dance.", 
        "Moderate; requires physical discipline, creativity, and performance ability. Involves practice, rehearsal, and a focus on both technical skills and artistic expression.", 
        "Scales lower than more academic subjects, but strong performance and choreography can result in good results for students pursuing dance or performing arts careers."
    ),
    ("Drama", 
        "Explores acting, performance, and theatre production. Students engage in role-playing, script analysis, and stagecraft to develop performance skills.", 
        "Moderate; requires strong communication skills, creativity, and the ability to work collaboratively in group performances. Involves physical expression and memorization of scripts.", 
        "Scales moderately; ideal for students pursuing careers in theatre, film, or television, with scaling based on performance and theoretical analysis of plays and drama."
    ),
    ("Music 1", 
        "A general music course covering performance, composition, and musicology. Students develop an understanding of music theory, performance skills, and the cultural significance of music.", 
        "Moderate; requires students to play a musical instrument or voice, and understand music theory. It involves both practical and theoretical components of music.", 
        "Scales moderately; while accessible to a wider range of students, it’s a great entry point for those interested in music, but it doesn’t scale as highly as advanced music subjects."
    ),
    ("Music 2", 
        "A more in-depth study of musical concepts and performance. Students focus on advanced music theory, composition, and performance techniques, often specializing in one musical area.", 
        "Challenging; requires advanced music theory knowledge, a high level of performance ability, and a strong commitment to mastering complex musical concepts.", 
        "Scales well; regarded highly for students pursuing professional careers in music, with good scaling based on performance and written assessments."
    ),
    ("Music Extension", 
        "For advanced students specializing in performance or composition. It involves highly specialized study in music theory, composition, and performance at a more sophisticated level.", 
        "Very challenging; demands a high level of expertise in music, either through performance or composition. It is designed for students with a deep passion for music and advanced skills.", 
        "Scales highly; one of the most selective and prestigious music courses, offering strong scaling for top performers pursuing music careers."
    ),
    ("Visual Arts", 
        "Covers artistic techniques, theory, and art history. Students develop skills in drawing, painting, sculpture, and digital media, as well as an understanding of art movements and history.", 
        "Moderate; requires creativity, attention to detail, and the ability to work with various materials. Involves both practical art-making and theoretical analysis.", 
        "Scales moderately; a solid choice for students aiming for careers in art, design, or multimedia, though it doesn’t scale as highly as more academic subjects."
    ),
    
    
    ("Personal Development, Health and Physical Education", 
    "Studies health, fitness, and human development. Students explore topics related to physical health, mental well-being, exercise physiology, and nutrition.", 
    "Moderate; requires an understanding of physical health and fitness principles, as well as the ability to work both independently and in teams. Students engage in practical physical activities and theoretical learning.", 
    "Scales moderately; beneficial for students pursuing careers in health, fitness, or education, though it does not scale as highly as more academic subjects."
    ),
    ("Community and Family Studies", 
        "Explores family dynamics, social structures, and community support. Students study the role of families in society, human development, and the factors affecting family life.", 
        "Moderate; involves research and understanding of social sciences, family studies, and the ability to analyze social issues. Includes a focus on practical knowledge and real-world application.", 
        "Scales moderately; good for students interested in social work, psychology, or education, though it may not scale as highly as subjects with more academic rigor."
    ),

    ("Arabic", 
    "Studies the Arabic language and culture. Students learn to communicate in Arabic, understand its grammar, and explore the cultural heritage of Arabic-speaking countries.", 
    "Moderate; involves learning a new script, grammar, and sentence structure. Requires regular practice and immersion in cultural contexts.", 
    "Scales moderately; helpful for students interested in international relations, linguistics, or careers in Arabic-speaking regions."
    ),
    ("Chinese", 
        "Covers Chinese language skills and cultural studies. Students focus on listening, speaking, reading, and writing in Mandarin, and gain insight into Chinese customs and traditions.", 
        "Moderate to challenging; learning Chinese characters and tonal pronunciation can be difficult for beginners. Requires consistent practice and exposure to the language.", 
        "Scales moderately to highly; valuable for students aiming for careers in international trade, diplomacy, or East Asian studies."
    ),
    ("French", 
        "Focuses on French language proficiency and culture. Students learn French grammar, vocabulary, and engage with French literature, history, and arts.", 
        "Moderate; emphasizes conversational and written skills, and an understanding of French-speaking cultures. Regular practice is key to mastery.", 
        "Scales moderately; useful for students pursuing careers in tourism, diplomacy, or European languages and cultures."
    ),
    ("German", 
        "Covers German language and cultural studies. Students develop their proficiency in German grammar, writing, and speaking, while also learning about German history and culture.", 
        "Moderate; requires understanding complex grammar rules and language structure. Students are encouraged to immerse themselves in German cultural texts.", 
        "Scales moderately; beneficial for students interested in European politics, translation, or global business."
    ),
    ("Indonesian", 
        "Studies Indonesian language skills and cultural aspects. Students focus on mastering Indonesian grammar, vocabulary, and comprehension, as well as understanding Indonesian culture.", 
        "Easier than some other languages; involves learning a simplified grammar structure and exposure to diverse Indonesian traditions and societies.", 
        "Scales moderately; useful for students interested in Southeast Asia, tourism, or international development."
    ),
    ("Italian", 
        "Focuses on Italian language and cultural appreciation. Students learn conversational and written Italian, alongside exploring Italy's artistic heritage, food, and traditions.", 
        "Moderate; involves learning grammar, syntax, and vocabulary while also appreciating Italy's cultural contributions to the world.", 
        "Scales moderately; a great option for students interested in Italian literature, art, or pursuing careers in tourism and hospitality."
    ),
    ("Japanese", 
        "Covers Japanese language learning and cultural understanding. Students study kanji, hiragana, katakana, and engage with traditional and contemporary Japanese culture.", 
        "Challenging; involves mastering three different writing systems and learning complex grammar rules. Regular exposure to Japanese media and practice is essential.", 
        "Scales moderately to highly; valuable for students pursuing careers in technology, business, or Japan-related studies."
    ),
    ("Korean", 
        "Studies Korean language skills and cultural insights. Students learn Hangul, Korean grammar, and vocabulary, and explore Korea’s modern and traditional culture.", 
        "Moderate; focuses on reading and writing Hangul and developing conversational abilities. Immersion in Korean films, music, and food culture enhances learning.", 
        "Scales moderately; beneficial for students interested in K-pop, Korean business culture, or international relations."
    ),
    ("Modern Greek", 
        "Covers Modern Greek language and culture. Students study the Greek language, learn about the Greek alphabet, and immerse themselves in the culture and traditions of Greece.", 
        "Moderate; involves mastering the Greek alphabet and syntax, with a focus on conversational and written language.", 
        "Scales moderately; great for students interested in Greek history, tourism, or business with Greece and Cyprus."
    ),
    ("Spanish", 
        "Studies Spanish language and cultural elements. Students learn Spanish vocabulary, grammar, and engage with Spanish-speaking countries' history, literature, and traditions.", 
        "Moderate; involves memorizing conjugations, learning grammatical rules, and understanding the nuances of Spanish culture.", 
        "Scales moderately to highly; useful for students interested in international relations, translation, or business in Spanish-speaking regions."
    ),
    ("Vietnamese", 
        "Covers Vietnamese language and cultural traditions. Students learn Vietnamese phonetics, sentence structure, and gain insight into the culture and traditions of Vietnam.", 
        "Moderate; involves understanding tonal pronunciation and sentence structure. Engaging with Vietnamese media helps improve fluency.", 
        "Scales moderately; beneficial for students interested in Southeast Asia, diplomacy, or trade with Vietnam."
    ),
    ("Latin", 
        "Focuses on Latin language and classical texts. Students study Latin grammar, sentence structure, and translate classical works of Roman literature and history.", 
        "Challenging; requires understanding complex grammatical structures and vocabulary. Students also explore ancient Roman culture and philosophy.", 
        "Scales moderately; ideal for students interested in history, archaeology, or pursuing careers in academia and linguistics."
    ),
    ("Classical Greek", 
        "Studies Ancient Greek language and literature. Students learn Ancient Greek grammar and explore key philosophical, historical, and literary texts from classical Greece.", 
        "Challenging; involves learning a complex grammar system and translating ancient texts. A strong understanding of classical literature is often necessary.", 
        "Scales moderately; valuable for students pursuing studies in classical studies, philosophy, or archaeology."
    ),

    # VET (Vocational Education and Training)
    ("Business Services", 
        "Provides practical business and administrative skills. This course prepares students for various roles within the business sector, covering areas like management, customer relations, and finance.", 
        "Moderate; requires an understanding of business operations and basic accounting. The course focuses on building essential workplace skills and professional knowledge.", 
        "Low scaling, as VET subjects are designed to provide competency-based skills rather than academic rigor, but can be beneficial in gaining work experience and job readiness."
    ),
    
    ("Construction", 
        "Covers building, safety, and trade skills. Students learn hands-on construction techniques, safety procedures, and the basics of building projects from start to finish.", 
        "Moderate; requires physical strength and an understanding of construction principles. Safety knowledge is key to succeeding in this field.", 
        "Low scaling, as it is a practical-based VET subject, but offers strong employment opportunities for students aiming for trade work."
    ),
    
    ("Entertainment Industry", 
        "Focuses on event management, audio-visual production, and stagecraft. Students gain skills for the entertainment industry, including sound, lighting, and event coordination.", 
        "Moderate to high; requires creativity, problem-solving, and teamwork. Students must be willing to work in a fast-paced environment and develop technical skills for live events.", 
        "Moderate scaling, as it provides vocational skills for the entertainment and event industries, which are in high demand."
    ),
    
    ("Hospitality", 
        "Provides skills for the food and hospitality industry. Students learn about customer service, event planning, restaurant management, and food preparation.", 
        "Moderate; requires communication skills, teamwork, and a strong work ethic. It also involves practical skills such as cooking, catering, and customer service.", 
        "Low scaling, as it is a VET subject, but excellent for gaining hands-on experience and progressing to managerial roles in hospitality."
    ),
    
    ("Information and Digital Technology", 
        "Covers IT systems, networking, and digital tools. Students learn how to design, implement, and maintain IT systems and networks, as well as work with software applications.", 
        "Challenging; requires an interest in technology and problem-solving. Students will develop technical expertise that is in demand across various industries.", 
        "Moderate scaling; provides solid career prospects in IT-related fields, such as network administration, cybersecurity, and software development."
    ),
    
    ("Primary Industries", 
        "Studies agricultural and farming industry skills. Students gain knowledge in crop production, animal care, and sustainable farming practices.", 
        "Moderate; requires a strong interest in the outdoors and working with animals or crops. Students will develop practical skills in farming, land management, and agricultural technology.", 
        "Low scaling, as it focuses on vocational skills for the agricultural sector, but offers strong employment prospects for those pursuing a career in farming or environmental management."
    ),
    
    ("Retail Services", 
        "Focuses on customer service and retail management. Students learn how to manage retail operations, handle customer inquiries, and promote products effectively.", 
        "Moderate; requires communication skills, customer service skills, and an understanding of retail operations. Students must be able to work in a fast-paced, customer-facing environment.", 
        "Low scaling, but it offers excellent career opportunities in retail management and sales positions, which are essential in the global economy."
    ),
    
    ("Tourism, Travel and Events", 
        "Provides skills for working in tourism and events management. Students learn about event coordination, tour guiding, and hospitality in the tourism sector.", 
        "Moderate; requires good organizational skills, the ability to work with diverse groups of people, and an interest in travel and event planning.", 
        "Low scaling, but offers strong prospects in the growing global tourism and events industries, which are essential to many economies."
    )
]

    


    cursor.executemany('INSERT INTO courses_extended (course, description, difficulty, scaling) VALUES (?, ?, ?, ?)', hsc_subjects_info)
   
    # Commit and close the connection
    conn.commit()
    conn.close()
    print("Database and table created successfully with sample data.")

# Run the function to create the database
if __name__ == "__main__":
    create_course_database()