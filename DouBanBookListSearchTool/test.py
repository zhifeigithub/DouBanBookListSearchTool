from selenium import webdriver

def func():
    tmp = '<html><body><form id="loginForm"><p class="content">Site content goes here.</p><input name="username" type="text" />username</form></body><html>'
    print(tmp.find_elements_by_class_name('content'))


if __name__ == '__main__':
    func()