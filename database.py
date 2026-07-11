import pymysql


def get_connection():

    conn = pymysql.connect(

        host="mysql-4e772e-tranlehaitrieu3010-5a61.l.aivencloud.com",

        port=13093,

        user="avnadmin",

        password="AVNS_nRB2CykZyJ-LHrfEQcz",

        database="company",

        ssl={
            "ca": "ca.pem"
        }

    )

    return conn
