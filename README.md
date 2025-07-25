# 🍋 Little Lemon Restaurant - Full-Stack Web Application

A modern, responsive restaurant management system built with Django and JavaScript, featuring user authentication, booking management, and a complete menu system.

## ✨ Features

### 🔐 Authentication System

- **JWT-based authentication** using Django REST Framework and SimpleJWT
- **User registration** with secure password validation
- **Login/logout functionality** with persistent sessions
- **Protected routes** - booking and reservations require authentication
- **Token-based API access** for secure data transmission

### 📅 Booking & Reservation Management

- **Real-time booking system** with date and time slot selection
- **Available time slots display** (11 AM - 8 PM)
- **Duplicate booking prevention** - prevents double bookings for same time/date
- **Reservation viewing** - authenticated users can view all reservations
- **Interactive booking interface** with dynamic slot updates

### 🍽️ Menu Management

- **Complete menu system** with item details and pricing
- **Individual menu item pages** with full descriptions
- **Responsive menu display** with professional styling
- **Admin interface** for easy menu management

### 🎨 User Interface

- **Modern, responsive design** that works on all devices
- **Professional restaurant branding** with Little Lemon theme
- **Intuitive navigation** with authentication-aware menu
- **Interactive elements** with smooth user experience
- **Google Maps integration** on reservations page

### 🔧 Technical Features

- **RESTful API architecture** with Django REST Framework
- **MySQL database** for robust data storage
- **CSRF protection** and security best practices
- **Error handling** with user-friendly messages
- **Console debugging** for development and troubleshooting

## 🛠️ Technologies Used

### Backend

- **Django 5.2.4** - Web framework
- **Django REST Framework** - API development
- **SimpleJWT** - JWT authentication
- **MySQL** - Database
- **Python 3.9+** - Programming language

### Frontend

- **HTML5** - Structure
- **CSS3** - Styling and responsive design
- **JavaScript (ES6+)** - Interactive functionality
- **Fetch API** - AJAX requests
- **LocalStorage** - Client-side token storage

### Development Tools

- **Pipenv** - Dependency management
- **Git** - Version control
- **Django Admin** - Content management

## 🚀 Installation & Setup

### Prerequisites

- Python 3.9 or higher
- MySQL server
- Git

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd Display-the-Little-Lemon-available-booking-times-v2
```

### Step 2: Set Up Virtual Environment

```bash
cd Exercise
pipenv install
pipenv shell
```

### Step 3: Configure Database

1. Create a MySQL database named `reservations`
2. Update database settings in `littlelemon/settings.py` if needed:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'reservations',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
    }
}
```

### Step 4: Run Migrations

```bash
python manage.py migrate
```

### Step 5: Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### Step 6: Add Sample Menu Items

```bash
python manage.py shell
```

```python
from restaurant.models import Menu

# Add sample menu items
Menu.objects.create(
    name='Greek Salad',
    price=12,
    menu_item_description='Fresh mixed greens with feta cheese, olives, tomatoes, cucumbers, and red onions, dressed with olive oil and lemon juice.'
)

Menu.objects.create(
    name='Bruschetta',
    price=8,
    menu_item_description='Toasted bread topped with diced tomatoes, fresh basil, garlic, and mozzarella cheese.'
)

# Add more items as needed...
exit()
```

### Step 7: Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to access the application.

## 📱 Usage Guide

### For Customers

1. **Register/Login**: Create an account or log in to access booking features
2. **Browse Menu**: View the complete menu with prices and descriptions
3. **Make Reservations**: Select date and time to book a table
4. **View Bookings**: Check your existing reservations

### For Administrators

1. **Admin Access**: Use Django admin at `/admin/` to manage content
2. **Menu Management**: Add, edit, or remove menu items
3. **Booking Overview**: View all reservations in the system
4. **User Management**: Monitor user accounts and activity

## 🔒 Security Features

- **JWT Authentication**: Secure token-based authentication
- **Password Validation**: Django's built-in password security
- **CSRF Protection**: Cross-site request forgery prevention
- **SQL Injection Prevention**: Django ORM protection
- **XSS Protection**: Content Security Policy headers

## 🧪 Testing

The project includes comprehensive unit tests for:

- User registration functionality
- Authentication system
- API endpoints
- Form validation

Run tests with:

```bash
python manage.py test
```

## 📁 Project Structure

```
Exercise/
├── littlelemon/          # Django project settings
├── restaurant/           # Main application
│   ├── models.py        # Database models
│   ├── views.py         # View logic and API endpoints
│   ├── urls.py          # URL routing
│   ├── forms.py         # Form definitions
│   ├── admin.py         # Admin interface configuration
│   └── templates/       # HTML templates
│       ├── base.html    # Base template
│       ├── menu.html    # Menu page
│       ├── book.html    # Booking page
│       ├── login.html   # Login page
│       └── partials/    # Template components
├── manage.py            # Django management script
├── Pipfile              # Python dependencies
└── db.sqlite3          # SQLite database (development)
```

## 🌟 Key Achievements

- **Full-stack development** with modern web technologies
- **Secure authentication system** with JWT tokens
- **Real-time booking functionality** with duplicate prevention
- **Responsive design** for all device types
- **Professional UI/UX** with restaurant branding
- **Database integration** with MySQL
- **API development** with Django REST Framework
- **Error handling** and user feedback
- **Code organization** and best practices

## 🔮 Future Enhancements

- Email confirmation for bookings
- Payment integration
- Customer reviews and ratings
- Advanced admin dashboard
- Mobile app development
- Integration with third-party delivery services

## 📞 Contact

For questions or collaboration opportunities, please reach out through my portfolio or GitHub profile.

---

**Built with ❤️ using Django and modern web technologies**
