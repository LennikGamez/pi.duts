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

clone_folder_structure_of_course(nav, "18cafcf4d0bd83fdb9b40206c70ac8df")
