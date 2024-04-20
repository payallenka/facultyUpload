import pymysql.cursors

# MySQL configuration
connection = pymysql.connect(host='rds-1.cvoue2sayoi0.us-east-1.rds.amazonaws.com',
                             user='masterUsername',
                             password='password',
                             db='VendOPrint',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# try:
#     with connection.cursor() as cursor:
#         # Fetch all subjects
#         cursor.execute("SELECT * FROM subject")
#         subjects = cursor.fetchall()

#         # Fetch all modules
#         cursor.execute("SELECT * FROM module")
#         modules = cursor.fetchall()

#         # Fetch all documents
#         cursor.execute("SELECT * FROM document")
#         documents = cursor.fetchall()

#         # Use fetched data for insertions or any other processing
#         for subject in subjects:
#             print(subject['subjectName'])  # Example: Print each subject

#         for module in modules:
#             print(module['moduleName'])  # Example: Print each module

#         for document in documents:
#             print(document['documentName'])  # Example: Print each document

# except pymysql.Error as e:
#     print(f"Error: {e}")
# finally:
#     connection.close()

def findSubject(subjectNameToBeFound):

    with connection.cursor() as cursor:
        # Fetch subjects
        cursor.execute("SELECT * FROM subject")
        subjects = cursor.fetchall()

    # Use fetched data for insertions or any other processing
        for subject in subjects:
            if(subjectNameToBeFound == subject['subjectName']):
                return True

        return False

def findModule(moduleNameToBeFound):

    with connection.cursor() as cursor:
        # Fetch subjects
        cursor.execute("SELECT * FROM module")
        subjects = cursor.fetchall()

    # Use fetched data for insertions or any other processing
        for subject in subjects:
            if(moduleNameToBeFound == subject['moduleName']):
                return True

        return False

def findDocument(documentNameToBeFound):

    with connection.cursor() as cursor:
        # Fetch subjects
        cursor.execute("SELECT * FROM document")
        subjects = cursor.fetchall()

    # Use fetched data for insertions or any other processing
        for subject in subjects:
            if(documentNameToBeFound == subject['documentName']):
                return True

        return False
   

print(findSubject('Operating System'))
print(findModule('IntroductionToOS'))
print(findDocument('PayalLenka_Operating System_IntroductionToOS_OS_LAB_manual_2023.pdf'))


