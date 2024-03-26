import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('D:\kuliah\FC\others\serviceAccountKey.json')
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://fv-project-81f32-default-rtdb.firebaseio.com/"
})

ref = db.reference('Mahasiswa')

data = { #basic parameter of students
    "162112233007":#key 
        { 
        'Nama': "ZIKRA", #key #value
        'Jurusan':"Teknik Robotika dan Kecerdasan Buatan", #value
        'Angkatan':2021,
        'total_attendance': 7,
        'year':3,
        'semester':6,
        'last_Attendance_Time': "2024-03-26 10:30:00"
    },
    "162112233032":#key 
        { 
        'Nama': "Bhisma Pradipta Putra", #key #value
        'Jurusan':"Teknik Robotika dan Kecerdasan Buatan", #value
        'Angkatan':2021,
        'total_attendance': 5,
        'year':3,
        'semester':6,
        'last_Attendance_Time': "2024-03-26 10:30:00"},
    "162112233035":#key 
        { 
        'Nama': "Klara Setyajati", #key #value
        'Jurusan':"Teknik Robotika dan Kecerdasan Buatan", #value
        'Angkatan':2021,
        'total_attendance': 6,
        'year':3,
        'semester':6,
        'last_Attendance_Time': "2024-03-26 10:30:00"
    },
    "162112233062":#key 
        { 
        'Nama': "Muhammad Ihsan Dewanto", #key #value
        'Jurusan':"Teknik Robotika dan Kecerdasan Buatan", #value
        'Angkatan':2021,
        'total_attendance': 7,
        'year':3,
        'semester':6,
        'last_Attendance_Time': "2024-03-26 10:30:00"
    },
    "162112233083":#key 
        { 
        'Nama': "Candra Naradhipa Cahyakusuma", #key #value
        'Jurusan':"Teknik Robotika dan Kecerdasan Buatan", #value
        'Angkatan':2021,
        'total_attendance': 5,
        'year':3,
        'semester':6,
        'last_Attendance_Time': "2024-03-26 10:30:00"
    },                
}
#send data
for key, value in data.items():
    ref.child(key).set(value)
print("Load Finished")