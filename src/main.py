from courses import get_list_of_courses
from file_downloader import clone_folder_structure_of_course
from navigator import Navigator
from login import get_tokens_from_login_page, login

domain = input("Domain: ")
username = input("Username: ")
password = input("Password: ")

nav = Navigator(domain)
security_token, login_ticket = get_tokens_from_login_page(nav)
res = login(nav, security_token, login_ticket, username, password)
print("You are now logged in :)")

courses = list(get_list_of_courses(nav))
clone_folder_structure_of_course(nav, courses[0]["id"], root_dir="./downloads/"+courses[0]["name"])
