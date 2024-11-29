from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import spacy
spacy.load('en_core_web_sm')
# from spacy.lang.en import English
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
chatbot = ChatBot('<b>Chat bot BOT</b>')

# nlp = spacy.load("en_core_web_sm")

chatbot = ChatBot(
    'ChatBot for College Enquiry',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': "Hi there, Welcome to nuva! If you need any assistance, I'm always here.Go ahead and write the number of any query. 😃✨<b><br><br>  Which of the following user groups do you belong to? <br><br>1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br><br>",
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'   
) 
chatbot.storage.drop()



trainer = ListTrainer(chatbot)

# python app.py
# Training with Personal Ques & Ans 
conversation = [
"Hi",
"Helloo!",
"Hey",

"How are you?",
"I'm good.</br> <br>Go ahead and write the number of any query.  <br> 1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

"Great",
"Go ahead and write the number of any query.<br> 1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

"good",
"Go ahead and write the number of any query.  <br> 2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

"fine",
"Go ahead and write the number of any query.  <br> 2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

"Thank You",
"Your Welcome ",

"Thanks",
"Your Welcome ",

"Bye",
"Thank You for visiting!..",

"What do you do?",
"I am made to give Information about navrachna university college.",

"What else can you do?",
"I can help you know more about nuv",
    
    "1",
    "<b>STUDENT <br>The following are frequently searched terms related to student . Please select one from the options below : <br> <br> 1.1 Curriculars <br>1.2  Extra-Curriculars<br>1.3  Administrative<br>1.4 Placements </b>",
    
    "1.1",
    "<b>  CURRICULAR <br>  These are the top results: <br> <br> 1.1.1 Resources<br> 1.1.2 Academic Calendar <br> 1.1.3 Curriculum </b>",
    "1.1.1",
    "<b> 1.1.1 Resources <br>The link to Resources  <a href=" 'https://nuv.ac.in/students-corner/#Resources' ">Click Here</a> </b>",
    "1.1.2",
    "<b > 1.1.2 Academic Calender<br>The link to Academic Calender<a href=" 'https://nuv.ac.in/academic-calendar' ">Click Here</a> </b>",
    "1.1.3",
    "<b> 1.1.3 Curriculum<br>The link to Curriculum <a href=" 'https://nuv.ac.in/choice-based_curriculum/' ">Click Here</a> </b>",

    "1.2",
    "<b>EXTRA-CURRICULAR<br>These are the top results: <br> <br> 1.2.1 Events<br> 1.2.2 Academic Council </b>",
    "1.2.1",
    "<b > 1.2.1 Events<br>The link to Events <a href=" 'https://nuv.ac.in/beyond-books/#TechnicalFestivals' ">Click Here</a></b>",
    "1.2.2",
    "<b > 1.2.2 Academic Council<br>The link to Academic Council<a href=" 'https://nuv.ac.in/academic-council/' ">Click Here</a> </b>",
   
    "1.3",
    "<b>1.3 ADMINISTRATIVE<br>These are the top results: <br> <br> 1.3.1 Students Corner <br>1.3.2 Student Start-up <br> 1.3.3 Nirantar </b>",
    "1.3.1",
    "<b> 1.3.1 Students Corner<br>The link to Students Corner <a href=" 'https://nuv.ac.in/students-corner/' ">Click Here</a> </b>",
    "1.3.2",
    "<b> 1.3.2 Student Start-up <br>The link to Student Start-up  <a href=" 'https://nuv.ac.in/innovation/' ">Click Here</a> </b>",
    "1.3.3",
    "<b> 1.3.3 Nirantar  <a href=" 'https://nuv.ac.in/nirantar/' ">Click Here</a> </b>",

  
    "1.4",
    "<b > PLACEMENTS These are the top results:<br> 1.4.1 Placements</b>",
    "1.4.1",
    "<b> 1.4.1 Placements<br>The link to Placements <a href=" 'https://nuv.ac.in/well-placed/' ">Click Here</a> </b>",
    
    "2",
    "<b >FACULTY<br>The following are frequently searched terms related to faculty. :</br></br>2.1 HUB <br>2.2  Examination </b>",
    
    "2.1",
    "<b > HUB These are the top results:<br> 2.1.1 HUB</b>",
    "2.1.1",
    "<b> 2.1.1 HUB<br>The link to HUB<a href=" 'http://hub.nuv.ac.in/' ">Click Here</a> </b>",
    
   
    "2.2",
    "<b > EXAMINATION <br>These are the top results:<br> <br> 2.3.1 EXAMINATION </b>",
    "2.3.1",
    "<b> 2.3.1 EXAMINATION <br>The link to EXAMINATION  <a href=" 'https://nuv.ac.in/students-corner/#Examination' ">Click Here</a> </b>",
  
    "3",
    "<b> PARENTS <br>The following are frequently searched terms related to Parents. Please select one from the options below : <br> <br> 3.1 About Us <br>3.2 Admission <br>3.3 Fee Payment <br>3.4 Placements </b> " ,

    "3.1",
    "<b > ABOUT US<br>These are the top results:<br> <br> 3.1.1 About University <br> 3.1.2 Leadership <br> 3.1.3 INFRASTRUCTURE </b>",
    "3.1.1",
    "<b > 3.1.1 About University<br>The link to About University <a href=" 'https://nuv.ac.in/aboutus/' ">Click Here</a> </b>",
    "3.1.2",
    "<b > 3.1.2 Leadership <br>The link to Leadership<a href=" 'https://nuv.ac.in/aboutus/#Leadership' ">Click Here</a> </b>",
    "3.1.3",
    "<b > 3.1.3 INFRASTRUCTURE <br>The link to INFRASTRUCTURE <a href=" 'https://nuv.ac.in/aboutus/#Infra' ">Click Here</a> </b>",

    "3.2",
    "<b > Admission<br>These are the top results:<br> <br> 3.2.1 All Notices  </b>",
    "3.2.1",
    "<b > 3.2.1 Admission<br>The link to Admission <a href=" 'https://nuv.ac.in/apply-online/' ">Click Here</a> </b>",

    "3.3",
    "<b > ABOUT US<br>These are the top results:<br> <br>3.3.1 FEEs Structure </b>",
    "3.3.1",
    "<b > 3.3.1 FEEs Structure<br>The link to FEEs Structure  <a href=" 'https://nuv.ac.in/apply-online/#fees' ">Click Here</a> </b>",
   
    "3.4",
    "<b > PLACEMENTS These are the top results:<br> <br>3.4.1 Placements </b>",
    "3.4.1",
    "<b> 3.4.1 Placements<br>The link to Placements <a href=" 'https://nuv.ac.in/well-placed/' ">Click Here</a> </b>",
 
    "4",
    "<b VISITORS <br>The following are frequently searched terms related to visitors. Please select one from the options below : <br> 4.1 About us <br>4.2 Programs We Offer <br>4.3 Student Bodies <br>4.3 Extra-Curricular </b>",
    
    "4.1",
    "<b > ABOUT US<br>These are the top results:<br> <br>4.1.1 Director's Address <br> 4.1.2 Principal's Address </b>",
    "4.1.1",
    "<b > 4.1.1 About University<br>The link to About University <a href=" 'https://nuv.ac.in/aboutus/' ">Click Here</a> </b>",
   
    "4.2",
    "<b > PROGRAMS WE OFFER <br>These are the top results:<br> <br>4.2.1 Programs</b>",
    "4.1.1",
    "<b > 4.2.1 Programs<br>The link to Programs <a href=" 'https://nuv.ac.in/e-brochure/bca/' ">Click Here</a> </b>",

    "4.3",
    "<b > STUDENT BODIES <br>These are the top results:<br> <br>4.3.1 Student Start-up <br> 4.3.2 Nirantar</b>",
    "4.3.1",
    "<b > 4.3.1 Students Start-up <br>The link to Students Start-up  <a href=" 'https://nuv.ac.in/innovation/' ">Click Here</a> </b>",
    "4.3.2",
    "<b > 4.3.2 Nirantar <br>The link to Nirantar<a href=" 'https://nuv.ac.in/nirantar/' ">Click Here</a> </b>",
    
    "4.4",
    "<b > EXTRA-CURRICULAR <br>These are the top results:<br> <br>4.4.1 Events  </b>",
    "4.4.1",
    "<b > 4.4.1 Events    <br>The link to Events    <a href=" 'https://nuv.ac.in/beyond-books/#TechnicalFestivals' ">Click Here</a> </b>",
  
]

trainer.train(conversation)
