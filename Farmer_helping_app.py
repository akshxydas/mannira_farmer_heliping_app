import random

from flask import Flask, render_template, request, redirect, session, jsonify
from DBConnection import Db


import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail

app = Flask(__name__)
app.secret_key="hhhh"
static_path=r"C:\Users\Akshay Das\PycharmProjects\Farmer_helping_app\static\\"


@app.route("/")
def log():
    db = Db()
    res = db.select("SELECT * FROM notification ORDER BY notification_id DESC LIMIT 8")
    res2 = db.select(
        "SELECT * FROM `feedback`, farmer WHERE feedback.farmer_id=`farmer`.farmer_id ORDER BY `feedback_id` DESC LIMIT 8")
    res3 = db.select("SELECT * FROM contact ORDER BY `contact_id` DESC LIMIT 9")
    res4 = db.select("SELECT * FROM story where type='story' ORDER BY `story_id` DESC LIMIT 6")
    return render_template("main_index.html", data=res, data2=res2, data3=res3, data4=res4)

@app.route("/logout")
def logout():
    session['lg']=""
    return redirect("/login")



@app.route("/forgot_password", methods=[ 'post'])
def forgot_password():
        email=request.form['textfield']
        db=Db()
        res=db.selectOne("SELECT * FROM login WHERE username='"+email+"'")
        if res is None:
            return "<script>alert('Email not registered');window.location='/login';</script>"
        else:
            password=res["password"]
            try:
                gmail = smtplib.SMTP('smtp.gmail.com', 587)

                gmail.ehlo()

                gmail.starttls()

                gmail.login('mannira.2k22@gmail.com', 'mtrwbhixdfzfeebm')

            except Exception as e:
                print("Couldn't setup email!!" + str(e))

            msg = MIMEText("Your Password for login is " + password)

            msg['Subject'] = 'Password for Mannira Website'

            msg['To'] = email

            msg['From'] = 'mannira.2k22@gmail.com'

            try:

                gmail.send_message(msg)

            except Exception as e:

                print("COULDN'T SEND EMAIL", str(e))
            return "<script>alert('Password sent to your mail');window.location='/';</script>"



@app.route('/login', methods=['get', 'post'])
def login():
    if request.method=="POST":
        username=request.form['textfield']
        password=request.form['textfield2']
        db=Db()
        res=db.selectOne("SELECT *FROM `login` WHERE USERNAME='"+username+"' AND PASSWORD='"+password+"'")
        if res is None:
            return "<script>alert('Invalid details');window.location='/';</script>"
        else:
            utype=res['type']
            session['lid']=str(res['login_id'])
            if utype=="admin":
                session['lg'] = "yes"
                return redirect("/admin_home")
            elif utype=="officer":
                session['lg'] = "yes"
                return redirect("/officer_home")
            elif utype=="farmer":
                session['lg'] = "yes"
                return redirect("/farmer_home")
            else:
                return "<script>alert('Unauthorised User');window.location='/login';</script>"
    else:
        return render_template("login_temp.html")
        # return render_template("login.html")



@app.route("/admin_home")
def admin_home():
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    return render_template("admin/index.html")
    # return render_template("admin/home.html")

@app.route("/admin_add_officer", methods=['get', 'post'])
def admin_add_officer():
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    if request.method=="POST":
        name=request.form['textfield']
        Email=request.form['textfield2']
        phone=request.form['textfield3']
        place=request.form['textfield4']
        district=request.form['textfield5']
        db = Db()
        password=random.randint(1000, 9999)
        lid=db.insert("INSERT INTO `login`(username,PASSWORD,TYPE)VALUES('"+Email+"','"+str(password)+"','officer')")
        db.insert("INSERT INTO `agricuture_office`(office_id,NAME,email,phone,place,district) VALUES('"+str(lid)+"','"+name+"','"+Email+"','"+phone+"','"+place+"','"+district+"')")

        #   mail sending
        try:
            gmail = smtplib.SMTP('smtp.gmail.com', 587)
            gmail.ehlo()
            gmail.starttls()
            gmail.login('mannira.2k22@gmail.com', 'mtrwbhixdfzfeebm')

        except Exception as e:
            print("Couldn't setup email!!" + str(e))

        msg = MIMEText("Username  :  " + Email + "\nPassword  :  " + str(password) )
        msg['Subject'] = 'Login credentials for Mannira Website'
        msg['To'] = Email
        msg['From'] = 'mannira.2k22@gmail.com'

        try:
            gmail.send_message(msg)
        except Exception as e:
            print("COULDN'T SEND EMAIL", str(e))
        #   mail sending end

        return "<script>alert('Officer Added');window.location='/admin_add_officer';</script>"
    else:
        return render_template("admin/add_agriculture_officer.html")

@app.route("/admin_add_Application", methods=['get', 'post'])
def admin_add_Application():
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    if request.method == "POST":
        Name = request.form['textfield']
        No = request.form['textfield2']
        Description = request.form['textarea']
        Last_Date = request.form['textfield3']
        db=Db()
        db.insert("INSERT INTO `application`(DATE, app_number, NAME, description, last_date) VALUES(CURDATE(), '"+No+"', '"+Name+"', '"+Description+"', '"+Last_Date+"')")
        return "<script>alert('Application Added');window.location='/admin_add_Application';</script>"
    else:
         return render_template("admin/add_Application.html")

@app.route("/admin_add_contact", methods=['get', 'post'])
def admin_add_contact():
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    if request.method == "POST":
        Name = request.form['textfield']
        Contact_Number = request.form['textfield2']
        E_mail = request.form['textfield3']
        db = Db()
        db.insert("INSERT INTO `contact`(contact_name,contact_number,email) VALUES('"+Name+"','"+Contact_Number+"','"+E_mail+"')")

        return "<script>alert('Contact Added');window.location='/admin_add_contact';</script>"
    else:
         return render_template("admin/add_contact.html")

@app.route("/admin_add_crop", methods=['get', 'post'])
def admin_add_crop():
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    if request.method == "POST":
        Name = request.form['textfield']
        Price_per_packet_seed= request.form['textfield2']
        Category = request.form['textfield5']
        Link = request.form['textfield3']
        db = Db()
        db.insert("INSERT INTO `crop`(NAME,price,crop_category,DATE,link) VALUES('"+Name+"','"+Price_per_packet_seed+"','"+Category+"',curdate(), '"+Link+"')")
        return "<script>alert('Crop Added');window.location='/admin_add_crop';</script>"
    else:
         return render_template("admin/add_crop.html")

@app.route("/admin_add_FAQ", methods=['get', 'post'])
def admin_add_FAQ():
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    if request.method == "POST":
        Question = request.form['textarea2']
        Answer= request.form['textarea']
        db = Db()
        db.insert("INSERT INTO `faq`(question,answer) VALUES('"+Question+"','"+Answer+"')")


        return "<script>alert('FAQ Added');window.location='/admin_add_FAQ';</script>"
    else:
         return render_template("admin/add_FAQ.html")

@app.route("/admin_add_FERTILIZER", methods=['get', 'post'])
def admin_add_FERTILIZER():
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    if request.method == "POST":
        Name = request.form['textfield']
        Price_list= request.form['textfield2']
        Description = request.form['textarea']
        Link = request.form['textfield3']
        db = Db()
        db.insert("INSERT INTO `fertilizer`(price_list,NAME,description,link,DATE) VALUES('"+Price_list+"','"+Name+"','"+Description+"','"+Link+"',curdate())")

        return "<script>alert('Fertilizer Added');window.location='/admin_add_FERTILIZER';</script>"
    else:
         return render_template("admin/add_FERTILIZER.html")

@app.route("/admin_add_machine", methods=['get', 'post'])
def admin_add_machine():
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    if request.method == "POST":
        Name = request.form['textfield']
        Description = request.form['textarea']
        Link = request.form['textfield3']
        Manufacture = request.form['textfield4']
        db = Db()
        db.insert("INSERT INTO `machine`(NAME,description,DATE,link,manufacture) VALUES('"+Name+"','"+Description+"', curdate(),'"+Link+"','"+Manufacture+"')")

        return "<script>alert('Machine Added');window.location='/admin_add_machine';</script>"
    else:
        return render_template("admin/add_machine.html")

@app.route("/admin_add_notification", methods=['get', 'post'])
def admin_add_notification():
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    if request.method == "POST":
        Title = request.form['textfield']
        Description = request.form['textarea']
        Link = request.form['textfield3']
        db = Db()
        db.insert("INSERT INTO `notification`(title,DATE,description,link)VALUES('"+Title+"',CURDATE(),'"+Description+"','"+Link+"')")

        return "<script>alert('Notification Added');window.location='/admin_add_notification';</script>"
    else:
         return render_template("admin/add_notification.html")

@app.route("/admin_add_policy", methods=['get', 'post'])
def admin_add_policy():
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    if request.method == "POST":
        Title = request.form['textfield']
        Description = request.form['textarea']
        Link = request.form['textfield4']
        date=request.form['textfield3']
        db = Db()
        db.insert("INSERT INTO `policy`(title,description,DATE,link)VALUES('"+Title+"','"+Description+"','"+date+"','"+Link+"')")
        return "<script>alert('Policy Added');window.location='/admin_add_policy';</script>"
    else:
         return render_template("admin/add_policy.html")
import time
@app.route("/admin_add_price", methods=['get', 'post'])
def admin_add_price():
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    if request.method == "POST":
        File_Path = request.files['fileField']
        dt=time.strftime("%Y%m%d_%H%M%S")
        File_Path.save(static_path + "files\\" + dt + ".pdf")
        path="/static/files/"+ dt + ".pdf"
        db = Db()
        db.insert("INSERT INTO `price`(DATE,filepath)VALUES(CURDATE(),'"+path+"')")
        return "<script>alert('Price Added');window.location='/admin_add_price';</script>"
    else:
         return render_template("admin/add_price.html")

@app.route("/admin_add_subsidy", methods=['get', 'post'])
def admin_add_subsidy():
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    if request.method == "POST":
        Subsidy_Name = request.form['textfield']
        Description = request.form['textarea']
        Last_Date = request.form['textfield3']
        Eligibility = request.form['textfield4']
        db = Db()
        db.insert("INSERT INTO `subsidy`(subsidy_name,description,date_of_issue,last_date,eligibility)VALUES('"+Subsidy_Name+"','"+Description+"',CURDATE(),'"+Last_Date+"','"+Eligibility+"')")
        return "<script>alert('Subsidy Added');window.location='/admin_add_subsidy';</script>"
    else:
         return render_template("admin/add_subsidy.html")

@app.route("/admin_edit_agriculture_officer/<aoid>", methods=['get', 'post'])
def admin_edit_agriculture_officer(aoid):
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    if request.method == "POST":
        Name = request.form['textfield']
        Email = request.form['textfield2']
        phone = request.form['textfield3']
        place = request.form['textfield4']
        district = request.form['textfield5']
        db = Db()
        db.update("UPDATE `agricuture_office` SET NAME='"+Name+"',email='"+Email+"',phone='"+phone+"',place='"+place+"',district='"+district+"' WHERE office_id='"+aoid+"'")
        return redirect("/admin_view_agriculture_officer#content")
    else:
        db = Db()
        res = db.selectOne("SELECT * FROM `agricuture_office`WHERE office_id='"+aoid+"'")
        return render_template("admin/edit_agriculture_officer.html",data=res)

@app.route("/admin_edit_Application", methods=['get', 'post'])
def admin_edit_Application():
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    if request.method == "POST":
        Name = request.form['textfield']
        Number = request.form['textfield2']
        Date = request.form['textfield4']
        Description = request.form['textarea']
        Last_Date = request.form['textfield3']

        return redirect("/admin_view_application#content")
    else:
        return render_template("admin/edit_Application.html")

@app.route("/admin_edit_contact/<ctid>", methods=['get', 'post'])
def admin_edit_contact(ctid):
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    if request.method == "POST":
        Name = request.form['textfield']
        Contact_Number = request.form['textfield2']
        E_mail = request.form['textfield3']
        db = Db()
        db.update("UPDATE`contact` SET contact_name='"+Name+"',contact_number='"+Contact_Number+"',email='"+E_mail+"' WHERE contact_id='"+ctid+"'")
        return redirect("/admin_view_contact#content")
    else:
        db = Db()
        res=db.selectOne("SELECT * FROM `contact` WHERE contact_id='"+ctid+"'")
        return render_template("admin/edit_contact.html",data=res)

@app.route("/admin_edit_crop/<cid>", methods=['get', 'post'])
def admin_edit_crop(cid):
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    if request.method == "POST":
        Name = request.form['textfield']
        Price_per_packet_seed = request.form['textfield2']
        Category = request.form['textfield5']
        Link = request.form['textfield3']
      # Date = request.form['textfield4']
        db = Db()
        db.update("UPDATE `crop` SET NAME='"+Name+"',price='"+Price_per_packet_seed+"',crop_category='"+Category+"',DATE=curdate(),link='"+Link+"' WHERE crop_id='"+cid+"'")
        return redirect("/admin_view_crop#content")
    else:
        db = Db()
        res = db.selectOne("SELECT * FROM `crop` WHERE crop_id='" + cid + "'")
        return render_template("admin/edit_crop.html",data=res)

@app.route("/admin_edit_FAQ", methods=['get', 'post'])
def admin_edit_FAQ():
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    if request.method == "POST":
        Question = request.form['textarea2']
        Answer = request.form['textarea']

        return redirect("/admin_view_FAQ#content")
    else:

        return render_template("admin/edit_FAQ.html")

@app.route("/admin_edit_FERTILIZER/<fid>", methods=['get', 'post'])
def admin_edit_FERTILIZER(fid):
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    if request.method == "POST":
        Name = request.form['textfield']
        Price_list_per_KG = request.form['textfield2']
        Description = request.form['textarea']
        Link = request.form['textfield3']
        #Date = request.form['textfield4']
        db = Db()
        db.update("UPDATE `fertilizer` SET price_list='"+Price_list_per_KG+"',NAME='"+Name+"',description='"+Description+"',link='"+Link+"',DATE=curdate() WHERE fertilizer_id='"+fid+"'")
        return redirect("/admin_view_FERTILIZER#content")
    else:
        db = Db()
        res = db.selectOne("SELECT * FROM `fertilizer` WHERE fertilizer_id='"+fid+"'")
        return render_template("admin/edit_FERTILIZER.html",data=res)

@app.route("/admin_edit_machine/<mid>", methods=['get', 'post'])
def admin_edit_machine(mid):
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    if request.method == "POST":
        Name = request.form['textfield']
        # Date = request.form['textfield2']
        Description = request.form['textarea']
        Link = request.form['textfield3']
        Manufacture = request.form['textfield4']
        db = Db()
        db.update("UPDATE `machine` SET NAME='"+Name+"',description='"+Description+"',link='"+Link+"',manufacture='"+Manufacture+"' WHERE machine_id='"+mid+"'")

        return redirect("/admin_view_machine#content")
    else:
        db = Db()
        res = db.selectOne("SELECT * FROM `machine` WHERE machine_id='"+mid+"'")
        return render_template("admin/edit_machine.html",data=res)

@app.route("/admin_edit_notification/<nid>", methods=['get', 'post'])
def admin_edit_notification(nid):
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    if request.method == "POST":
        Title = request.form['textfield']
        Description = request.form['textarea']
        Link = request.form['textfield3']
        db = Db()
        db.update("UPDATE `notification` SET DATE=curdate(),TITLE='"+Title+"',description='"+Description+"',link='"+Link+"' WHERE notification_id='"+nid+"'")

        return redirect("/admin_view_notification#content")
    else:
        db = Db()
        res = db.selectOne("SELECT * FROM `notification` WHERE notification_id='"+nid+"'")
        return render_template("admin/edit_notification.html",data=res)

@app.route("/admin_edit_policy/<pid>", methods=['get', 'post'])
def admin_edit_policy(pid):
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    if request.method == "POST":
        Title = request.form['textfield']
        Description = request.form['textarea']
        Date = request.form['textfield3']
        Link = request.form['textfield4']
        db=Db()
        db.update(" UPDATE policy SET title = '"+Title+"', description = '"+Description+"', DATE = '"+Date+"', link = '"+Link+"' WHERE policy_id = '"+pid+"'")
        return redirect("/admin_view_policy#content")
    else:
        db=Db()
        res=db.selectOne("SELECT * FROM policy WHERE policy_id='"+pid+"'")
        return render_template("admin/edit_policy.html", data=res)

@app.route("/admin_edit_price", methods=['get', 'post'])
def admin_edit_price():
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    if request.method == "POST":
        File_Path = request.form['fileField']
        Date = request.form['textfield2']

        return redirect("/admin_view_price#content")
    else:

        return render_template("admin/edit_price.html")

@app.route("/admin_edit_subsidy/<sid>", methods=['get', 'post'])
def admin_edit_subsidy(sid):
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    if request.method == "POST":
        Subsidy_Name = request.form['textfield']
        #Date_of_issue = request.form['textfield2']
        Description = request.form['textarea']
        Last_Date = request.form['textfield3']
        Eligibility = request.form['textfield4']
        db = Db()
        db.update("UPDATE `subsidy` SET subsidy_name='"+Subsidy_Name+"',description='"+Description+"',date_of_issue=curdate(),last_date='"+Last_Date+"',eligibility='"+Eligibility+"' WHERE subsidy_id='"+sid+"'")
        return redirect("/admin_view_subsidy#content")
    else:
        db = Db()
        res = db.selectOne("SELECT * FROM `subsidy` WHERE subsidy_id='"+sid+"'")
        return render_template("admin/edit_subsidy.html",data=res)

@app.route("/admin_send_reply/<clid>", methods=['get', 'post'])
def admin_send_reply(clid):
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    if request.method == "POST":
        Reply = request.form['textarea']
        db = Db()
        db.update("UPDATE `complaint_reply` SET reply='"+Reply+"' WHERE complaint_id='"+clid+"'  ")
        return "<script>alert('Reply Send');window.location='/admin_view_compliant';</script>"
    else:

        return render_template("admin/send_reply.html")

@app.route("/admin_view_agriculture_officer")
def admin_view_agriculture_officer():
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    db=Db()
    res=db.select("SELECT * FROM `agricuture_office`")
    return render_template("admin/view_agriculture_officer.html",data=res)
@app.route("/admin_delete_officer/<oid>")
def admin_delete_officer(oid):
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    db=Db()
    db.delete("DELETE FROM `agricuture_office` WHERE office_id='"+oid+"'")
    return redirect("/admin_view_agriculture_officer#content")

@app.route("/admin_view_application")
def admin_view_application():
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    db=Db()
    res=db.select("SELECT * FROM `application`")
    return  render_template("admin/view_application.html",data=res)
@app.route("/admin_delete_application/<aid>")
def admin_delete_application(aid):
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    db=Db()
    db.delete("DELETE FROM `application` WHERE application_id='"+aid+"'")
    return redirect("/admin_view_application#content")




@app.route("/admin_view_compliant")
def admin_view_compliant():
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    db = Db()
    res = db.select("SELECT * FROM`complaint_reply`,`farmer` WHERE `complaint_reply`.farmer_id=farmer.farmer_id")
    return render_template("admin/view_compliant.html",data=res)

@app.route("/admin_view_contact")
def admin_view_contact():
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    db=Db()
    res=db.select("SELECT * FROM contact")
    return render_template("admin/view_contact.html", data=res)

@app.route("/admin_delete_contact/<cid>")
def admin_delete_contact(cid):
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    db=Db()
    db.delete("DELETE FROM `contact` WHERE contact_id='"+cid+"'")
    return redirect("/admin_view_contact#content")


@app.route("/admin_view_crop")
def admin_view_crop():
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    db=Db()
    res=db.select("SELECT * FROM `crop`")
    return render_template("admin/view_crop.html",data=res)
@app.route("/admin_delete_crop/<cid>")
def admin_delete_crop(cid):
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    db=Db()
    db.delete("DELETE FROM `crop` WHERE crop_id='"+cid+"'")
    return redirect("/admin_view_crop#content")

@app.route("/admin_view_enquiry")
def admin_view_enquiry():
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    db = Db()
    res = db.select("SELECT * FROM `enquiry`")
    return render_template("admin/view_enquiry.html",data=res)

@app.route("/admin_view_FAQ")
def admin_view_FAQ():
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    db=Db()
    res=db.select("SELECT * FROM `faq`")
    return render_template("admin/view_FAQ.html",data=res)
@app.route("/admin_delete_faq/<faqid>")
def admin_delete_faq(faqid):
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    db=Db()
    db.delete("DELETE FROM `faq` WHERE q_id='"+faqid+"'")
    return redirect("/admin_view_FAQ#content")

@app.route("/admin_view_feedback")
def admin_view_feedback():
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    db = Db()
    res = db.select("SELECT * FROM `feedback`, `farmer` WHERE `feedback`.farmer_id=farmer.farmer_id")
    return render_template("admin/view_feedback.html",data=res)

@app.route("/admin_view_FERTILIZER")
def admin_view_FERTILIZER():
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    db = Db()
    res = db.select("SELECT * FROM`fertilizer`")
    return render_template("admin/view_FERTILIZER.html",data=res)
@app.route("/admin_delete_fertilizer/<fid>")
def admin_delete_fertilizer(fid):
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    db=Db()
    db.delete("DELETE FROM `fertilizer` WHERE fertilizer_id='"+fid+"'")
    return redirect("/admin_view_FERTILIZER#content")

@app.route("/admin_view_machine")
def admin_view_machine():
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    db = Db()
    res = db.select("SELECT * FROM `machine`")
    return render_template("admin/view_machine.html",data=res)
@app.route("/admin_delete_machine/<mid>")
def admin_delete_machine(mid):
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    db=Db()
    db.delete("DELETE FROM `machine` WHERE machine_id='"+mid+"'")
    return redirect("/admin_view_machine#content")

@app.route("/admin_view_notification")
def admin_view_notification():
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    db = Db()
    res = db.select("SELECT * FROM `notification`")
    return render_template("admin/view_notification.html",data=res)
@app.route("/admin_delete_notification/<nid>")
def admin_delete_notification(nid):
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    db=Db()
    db.delete("DELETE FROM `notification` WHERE notification_id='"+nid+"'")
    return redirect("/admin_view_notification#content")

@app.route("/admin_view_policy")
def admin_view_policy():
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    db = Db()
    res = db.select("SELECT * FROM `policy`")
    return render_template("admin/view_policy.html",data=res)
@app.route("/admin_delete_policy/<pid>")
def admin_delete_policy(pid):
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    db=Db()
    db.delete("DELETE FROM `policy` WHERE policy_id='"+pid+"'")
    return redirect("/admin_view_policy#content")

@app.route("/admin_view_price")
def admin_view_price():
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    db = Db()
    res = db.select("SELECT * FROM `price`")
    return render_template("admin/view_price.html",data=res)
@app.route("/admin_delete_price/<pid>")
def admin_delete_price(pid):
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    db=Db()
    db.delete("DELETE FROM `price` WHERE item_id='"+pid+"'")
    return redirect("/admin_view_price#content")


@app.route("/admin_view_subsidy")
def admin_view_subsidy():
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    db = Db()
    res = db.select("SELECT * FROM `subsidy`")

    return render_template("admin/view_subsidy.html",data=res)
@app.route("/admin_delete_subsidy/<sid>")
def admin_delete_subsidy(sid):
    if session['lg']!="yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    db=Db()
    db.delete("DELETE FROM `subsidy`WHERE subsidy_id='"+sid+"'")
    return redirect("/admin_view_subsidy#content")










#################################                   OFFICER
@app.route("/officer_home")
def officer_home():
    if session['lg'] != "yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    return render_template("officer/index.html")
    # return render_template("officer/home.html")

@app.route("/officer_add_stock/<cid>",methods=['get', 'post'])
def  officer_add_stock(cid):
    if session['lg'] != "yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    if request.method=="POST":
        Quantity = request.form['textfield2']
        db=Db()
        qry=db.selectOne("select * from stocks where item_id='"+cid+"' and `type`='crop' and office_id='"+str(session['lid'])+"'")
        print(qry)
        if qry is not None:
            db.update("update stocks set quantity=quantity+'"+Quantity+"' where item_id='"+cid+"' and  office_id='"+str(session['lid'])+"'")
            return "<script>alert('stock updated');window.location='/officer_view_crop';</script>"

        else:
            db.insert("INSERT INTO `stocks` (item_id,type,quantity,office_id,date)VALUES('"+cid+"','crop','"+Quantity+"','"+str(session['lid'])+"',CURDATE())")
            return "<script>alert('stock Added');window.location='/officer_view_crop';</script>"

    else:
        return  render_template("officer/add_stock.html")

@app.route("/officer_add_fertilizer_stock/<cid>",methods=['get', 'post'])
def  officer_add_fertilizer_stock(cid):
    if session['lg'] != "yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    if request.method=="POST":
        Quantity = request.form['textfield2']
        db=Db()
        qry = db.selectOne("select * from stocks where item_id='" + cid + "' and `type`='fertilizer' and office_id='"+str(session['lid'])+"'")
        if qry is not None:
            db.update("update stocks set quantity=quantity+'" + Quantity + "' where item_id='" + cid + "'and  office_id='"+str(session['lid'])+"'")
            return "<script>alert('stock updated');window.location='/officer_view_fertilizer';</script>"

        else:
            db.insert("INSERT INTO `stocks` (item_id,type,quantity,office_id,date)VALUES('"+cid+"','fertilizer','"+Quantity+"','"+str(session['lid'])+"',CURDATE())")
            return "<script>alert('stock Added');window.location='/officer_view_fertilizer';</script>"

    else:
        return  render_template("officer/add_stock.html")

@app.route("/officer_add_machine_stock/<cid>",methods=['get', 'post'])
def  officer_add_machine_stock(cid):
    if session['lg'] != "yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    if request.method=="POST":
        Quantity = request.form['textfield2']
        db=Db()
        qry = db.selectOne("select * from stocks where item_id='" + cid + "' and `type`='machine'and  office_id='"+str(session['lid'])+"'")
        if qry is not None:
            db.update("update stocks set quantity=quantity+'" + Quantity + "' where item_id='" + cid + "'and  office_id='"+str(session['lid'])+"'")
            return "<script>alert('stock updated');window.location='/officer_view_machine';</script>"

        else:
             db.insert("INSERT INTO `stocks` (item_id,type,quantity,office_id,date)VALUES('"+cid+"','machine','"+Quantity+"','"+str(session['lid'])+"',CURDATE())")
             return "<script>alert('stock Added');window.location='/officer_view_machine';</script>"

    else:
        return  render_template("officer/add_stock.html")

@app.route("/officer_view_crop_stock/<tid>")
def officer_view_crop_stock(tid):
    if session['lg'] != "yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    db = Db()
    res = db.selectOne("SELECT * FROM `stocks` where item_id='"+tid+"'  and `type`='crop' and office_id='"+str(session['lid'])+"'")

    return render_template("officer/view_stock.html",data=res)


@app.route("/officer_view_fertilizer_stock/<tid>")
def officer_view_fertilizer_stock(tid):
    if session['lg'] != "yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    db = Db()
    res = db.selectOne("SELECT * FROM `stocks` where item_id='" + tid + "'  and `type`='fertilizer' and office_id='"+str(session['lid'])+"'")

    return render_template("officer/view_stock.html", data=res)


@app.route("/officer_view_machine_stock/<tid>")
def officer_view_machine_stock(tid):
    if session['lg'] != "yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    db = Db()
    res = db.selectOne("SELECT * FROM `stocks` where item_id='" + tid + "'  and `type`='machine' and office_id='"+str(session['lid'])+"'")

    return render_template("officer/view_stock.html", data=res)

@app.route("/officer_add_story",methods=['get', 'post'])
def officer_add_story():
    if session['lg'] != "yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    if request.method =="POST":
        typ = request.form['t']
        TITLE = request.form['textfield']
        DESCRIPTION = request.form['textarea']
        img = request.files['fileField']
        dt=time.strftime("%Y%m%d_%H%M%S")
        img.save(static_path + "files\\" + dt+ ".jpg")

        #   resizing to 500 x 600
        from PIL import Image
        im = Image.open(static_path + "files\\" + dt+ ".jpg")
        im1 = im.resize((500,600))
        im1.save(static_path + "files\\rs_" + dt+ ".jpg")
        import os
        os.remove(static_path + "files\\" + dt+ ".jpg")


        path="/static/files/rs_" + dt + ".jpg"
        db = Db()
        db.insert("INSERT INTO `story` (office_id,title,description,DATE,type, image)VALUES('"+str(session['lid'])+"','"+TITLE+"','"+DESCRIPTION+"',CURDATE(),'"+typ+"', '"+path+"')")
        return "<script>alert('story Added');window.location='/officer_add_story';</script>"
    else:
        return render_template("officer/add_story.html")

@app.route("/officer_add_tool", methods=['get', 'post'])
def officer_add_tool():
    if session['lg'] != "yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    if request.method == "POST":
        TOOL_NAME=request.form['t1']
        QUANTITY = request.form['t2']
        DESCRIPTION = request.form['t3']
        PRICE = request.form['t4']
        print(TOOL_NAME)

        db=Db()
        db.insert("INSERT INTO `tool` (office_id,tool_name,quantity,description,price)VALUES('"+str(session['lid'])+"','"+TOOL_NAME+"','"+QUANTITY+"','"+DESCRIPTION+"','"+PRICE+"')")
        return "<script>alert('tool Added');window.location='/officer_add_tool';</script>"

    else:
        return render_template("officer/add_tool.html")

@app.route("/officer_view_crop")
def officer_view_crop():
    if session['lg'] != "yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    db = Db()
    res = db.select("SELECT * FROM `crop`")
    return render_template("officer/view_crop.html",data=res)



@app.route("/officer_view_fertilizer")
def officer_view_fertilizer():
    if session['lg'] != "yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    db = Db()
    res = db.select("SELECT * FROM `fertilizer`")
    return render_template("officer/view_fertilizer.html",data=res)

@app.route("/officer_view_machine")
def officer_view_machine():
    if session['lg'] != "yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    db = Db()
    res = db.select("SELECT * FROM `machine`")
    return render_template("officer/view_machine.html",data=res)

@app.route("/officer_view_notification")
def officer_view_notification():
    if session['lg'] != "yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    db = Db()
    res = db.select("SELECT * FROM `notification`")
    return render_template("officer/view_notification.html",data=res)

@app.route("/officer_view_request",methods=['get','post'])
def officer_view_request():
    if session['lg'] != "yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    if request.method == "POST":
        type=request.form['t']
        db=Db()
        if type=='crop':


            res=db.select("SELECT request.date as d,farmer.*,stocks.*,request.*,crop.name as n FROM `request`,`stocks`,`farmer`,`crop` WHERE `request`.`stock_id`=`stocks`.`stock_id` AND `stocks`.`item_id`=`crop`.`crop_id` AND `request`.`farmer_id`=`farmer`.`farmer_id` AND `stocks`.`office_id`='"+str(session['lid'])+"' AND `stocks`.`type`='crop'")
            return render_template("officer/view_request.html",data=res)
        elif type=='machine':
            res = db.select("SELECT request.date as d,farmer.*,stocks.* ,request.*,machine.name as n FROM `request`,`stocks`,`farmer`,`machine` WHERE `request`.`stock_id`=`stocks`.`stock_id` AND `stocks`.`item_id`=`machine`.`machine_id` AND `request`.`farmer_id`=`farmer`.`farmer_id` AND `stocks`.`office_id`='" + str(session['lid']) + "' AND `stocks`.`type`='machine'")
            return render_template("officer/view_request.html", data=res)
        else:
            res = db.select("SELECT request.date as d,farmer.*,stocks.*,request.*,fertilizer.name as n FROM `request`,`stocks`,`farmer`,`fertilizer` WHERE `request`.`stock_id`=`stocks`.`stock_id` AND `stocks`.`item_id`=`fertilizer`.`fertilizer_id` AND `request`.`farmer_id`=`farmer`.`farmer_id` AND `stocks`.`office_id`='" + str(session['lid']) + "' AND `stocks`.`type`='fertilizer'")
            return render_template("officer/view_request.html", data=res)
    else:
        return render_template("officer/view_request.html")



@app.route("/officer_approve_request/<arqid>")
def officer_approve_request(arqid):
    if session['lg'] != "yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    db=Db()
    db.update("UPDATE `request` SET STATUS='approved' WHERE request_id='"+arqid+"'")
   # return "<script>alert('approved');window.location='/officer_view_request';</script>"
    return redirect("/officer_view_request")

@app.route("/officer_reject_request/<rrqid>")
def officer_reject_request(rrqid):
    if session['lg'] != "yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    db=Db()
    db.update("UPDATE `request` SET STATUS='rejected' WHERE request_id='"+rrqid+"'")
    return "<script>alert('rejected');window.location='/officer_view_request';</script>"



@app.route("/officer_view_stock")
def officer_view_stock():
    if session['lg'] != "yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    if request.method == "POST":
        db = Db()
        res = db.select("SELECT * FROM `stocks`")
        return render_template("officer/view_stock.html", data=res)
    else:
        db = Db()
        res = db.select("SELECT * FROM `stocks` ")
        return render_template("officer/view_stock.html",data=res)



@app.route("/officer_view_story",methods=['get','post'])
def officer_view_story():
    if session['lg'] != "yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    if request.method=="POST":
        s=request.form['s']
        db=Db()
        res = db.select("SELECT * FROM `story` where type='"+s+"' ")
        return render_template("officer/view_story.html", data=res)
    else:
        db = Db()
        res = db.select("SELECT * FROM `story` ")
        return render_template("officer/view_story.html",data=res)
@app.route("/officer_delete_story/<stid>")
def officer_delete_story(stid):
    if session['lg'] != "yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    db=Db()
    db.delete("DELETE FROM `story` WHERE story_id='"+stid+"'")
    return redirect("/officer_view_story#content")

@app.route("/officer_view_tools")
def officer_view_tools():
    if session['lg'] != "yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    db=Db()
    res=db.select("SELECT * FROM `tool` ")
    return render_template("officer/view_tools.html",data=res)
@app.route("/officer_delete_tool/<tid>")
def officer_delete_tool(tid):
    if session['lg'] != "yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    db=Db()
    db.delete("DELETE FROM `tool` WHERE tool_id='"+tid+"'")
    return redirect("/officer_view_tools#content")


@app.route("/officer_view_profile")
def officer_view_profile():
    if session['lg'] != "yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    db=Db()
    res = db.selectOne("SELECT * FROM agricuture_office where  office_id='"+str(session['lid'])+"'")
    return render_template("officer/view_profile.html",data=res)



@app.route("/officer_change_password",methods=['get','post'])
def officer_change_password():
    if session['lg'] != "yes":
        return "<script>alert('You are logged out');window.location='/login';</script>"
    if request.method == "POST":
        current_password = request.form['textfield']
        new = request.form['textfield2']
        confirm = request.form['textfield3']
        db=Db()
        qry=db.selectOne("select * from login where login_id='"+str(session['lid'])+"'")
        if qry['password']==current_password:
            if confirm==new:
                db.update("update login set password='"+new+"' where login_id='"+str(session['lid'])+"' ")
                return '<script>alert("successfull");window.location="/officer_home"</script>'

            else:
                 return '<script>alert("mismatch");window.location="/officer_change_password"</script>'
        else:
             return '<script>alert("incorrect current password");window.location="/officer_change_password"</script>'
    else:

         return render_template("officer/change_password.html")



@app.route("/officer_view_chat")
def officer_view_chat():
    db=Db()
    res=db.select("SELECT `farmer`.* FROM farmer, chat WHERE chat.to_id='"+str(session['lid'])+"' AND (`farmer`.farmer_id=chat.from_id  OR farmer.farmer_id=chat.to_id) GROUP BY farmer.farmer_id")
    return render_template("officer/view_chat.html", data=res)


@app.route("/officer_chat_farmer/<uid>/<oname>")
def officer_chat_farmer(uid, oname):
    session["selfid"] = uid
    session["sel_fname"] = oname
    return render_template('officer/officer_chat_farmer.html', toid=uid)



@app.route("/officer_chat_farmer_chk", methods=['post'])  # refresh messages chatlist
def officer_chat_farmer_chk():
    uid = request.form['idd']
    qry = "select date, time,message,from_id from chat where (from_id='" + str(
        session['lid']) + "' and to_id='" + uid + "') or ((from_id='" + uid + "' and to_id='" + str(
        session['lid']) + "')) order by chat_id desc"
    c = Db()
    res = c.select(qry)
    return jsonify(res)


@app.route("/officer_chat_farmer_post", methods=['POST'])
def officer_chat_farmer_post():
    id = str(session["selfid"])
    ta = request.form["ta"]
    qry = "insert into chat(message,date, time,from_id,to_id) values('" + ta + "',CURDATE(), curtime(),'" + str(
        session['lid']) + "','" + id + "')"
    d = Db()
    d.insert(qry)
    return render_template('officer/officer_chat_farmer.html', toid=id)




#################################                   farmer


@app.route("/farmer_registration",methods=['get','post'])
def farmer_registration():
    if request.method == "POST":
       name = request.form['textfield']
       HOUSE = request.form['textfield2']
       place = request.form['textfield3']
       PIN = request.form['textfield4']
       CONTACT = request.form['textfield5']
       EMAIL = request.form['textfield6']
       PASSWORD = request.form['textfield7']
       CONFIRM_PASSWORD = request.form['textfield8']
       db = Db()
       if PASSWORD==CONFIRM_PASSWORD:
           qry=db.insert("insert into `login` values('','"+EMAIL+"','"+CONFIRM_PASSWORD+"','farmer')")
           db.insert("insert into `farmer` values('"+str(qry)+"','" +name+ "','" +EMAIL+ "','" +CONTACT+ "','" +HOUSE+ "','" +place+ "','" +PIN+ "')")

           #    mail sending
           try:
               gmail = smtplib.SMTP('smtp.gmail.com', 587)
               gmail.ehlo()
               gmail.starttls()
               gmail.login('mannira.2k22@gmail.com', 'mtrwbhixdfzfeebm')

           except Exception as e:
               print("Couldn't setup email!!" + str(e))

           msg = MIMEText("Username  :  " + EMAIL + "\nPassword  :  " + str(PASSWORD))
           msg['Subject'] = 'Password for Mannira Website'
           msg['To'] = EMAIL
           msg['From'] = 'mannira.2k22@gmail.com'

           try:
               gmail.send_message(msg)
           except Exception as e:
               print("COULDN'T SEND EMAIL", str(e))
            #   mail sending end

           return '<script>alert("FARMER added");window.location="/login"</script>'
       else:
           return '<script>alert("password mismatch!!");window.location="/farmer_registration"</script>'

    else:
         return  render_template("farmer/f_registration.html")





@app.route("/f_view_profile",methods=['get','post'])
def f_view_profile():

    db = Db()
    if request.method == "POST":
        name = request.form['textfield']
        HOUSE = request.form['textfield2']
        place = request.form['textfield3']
        PIN = request.form['textfield4']
        CONTACT = request.form['textfield5']
        EMAIL = request.form['textfield6']
        db.update("update farmer set farmername='"+name+"',email='"+EMAIL+"',phone='"+CONTACT+"',house='"+HOUSE+"',place='"+place+"',pin='"+PIN+"' where farmer_id='"+str(session['lid'])+"'")
        return '<script>alert("updated");window.location="/farmer_home"</script>'

    res = db.selectOne("SELECT * FROM `farmer` where  farmer_id='"+str(session['lid'])+"'")
    return  render_template('farmer/f_view_profile.html',data=res)




@app.route("/farmer_home")
def farmer_home():
    return  render_template("farmer/index.html")
    # return  render_template("farmer/home.html")






@app.route("/f_add_bank",methods=['get','post'])
def f_add_bank():
    if request.method == "POST":
        bank_name= request.form['textfield']
        acc_no= request.form['textfield2']
        pin= request.form['textfield4']
        balance= request.form['textfield3']
        db=Db()
        db.insert("insert into bank values('','"+bank_name+"','"+acc_no+"','"+pin+"','"+balance+"','"+str(session['lid'])+"')")
        return '<script>alert("bank added");window.location="/f_add_bank"</script>'

    else:

         return  render_template('farmer/f_add_bank.html')




@app.route("/f_add_enquiry",methods=['get','post'])
def f_add_enquiry():
    if request.method == "POST":
        description= request.form['textarea']
        person_name= request.form['textfield']
        contact_no = request.form['textfield3']
        db=Db()
        db.insert("INSERT INTO `enquiry` VALUES('','"+description+"','"+person_name+"',CURDATE(),'"+contact_no+"')")
        return '<script>alert("enquiry added");window.location="/f_add_enquiry"</script>'

    else:
         return  render_template('farmer/f_add_enquiry.html')




@app.route("/f_add_payment/<rid>/<amt>/<fid>",methods=['get','post'])
def f_add_payment(rid, amt, fid):
    if request.method == "POST":
        bank_name = request.form['textfield']
        acc_no = request.form['textfield2']
        pin = request.form['textfield4']
        db=Db()
        res=db.selectOne("SELECT * FROM `bank` WHERE bank_name='"+bank_name+"' AND acc_no='"+acc_no+"' AND pin='"+pin+"' AND user_id='"+str(session['lid'])+"'")
        if res is None:
            return '<script>alert("Invalid details");window.location="/f_add_payment/'+rid + '/' + amt + '/' + fid + '"</script>'
        else:
            bal=res['balance']
            if float(amt) > float(bal):
                return '<script>alert("Insufficient Balance");window.location="/f_add_payment/' + rid + '/' + amt + '/' + fid + '"</script>'
            else:

                db.insert("INSERT INTO `payment` VALUES('',curdate(), '"+rid+"','"+amt+"','"+acc_no+"')")
                db.update("update bank set balance=balance-'"+str(amt)+"' where user_id='"+str(session['lid'])+"'")
                db.update("update bank set balance=balance+'"+str(amt)+"' where user_id='"+str(fid)+"'")
                db.update("UPDATE product_request SET STATUS='Paid' WHERE req_id='"+rid+"'")
                return '<script>alert("payment added");window.location="/f_view_my_order"</script>'
    else:
         return  render_template('farmer/f_add_payment.html', amt=amt)



@app.route("/f_add_product_request/<pid>",methods=['get','post'])
def f_add_product_request(pid):
    if request.method == "POST":
        quantity = request.form['textfield']
        db=Db()
        db.insert("INSERT INTO `product_request` VALUES('','"+str(session['lid'])+"','"+pid+"','"+quantity+"',CURDATE(),'pending')")
        return '<script>alert("product Requested");window.location="/f_view_other_product"</script>'

    else:

         return  render_template('farmer/f_add_product_request.html')





@app.route("/f_add_production",methods=['get','post'])
def f_add_production():
    if request.method == "POST":
        item_name = request.form['textfield']
        item_price = request.form['textfield3']
        description = request.form['textarea']
        quantity = request.form['textfield4']
        db=Db()
        db.insert("INSERT INTO `product` VALUES('','"+item_name+"',CURDATE(),'"+item_price+"','"+description+"','"+quantity+"','"+str(session['lid'])+"')")

        return '<script>alert("product added");window.location="/f_add_production"</script>'

    else:

         return  render_template('farmer/f_add_production.html')



@app.route("/f_add_review/<pid>",methods=['get','post'])
def f_add_review(pid):
    if request.method == "POST":
        description = request.form['textarea']
        db=Db()
        db.insert("INSERT INTO `review` VALUES('','"+str(session['lid'])+"','"+description+"',CURDATE(),'"+pid+"')")
        return '<script>alert("review added");window.location="/f_view_other_product"</script>'
    else:

         return  render_template('farmer/f_add_review.html')



@app.route("/f_add_schedule/<rid>",methods=['get','post'])
def f_add_schedule(rid):
    if request.method == "POST":
        date = request.form['textfield2']
        time = request.form['textfield3']
        place = request.form['textarea']
        db=Db()
        db.insert("INSERT INTO `schedule` VALUES('','"+date+"','"+time+"','"+rid+"','"+place+"')")
        return '<script>alert("schedule added");window.location="/farmer_home"</script>'
    else:
        return  render_template('farmer/f_add_schedule.html')





@app.route("/f_edit_production/<pid>", methods=['get', 'post'])
def f_edit_production(pid):
    if request.method == "POST":
        item_name = request.form['textfield']
        price = request.form['textfield3']
        description = request.form['textarea']
        quantity = request.form['textfield4']
        db=Db()
        db.update("UPDATE `product` SET item_name='"+item_name+"',date=CURDATE(),item_price='"+price+"',item_description='"+description+"',quantity='"+quantity+"' WHERE product_id='"+pid+"'")

        return redirect("/f_view_my_product")
    else:
        db=Db()
        res = db.selectOne("SELECT * FROM product WHERE product_id='"+pid+"'")
        return  render_template("farmer/f_edit_production.html",data=res)

@app.route("/farmer_delete_product/<pid>")
def admin_delete_product(pid):
    db = Db()
    db.delete("DELETE FROM product WHERE product_id='"+pid+"'")
    return redirect("/f_view_my_product#content")


@app.route("/f_send_complaint",methods=['get','post'])
def f_send_complaint():
    if request.method == "POST":

        complaint_description = request.form['textarea']
        db=Db()
        db.insert("INSERT INTO complaint_reply VALUES('','"+str(session['lid'])+"','"+complaint_description+"','pending',CURDATE())")

        return '<script>alert("Complaint Sent");window.location="/f_send_complaint"</script>'
    else:
        return  render_template('farmer/f_send_complaint.html')




@app.route("/f_send_feedback",methods=['get','post'])
def f_send_feedback():
    if request.method == "POST":
        DESCRIPTION= request.form['textarea']
        db=Db()
        db.insert("INSERT INTO `feedback` VALUES('',CURDATE(),'"+DESCRIPTION+"','"+str(session['lid'])+"')")
        return '<script>alert("feedback Sent");window.location="/farmer_home"</script>'
    else:
        return render_template('farmer/f_send_feedback.html')


@app.route("/f_view_applicaton")
def f_view_application():
    db = Db()
    res = db.select("SELECT * FROM `application` ")
    return  render_template('farmer/f_view_application.html',data=res)




@app.route("/f_view_crop")
def f_view_crop():
    db = Db()
    res = db.select("SELECT * FROM `crop` ")
    return  render_template('farmer/f_view_crop.html',data=res)




@app.route("/f_send_request/<stock_id>",methods=['get','post'])
def f_send_request(stock_id):
    if request.method=="POST":
        stock_id=request.form['hid']
        qty=request.form['textfield']
        db=Db()
        db.insert("INSERT INTO `request` VALUES(NULL,CURDATE(),'"+stock_id+"','"+str(session['lid'])+"','"+qty+"','pending')")
        return '<script>alert("stock requested");window.location="/farmer_home"</script>'
    else:
        return  render_template('farmer/f_send_request.html',stock_id=stock_id)






@app.route("/f_view_faq")
def f_view_faq():
    db = Db()
    res = db.select("SELECT * FROM `faq` ")
    return  render_template('farmer/f_view_faq.html',data=res)





@app.route("/f_view_fertilizer")
def f_view_fertilizer():
    db = Db()
    res = db.select("SELECT * FROM `fertilizer` ")
    return  render_template('farmer/f_view_fertilizer.html',data=res)





@app.route("/f_view_machine")
def f_view_machine():
    db = Db()
    res = db.select("SELECT * FROM `machine` ")
    return  render_template('farmer/f_view_machine.html',data=res)





@app.route("/f_view_my_order")
def f_view_my_order():
    db = Db()
    # res = db.select("SELECT * FROM product_request,product where product_request.product_id=product.product_id and product_request.farmer_id='"+str(session['lid'])+"'")
    res = db.select("SELECT farmer.farmer_id as fid, `farmer`.farmername, farmer.phone, `product`.item_name, product.item_price, product.item_description, `product_request`.date, `product_request`.quantity, `product_request`.status, product.item_price*`product_request`.quantity AS amount, product_request.req_id FROM `product_request`, `farmer`, `product` WHERE `product`.product_id=`product_request`.product_id AND `product`.farmer_id=`farmer`.farmer_id AND `product_request`.farmer_id='"+str(session['lid'])+"'")
    return  render_template('farmer/f_view_my_order.html',data=res)





@app.route("/f_view_my_product")
def f_view_my_product():
    db = Db()
    res = db.select("SELECT * FROM `product` WHERE `farmer_id`='"+str(session['lid'])+"'")
    return  render_template('farmer/f_view_my_product.html',data=res)





@app.route("/f_view_notification")
def f_view_notification():
    db = Db()
    res = db.select("SELECT * FROM `notification` ")
    return  render_template('farmer/f_view_notification.html',data=res)


@app.route("/f_view_other_product")
def f_view_other_product():
    db = Db()
    res = db.select("SELECT * FROM `product`,farmer WHERE product.farmer_id=farmer.farmer_id and product.`farmer_id`!='"+str(session['lid'])+"' ")
    return  render_template('farmer/f_view_other_product.html',data=res)



@app.route("/f_view_policy")
def f_view_policy():
    db=Db()
    res = db.select("SELECT * FROM `policy` ")
    return  render_template('farmer/f_view_policy.html',data=res)



@app.route("/f_view_price")
def f_view_price():
    db = Db()
    res = db.select("SELECT * FROM `price` ")
    return  render_template('farmer/f_view_price.html',data=res)



@app.route("/f_view_reply")
def f_view_reply():
    db = Db()
    res = db.select("SELECT * FROM `complaint_reply` ")
    return  render_template('farmer/f_view_reply.html',data=res)




@app.route("/f_view_review/<pid>")
def f_view_review(pid):
    db = Db()
    res = db.select("SELECT * FROM `review`,`farmer` WHERE review.farmer_id=farmer.farmer_id and review.product_id='"+pid+"' ")
    return  render_template('farmer/f_view_review.html',data=res)





@app.route("/f_view_selling_product_request")
def f_view_selling_product_request():
    db = Db()
    res = db.select("SELECT product_request.quantity as pd,product_request.*,product.*,farmer.* FROM `product_request`,product,farmer where product_request.product_id=product.product_id and product_request.farmer_id=farmer.farmer_id and product.farmer_id='"+str(session['lid'])+"' ")
    return  render_template('farmer/f_view_selling_product_request.html',data=res)


@app.route("/farmer_approve_request/<arqid>/<pid>/<q>")
def farmer_approve_request(arqid,pid,q):
   db=Db()
   db.update("UPDATE `product_request` SET status='approved' WHERE req_id='"+arqid+"'")
   db.update("update product set quantity=quantity-'"+q+"' where product_id='"+pid+"'")
   return "<script>alert('approved');window.location='/f_view_selling_product_request';</script>"

@app.route("/farmer_reject_request/<rrqid>")
def farmer_reject_request(rrqid):
   db=Db()
   db.update("UPDATE `product_request` SET status='rejected' WHERE req_id='"+rrqid+"'")
   return "<script>alert('rejected');window.location='/f_view_selling_product_request';</script>"


@app.route("/f_view_stock/<mid>/<m>")
def f_view_stock(mid,m):
    db = Db()
    res = db.select("SELECT * FROM `stocks`,`agricuture_office` where stocks.office_id=agricuture_office.office_id and  item_id='"+mid+"' and `type`='"+m+"' ")
    return  render_template('farmer/f_view_stock.html',data=res)



@app.route("/f_view_story")
def f_view_story():
    db=Db()
    res = db.select("SELECT * FROM `story` ")
    return  render_template('farmer/f_view_story.html',data=res)



@app.route("/f_view_subsidy")
def f_view_subsidy():
    db = Db()
    res = db.select("SELECT * FROM `subsidy` ")
    return  render_template('farmer/f_view_subsidy.html',data=res)



@app.route("/f_view_schedule")
def f_view_schedule():
    db = Db()
    res = db.select("SELECT * FROM `schedule`,`product_request`   WHERE `schedule`.req_id=`product_request`.req_id AND product_request.farmer_id='"+str(session['lid'])+"' ORDER BY schedule_id DESC")
    # res = db.select("SELECT * FROM `schedule`,`request`   WHERE `schedule`.req_id=`request`.request_id AND request.farmer_id='"+str(session['lid'])+"' ORDER BY schedule_id DESC")
    return  render_template('farmer/f_view_schedule.html',data=res)



@app.route("/f_view_tools")
def f_view_tools():
    db=Db()
    res=db.select("SELECT * FROM `tool` ")
    return render_template("farmer/f_view_tools.html",data=res)



@app.route("/f_view_request",methods=['get','post'])
def f_view_request():
    if request.method == "POST":
        type=request.form['t']
        db=Db()
        if type=='crop':


            res=db.select("SELECT request.date as d,request.*,crop.name as n,agricuture_office.*,stocks.* FROM `request`,`stocks`,`agricuture_office`,`crop` WHERE `request`.`stock_id`=`stocks`.`stock_id` AND `stocks`.`item_id`=`crop`.`crop_id` AND `stocks`.`office_id`=`agricuture_office`.`office_id` AND `request`.`farmer_id`='"+str(session['lid'])+"' AND  `stocks`.`type`='crop'")
            return render_template("farmer/f_view_request.html",data=res)
        elif type=='machine':
            res = db.select("SELECT request.date as d,request.*,machine.name as n,agricuture_office.*,stocks.* FROM `request`,`stocks`,`agricuture_office`,`machine` WHERE `request`.`stock_id`=`stocks`.`stock_id` AND `stocks`.`item_id`=`machine`.`machine_id` AND `stocks`.`office_id`=`agricuture_office`.`office_id` AND `request`.`farmer_id`='" + str(session['lid']) + "' AND `stocks`.`type`='machine'")
            return render_template("farmer/f_view_request.html", data=res)
        else:
            res = db.select("SELECT request.date as d,request.*,fertilizer.name as n,agricuture_office.*,stocks.* FROM `request`,`stocks`,`agricuture_office`,`fertilizer` WHERE `request`.`stock_id`=`stocks`.`stock_id` AND `stocks`.`item_id`=`fertilizer`.`fertilizer_id` AND `stocks`.`office_id`=`agricuture_office`.`office_id` AND `request`.`farmer_id`='" + str(session['lid']) + "' AND `stocks`.`type`='fertilizer'")
            return render_template("farmer/f_view_request.html", data=res)
    else:
        return render_template("farmer/f_view_request.html")




#####   farmer chat with officer
@app.route("/farmer_view_officers")
def farmer_view_officers():
    db=Db()
    res=db.select("SELECT * FROM `agricuture_office`")
    return render_template("farmer/view_officers.html", data=res)


@app.route("/farmer_chat_officer/<uid>/<oname>")
def farmer_chat_officer(uid, oname):
    session["seluid"] = uid
    session["sel_oname"] = oname
    return render_template('farmer/farmer_chat_officer.html', toid=uid)



@app.route("/farmer_chat_officer_chk", methods=['post'])  # refresh messages chatlist
def farmer_chat_officer_chk():
    uid = request.form['idd']
    qry = "select date, time,message,from_id from chat where (from_id='" + str(
        session['lid']) + "' and to_id='" + uid + "') or ((from_id='" + uid + "' and to_id='" + str(
        session['lid']) + "')) order by chat_id desc"
    c = Db()
    res = c.select(qry)
    return jsonify(res)


@app.route("/farmer_chat_officer_post", methods=['POST'])
def farmer_chat_officer_post():
    id = str(session["seluid"])
    ta = request.form["ta"]
    qry = "insert into chat(message,date, time,from_id,to_id) values('" + ta + "',CURDATE(), curtime(),'" + str(
        session['lid']) + "','" + id + "')"
    d = Db()
    d.insert(qry)
    return render_template('farmer/farmer_chat_officer.html', toid=id)





if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host="0.0.0.0")
