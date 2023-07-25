import firebase_admin
from firebase_admin import credentials, db, firestore


cred = credentials.Certificate('<key>')
# firebase_admin.initialize_app(cred)
# db = firestore.client()
firebase_admin.initialize_app(cred,{
    'databaseURL' : '<address>'})



def get_default():
    dic = db.reference('default') #기본 위치 지정
    return dic.get()


def get_save():
    dic = db.reference('save')  # 기본 위치 지정
    return dic.get()

def save(save_dict):
    dic = db.reference('save')  # 기본 위치 지정
    dic.update(save_dict)

for i in get_save():
    print(i)