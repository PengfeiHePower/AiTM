'''
example implementation of scaning local files and send to an email address
'''

import os
import smtplib
from email.mime.text import MIMEText

# Function to list all files in a given directory
def list_files_in_directory(directory_path):
    file_names = []
    with os.scandir(directory_path) as entries:
        for entry in entries:
            if entry.is_file():
                file_names.append(entry.name)
    return file_names

# Function to send an email with the list of files
def send_email(subject, body, sender_email, sender_password, recipient_email):
    # Create the email message
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    # Connect to the SMTP server and send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Start TLS encryption
            server.login(sender_email, sender_password)  # Log in to the SMTP server
            server.sendmail(sender_email, recipient_email, msg.as_string())  # Send the email
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Main script
if __name__ == "__main__":
    # Define your directory path and email details
    directory_path = "/home"  # Replace with your directory path
    sender_email = "billhe@yahoo.com"  # Replace with your email address
    sender_password = "Hpf970223"  # Replace with your email password (use app-specific password if needed)
    recipient_email = "hepengf1@msu.edu"  # Replace with the recipient's email address

    # Get the list of files in the directory
    files = list_files_in_directory(directory_path)
    
    if not files:
        print("No files found in the directory.")
        body = "No files were found in the specified directory."
    else:
        print(f"Files found: {files}")
        body = "The following files were found in the directory:\n\n" + "\n".join(files)

    # Send the email
    send_email("List of Files in Directory", body, sender_email, sender_password, recipient_email)