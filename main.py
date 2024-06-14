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
I am currently a PhD student at University College Dublin in Ireland, specializing in solar power forecasting and estimation using artificial intelligence techniques. I work at the <a href= 'https://soumyabrata.dev/theia/'>THEIA lab</a> at UCD. My primary research interest lies in the application of artificial intelligence in different domains. 
<br>
Previously, I served as a Lecturer at <a href= 'https://www.rtm-aktu.edu.bd/'>RTM Al-Kabir Technical University</a> and worked as a Research Assistant at <a href= 'https://sites.google.com/site/tanzilctg/Home'>TnR Lab</a>, North South University. My academic and research journey began with a Bachelor of Science degree in Computer Science and Engineering from <a href= 'http://www.northsouth.edu/'>North South University</a>, Bangladesh.

Apart from academics, I have participated in many contests. I was highly engaged in co-curricular activities. During last two years of my bachelors I served as the coordinator of Team R&D and one of the Sub-executives of Team Provision at <a href='https://nsusc.acm.org/home.html' >NSU ACM SC</a>.

In my free time, I love watching movies, series, traveling and taking photos. I like to try out new recipes from time to time as well!

<br>
</div>
<div class="text-center">
  <a href="https://www.linkedin.com/in/ifran-rahman-nijhum-1421b8179/" class="btn btn-light" style="color: #000000">LinkedIn</a>
  <a href="https://github.com/ifran-rahman" class="btn btn-light" style="color: #000000">Github</a>
  <a href=" https://www.researchgate.net/profile/Ifran_Rahman" class="btn btn-light" style="color: #000000">
  Researchgate</a>
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
        <a class="nav-link" href="#research-and-publications">Research</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#resume">Resume</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#achievements">Achievements</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#service">Service</a>
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
## Research and Publications
''')
st.markdown('''
### Publications
''')

txt5('https://github.com/ifran-rahman/Heartisan/blob/main/images/incremental%20learning.jpg?raw=true', 
'''
<div style="text-align: left">
<b>  <a href="https://ieeexplore.ieee.org/abstract/document/10178842"> Heartisan: An Incremental Learning Based Arrhythmia Detection, Data Collection, and Monitoring System</a> </b> <br>
<b> Authors: </b> Ifran Rahman Nijhum, Anan Ghosh, Hasibul Hassan, Yearat Hossain, Tanzilur Rahman <br>
<b> Conference: </b> IEEE 36th International Symposium on Computer Based Medical Systems (CBMS) 2023, L'Aquila, Italy, 22nd - 24th June, 2023.
<a href="https://github.com/ifran-rahman/Heartisan">repo</a> 
</div>
''')

txt5('images/vispol2.png', 
'''
<div style="text-align: left">
<b> <a href="https://www.sciencedirect.com/science/article/pii/S2772662223001236"> An end-to-end pollution analysis and detection system using artificial intelligence and object detection algorithms </a> </b> <br>
-	Comprehensive analysis of visual pollution on state of the art object detection models<br>
-	End to end incremental learning based data collection and analytics system for visual pollution.
<b> Journal: </b> Decision Analytics Journal | Elsavier
</div>
''')
txt5('images/vispol.png', 
'''
<div style="text-align: left">
<b> <a href="https://ieeexplore.ieee.org/document/9666654"> Visual Pollution Detection Using Google Street View and YOLO </a> </b> <br>
<b> Authors: </b> Yearat Hossain, Ifran Rahman Nijhum, Abu Adnan Sadi, Md. Tazin Morshed Shad, Rashedur M. Rahman <br>
<b> Conference: </b> IEEE 12th Annual Ubiquitous Computing, Electronics & Mobile Communication Conference (UEMCON)
</div>
''')
txt5( 
'''
<div style="text-align: left">
<b> <a>Enhancing Image Quality of Aging Smartphones Using Multi-Scale Residual Feature Fusion Network (_Accepted_) </a> </b> <br>
<b> Authors: </b> M. Y. Hossain, M. M. H. Rakib, I. R. Nijhum and T. Rahman. <br>
<b> Conference: </b> The Third International Conference on Intelligent Systems and Patterns Recognition, Hammamet, Tunisia, 11th – 13th May 2023.</div>
''')
# st.markdown('''
# #### In Revision (_Decision Analytics Journal_)
# ''')


# st.markdown('''
# #### Under Review
# ''')

# txt5('https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2018/12/Screenshot-from-2018-11-29-13-03-17.png', 
# '''
# <div style="text-align: left">
# <b> <a> Solving a Local Object Detection Problem</a> </b> <br>

# Leading a group of 10 undergrad students from <a href='https://nsusc.acm.org/home.html' >NSU ACM SC</a>, to solve a local object detection problem. Guiding them from to build a 
# solution from scratch, including building dataset, training models and building mobile application etc</div>
# ''')

st.markdown('''
### Projects 
''')
txt5('https://www.researchgate.net/publication/350720259/figure/fig2/AS:1010160138989570@1617852353760/Flower-Android-client-architecture.ppm', 
'''
<div style="text-align: left">
<b> <a> Data Secured Biomedical Software </a> </b> <br>
Working on building the federated learning and machine learning pipeline. 
</div>
''')

txt5('images/drkd.png', 
'''
<div style="text-align: left">
<b> <a> Dynamic Rectification Knowledge Distillation Method for CRNN models </a> </b> <br>

Improved OCR model using a novel knowledge distillation method. 
</div>
''')

txt5('images/data_analytics.png', 
'''
<div style="text-align: left">
<b> <a> Customer Sales Data Analysis and Revenue Prediction</a> </b> <br>

Customer data analysis using Google Looker Studio (Data Studio). Deployed Revenue prediction model.<br>
<a href="https://ifran-rahman-customer-data-analysis-prediction-api-qhfvfk.streamlitapp.com/">deployed site</a> &nbsp;
<a href="https://datastudio.google.com/reporting/8d8f0ff8-b3b2-4ec2-8556-f095e695c55e">dashboard</a> &nbsp;
</div>
''')

txt5('images/janao.png', 
'''
<div style="text-align: left">
<b> <a> Janao: Public Harassment & Crime Reporting System </a> </b> <br>
-	Users can send image, location and information of a crime scene immediately to the law enforcement agency <br>
-	Law enforcement agency has another application to receive and view the sent crimes and details list
<a href="https://github.com/ifran-rahman/Janao">repo</a> 
</div>
''')

txt5('images/d-m-s.png', 
'''
<div style="text-align: left">
<b> <a> Document Management Service </a> </b> <br>

A mobile application to digitize and manage documents and files of a particular organization. <br>
-	View all employee’s public profile and files <br>
-	Private repository for private files <br>
-	Upload and capture document images and other files 
<a href="https://github.com/ifran-rahman/Document-Digitization-Service">repo</a> 
</div>
''')

#####################

st.markdown('''
## Resume
''')

st.markdown('''
### Education
''')
st.markdown('''
**Doctor of Philosophy - PhD**, *University College Dublin*, Ireland, 2023 - Present
- Research topic - `Accurate Forecasting of Photovoltaic Potential for Efficient Integration into Residential Homes`
''')

st.markdown('''
**Bachelor of Science in Computer Science and Engineering**, *North South University*, Bangladesh, 2018 - 2022
- Research thesis entitled `Implementing Different Knowledge Distillation methods on Bangla OCR`
- `Received Best Poster Award`
''')

st.markdown('''
### Work Experience
''')
txt('**Lecturer**, Department of Computer Science & Engineering, *RTM Al-Kabir Technical University*, Bangladesh','FEB 2023 - Present')
# st.markdown('''
# - 
# ''')
txt('**Research Assistant**, TnR Lab, *North South University*, Bangladesh','JAN 2023 - Present')
st.markdown('''
- Working on building a data secured ML pipeline.
''')
txt('**Intern**, Data Science Department, Cramstack Limited, Bangladesh','NOV 2021 – MAY 2022')
st.markdown('''
- Research and writing documentations on text summarizers, OCR APIs 
- Document processing, data extraction for a file management application.
- Data cleaning, processing and visualization using BI tool.
''')

#####################
st.markdown('''
### Skills
''')
txt3('`Programming`', '`Python` `Java` `Familiar with:`  `C` `C++` `Arduino`')
txt3('`Frameworks`', '`Pytorch` `TensorFlow` `Keras` `Fast API` `Flower for Federated Learning` `Native Android (Java)` `Flutter`')
txt3('`Database`', '`MySQL` `Firebase`')
txt3('`Version Control and Tools`', '`Git` `GitHub` `Bitbucket`')
txt3('`Data visualization`', '`Google Data Studio` `matplotlib` `seaborn` `plotly`')
txt3('`Presentation`','`PowerPoint`  `Word` `Canva`')

st.markdown('''
## Achievements
''')

txt5('images/ic.jpg', 
'''
<div style="text-align: left">
<b> Champion</b>, Best Poster Category, <i>Innovation Challenge, 2022 </i> <br>

Final year thesis showcase.</div>
''')
txt5('images/hacknsu.jpg', 
'''
<div style="text-align: left">
<b> 1st Runner Up </b>, <i>HackNSU, 2019</i> <br>

Developed an web based solution to the then undergraduate admission problems of Bangladesh.</div>
''')

#####################
st.markdown('''
## Service
''')

txt('**Coordinator**, Team Research & Development, *NSU ACM Student Chapter*','Jan 2020 - Jan 2022')
st.markdown('''
- Instructed an object detection research project. 
- Managed an international programming contest “Semi-code”, Inter-University Hackathon "HackNSU Season 3”. 
- Planned and arranged intra-hackathons, programming contests, and team meetings. 
''')
txt('**Sub Executive**, Team Provision, *NSU ACM Student Chapter*', 'Nov 2020 - Feb 2022')
st.markdown('''
- One of the leads of a team of nearly two hundred members.
- Worked in arranging, planning contests, recruitment events and maintaining order and discipline in the team. 
''')

#####################
st.markdown('''
## Contact
''')
txt2('Email', 'ifran.nijhum@ucdconnect.ie')
txt2('Personal Email', 'ifranrahmannijhum@gmail.com')
txt2(' ', ' ')

