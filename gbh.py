from selenium import webdriver

try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://gbh.com.do/")

    # Opcion de Inicio
    inicio_menu = driver.find_element_by_id("menu-item-21")

    # Opcion de Servicios
    servicios_menu = driver.find_element_by_id("menu-item-209")
    servicios_menu.click()

    # Rellenar arreglo con los Servicios de Desarrollo
    lista_servicios_desarrollo = driver.find_element_by_id("menu-item-229")
    itemsDesarrollo = lista_servicios_desarrollo.find_elements_by_tag_name("li")
    servicio_desarrollo = []

    for itemDesarrollo in itemsDesarrollo:
        text = itemDesarrollo.text
        servicio_desarrollo.append(text)

    # Rellenar arreglo con los Servicios de Soporte
    lista_servicios_soporte = driver.find_element_by_id("menu-item-230")
    itemsSoporte = lista_servicios_soporte.find_elements_by_tag_name("li")
    servicio_soporte = []

    for itemSoporte in itemsSoporte:
        text1 = itemSoporte.text
        servicio_soporte.append(text1)

    # Navegar las opciones de Servicios de Desarrollo
    print("Servicios de Desarrollo")
    for count in range(0, len(servicio_desarrollo)):

        driver.find_element_by_link_text(servicio_desarrollo[count]).click()
        print("Se ha navegado en el servicio: " + servicio_desarrollo[count])
        servicios_menu = driver.find_element_by_id("menu-item-209")
        servicios_menu.click()

    # Navegar las opciones de Servicios de Soporte
    print("\n")
    print("Servicios de Soporte")
    for count1 in range(0, len(servicio_soporte)):

        driver.find_element_by_link_text(servicio_soporte[count1]).click()
        print("Se ha navegado en el servicio: " + servicio_soporte[count1])
        servicios_menu = driver.find_element_by_id("menu-item-209")
        servicios_menu.click()

    # Navegar en la opcion de Portafolio
    portafolio_menu = driver.find_element_by_id("menu-item-62")
    portafolio_menu.click()
    print("\n")
    print("Se ha navegado en la opcion de Portafolio")

    # Navegar en la opcion de Contactanos
    contactanos_menu = driver.find_element_by_id("menu-item-65")
    contactanos_menu.click()
    print("\n")
    print("Se ha navegado en la opcion de Contactanos")

    # Navegar en la opcion de Empleos
    empleo_menu = driver.find_element_by_id("menu-item-126")
    empleo_menu.click()

    # Navegar en la opcion de Blog
    blog_menu = driver.find_element_by_id("menu-item-20")
    blog_menu.click()
    print("\n")
    print("Se ha navegado en la opcion de Empleo")

except:
    driver.get("http://gbh.com.do/")
    print("Error")



