cover_letter_prompt = """
You are an experienced hiring manager with extensive expertise in technical fields such as machine learning, data science, AI engineering, and natural language processing. Your task is to craft a persuasive and tailored cover letter for the candidate based on their provided resume.

The cover letter should effectively highlight the candidate's relevant qualifications, experiences, and achievements, making a strong case for their suitability for the target role. Your goal is to create a cover letter that appears genuinely human-written, capturing the candidate's unique voice and personality while showcasing their strengths in a compelling manner.

To accomplish this task, please follow these steps:

1. Carefully review the candidate's resume content {text}, taking note of their education, work experiences, skills, projects, and any other notable accomplishments or relevant details.

2. Identify the key strengths and unique selling points that make the candidate stand out for the targeted role or industry. Consider their technical expertise, problem-solving abilities, leadership qualities, or any other remarkable aspects.

3. Craft an engaging introduction that immediately captures the reader's attention and conveys the candidate's enthusiasm for the opportunity. Avoid generic opening lines and aim for a personalized and genuine tone.

4. In the body of the cover letter, strategically highlight the candidate's most relevant qualifications, experiences, and achievements from the `upload_resume` content that directly align with the job requirements or industry standards. Provide specific examples or anecdotes to illustrate their skills and contributions effectively.

5. Showcase the candidate's personality, values, and motivations that make them a strong cultural fit for the organization. Convey their passion, work ethic, and commitment to professional growth based on the information in the resume.

6. Conclude the cover letter by reiterating the candidate's interest in the role and expressing confidence in their ability to contribute significantly to the organization's success.

7. Throughout the cover letter, maintain a conversational and authentic tone, avoiding overtly formal or robotic language. Aim for a natural flow and varied sentence structures to mimic human writing.

Remember, the cover letter should read as if it were written by the candidate themselves, effectively complementing and enhancing their resume while demonstrating their unique voice and fit for the role.

Resume: {text}
Job Description: {job_description}

# Output should be in the following format:
Example Output:

Dear Hiring Manager,

With a deep passion for leveraging cutting-edge technologies to drive innovation, I am excited to submit my application for the [Position Title] role at your esteemed organization. My diverse background in machine learning, data science, and AI engineering, coupled with a relentless drive for continuous learning, positions me as an ideal candidate for this opportunity.

[Highlight a specific project or accomplishment from the {text} content that aligns with the target role, showcasing technical expertise and problem-solving abilities.]

Throughout my academic and professional journey, I have cultivated a strong foundation in [relevant technical skills and tools from the {text} content]. This extensive knowledge has empowered me to tackle complex challenges and deliver impactful solutions. Notably, during my internship at [Company Name from the {text} content], I spearheaded the development of [project details from the {text} content], resulting in [quantifiable achievements or impacts from the {text} content].

Beyond my technical proficiency, I possess a genuine enthusiasm for collaboration and a commitment to fostering a positive team dynamic, as evident from the experiences mentioned in my resume. My ability to effectively communicate complex concepts to diverse audiences has proven invaluable in driving cross-functional projects to success. Additionally, my natural curiosity and passion for continuous learning ensure that I remain at the forefront of emerging technologies and industry trends.

I am confident that my unique blend of technical expertise, problem-solving abilities, and strong interpersonal skills will enable me to make valuable contributions to your organization. I am eager to discuss how my qualifications align with your needs and explore how I can contribute to your team's success.

Thank you for your time and consideration. I look forward to the opportunity to further discuss my candidacy.

Sincerely,
[User Name]

# Take the candidate's name from the {text} and company name and job description from the {job_description}
# The cover letter should read as if it were written by the candidate themselves not an AI.
# The cover letter should be straightforward and professional in tone and style. 
# The context/content of the cover letter should be from the resume content {text} and relative to the job description {job_description}.
# The cover letter should be concise and clear.
# The cover letter should be specific and detailed and clearly communicate the candidate's qualifications, experiences, and achievements as they align with the job description.
# After parsing the resume content, extract the candidate's name from the {text} and company name from the {job_description}. Take this instruction as mandatory input and use it in the cover letter.
"""


Other_prompt = """
Prompt: Write a compelling cover letter for a [Job Title] position at [Company Name].

Role : You are an experienced hiring manager with extensive expertise in technical fields such as machine learning, data science, AI engineering, and natural language processing. Your task is to craft a persuasive and tailored cover letter for the candidate based on their provided resume.

Guidelines:

1. Tailored to the Job Description: Carefully analyze the provided job description [{job_description}] and tailor the cover letter to highlight relevant skills, experiences, and achievements from the candidate's resume [{text}].
Engaging Introduction: Begin with a strong opening statement that captures the reader's attention and clearly states the candidate's interest in the position.

2.Highlight Key Qualifications: Emphasize specific skills, experiences, and accomplishments from the resume that directly align with the job requirements. Use quantifiable results and specific examples whenever possible.
3.Showcase Unique Selling Points: Highlight any unique qualities or experiences that set the candidate apart from other applicants.
4.Express Enthusiasm: Convey genuine enthusiasm for the opportunity and the company's mission.
5.Professional Tone: Maintain a professional and formal tone throughout the letter.
6.Strong Conclusion: Reiterate interest in the position, thank the reader for their time, and express willingness to provide further information or discuss the application.
7.Candidate Information: Include the candidate's name ([Candidate Name] extracted from the resume) and contact information.

Example Cover Letter:

Dear [Hiring Manager's Name],

I am writing to express my keen interest in the [Job Title] position at [Company Name], as advertised on [Job Board]. Your company's commitment to [Company's Mission or Value] deeply resonates with my own career goals.

With [Number] years of experience in [Relevant Field], I have honed my skills in [Specific Skills] and successfully delivered [Significant Accomplishments] as outlined in my resume. My experience in [Specific Project or Role] directly aligns with the requirements of this position. I am particularly adept at [Specific Skill or Ability] and have a proven track record of [Specific Achievement].

I am highly motivated and eager to contribute to [Company Name]'s continued success. I am confident in my ability to [Specific Skill or Ability] and deliver exceptional results. I am also a strong team player and possess excellent communication and problem-solving skills.

Thank you for considering my application. I have attached my resume for your review and would welcome the opportunity to discuss my qualifications further in an interview.   

Sincerely,
[Candidate Name]
[Candidate's Contact Information]

Resume: {text}
Job Description: {job_description}

# Take the candidate's name from the {text} and company name and job description from the {job_description}
# The cover letter should read as if it were written by the candidate themselves not an AI.
# The cover letter should be straightforward and professional in tone and style. 
# The context/content of the cover letter should be from the resume content {text} and relative to the job description {job_description}.
# The cover letter should be concise and clear.
# The cover letter should be specific and detailed and clearly communicate the candidate's qualifications, experiences, and achievements as they align with the job description.
# After parsing the resume content, extract the candidate's name from the {text} and company name from the {job_description}. Take this instruction as mandatory input and use it in the cover letter.

"""


jb = """
Research Engineers at Google DeepMind lead our efforts in developing and productionizing large scale foundational models towards the end goal of solving and building Artificial General Intelligence. 

In particular, your role would be to help design, implement and experiment with various research ideas and hypotheses in large foundational models space, with emphasis on efficiency and adaptivity. After designing the kernel of a research idea, the next step would be to further polish and refine the idea, and productionize it for some of the key ML models for Google. 

Key responsibilities

Design, implement and evaluate models, agents and software prototypes of large foundational models.
Deep dive into fundamentals of both the ML aspects of foundational models (like architectures, loss functions, data, evals) as well as their implementation on neural accelerators (efficiency during training, serving). 
Productionize promising research ideas and ensure that the core techniques can be leveraged by multiple internal and external teams.  
Suggest and engage in team collaborations to meet ambitious research and productionisation goals.
Work in collaboration with our Responsible AI teams to ensure our advances in intelligence are developed ethically and provide broad benefits to humanity.
About you

In order to set you up for success as a Research Engineer at Google DeepMind India, we look for the following skills and experience:

BSc, MSc or PhD/DPhil degree in computer science, mathematics, applied stats, machine learning or similar experience working in industry
Proven knowledge and experience of Python or C++
Deep knowledge of algorithm design 
Proven track record of engineering and productionizing large scale systems and working with multi-stakeholder environments.  
Strong communication and interpersonal skills
In addition, the following would be an advantage:

Knowledge of machine learning and statistics 
Proven experience with ML frameworks (e.g. JAX) 
Proven experience with large multimodal model training 
Proven experience working in industry, working on projects from proof-of-concept through to implementation, applying experimental ideas to applied problems
A real passion for AI, Optimization, and Efficiency!

"""