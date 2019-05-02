import pickle
import requests

test = requests.get("https://www.gsmarena.com/alcatel-phones-f-5-0-p10.php")

url = "https://www.gsmarena.com/"

source = requests.get(url + "makers.php3")

makers = {}

not_connected = []


class ModelCount:
    count = 0


def save_obj(obj, name):
    with open(name + '.pkl', 'wb') as f:
        # pickle.dump(obj, f)
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

    makers[brand]["models"][model]["specs"]["battery"] = 0
    makers[brand]["models"][model]["specs"]["year"] = 0
    makers[brand]["models"][model]["specs"]["height"] = 0
    makers[brand]["models"][model]["specs"]["width"] = 0
    makers[brand]["models"][model]["specs"]["weight"] = 0
    makers[brand]["models"][model]["specs"]["sim"] = no_data
    makers[brand]["models"][model]["specs"]["numofsim"] = 0
    makers[brand]["models"][model]["specs"]["simtype"] = 0  # 1 full, 2 mini, 3 micro, 4 nano, 0 no
    makers[brand]["models"][model]["specs"]["displaysize"] = 0
    makers[brand]["models"][model]["specs"]["displayresolution"] = 0
    makers[brand]["models"][model]["specs"]["os"] = 0  # 1 android, 2 apple, 3 microsoft, 4 blackberry, 5 firefox, 6 symbian, 0 other
    makers[brand]["models"][model]["specs"]["chipset"] = no_data
    makers[brand]["models"][model]["specs"]["cpu"] = no_data  # todo need to be dealt with
    makers[brand]["models"][model]["specs"]["gpu"] = no_data
    makers[brand]["models"][model]["specs"]["memoryslot"] = 0
    makers[brand]["models"][model]["specs"]["maxextmemory"] = 0
    makers[brand]["models"][model]["specs"]["RAM"] = no_data  # todo need to be dealt with
    makers[brand]["models"][model]["specs"]["cam1MP"] = 0
    makers[brand]["models"][model]["specs"]["cam1video"] = 0
    makers[brand]["models"][model]["specs"]["cam2MP"] = 0
    makers[brand]["models"][model]["specs"]["cam2video"] = 0
    makers[brand]["models"][model]["specs"]["ir"] = 0
    makers[brand]["models"][model]["specs"]["radio"] = 0 # todo nee to be checked
    makers[brand]["models"][model]["specs"]["usb"] = 0  # 1 type c/iphone, 2 mini, 3 micro, 0 else
    makers[brand]["models"][model]["specs"]["nfc"] = 0
    makers[brand]["models"][model]["specs"]["fingerprint"] = 0
    makers[brand]["models"][model]["specs"]["price"] = no_data  # todo need to be dealt with
    makers[brand]["models"][model]["specs"]["basemark"] = 0
    makers[brand]["models"][model]["specs"]["loudspeaker"] = 0
    makers[brand]["models"][model]["specs"]["audioquality"] = 0
    makers[brand]["models"][model]["specs"]["endurance"] = 0

    specs_list_found = False
    ir = False
    for line in source.iter_lines():

        parsed = str(line, 'utf-8', 'ignore')
        if parsed.find("<div id=\"specs-list\">") == 0:
            specs_list_found = True

        if parsed.find("<p class=\"note\">") == 0:
            break

        if parsed.find("batsize") >= 0:
            try:
                makers[brand]["models"][model]["specs"]["battery"] = int(
                    parsed[parsed.find("spec=\"batsize-hl\">") + 18:parsed.find("</span>")])
            except:
                makers[brand]["models"][model]["specs"]["battery"] = 0

        if specs_list_found is True:
            if parsed.find("data-spec=\"year\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["year"] = int(parsed[parsed.find(">") + 1:parsed.find(",")])
                except:
                    makers[brand]["models"][model]["specs"]["year"] = 0
            if parsed.find("data-spec=\"dimensions\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["height"] = float(
                        parsed[parsed.find(">") + 1:parsed.find(" x ")])
                    parsed = parsed[parsed.find(" x ") + 3:]
                    makers[brand]["models"][model]["specs"]["width"] = float(parsed[:parsed.find(" x ")])
                except:
                    makers[brand]["models"][model]["specs"]["height"] = 0
                    makers[brand]["models"][model]["specs"]["width"] = 0
            if parsed.find("data-spec=\"weight\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["weight"] = float(
                        parsed[parsed.find(">") + 1:parsed.find(" g ")])
                except:
                    makers[brand]["models"][model]["specs"]["weight"] = 0
            if parsed.find("data-spec=\"sim\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["sim"] = parsed[parsed.find(">") + 1:parsed.find("</")]
                    if makers[brand]["models"][model]["specs"]["sim"].find("Nano") >= 0:
                        makers[brand]["models"][model]["specs"]["simtype"] = 4
                    elif makers[brand]["models"][model]["specs"]["sim"].find("Micro") >= 0:
                        makers[brand]["models"][model]["specs"]["simtype"] = 3
                    elif makers[brand]["models"][model]["specs"]["sim"].find("Mini") >= 0:
                        makers[brand]["models"][model]["specs"]["simtype"] = 2
                    elif makers[brand]["models"][model]["specs"]["sim"].find("No") >= 0:
                        makers[brand]["models"][model]["specs"]["simtype"] = 0
                    else:
                        makers[brand]["models"][model]["specs"]["simtype"] = 1

                    if makers[brand]["models"][model]["specs"]["sim"].find("Quad") >= 0:
                        makers[brand]["models"][model]["specs"]["numofsim"] = 4
                    elif makers[brand]["models"][model]["specs"]["sim"].find("Triple") >= 0:
                        makers[brand]["models"][model]["specs"]["numofsim"] = 3
                    elif makers[brand]["models"][model]["specs"]["sim"].find("Dual") >= 0:
                        makers[brand]["models"][model]["specs"]["numofsim"] = 2
                    elif makers[brand]["models"][model]["specs"]["sim"].find("Single") >= 0 or makers[brand]["models"][model]["specs"]["sim"].find("Yes") >= 0:
                        makers[brand]["models"][model]["specs"]["numofsim"] = 1
                    else:
                        makers[brand]["models"][model]["specs"]["numofsim"] = 0
                except:
                    makers[brand]["models"][model]["specs"]["sim"] = no_data
            if parsed.find("data-spec=\"displaysize\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["displaysize"] = float(
                        parsed[parsed.find(">") + 1:parsed.find(" inches")])
                except:
                    makers[brand]["models"][model]["specs"]["displaysize"] = 0
            if parsed.find("data-spec=\"displayresolution\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["displayresolution"] = parsed[
                                                                                   parsed.find(">") + 1:parsed.find(
                                                                                       " pixels")]
                    try:
                        a = makers[brand]["models"][model]["specs"]["displayresolution"][:makers[brand]["models"][model]["specs"]["displayresolution"].find(" x ")]
                        b = makers[brand]["models"][model]["specs"]["displayresolution"][makers[brand]["models"][model]["specs"]["displayresolution"].find(" x ") + 3:]
                        makers[brand]["models"][model]["specs"]["displayresolution"] = int(a) * int(b)
                    except:
                        makers[brand]["models"][model]["specs"]["displayresolution"] = 0
                except:
                    makers[brand]["models"][model]["specs"]["displayresolution"] = 0
            if parsed.find("data-spec=\"os\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["os"] = parsed[parsed.find(">") + 1:parsed.find("</")]
                    if brand == "Apple":
                        makers[brand]["models"][model]["specs"]["os"] = 2
                    elif makers[brand]["models"][model]["specs"]["os"].find("Android") >= 0:
                        makers[brand]["models"][model]["specs"]["os"] = 1
                    elif makers[brand]["models"][model]["specs"]["os"].find("Microsoft") >= 0:
                        makers[brand]["models"][model]["specs"]["os"] = 3
                    elif makers[brand]["models"][model]["specs"]["os"].find("BlackBerry") >= 0:
                        makers[brand]["models"][model]["specs"]["os"] = 4
                    elif makers[brand]["models"][model]["specs"]["os"].find("Symbian") >= 0:
                        makers[brand]["models"][model]["specs"]["os"] = 5
                    elif makers[brand]["models"][model]["specs"]["os"].find("Firefox") >= 0:
                        makers[brand]["models"][model]["specs"]["os"] = 6
                    else:
                        makers[brand]["models"][model]["specs"]["os"] = 0
                except:
                    makers[brand]["models"][model]["specs"]["os"] = 0
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
                    makers[brand]["models"][model]["specs"]["memoryslot"] = parsed[
                                                                            parsed.find(">") + 1:parsed.find("</")]
                    if makers[brand]["models"][model]["specs"]["memoryslot"].find("No") >= 0:
                        makers[brand]["models"][model]["specs"]["memoryslot"] = 0
                        makers[brand]["models"][model]["specs"]["maxextmemory"] = 0
                    else:
                        start = makers[brand]["models"][model]["specs"]["memoryslot"].find("up to")
                        end = makers[brand]["models"][model]["specs"]["memoryslot"].find("GB")
                        if start >= 0 and end >= 0:
                            makers[brand]["models"][model]["specs"]["maxextmemory"] = makers[brand]["models"][model]["specs"]["memoryslot"][start + 5:end]
                            makers[brand]["models"][model]["specs"]["memoryslot"] = 1
                except:
                    makers[brand]["models"][model]["specs"]["memoryslot"] = 0
            if parsed.find("data-spec=\"internalmemory\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["RAM"] = parsed[parsed.find(">") + 1:parsed.find(" RAM")]
                except:
                    makers[brand]["models"][model]["specs"]["RAM"] = no_data
            if parsed.find("data-spec=\"cam1modules\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["cam1MP"] = int(
                        parsed[parsed.find(">") + 1:parsed.find(" MP")])
                except:
                    makers[brand]["models"][model]["specs"]["cam1MP"] = 0
            if parsed.find("data-spec=\"cam1video\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["cam1video"] = int(
                        parsed[parsed.find(">") + 1:parsed.find("p", parsed.find(">"))])
                except:
                    makers[brand]["models"][model]["specs"]["cam1video"] = 0
            if parsed.find("data-spec=\"cam2modules\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["cam2MP"] = int(
                        parsed[parsed.find(">") + 1:parsed.find(" MP")])
                except:
                    makers[brand]["models"][model]["specs"]["cam2MP"] = 0
            if parsed.find("data-spec=\"cam2video\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["cam2video"] = int(
                        parsed[parsed.find(">") + 1:parsed.find("p@")])
                except:
                    makers[brand]["models"][model]["specs"]["cam2video"] = 0
            if parsed.find(">Infrared port<") >= 0:
                makers[brand]["models"][model]["specs"]["radio"] = 1
            if parsed.find("data-spec=\"radio\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["radio"] = parsed[parsed.find(">") + 1:parsed.find("</")]
                except:
                    makers[brand]["models"][model]["specs"]["radio"] = 0
            if parsed.find("data-spec=\"usb\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["usb"] = parsed[parsed.find(">") + 1:parsed.find("</")]
                    if brand == "Apple":
                        makers[brand]["models"][model]["specs"]["usb"] = 1
                    elif makers[brand]["models"][model]["specs"]["usb"].find("mini") >= 0:
                        makers[brand]["models"][model]["specs"]["usb"] = 2
                    elif makers[brand]["models"][model]["specs"]["usb"].find("micro") >= 0:
                        makers[brand]["models"][model]["specs"]["usb"] = 3
                    else:
                        makers[brand]["models"][model]["specs"]["usb"] = 0
                except:
                    makers[brand]["models"][model]["specs"]["usb"] = 0
            if parsed.find("Fingerprint ") >= 0 or parsed.find("fingerprint ") >= 0:
                makers[brand]["models"][model]["specs"]["fingerprint"] = 1
            if parsed.find("nfc") >= 0 or parsed.find("Nfc") >= 0 or parsed.find("NFC") >= 0:
                makers[brand]["models"][model]["specs"]["nfc"] = 1
            if parsed.find("data-spec=\"price\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["price"] = int(
                    # parsed[parsed.find(">About ") + 7:parsed.find(" ", parsed.find(">About ") + 7)])
                    parsed[parsed.find(">About ") + 7:parsed.find("</")])
                except:
                    makers[brand]["models"][model]["specs"]["price"] = no_data
            if parsed.find("Basemark X: ") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["basemark"] = int(
                        parsed[parsed.find("Basemark X: ") + 12:parsed.find("</")])
                except:
                    makers[brand]["models"][model]["specs"]["basemark"] = 0
            if parsed.find(">Voice ") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["loudspeaker"] = float(
                        parsed[parsed.find(">Voice ") + 7:parsed.find("dB ")])
                except:
                    makers[brand]["models"][model]["specs"]["loudspeaker"] = 0
            if parsed.find("Crosstalk") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["audioquality"] = float(
                        parsed[parsed.find(">Noise -") + 8:parsed.find("dB ")])
                except:
                    makers[brand]["models"][model]["specs"]["audioquality"] = 0
            if parsed.find(">Endurance rating") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["endurance"] = int(
                        parsed[parsed.find(">Endurance rating ") + 18:parsed.find("h<")])
                except:
                    makers[brand]["models"][model]["specs"]["endurance"] = 0


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




