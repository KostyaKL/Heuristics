import pickle
import requests

test = requests.get("https://www.gsmarena.com/alcatel-phones-f-5-0-p10.php")

url = "https://www.gsmarena.com/"

source = requests.get(url+"makers.php3")

makers = {}

not_connected = []


class ModelCount:
    count = 0


def save_obj(obj, name):
    with open(name + '.pkl', 'wb') as f:
        #pickle.dump(obj, f)
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)


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
            makers[brand_name] = {}
            makers[brand_name]["count"] = brand_count
            makers[brand_name]["url"] = brand_url
            makers[brand_name]["models"] = {}

        if parsed == '<table>':
            table = True


def get_models(brand, model_count):
    if brand in not_connected:
        not_connected.remove(brand)
    source = requests.get(makers[brand]["url"])
    model_class_found = False
    page_class_found = True
    work = False
    print(brand, makers[brand]["count"], source)
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
                    model_count.count += 1

                    makers[brand]["models"][model_name] = {}
                    makers[brand]["models"][model_name]["url"] = model_url
                    makers[brand]["models"][model_name]["img"] = model_img
                    makers[brand]["models"][model_name]["specs"] = {}
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


def get_specs(brand, model):
    source = requests.get(makers[brand]["models"][model]["url"])


makers = load_obj("db")

# get_brands()
#
print("total number of models:", sum(int(makers[brand]["count"]) for brand in makers))
#
# for brand in makers:
#     for retry in range(0,5):
#         try:
#             get_models(brand, ModelCount)
#             break
#         except:
#             print(brand, "not connected -------------------------------------->")
#             not_connected.append(brand)
#
# print("not connected:", not_connected)
#
# print("expected", sum(int(makers[brand]["count"]) for brand in makers), "models, found", ModelCount.count)
#
# save_obj(makers, "db")

for brand in makers:
    for model in makers[brand]:
        get_specs(brand, model)

print(" ")
