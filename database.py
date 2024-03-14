import psycopg2
# psycopg2 is a popular Python adapter for PostgreSQL that allows you to interact with PostgreSQL databases using Python code

try:
    conn = psycopg2.connect("dbname= meat user=postgres password=39457485")
    cur =conn.cursor()
except Exception as e:
    print(e)

def fetch_data(tbname):
    try:
        q = "SELECT * FROM " + tbname + ";"
        cur.execute(q)
        records = cur.fetchall()
        return records 
    except Exception as e:
        return e   
    
def add_user(v):
    vs = str(v)
    q = "insert into users(fullname,email,phone,address,h_password, created_at) "\
        "values" + vs
    cur.execute(q)
    conn.commit()
    return q