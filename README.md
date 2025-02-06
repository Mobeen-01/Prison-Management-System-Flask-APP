
# Prison Management System

[![Rasa](https://img.shields.io/badge/Rasa-3.x-purple.svg?style=flat&logo=rasa)](https://rasa.com)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?style=flat&logo=python)](https://www.python.org)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

## Introduction

The **Prison Management System** is a web-based application designed to automate the routine functions of prison management. This system helps manage prisoner records, track their locations, movements, and sentencing details while ensuring efficient and streamlined operations for prison staff. The system is built to replace the outdated manual methods currently in use, addressing issues such as record mismanagement, redundancy, and inefficient access to data.

By automating prisoner data entry, updating records, and retrieving information, this system ensures that both government authorities and prison staff can efficiently manage prisoner details, court reports, and other critical data with ease. The primary goal of the system is to enhance operational efficiency, accuracy, and reduce the reliance on manual processes.

## Features

- **User Authentication**: Secure login system for different roles (admin, prison officer) with user authentication.
- **Prisoner Record Management**: Add, update, delete, and view prisoner details including ID, name, charge, sentence, and location.
- **Prisoner Movement Tracking**: Track the movement of prisoners within the prison system.
- **Location Management**: Manage and update prisoner location details.
- **Report Generation**: Generate court reports and other essential documents quickly.
- **Efficient Data Access**: Access and manage prisoner information with speed, ensuring accurate and easy retrieval.
- **Secure Database**: Use of a secure MySQL database to store records, ensuring no redundancy or missing data.

## Benefits

- **Improved Efficiency**: Automates the manual processes, improving speed and accuracy in managing prisoner data.
- **Data Integrity**: Ensures that data is consistent, accurate, and easily retrievable without redundancy.
- **Secure Access**: Provides authenticated access to authorized personnel, ensuring that confidential data is protected.
- **Ease of Use**: Intuitive user interface makes it easy for prison staff to add, update, and manage records.
- **Centralized System**: Access prisoner records globally, with a web-based solution that can be accessed from any location with an internet connection.
- **Cost Reduction**: Reduces the need for paper-based records, minimizing maintenance costs and the risk of data loss.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Backend**: Python (Flask)
- **Database**: MySQL
- **Web Server**: Flask Container
- **Security**: User Authentication (Login system)

## How to Use

### Prerequisites

Before using the Prison Management System, ensure that you have the following installed:

1. **Python 3.x** and **Flask** for the backend:
   - Install Flask:
     ```bash
     pip install flask
     ```

2. **MySQL** for the database:
   - Ensure MySQL server is running and accessible.
   - Create a database for the prison management system.

3. **Frontend**:
   - Static files (HTML, CSS, JavaScript) included in the project directory.

### Setting Up the Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/prison-management-system.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd prison-management-system
   ```

3. **Set Up the Database**:
   - Create a MySQL database and configure the connection string in the project’s backend.

4. **Run the Flask Server**:
   - Navigate to the project directory and run the Flask app:
     ```bash
     python app.py
     ```

5. **Access the Application**:
   - Open a web browser and visit `http://localhost:5000` to access the system.

### How to Perform Operations

#### 1. **Login**
   - Upon launching the system, the login page will appear.
   - Enter your username and password. Upon successful login, you will be redirected to the dashboard.

#### 2. **Add Prisoner Information**
   - From the dashboard, you can add a new prisoner by providing details like Prisoner ID, Name, Charges, Sentence Duration, etc.
   - Click the **Add Prisoner** button to submit.

#### 3. **View Prisoner Data**
   - You can view the list of all prisoners stored in the system by clicking the **View Prisoners** button.

#### 4. **Search Prisoner**
   - Use the search feature to look up prisoner details by ID, name, or other attributes.

#### 5. **Track Prisoner Movement**
   - Track the movement of prisoners within the system by entering details such as date, time, and prisoner location.

#### 6. **Update or Delete Information**
   - Update or delete prisoner information from the system as necessary. Use the **Edit** or **Delete** options next to each prisoner’s record.

### System Execution Sequence

1. **Login Page**: Authenticate users with valid credentials.
2. **Dashboard**: After login, navigate to the dashboard where you can manage prisoner records.
3. **Operations**: Perform various operations such as adding new prisoners, tracking movements, and generating reports.

### Screenshot of Operations

- **Login Page**:
   ![Login Page](screenshots/login_page.png)

- **Add Prisoner Form**:
   ![Add Prisoner](screenshots/add_prisoner.png)

- **Prisoner Records**:
   ![Prisoner Records](screenshots/prisoner_records.png)

## Conclusion

The **Prison Management System** streamlines the processes involved in managing prisoners, improving the efficiency and accuracy of record-keeping. By automating critical tasks, the system ensures better resource management and provides a more secure, user-friendly platform for prison staff and government officials alike.

This project provides a prototype solution for prison management that can be scaled and customized for use in real-world settings, particularly in developing countries like Pakistan.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
