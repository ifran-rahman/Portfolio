import streamlit as st
from functions import * 
from PIL import Image

st.set_page_config(
        page_title="Ifran Rahman Nijhum", page_icon = "favicon (1).ico"
)
with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
image = Image.open('dp.png')

#####################
# Header 
homeview( image,  
'''
<div style="text-align: left"> 
<h1> Ifran Rahman Nijhum </h1>

I am a fresh graduate. I have completed my BS in CSE from <a href= 'http://www.northsouth.edu/'>North South University</a>, Bangladesh. Previously I worked at <a href='https://cramstack.com/'>
Cramstack</a> as a data science intern. I am currently working on some computer vision and biomedical-based research projects. I have experience and interest in working with Machine Learning and Mobile Application Development. 
I had a paper published in which we worked on an Object Detection model.

Apart from academics, I have participated in many contests. I was highly engaged in co-curricular activities. During last two years of my bachelors I served as the coordinator of Team R&D and one of the Sub-executives of Team Provision at <a href='https://nsusc.acm.org/home.html' >NSU ACM SC</a>.

In my free time, I love watching movies, traveling etc. I like to try out new recepies from time to time as well.
<br>
</div>
<div class="text-center">
  <a href="https://www.linkedin.com/in/ifran-rahman-nijhum-1421b8179/" class="btn btn-light" style="color: #000000">LinkedIn</a>
  <a href="https://github.com/ifran-rahman" class="btn btn-light" style="color: #000000">Github</a>
  <a href=" https://www.researchgate.net/profile/Ifran_Rahman" class="btn btn-light" style="color: #000000">Researchgate</a>
  <a href="https://medium.com/@ifranrahmannijhum-1215" class="btn btn-light" style="color: #000000">Medium</a>  
  </div>
''')


#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-light" style="background-color: #ffffff;">
  <a class="navbar-brand" href= "/" target="_blank">Ifran Rahman Nijhum</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav ml-auto">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#publications-and-projects">Research</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#resume">Resume</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#contact">Contact</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)
st.markdown('''
<br><br><br><br>
''', unsafe_allow_html = True)

st.markdown('''
## Publications and Projects
''')
st.markdown('''
### Publications
''')

txt5('images/vispol.png', 
'''
<div style="text-align: left">
<b> <a href="https://ieeexplore.ieee.org/document/9666654"> Visual Pollution Detection Using Google Street View and YOLO </a> </b> <br>
<b> Authors: </b> Yearat Hossain, Ifran Rahman Nijhum, Abu Adnan Sadi, Md. Tazin Morshed Shad, Rashedur M. Rahman <br>
<b> Conference: </b> IEEE 12th Annual Ubiquitous Computing, Electronics & Mobile Communication Conference (UEMCON)
</div>
''')
st.markdown('''
### Projects (_On going_)
''')

txt5('images/ecg.png', 
'''
<div style="text-align: left">
<b> <a> Heartisan: An Integrated System for ECG Data Monitoring, Collection and Arrhythmia Prediction  </a> </b> <br>

Individual can monitor their ECG graphs and heart arrhythmia conditions. Predicted beats and data can be pushed for verification. 
Doctors can verify each predicted beat. Model gets trained after a certain period of time depending on some criterias.</div>
''')

txt5('images/drkd.png', 
'''
<div style="text-align: left">
<b> <a> Application of a new knowledge distillation methods on OCR models </a> </b> <br>

Trying to improve OCR model using a new knowledge distillation method.
Performing several research experiments on the OCR model.</div>
''')

txt5('images/vispol2.png', 
'''
<div style="text-align: left">
<b> <a> Real World Application of an Object Detection System including Comprehensive Analysis on Different Models </a> </b> <br>

Using a mobile app to get image and location of particular interest. The collected data gets processed for
visualization and further research of an object detction problem. The work also includes comprehensive analysis
of the dataset on different state of the art models. </div>
''')

txt5('https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2018/12/Screenshot-from-2018-11-29-13-03-17.png', 
'''
<div style="text-align: left">
<b> <a> Solving a Local Object Detection Problem</a> </b> <br>

Leading a group of 10 undergrad students from <a href='https://nsusc.acm.org/home.html' >NSU ACM SC</a>, to solve a local object detection problem. Guiding them from to build a 
solution from scratch, including building dataset, training models and building mobile application etc</div>
''')

st.markdown('''
### Projects (_Previous_)
''')

txt5('images/janao.png', 
'''
<div style="text-align: left">
<b> <a> Janao: Public Harassment & Crime Reporting System </a> </b> <br>

A public service application. Helps user to send image, location and necessary information of a crime scene immediately 
to the law enforcement agency. Law enforcement agency has another application to receive and view the sent crimes and details list. <br>
<a href="https://github.com/ifran-rahman/Janao">github</a> 
</div>
''')

txt5('images/dms.png', 
'''
<div style="text-align: left">
<b> <a> Document Management System </a> </b> <br>

A multiplatform document management system. Built using Native android and Django.</div>
''')

#####################

st.markdown('''
## Resume
''')

st.markdown('''
### Education
''')

st.markdown('''
**Bachelor of Science in Computer Science and Engineering**, *North South University*, Bangladesh
- Research thesis entitled `Implementing Different Knowledge Distillation methods on Bangla OCR`
- `Received Best Poster Award`
''')

st.markdown('''
### Work Experience
''')

txt('**Apprentice**, Data Science Department, *Cramstack Limited*, Bangladesh','FEB 2022 - MAY 2022')
st.markdown('''
- Researched OCR apis and wrote documentation on various topics.
- Worked on data cleaning and preparation. Used google data studio for visualization.
''')
txt('**Intern**, Data Science Department, Cramstack Limited, Bangladesh','NOV 2021 – JAN 2022')
st.markdown('''
- Wrote scrips for a doc management application for document manipulation, ocr etc.
- Worked on data cleaning and preparation. Used google data studio for visualization.
''')

#####################
st.markdown('''
### Skills
''')
txt3('`Programming`', '`Python` `Java` `Familiar with:`  `C` `C++` `Arduino`')
txt3('`Frameworks`', '`Pytorch` `TensorFlow` `Keras` `Native Android (Java)` `Flutter`')
txt3('`Database`', '`MySQL` `Firebase`')
txt3('`Version Control and Tools`', '`Git` `GitHub` `Bitbucket`')
txt3('`Data visualization`', '`Google Data Studio` `matplotlib` `seaborn` `plotly`')
txt3('`Presentation`','`PowerPoint`  `Word` `Canva`')

#####################
st.markdown('''
### Service
''')

txt('**Coordinator**, Team Research & Development, *NSU ACM Student Chapter*,' 2020 – 2022 ')
st.markdown('''
- Currently instructing a research project (stated in the project section of this website).
- Managed an international programming contest “Semi-code”, Inter-University Hackathon "HackNSU Season 3”. 
- Planned and arranged intra hackathons, programming contests, and team meetings. 
''')
txt('**Sub Executive**, Team Provision, *NSU ACM Student Chapter*, ' 2020 – 2022 ')
st.markdown('''
- One of the leads of a team of nearly two hundred members.
- Worked in arranging, planning contests, recruitment events and maintaining order and discipline in the team. 
''')

#####################
st.markdown('''
## Contact
''')
txt2('Email', 'ifran.nijhum@northsouth.edu')
txt2('Personal Email', 'ifranrahmannijhum@gmail.com')
