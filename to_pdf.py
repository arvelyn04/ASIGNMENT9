from fpdf import FPDF

pdf = FPDF ('P','mm','Letter')

pdf.add_page()

import json

myjsonfile=open('resume.json','r')
jsondata=myjsonfile.read()

obj=json.loads(jsondata)

pdf.set_font('arial','BIU',23)
pdf.set_text_color (r=0, g=0, b=0)

pdf.cell(180,18,str(obj['NAME']),ln=True)

pdf.set_font('arial','BI',10)
pdf.set_text_color (r=0, g=0, b=0)

pdf.cell(10,6,str(obj['LABEL']),ln=True)

pdf.set_font('arial','',10)
pdf.set_text_color (r=0, g=0, b=0)

pdf.cell(130,10,"Email:"+str(obj['EMAIL']),ln=True)
pdf.cell(130,10,"Contact Number:"+str(obj['CONTACT NUMBER']),ln=True)
pdf.cell(130,10,"URL:"+str(obj['URL']),ln=True)


pdf.set_font('arial','BIU',13)
pdf.set_text_color (r=0, g=0, b=0)

pdf.cell(180,12,'PERSONAL INFORMATION',ln=True)

pdf.set_font('arial','',10)
pdf.set_text_color (r=0, g=0, b=0)

pdf.cell(130,10,"Age:"+str(obj['AGE']),ln=True)
pdf.cell(130,10,"Gender:"+str(obj['GENDER']),ln=True)
pdf.cell(130,10,"Civil Status:"+str(obj['CIVIL STATUS']),ln=True)
pdf.cell(130,10,"Address:"+str(obj['ADDRESS']),ln=True)
pdf.cell(130,10,"Postal Code:"+str(obj['POSTAL CODE']),ln=True)
pdf.cell(130,10,"Nationality:"+str(obj['NATIONALITY']),ln=True)
pdf.cell(130,10,"Height:"+str(obj['HEIGHT']),ln=True)
pdf.cell(130,10,"Weight:"+str(obj['WEIGHT']),ln=True)

pdf.set_font('arial','BIU',13)
pdf.set_text_color (r=0, g=0, b=0)

pdf.cell(180,12,'BACKGROUND',ln=True)

pdf.set_font('arial','',10)
pdf.set_text_color (r=0, g=0, b=0)

pdf.cell(130,10,"Name of the Company:"+str(obj['AGE']),ln=True)
pdf.cell(130,10,"Position:"+str(obj['GENDER']),ln=True)
pdf.cell(130,10,"Company's URL:"+str(obj['CIVIL STATUS']),ln=True)
pdf.cell(130,10,"Start Date:"+str(obj['ADDRESS']),ln=True)
pdf.cell(130,10,"End Date:"+str(obj['POSTAL CODE']),ln=True)

pdf.set_font('arial','BIU',13)
pdf.set_text_color (r=0, g=0, b=0)

pdf.cell(180,12,'PROFILES',ln=True)

pdf.set_font('arial','',10)
pdf.set_text_color (r=0, g=0, b=0)

pdf.cell(130,10,str(obj['PROFILE1']),ln=True)
pdf.cell(130,10,str(obj['PROFILE2']),ln=True)
pdf.cell(130,10,str(obj['PROFILE3']),ln=True)
pdf.cell(130,10,str(obj['PROFILE4']),ln=True)
pdf.cell(130,10,str(obj['PROFILE5']),ln=True)

pdf.set_font('arial','BIU',13)
pdf.set_text_color (r=0, g=0, b=0)

pdf.cell(150,12,'EDUCATIONAL ATTAINMENT',ln=True)

pdf.set_font('arial','',10)
pdf.set_text_color (r=0, g=0, b=0)

pdf.cell(130,10,"Elementary:"+str(obj['ELEMENTARY']),ln=True)
pdf.cell(130,10,"Secondary:"+str(obj['SECONDARY']),ln=True)
pdf.cell(130,10,"Senior-High:"+str(obj['SENIOR-HIGH']),ln=True)
pdf.cell(130,10,"Tertiary:"+str(obj['TERTIARY']),ln=True)

pdf.set_font('arial','BIU',13)
pdf.set_text_color (r=0, g=0, b=0)

pdf.cell(150,12,'SKILLS:',ln=True)

pdf.set_font('arial','',10)
pdf.set_text_color (r=0, g=0, b=0)

pdf.cell(130,10,"Skills:"+str(obj['SKILLS']),ln=True)
pdf.cell(130,10,"Level:"+str(obj['LEVEL']),ln=True)
pdf.cell(130,10,"Keywords:"+str(obj['KEYWORDS']),ln=True)

pdf.set_font('arial','BIU',13)
pdf.set_text_color (r=0, g=0, b=0)

pdf.cell(150,12,'LANGUAGES:',ln=True)

pdf.set_font('arial','',10)
pdf.set_text_color (r=0, g=0, b=0)

pdf.cell(130,10,"Languages:"+str(obj['LANGUAGES']),ln=True)

pdf.output('RAMOS_ARVELYN.pdf')