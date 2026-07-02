# Flask Authentication App

A simple Flask web application with user authentication (registration, login, logout) using Flask-SQLAlchemy and MySQL.

## Features

- User Registration with password hashing
- User Login/Logout with session management
- Protected dashboard route
- Flash messages for user feedback
- Responsive UI with Bootstrap
- MySQL database integration

## Tech Stack

- **Backend**: Flask (Python)
- **Database**: MySQL with SQLAlchemy ORM
- **Authentication**: Werkzeug password hashing
- **Frontend**: HTML, CSS, JavaScript (Bootstrap 5)
- **Session Management**: Flask-Session

## Project Structure

```
python_basics/
├── app.py              # Main application file
├── config.py           # Configuration settings
├── extensions.py       # Database initialization
├── models.py           # User model
├── requirements.txt    # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css
│   ├── images/
│   └── js/
└── templates/
    ├── layout.html     # Base template
    ├── index.html      # Home page
    ├── login.html      # Login page
    ├── registration.html # Registration page
    └── dashboard.html  # Protected dashboard
```

## Installation

### Prerequisites

- Python 3.8+
- MySQL Server
- pip (Python package manager)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/karanmaurya767/FlaskApp.git
   cd FlaskApp
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # source venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Database**
   - Create a MySQL database named `flask_login`
   - Update `config.py` with your MySQL credentials:
     ```python
     SQLALCHEMY_DATABASE_URI = "mysql+pymysql://username:password@localhost/flask_login"
     ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the app**
   Open http://localhost:5000 in your browser

## Dependencies

```
Flask==2.3.3
Flask-SQLAlchemy==3.0.5
pymysql==1.1.0
Werkzeug==2.3.7
```

Install with:
```bash
pip install Flask Flask-SQLAlchemy pymysql Werkzeug
```

## Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Home page |
| `/register` | GET, POST | User registration |
| `/login` | GET, POST | User login |
| `/dashboard` | GET | Protected dashboard (requires login) |
| `/logout` | GET | User logout |

## Security Features

- Password hashing using Werkzeug's `generate_password_hash` and `check_password_hash`
- Session-based authentication
- SQL injection prevention via SQLAlchemy ORM
- CSRF protection (can be added with Flask-WTF)

## Screenshots

### Home Page
![Home](static/images/home.png)

### Login Page
![Login](static/images/login.png)

### Registration Page
![Register](static/images/register.png)

### Dashboard
![Dashboard](static/images/dashboard.png)

## Future Improvements

- [ ] Add email verification
- [ ] Implement password reset functionality
- [ ] Add user profile management
- [ ] Add role-based access control
- [ ] Add unit tests
- [ ] Dockerize the application
- [ ] Add CI/CD pipeline

## License

This project is licensed under the MIT License.

## Author

**Karan Maurya**
- GitHub: [@karanmaurya767](https://github.com/karanmaurya767)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request