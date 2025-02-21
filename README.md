# RecipeShare 🍽️

RecipeShare is a Django-based web application that allows users to create, edit, and share recipes with step-by-step instructions.

---

## 🌟 Features

### 🔹 Recipe Management
- Add, edit, and delete recipes.
- Upload images for recipes.
- Categorize recipes and add tags.

### 🔹 Step-by-Step Instructions
- Add multiple steps to each recipe dynamically.
- Delete specific steps if needed.
- Formset-based inline editing.

### 🔹 Authentication & User Management
- User login and registration.
- Restrict recipe editing to the author.

### 🔹 Enhanced UI/UX
- Responsive design using Bootstrap.
- Dynamic form handling with JavaScript.
- Real-time validation for forms.

### 🔹 Additional Features
- Recipe nutritional information.
- Recipe filtering by category or tags.
- User dashboard with recipe overview.


---
## NOTE : I am not a FRONTEND developer so the focus is on Backend (Django), if there is any mistake sorry.
## 🚀 Installation

### 1️⃣ Clone the Repository
    
     git clone https://github.com/Alirezz2020/.-Recipe-Sharing-Site-.git
     cd .-Recipe-Sharing-Site-

### 2️⃣ Set Up a Virtual Environment
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
### 3️⃣ Install Dependencies
    pip install -r requirements.txt

### 4️⃣ Run Migrations
    python manage.py migrate
### 5️⃣ Create a Superuser (Optional)
    python manage.py createsuperuser
### 6️⃣ Run the Development Server
    python manage.py runserver
## Now, visit http://127.0.0.1:8000/ in your browser!
    

# 🛠️ Technologies Used
Django (CBVs)
Django Formsets
Bootstrap (UI styling)
JavaScript (Dynamic form handling)
SQLite/PostgreSQL (Database)
Gunicorn (For deployment)


# 📌 Contribution
Want to contribute? Fork this repository, create a new branch, and submit a PR!

    git checkout -b feature-new-feature
    git commit -m "Added new feature"
    git push origin feature-new-feature

# 📜 License
This project is licensed under the MIT License.

