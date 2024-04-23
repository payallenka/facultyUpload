import os

import boto3
import find
import pymysql.cursors
from botocore.exceptions import ClientError
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request

load_dotenv()

app = Flask(__name__)

# MySQL configuration
connection = pymysql.connect(
    host=os.environ.get("DB_HOST"),
    user=os.environ.get("DB_USERNAME"),
    password=os.environ.get("DB_PASSWORD"),
    db=os.environ.get("DB_NAME"),
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
)

# AWS S3 configuration
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
BUCKET_NAME = os.environ.get("AWS_S3_BUCKET_NAME")

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get form data
        selected_option_subject = request.form.get("subject")
        selected_option_module = request.form.get("module")
        document_file = request.files["file"]
        first_name = request.form.get("firstName")

        # Validate form data
        if not (
            selected_option_subject
            and selected_option_module
            and document_file
            and first_name
        ):
            return jsonify({"error": "Please fill in all the fields"})

        try:
            # Upload file to S3
            new_file_name = f"{first_name}_{selected_option_subject}_{selected_option_module}_{document_file.filename}"
            s3.upload_fileobj(
                document_file,
                BUCKET_NAME,
                new_file_name,
                ExtraArgs={"ACL": "public-read"},
            )

            # Insert data into MySQL tables
            with connection.cursor() as cursor:

                if find.findSubject(selected_option_subject):
                    pass
                else:
                    # Insert subject
                    cursor.execute(
                        "INSERT INTO subject (subjectName) VALUES (%s)",
                        (selected_option_subject,),
                    )
                    connection.commit()

                if find.findModule(selected_option_module):
                    pass
                else:
                    # Insert module
                    cursor.execute(
                        "INSERT   INTO module (moduleName, subjectId) VALUES (%s, (SELECT subjectId FROM subject WHERE subjectName = %s))",
                        (selected_option_module, selected_option_subject),
                    )
                    connection.commit()

                if find.findDocument(new_file_name):
                    pass
                else:
                    # Insert document
                    cursor.execute(
                        "INSERT INTO document (documentName, moduleId) VALUES (%s, (SELECT moduleId FROM module WHERE moduleName = %s LIMIT 1))",
                        (new_file_name, selected_option_module),
                    )
                    connection.commit()

            return render_template("confirmation.html")
        except ClientError as e:
            return jsonify({"error": e.response["Error"]["Message"]}), 500

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
