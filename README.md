# Database Project - Industrial Work Control System

## 📋 Overview

This is a web system developed in **Flask** for controlling and recording industrial jobs, allowing the management of machine operations, operators, and clients.  

The project was built as part of a **database assignment** and demonstrates the implementation of a complete web application with a user interface and persistent data storage.  

🔗 **Live Demo**: [Database Project on Render](https://database-project-rkeb.onrender.com)

---

## 🚀 Features

### Main Capabilities
- **Login System**: Simple authentication with fixed credentials (`admin/machinery`)  
- **Job Registration**: Form for registering new industrial jobs  
- **Data Visualization**: Table showing all registered jobs  
- **Automatic Calculation**: Total job time calculated automatically  
- **Responsive Interface**: Modern CSS design with Font Awesome  

### Data Managed
- Operator (responsible person)  
- Machine (Doosan 5700, Doosan 6700)  
- Client name  
- Drawing/Project number  
- Start date & time  
- End date & time  
- Total job duration  

---

## 🛠️ Technologies Used

### Backend
- Python 3.x  
- Flask (web framework)  
- SQLAlchemy (ORM)  
- PostgreSQL (production database)  

### Frontend
- HTML5  
- CSS3 (responsive design)  
- JavaScript (form validation & interactivity)  
- Font Awesome (icons)  
- Google Fonts (Open Sans)  

### Database
- SQLite (local development)  
- PostgreSQL (production, configurable)  

---

## 📁 Project Structure

DataBase_Project/
├── app.py # Main Flask app
├── models.py # SQLAlchemy models
├── config.py # App configuration
├── instance/
│ └── mydb.db # Local SQLite database
├── static/
│ ├── css/
│ │ └── styles.css # CSS styles
│ └── js/
│ └── login.js # JavaScript scripts
├── templates/
│ ├── base.html # Base template
│ ├── home.html # Main page
│ ├── login.html # Login page
│ └── newRegister.html # Job registration form
└── 4_Databases_Assignment.pdf # Assignment documentation


---

## 📊 Data Model

**Table: jobs**

| Field          | Type       | Description                       |
| -------------- | ---------- | --------------------------------- |
| id             | Integer    | Primary key (auto-increment)      |
| name           | String(50) | Operator’s name                   |
| machine        | String(50) | Machine type                      |
| costumer       | String(50) | Client’s name                     |
| drawing_number | String(50) | Drawing number                    |
| start_date     | Date       | Start date                        |
| start_time     | Time       | Start time                        |
| end_date       | Date       | End date                          |
| end_time       | Time       | End time                          |
| total_time     | Time       | Calculated total time             |

---

## 🎯 Application Routes

- **GET /** → Login page  
- **GET /home** → Main job listing page  
- **GET /newRegister** → Job registration form  
- **POST /newRegister** → Save new job  

---

## 🔐 Authentication

- **Username**: `admin`  
- **Password**: `machinery`  

---

## 🎨 User Interface

- Responsive layout (mobile-friendly)  
- Clean & modern design  
- Navigation with icons  
- Success/error feedback messages  
- Organized job table  

### Pages
1. **Login** – Authentication  
2. **Home** – All registered jobs  
3. **New Register** – Add a new job  

---

## 🔄 Project Evolution

### ✅ Current Version (1.0)
- Basic authentication  
- Full job CRUD  
- Responsive interface  
- Automatic job time calculation  
- Database integration  
- Form validation  

### 🔮 Future Improvements
- Robust authentication  
- Backend data validation  
- Reports & statistics  
- Search & filtering  
- Edit & delete jobs  
- User roles/permissions  
- REST API integration  
- Automated testing  
- API documentation  

---

## 🐛 Known Issues
1. **Time calculation bug**: Lines 49–51 in `app.py` contain unused code that may cause errors.  
2. **Data validation**: Missing backend validation.  
3. **Security**: Hardcoded credentials in JavaScript.  
4. **Home page table**: “End time” column incorrectly shows “End date” (line 32 in `home.html`).  

---

## 📝 Development Notes

### Decisions
- Flask chosen for simplicity & flexibility  
- SQLAlchemy for ORM  
- Jinja2 templates  
- Pure CSS (no frameworks)  

### Standards
- MVC structure  
- Template inheritance  
- Centralized configuration  
- Basic error handling  

---

## 👥 Contribution

1. Fork the repo  
2. Create a feature branch  
3. Commit your changes  
4. Push to your branch  
5. Open a Pull Request  

---

## 📄 License

This project was developed as part of an **academic assignment**. See `4_Databases_Assignment.pdf` for requirements & specifications.  

---

## 📞 Contact

For questions or suggestions, please use the repository’s communication channels.  

---

**Developed as part of a Database Assignment – 2025**  