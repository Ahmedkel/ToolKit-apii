# Toolkit API Web App

Welcome to Toolkit API, a web application designed for sharing various websites that serve as usable tools, ranging from AI tools to uploading tools and more!

🚀 **Features:**
- Share and discover a wide range of useful websites and tools.
- Explore AI tools, uploading tools, and more.
- Built-in search functionality to easily find what you're looking for.

🔧 **Technologies Used:**
- Django
- HTML
- JavaScript
- CSS

🛠️ **Installation:**
## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.6 or newer
- Git
- Pipenv

## Installation

### Step 1: Clone the Repository

Clone the repository to your local machine and navigate to the directory:

```bash
git clone https://github.com/Ahmedkel/ToolKit-apii.git
cd ToolKit-apii
```

### Step 2: Install Pipenv (if you dont have it alredy)

Install Pipenv, which we'll use for managing project dependencies:

```bash
pip install pipenv
```

### Step 3: Install Dependencies

Install all necessary dependencies specified in the `Pipfile.lock`:

```bash
pipenv install
```

### Step 4: Activate the Virtual Environment

Activate the Pipenv virtual environment:

```bash
pipenv shell
```

### Step 5: Initialize the admin user Django Project

- Ensure Django and Django REST Framework are installed within the virtual environment:

- Create a superuser account for accessing the admin site:


```bash
cd Toolkit
python manage.py createsuperuser
```

### Step 6: Start the Development Server

Run the development server to launch your API:

```bash
python manage.py runserver
```

You can now access your API at `http://127.0.0.1:8000/`.

## Notes

- Ensure that the port `8000` is not already allocated by other apps.
- To access the admin panel go to `http://127.0.0.1:8000/admin/`.

🌐 **Usage:**
1. Register for an admin account or log in if you already have one.
2. Explore the various tools and websites shared by the community.
3. Submit your own tools or websites to share with others.

📝 **Preview:**
![Project Preview](./img/preview.png)


📝 **Contributing:**
Contributions are welcome! If you have suggestions for new features, improvements, or bug fixes, please submit a pull request.

📧 **Contact:**
For any inquiries or support, feel free to contact us at [ahmedkeloch@gmail.com](mailto:ahmedkeloch@gmail.com).

📄 **License:**
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the [LICENSE](LICENSE) file for more details.
