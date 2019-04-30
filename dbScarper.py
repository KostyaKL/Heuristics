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
    if brand in not_connected:
        not_connected.remove(brand + " " + model)
    source = requests.get(makers[brand]["models"][model]["url"])

    print(brand, model)
    
    no_data = "no data"

    makers[brand]["models"][model]["specs"]["battery"] = no_data
    makers[brand]["models"][model]["specs"]["year"] = no_data
    makers[brand]["models"][model]["specs"]["height"] = no_data
    makers[brand]["models"][model]["specs"]["width"] = no_data
    makers[brand]["models"][model]["specs"]["weight"] = no_data
    makers[brand]["models"][model]["specs"]["sim"] = no_data
    makers[brand]["models"][model]["specs"]["numofsim"] = no_data
    makers[brand]["models"][model]["specs"]["simtype"] = no_data
    makers[brand]["models"][model]["specs"]["displaysize"] = no_data
    makers[brand]["models"][model]["specs"]["displayresolution"] = no_data
    makers[brand]["models"][model]["specs"]["os"] = no_data
    makers[brand]["models"][model]["specs"]["chipset"] = no_data
    makers[brand]["models"][model]["specs"]["cpu"] = no_data
    makers[brand]["models"][model]["specs"]["gpu"] = no_data
    makers[brand]["models"][model]["specs"]["memoryslot"] = no_data
    makers[brand]["models"][model]["specs"]["maxextmemory"] = no_data
    makers[brand]["models"][model]["specs"]["RAM"] = no_data
    makers[brand]["models"][model]["specs"]["cam1MP"] = no_data
    makers[brand]["models"][model]["specs"]["cam1video"] = no_data
    makers[brand]["models"][model]["specs"]["cam2MP"] = no_data
    makers[brand]["models"][model]["specs"]["cam2video"] = no_data
    makers[brand]["models"][model]["specs"]["ir"] = no_data
    makers[brand]["models"][model]["specs"]["radio"] = no_data
    makers[brand]["models"][model]["specs"]["usb"] = no_data
    makers[brand]["models"][model]["specs"]["nfc"] = "No"
    makers[brand]["models"][model]["specs"]["fingerprint"] = "No"
    makers[brand]["models"][model]["specs"]["price"] = no_data
    makers[brand]["models"][model]["specs"]["basemark"] = no_data
    makers[brand]["models"][model]["specs"]["loudspeaker"] = no_data
    makers[brand]["models"][model]["specs"]["audioquality"] = no_data
    makers[brand]["models"][model]["specs"]["endurance"] = no_data

    specs_list_found = False
    ir = False
    for line in source.iter_lines():
        if ir is True:
            ir = False
            try:
                makers[brand]["models"][model]["specs"]["ir"] = parsed[parsed.find(">") + 1:parsed.find("<")]
            except:
                makers[brand]["models"][model]["specs"]["ir"] = no_data

        parsed = str(line, 'utf-8', 'ignore')
        if parsed.find("<div id=\"specs-list\">") == 0:
            specs_list_found = True

        if parsed.find("<p class=\"note\">") == 0:
            break

        if parsed.find("batsize") >= 0:
            try:
                makers[brand]["models"][model]["specs"]["battery"] = int(parsed[parsed.find("spec=\"batsize-hl\">")+18:parsed.find("</span>")])
            except:
                makers[brand]["models"][model]["specs"]["battery"] = no_data

        if specs_list_found is True:
            if parsed.find("data-spec=\"year\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["year"] = int(parsed[parsed.find(">") + 1:parsed.find(",")])
                except:
                    makers[brand]["models"][model]["specs"]["year"] = no_data
            if parsed.find("data-spec=\"dimensions\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["height"] = float(parsed[parsed.find(">") + 1:parsed.find(" x ")])
                    parsed = parsed[parsed.find(" x ") + 3:]
                    makers[brand]["models"][model]["specs"]["width"] = float(parsed[:parsed.find(" x ")])
                except:
                    makers[brand]["models"][model]["specs"]["height"] = no_data
                    makers[brand]["models"][model]["specs"]["width"] = no_data
            if parsed.find("data-spec=\"weight\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["weight"] = float(parsed[parsed.find(">") + 1:parsed.find(" g ")])
                except:
                    makers[brand]["models"][model]["specs"]["weight"] = no_data
            if parsed.find("data-spec=\"sim\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["sim"] = parsed[parsed.find(">") + 1:parsed.find("</")]
                except:
                    makers[brand]["models"][model]["specs"]["sim"] = no_data
            if parsed.find("data-spec=\"displaysize\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["displaysize"] = float(parsed[parsed.find(">") + 1:parsed.find(" inches")])
                except:
                    makers[brand]["models"][model]["specs"]["displaysize"] = no_data
            if parsed.find("data-spec=\"displayresolution\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["displayresolution"] = parsed[parsed.find(">") + 1:parsed.find(" pixels")]
                except:
                    makers[brand]["models"][model]["specs"]["displayresolution"] = no_data
            if parsed.find("data-spec=\"os\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["os"] = parsed[parsed.find(">") + 1:parsed.find("</")]
                except:
                    makers[brand]["models"][model]["specs"]["os"] = no_data
            if parsed.find("data-spec=\"chipset\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["chipset"] = parsed[parsed.find(">") + 1:parsed.find("</")]
                except:
                    makers[brand]["models"][model]["specs"]["chipset"] = no_data
            if parsed.find("data-spec=\"cpu\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["cpu"] = parsed[parsed.find(">") + 1:parsed.find("</")]
                except:
                    makers[brand]["models"][model]["specs"]["cpu"] = no_data
            if parsed.find("data-spec=\"gpu\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["gpu"] = parsed[parsed.find(">") + 1:parsed.find("</")]
                except:
                    makers[brand]["models"][model]["specs"]["gpu"] = no_data
            if parsed.find("data-spec=\"memoryslot\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["memoryslot"] = parsed[parsed.find(">") + 1:parsed.find("</")]
                except:
                    makers[brand]["models"][model]["specs"]["memoryslot"] = no_data
            if parsed.find("data-spec=\"internalmemory\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["RAM"] = parsed[parsed.find(">") + 1:parsed.find(" GB")]
                except:
                    makers[brand]["models"][model]["specs"]["RAM"] = no_data
            if parsed.find("data-spec=\"cam1modules\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["cam1MP"] = int(parsed[parsed.find(">") + 1:parsed.find(" MP")])
                except:
                    makers[brand]["models"][model]["specs"]["cam1MP"] = no_data
            if parsed.find("data-spec=\"cam1video\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["cam1video"] = int(parsed[parsed.find(">") + 1:parsed.find("p", parsed.find(">"))])
                except:
                    makers[brand]["models"][model]["specs"]["cam1video"] = no_data
            if parsed.find("data-spec=\"cam2modules\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["cam2MP"] = int(parsed[parsed.find(">") + 1:parsed.find(" MP")])
                except:
                    makers[brand]["models"][model]["specs"]["cam2MP"] = no_data
            if parsed.find("data-spec=\"cam2video\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["cam2video"] = int(parsed[parsed.find(">") + 1:parsed.find("p@")])
                except:
                    makers[brand]["models"][model]["specs"]["cam2video"] = no_data
            if parsed.find(">Infrared port<") >= 0:
                ir = True
            if parsed.find("data-spec=\"radio\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["radio"] = parsed[parsed.find(">") + 1:parsed.find("<")]
                except:
                    makers[brand]["models"][model]["specs"]["radio"] = no_data
            if parsed.find("data-spec=\"usb\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["usb"] = parsed[parsed.find(">") + 1:parsed.find("</")]
                except:
                    makers[brand]["models"][model]["specs"]["usb"] = no_data
            if parsed.find("Fingerprint ") >= 0 or parsed.find("fingerprint ") >= 0:
                makers[brand]["models"][model]["specs"]["fingerprint"] = "Yes"
            if parsed.find("nfc") >= 0 or parsed.find("Nfc") >= 0 or parsed.find("NFC") >= 0:
                makers[brand]["models"][model]["specs"]["nfc"] = "Yes"
            if parsed.find("data-spec=\"price\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["price"] = int(parsed[parsed.find(">About ") + 7:parsed.find(" ", parsed.find(">About ") + 7)])
                except:
                    makers[brand]["models"][model]["specs"]["price"] = no_data
            if parsed.find("Basemark X: ") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["basemark"] = int(parsed[parsed.find("Basemark X: ") + 12:parsed.find("</")])
                except:
                    makers[brand]["models"][model]["specs"]["basemark"] = no_data
            if parsed.find(">Voice ") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["loudspeaker"] = float(parsed[parsed.find(">Voice ") + 7:parsed.find("dB ")])
                except:
                    makers[brand]["models"][model]["specs"]["loudspeaker"] = no_data
            if parsed.find("Crosstalk") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["audioquality"] = float(parsed[parsed.find(">Noise ") + 7:parsed.find("dB ")])
                except:
                    makers[brand]["models"][model]["specs"]["audioquality"] = no_data
            if parsed.find(">Endurance rating") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["endurance"] = int(parsed[parsed.find(">Endurance rating ") + 18:parsed.find("h<")])
                except:
                    makers[brand]["models"][model]["specs"]["endurance"] = no_data



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

# for brand in makers:
#     for model in makers[brand]["models"]:
#         for retry in range(0, 5):
#             try:
#                 get_specs(brand, model)
#                 break
#             except:
#                 print(brand, model, "not connected -------------------------------------->")
#                 not_connected.append(brand + " " + model)
#
# save_obj(makers, "db")

with open('test.csv', 'w') as f:
    printout = "brand,model"
    for key in makers["Acer"]["models"]["Chromebook Tab 10"]["specs"]:
        printout = printout + "," + key
    f.write(printout + "\n")
    for brand in makers:
        for model in makers[brand]["models"]:
            printout = brand + "," + model
            for spec in makers[brand]["models"][model]["specs"]:
                tmp = str(makers[brand]["models"][model]["specs"][spec])
                if tmp.find(",") >= 0:
                    tmp = "\"" + tmp + "\""
                printout = printout + "," + tmp
            f.write(printout + "\n")




