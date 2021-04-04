import random
import smtplib
from validate_email import validate_email

otp_num = random.randint(1000,10000)   #genrate a 4-digit otp number
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()  # for security...
server.login('mithaimadhuri3421@gmail.com',password='kkumptfmirwsbwlw')  #login with 2 step verification
msg = 'Hello user,Your OTP is '+str(otp_num)
server.sendmail('mithaimadhuri3421@gmail.com','technoguru21.10@gmail.com',msg)
server.quit()

#verified OTP
user_otp = int(input('Enter your recived OTP :'))

if(user_otp == otp_num):
    print('Your OTP Access Successfully! :)')
    print(validate_email('technoguru21.10@gmail.com'))   #  validate_email returning   "True"
else:
    print('Your given OTP is wrong, please try again. :(')