import firebase_admin
from firebase_admin import credentials, db, firestore
import initial

cred = credentials.Certificate(initial.firebase_json)
firebase_admin.initialize_app(cred,{
    'databaseURL' : initial.firebase_url})

def get_default(): #기본 데이터 불러오기
    dic = db.reference('default')
    return dic.get()

def get_save(): #동화 불러오기
    dic = db.reference('save')
    return dic.get()

def save(save_dict): #동화 저장하기
    dic = db.reference('save')
    dic.update(save_dict)

fairy_dict = get_default()