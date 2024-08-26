# Django Project

## Overview
This is a Django project designed for managing and processing form submissions, integrating with Google Sheets via a service account, and sending emails using SMTP.

## Features
- Form submission handling
- Database integration
- Email notifications using SMTP
- Google Sheets integration via Google service account

## Prerequisites
- Python 3.x
- Django 3.x or higher
- Google service account credentials
- SMTP credentials for email notifications

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/erfnkrm/brandexpert.git
    
    cd erfnkrm
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv env
    source env/bin/activate   # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the root directory and add the following configurations:
    ```plaintext
    SECRET_KEY=your_secret_key
    DEBUG=True

    EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
    EMAIL_HOST=smtp.gmail.com
    EMAIL_PORT=587
    EMAIL_USE_TLS=True
    EMAIL_HOST_USER=your_email@gmail.com
    EMAIL_HOST_PASSWORD=your_email_password

    GOOGLE_SERVICE_ACCOUNT_JSON={"type": "service_account", ...}  # JSON string of your Google service account credentials
    ```

5. **Apply database migrations**:
    ```sh
    python manage.py migrate
    ```

6. **Create a superuser** (optional, for accessing Django admin):
    ```sh
    python manage.py createsuperuser
    ```

7. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

8. **Access the application**:
    Open a web browser and go to `http://127.0.0.1:8000`.

## Usage

### Form Submission
- Navigate to the form page (e.g., `/form/`).
- Fill out the form and submit.

### Email Notifications
- Upon form submission, an email notification will be sent to the configured recipient.

### Google Sheets Integration
- The form data will be saved to a Google Sheet using the provided service account credentials.

## Troubleshooting

### Common Issues
- **SMTP Authentication Error**: Ensure your email and password are correct. For Gmail, enable "Less secure app access" in your Google account settings.
- **File Not Found Error**: Make sure your `GOOGLE_SERVICE_ACCOUNT_JSON` path or JSON string is correct.

### Debugging
- Check the Django debug logs for detailed error messages.
- Verify your environment variables and settings in the `.env` file.

## Contributing
- Fork the repository.
- Create a new branch (`git checkout -b feature-branch`).
- Commit your changes (`git commit -am 'Add new feature'`).
- Push to the branch (`git push origin feature-branch`).
- Open a pull request.


## Contact
For questions or support, please contact `erfankarimi133081@gmail.com`.

