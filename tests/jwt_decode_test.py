from jose import jws

key = {
"keys": [
{
"e": "AQAB",
"kid": "6a1d26d992be7a4b689bdce1911f4e9adc75d9f1",
"kty": "RSA",
"n": "y4D9be-o8MKZZYpr9GgmqNFw_pH0a7jPDWG1zYMwFUVSDCY30WsBADGRkDWKKWTgVQ9vzZdjPh1WsffBMD71ghn06Uhx8lCbxemM64N9VGBmlLN26aeu-zJAVblbEjnTh35r-LXD6TKdQcvm3CDvR3oTZ4j1x5G-Yil5JKevvbJ8Wu98VIqgTjx-RQf-EqTau9btxzCEzxw5LxD_De9tK3j82vo7FXWHZ5XmoY6TvQfJHZD0oT6tQgqtgCN1a_C9xV3oOnSStBW9V35buQX3cMYf1la7M3pzsk7HrlQP6YTnQEts8U8LewzcBUwAgkTcVigUx6oWNLfaBJZ4bwgBBQ",
"alg": "RS256",
"use": "sig"
},
{
"e": "AQAB",
"use": "sig",
"kty": "RSA",
"alg": "RS256",
"n": "0YudnviuwNdcCoXEMwMlJWhxWYpmAeRXQ8Df5bCVf5xFVEmL5am_2TTWRwRf34vqJuoGpyf3S7zJeJv8I2Lyvmpw33LReREkObCt1up17JGw5_d9K2Mf59EnnPkd7YUGklUxje8rxILiThiPdEaF8P5pRee-WD2mmQSug0rqNlMpadYVaMv3Y_HLr97Heh1ACRofYfv2hmGSmC6oo0SN4d5gP-_ggAzg9Ko7LDVcBg6TWAfJLh33GpMtAI2MPjd6XFJju-R9d68IDCIUo-CE8K0pAZnXGS8aWln_dpjZhlMjXrgY423Qa4YNsloPcwkQ20rk8XGYFr0H_9GuWIaWWQ",
"kid": "19fe2a7b6795239606ca0a750794a7bd9fd95961"
}
]
}

print(jws.verify(token="eyJhbGciOiJSUzI1NiIsImtpZCI6IjE5ZmUyYTdiNjc5NTIzOTYwNmNhMGE3NTA3OTRhN2JkOWZkOTU5NjEiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiI3MjI2MDYzODAxMzctb2c4b2szdHVvdGJyY2xrbzlmdWZpaDllY2RyYjAxYTkuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiI3MjI2MDYzODAxMzctb2c4b2szdHVvdGJyY2xrbzlmdWZpaDllY2RyYjAxYTkuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMTczNTg4MzM1NTcyODU0NDI3MDkiLCJlbWFpbCI6InR1c2hhcnZpY2tleTE5OTlAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImF0X2hhc2giOiI1aG1ZX0lFZzdtdzVRQ0ZoMEdxNm9nIiwibm9uY2UiOiIxNWIwMDI0Ni1jYzBlLTQ2MjQtYWVkMi1kZWUyNjY0ZjVmZjciLCJpYXQiOjE2MjQwMjMzMzQsImV4cCI6MTYyNDAyNjkzNH0.cFSovsTwFQ9QEDbx6waWs8CDJoWFWrVXBrkhO7rNrxlskAxda3eApZuMX8LPYHHBnJsApRqXIE4SejaHrwbRkeBpen5sIFgUfD9G2tiNVGHdpLgu2wKZIelH7rtz6qXwqe0esgAD55UliriRStFFs53lohY-rSBg_g-Z7RFllZ9oF66qzM1xo5AgkD9fFg9NwO6Nf0UDQVCyoarGgxhKWdzfwTpKldIhA8L8EF2tjEoIpQRQgR01Yw_0Eoz0vW0HpWvTW8bz5l_LPm44MLi8uACiosDJIxJ9NjwO8IL9wrmXolNcI8Q2ED-xSwXxZdYsrnDToafKVkLfwiesRG8nyg",
    algorithms="RS256", key=key))