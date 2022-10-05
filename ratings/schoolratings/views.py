from cmath import nan
from email.headerregistry import Address
from django.shortcuts import render
from .models import *
import pandas as pd
import json
df_1=pd.DataFrame()
df_2=pd.read_excel(r"D:\Django\ratings\sample_data_main.xlsx")
df=pd.DataFrame()
df2=pd.read_excel(r"D:\Django\ratings\sample_data_main.xlsx")
df_2=pd.read_excel(r"D:\Django\ratings\sample_data_main.xlsx")
df=pd.DataFrame()
df2=pd.read_excel(r"D:\Django\ratings\sample_data_main.xlsx")
def home(request):
    return render(request,'index.html',{"i":1})
def school(request,state,city,g,pg_num):
    print(city)
    if city=="school":
        df_1=pd.read_excel(r"D:\Django\ratings\sample_data_details.xlsx")

    

    else:
        v1=pd.read_excel(r"D:\Django\ratings\sample_data_details.xlsx")

        df_1=v1.loc[v1["city"]==city]

    if g=="p":

        df=df_1.loc[df_1["type_of_school"]=="p"]

    elif g=="e":
        df=df_1.loc[df_1["type_of_school"]=="e"]

    elif g=="m":
        df=df_1.loc[df_1["type_of_school"]=="m"]

    elif g=="h":
        df=df_1.loc[df_1["type_of_school"]=="h"]
    elif g=="public":
        df=df_1.loc[df_1["type_of_school"]=="public"]
    elif g=="charter":
        df=df_1.loc[df_1["type_of_school"]=="charter"]
    elif g=="private":
        df=df_1.loc[df_1["type_of_school"]=="private"]

    s=list(df["school"])
    t=list(df["type"])
    r=list(df["review"])
    d=list(df["district"])
    t_s=list(df["total_students"])
    s_r=list(df["stud_t_ratio"])
    address=list(df["address"])
    grades=list(df["Grades"])

    ResultLog.objects.create(
        total_students=json.dumps(list(df["total_students"])),
        city=json.dumps(list(df["city"])),
        school = json.dumps(list(df["school"])),
        type = json.dumps(list(df["type"])),
        grades = json.dumps(list(df["Grades"])),
        stud_t_ratio=json.dumps(list(df["stud_t_ratio"])),
        review=json.dumps(list(df["review"])),
        district=json.dumps(list(df["district"])),
        address=json.dumps(list(df["address"]))
    )
    print("done")
    if (len(s)//15)*15<len(s):
        length=(len(s)//15) + 1
    else:
        length=(len(s)//15)
    s=s[(pg_num-1)*15:pg_num*15]
    t=t[(pg_num-1)*15:pg_num*15]
    r=r[(pg_num-1)*15:pg_num*15]
    d=d[(pg_num-1)*15:pg_num*15]
    t_s=t_s[(pg_num-1)*15:pg_num*15]

    grades=grades[(pg_num-1)*15:pg_num*15]
    address=address[(pg_num-1)*15:pg_num*15]


    data=zip(s,t,r,address,t_s,grades)
    context={
        "data":data,
        "loop":range(1,length+1),
        'x':pg_num,
        'state':"California",
        'length':length
    }
    return render(request,'school.html',context)

def sch_details(request,state,city,g,school):


    if city=="school":
        df_1=pd.read_excel(r"D:\Django\ratings\sample_data_details.xlsx")
    else:
        v1=pd.read_excel(r"D:\Django\ratings\sample_data_details.xlsx")
        df_1=v1.loc[v1["city"]==city]
    if g=="p":
        df=df_1.loc[df_1["type_of_school"]=="p"]

    elif g=="e":
        df=df_1.loc[df_1["type_of_school"]=="e"]

    elif g=="m":
        df=df_1.loc[df_1["type_of_school"]=="m"]

    elif g=="h":
        df=df_1.loc[df_1["type_of_school"]=="h"]
    elif g=="public":
        df=df_1.loc[df_1["type_of_school"]=="public"]
    elif g=="charter":
        df=df_1.loc[df_1["type_of_school"]=="charter"]
    elif g=="private":
        df=df_1.loc[df_1["type_of_school"]=="private"]
    s=list(df["school"])
    t=list(df["type"])
    r=list(df["review"])
    d=list(df["district"])
    t_s=list(df["total_students"])
    s_r=list(df["stud_t_ratio"])
    address=list(df["address"])
    index_val=list(df["school"]).index(school.replace(" ","-"))
    s=s[index_val]
    t=t[index_val]
    r=r[index_val]
    d=d[index_val]
    t_s=t_s[index_val]
    s_r=s_r[index_val]
    address=address[index_val]

    index_val=list(df2["schl_name"]).index(school.replace("-"," "))
    module=list(df2["module_name"])
    fr_t_schl=list(df2["response_clearfix"])
    ac_progress=list(df2["academic_progress"])
    student_demography=list(df2["Students"])
    Advanced_courses=list(df2["Advanced_courses"])
    Test_scores=list(df2["Test_scores"])
    Equity_overview=list(df2["Equity_overview"])

    Low_income_students=list(df2["Low-income_students"])
    Students_with_Disabilities=list(df2["Students_with_Disabilities"])
    courses_and_program=list(df2["courses_and_program"])
    tab_Race_ethnicity=list(df2["tab_Race_ethnicity"])
    tab_low_income=list(df2['tab_low_income'])
    Race_ethnicity=list(df2["Race_ethnicity"])
    neighborhood=list(df2["neighborhood"])
    web_link=list(df2["web_link"])
    review=list(df2["Review"])
    fr_t_schl=fr_t_schl[index_val]
    student_demography=student_demography[index_val]
    ac_progress=ac_progress[index_val]
    courses_and_program=courses_and_program[index_val]
    neighborhood=neighborhood[index_val]
    web_link=web_link[index_val]
    Advanced_courses=Advanced_courses[index_val]
    Test_scores=Test_scores[index_val]
    Equity_overview=Equity_overview[index_val]
    Race_ethnicity=Race_ethnicity[index_val]
    Low_income_students=Low_income_students[index_val]
    Students_with_Disabilities=Students_with_Disabilities[index_val]
    tab_Race_ethnicity=tab_Race_ethnicity[index_val]
    tab_low_income=tab_low_income[index_val]
    tab_Race_ethnicity=tab_Race_ethnicity.split(",")
    tab_r=[]

    tab_rv=[]
    di_r={}
    Race_ethnicity=Race_ethnicity.split(";")
    for i in tab_Race_ethnicity:
        i=i.split(':')
        tab_r.append(i[0])

        tab_rv.append(i[1])
    j=0
    for i in tab_rv:
        if tab_r[j] in di_r:

            temp_d={}
            re=Race_ethnicity[j].split(",")
            for l in re:
                tm_re=l.split(":")
                temp_d[tm_re[0]]=tm_re[1].replace("%","").strip()

            di_r[tab_r[j]][i]=temp_d
        else:
            temp_d={}
            re=Race_ethnicity[j].split(",")
            for l in re:
                tm_re=l.split(":")
                temp_d[tm_re[0]]=tm_re[1].replace("%","").strip()
            di_r[tab_r[j]]={}
            di_r[tab_r[j]][i]=temp_d
        j+=1
    
    module=(module[index_val].split(","))
    modules=[]
    for i in module:
        modules.append(i.strip().replace("\n",""))
    review=review[index_val]
    x=[]
    try:
        for i in fr_t_schl.split(","):
            x.append(i)
    except:
        x.append("Do you work at this school? \n Claim this school to update information and let us know what makes your school special.")

    y=[]
    try:
        for i in courses_and_program.split(","):
            y.append(i)
    except:
        y.append(courses_and_program)

    nh=[]
    try:
        for i in neighborhood.split("   "):
            if i.strip()!='':
                nh.append(i.strip())
    except:
        y.append(courses_and_program)
    
    a_p=[]


    try:
        for i in ac_progress.split(","):


            a_p.append(i)
    except:
        a_p.append(ac_progress)
    s_d=[]
    try:
        for i in student_demography.split(","):
            s_d.append(i)
    except:
        s_d.append(student_demography)

    a_c=[]
    try:
        for i in Advanced_courses.split(","):
            a_c.append(i)
    except:
        a_c.append(Advanced_courses)

    t_s=[]
    try:

        for i in Test_scores.split(","):
            t_s.append(i)
    except:
        t_s.append(Test_scores)

    e_o=[]
    try:
        for i in Equity_overview.split(","):
            e_o.append(i)
    except:
        e_o.append("In this section, we publish a rating that reflects how well this school is serving disadvantaged students, compared to other schools in the state, based on college readiness, learning progress, and test score data provided from the state’s Department of Education. The state does not provide enough information for us to calculate an Equity Rating for this school.")



    l_i_s=[]
    try:
        for i in Low_income_students.split(","):
            l_i_s.append(i)
    except:
        l_i_s.append(Low_income_students)


    s_w_d=[]
    try:
        for i in Students_with_Disabilities.split(","):
            s_w_d.append(i)
    except:
        s_w_d.append(Students_with_Disabilities)
    reviews=[]
    try:
        for i in review.split(","):
            i=i.replace("%","")
            reviews.append(i)
    except:
        reviews.append(review)
    nh=[]    
    try:
        for i in neighborhood.split("   "):
            if i.strip()!='':
                nh.append(i.strip())
    except:
        y.append(courses_and_program)    
    rev_sum=0
    count=5
    for i in reviews:
        if count:
            try:
                rev_sum+=int(i)*count
            except:
                rev_sum+=0
        count-=1
    avg=int(str(rev_sum)[:2])/20
    sch_leader=nh[2]
    sl=sch_leader.split(":")
    


    context={
        's':s,
        't':t,
        'r':r,
        'd':d,
        't_s':t_s,
        'school':school,
        's_r':s_r,
        'add':address,
        'module':modules,
        'fr_t_schl':x,
        'courses_and_program':y,
        'ac_progress':a_p[0],
        'student_demography':s_d,
        'neighborhood':nh,
        "web_link":web_link,
        's_w_d':s_w_d,
        'l_i_s':l_i_s,
        'r_e':Race_ethnicity,
        'e_o':e_o,
        't_s':t_s,
        'a_c':a_c,
        's_d':s_d,
        'review':reviews,
        'di_r':di_r,
        'state':state,
        'city':city,
        'g':g,
        'starrange': range(1,6),
        'numrange':range(0,5),
        'n':"\N{WHITE MEDIUM STAR}",
        'average':avg,
        'slm':sl[0],
        'sl_name':sl[1],
        'nh':nh
        }

    return render(request,'school_details.html',context)




































def state(request,state,city):
    if city!="school":
        v1=pd.read_excel(r"D:\Django\ratings\sample_data_details.xlsx")
        v1=pd.read_excel(r"E:\sample_data_details.xlsx")

        df_1=v1.loc[v1["city"]==city]
        y=list(df_1["type_of_school"])
        c=list(df_1["city"])

    else:
        v1=pd.read_excel(r"D:\Django\ratings\sample_data_details.xlsx")
        v1=pd.read_excel(r"D:\Django\ratings\sample_data_details.xlsx")
        y=list(v1["type_of_school"])
        c=list(v1["city"])


    context={
        "preschool_link":"/"+state+"/"+city+"/"+"grade=p"+"/"+"1",
        "p":y.count("p"),
        'state':state,
        "elementary_link":"/"+state+"/"+city+"/"+"grade=e"+"/"+"1",
        "e":y.count("e"),
        "middle_link":"/"+state+"/"+city+"/"+"grade=m"+"/"+"1",
        "m":y.count("m"),
        "high_link":"/"+state+"/"+city+"/"+"grade=h"+"/"+"1",
        "h":y.count("h"),
        "public_link":"/"+state+"/"+city+"/"+"grade=public"+"/"+"1",
        "public":y.count("public"),
        "charter_link":"/"+state+"/"+city+"/"+"grade=charter"+"/"+"1",
        "charter":y.count("charter"),
        "private_link":"/"+state+"/"+city+"/"+"grade=private"+"/"+"1",
        "private":y.count("private"),
        'city':c[:8]


    }
    return render(request,'state.html',context)

def review_page(request,state,city,g,school):
    if request.method == 'POST':
        g =request.POST.get("rate")
        like_school =request.POST.get("like_school")
        review_box =request.POST.get("review_box")
        review_box =request.POST.get("review_box")
        Family_Engagement =request.POST.get("Family_Engagement")
        Social_emotional_support =request.POST.get("Social_emotional_support")
        Safety_val =request.POST.get("Safety_val")
        teaching_val =request.POST.get("teaching_val")
        spec_edu_val =request.POST.get("spec_edu_val")
        learning_val =request.POST.get("learning_val")

    else:
        return render(request,'review.html')
