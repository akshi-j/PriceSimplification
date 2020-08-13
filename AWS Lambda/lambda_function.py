import boto3
import pyrebase
import datetime

config = {
    "apiKey": "AIzaSyA0t_1M9E5IcBO3-9xxHw7VCZqX6uHm_k8",
    "authDomain": "price-by-sku.firebaseapp.com",
    "databaseURL": "https://price-by-sku.firebaseio.com",
    "projectId": "price-by-sku",
    "storageBucket": "price-by-sku.appspot.com",
    "messagingSenderId": "1005343750508",
    "appId": "1:1005343750508:web:be57ca523b0da0db26db49",
    "measurementId": "G-493J25Q82W"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

def lambda_handler(event, context):
    """Read file from s3 on trigger."""
    s3 = boto3.client("s3")
    if event:
        file_obj = event["Records"][0]
        bucketname = str(file_obj['s3']['bucket']['name'])
        filename = str(file_obj['s3']['object']['key'])
        fileObj = s3.get_object(Bucket=bucketname, Key=filename)
        file_content = fileObj["Body"].read().decode('utf-8').split('\n')
        for i in range(1, len(file_content)):
            line = file_content[i].split(',')
            db.child("Products").child(line[0]).update({"Price": line[1]})
            your_dt = datetime.datetime.fromtimestamp(int(line[3]))
            db.child("Products").child(line[0]).update({"LastUpdated": your_dt.strftime("%d-%m-%Y")})

    return 'Thanks'