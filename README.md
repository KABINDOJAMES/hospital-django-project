# HOSPITAL DJANGO PROJECT
This is a web application that can be used by hospitals and clinics. By editing the templates, it can be used on many projects.
> ## Steps to run project are provided below

## This project includes:
- [x] A homepage, the and images included are editable in the admin panel. You can write your own text and include images. You can also reformat the layout.
      This project includes a html editor used to convert simple word documents directly into HTML
- [x] A services section, you can write what your hospital or blog provides in this section. There is a service detail section that displays each service on its on page.
![services section](https://user-images.githubusercontent.com/90185274/222881516-e887ed6e-5191-4e28-ad74-81a05a922438.PNG)
![service detail section](https://user-images.githubusercontent.com/90185274/222881537-d0483b8d-a493-4856-91dc-bbcafc793c38.PNG)

- [x] A pharmacy section, allows you to explain to your customers what medication you offer at your hospital or clinic.
![pharmacy section](https://user-images.githubusercontent.com/90185274/222881558-36f28767-7bf3-4872-af65-c0256c06732e.PNG)

- [x] An about page, describes about yourself and the hospital to your customers.
- [x] Social Media links, to include your facebook, twitter, instagram, and any link.
![footer section](https://user-images.githubusercontent.com/90185274/222881585-9a2613ed-3d07-435d-bc3c-5f7d755cbb22.PNG)

- [x] Contact section, to allow customers contact you.
![contact section](https://user-images.githubusercontent.com/90185274/222881577-a515f517-7235-4011-8370-dffbe81add0e.PNG)

## Steps To Run The Project
> ## If you need any help, you can reach me through enquiry@dogojanja.com
The steps below make an assumption that you have:
 - [x] Python Installed In Your System
 - [x] Pip installed
 - [x] Virtual Environment

- Start By Cloning the project
```
git clone https://github.com/KABINDOJAMES/hospital-django-project.git
```
- Create a virtual environment for the project
```
virtualenv my_env
```
   Example 
   ```
   virtualenv hospital
   ```
- Activate your virtual environment
 ```
 my_env\scripts\activate
 ```
   Example
   ```
   hospital\scripts\activate
   ```
 - Change directory to your cloned repository
 - Install requirements by running
 ```
 pip install requirements.txt
 ```
 - Make Database Migrations
  ```
  python manage.py makemigrations
  ```
  Then
  ```
  python manage.py migrate
  ```
  - Create a super user 
   ```
   python manage.py createsuperuser
   ```
   Follow prompts and create a super user successfully to be able to login to admin panel
   
   - Start Your web application at local host 
   ```
   python manage.py runserver
   ```
   ### You Are Good To Go
   
   You can login to the admin panel and make changes to the text displayed on the web page, you can edit the following:
   - [x] Your homepage text and images
   - [x] You can edit and add new services
   - [x] Social Media Links
   - [x] About Section and Contact us
   - [x] Pharmacy section
   ![admin](https://user-images.githubusercontent.com/90185274/222882303-9cdcc6c4-93b8-4e4a-9bb2-b3af683a6d1d.PNG)

   
   If Any Errors, Please leave a comment
   > # The project is sponsored by https://www.dogojanja.com
