import requests

test = requests.get("https://www.gsmarena.com/alcatel-phones-f-5-0-p10.php")

url = "https://www.gsmarena.com/"

source = requests.get(url+"makers.php3")

makers = {}

not_connected = []

model_count = 0

def get_brands():
    table = False
    for line in source.iter_lines():
        parsed = str(line, 'utf-8')
        if parsed == '</table>':
            break

        if table is True and parsed != '':
            brand_name = parsed[(parsed.find(".php>") + 5):(parsed.find("<br>"))]
            brand_count = parsed[(parsed.find("<span>") + 6):(parsed.find(" devices"))]
            brand_url = url + parsed[(parsed.find("href=") + 5):(parsed.find(".php>"))] + ".php"
            makers[brand_name] = [brand_count, brand_url, {}]

        if parsed == '<table>':
            table = True

def get_models(brand, model_count):
    if brand in not_connected:
        not_connected.remove(brand)
    source = requests.get(makers[brand][1])
    model_class_found = False
    page_class_found = True
    work = False
    print(brand, makers[brand][0], source)
    while page_class_found is True:
        page_class_found = False
        for line in source.iter_lines():
            parsed = str(line, 'utf-8', 'ignore')
            if parsed == "<div class=\"makers\">":
                model_class_found = True

            if parsed.find("<li>") == 0 and model_class_found is True:
                raw_models = parsed
                model_class_found = False
                work = True

            if work is True:
                while raw_models.find("<span>") >= 0:
                    model_url = url + raw_models[(raw_models.find("href=\"") + 6):(raw_models.find(".php"))] + ".php"
                    model_name = raw_models[(raw_models.find("<span>") + 6):(raw_models.find("</span>"))]
                    model_img = raw_models[(raw_models.find("<img src=") + 9):(raw_models.find(" title="))]
                    raw_models = raw_models[raw_models.find("</span>") + 4:]

                    # print("\t", model_name)
                    model_count += 1

                    makers[brand][2][model_name] = [model_url, model_img]
                work = False

            if parsed == "<div class=\"nav-pages\">":
                page_class_found = True;

            if parsed.find("<a class=") == 0 and page_class_found is True:
                next = parsed[(parsed.find("class=\"pages-next\" href=") + 25):(parsed.find("\" title=\"Ne"))]
                if parsed.find("disabled pages-next") >= 0:
                    page_class_found = False
                    break
                else:
                    source = requests.get(url + next)

get_brands()

print("total number of models:", sum(int(makers[brand][0]) for brand in makers))

for brand in makers:
    for retry in range(0,5):
        try:
            get_models(brand, model_count)
            break
        except:
            print(brand, "not connected")
            not_connected.append(brand)

print("not connected:", not_connected)

print("expected", sum(int(makers[brand][0]) for brand in makers), "models, found", model_count)
