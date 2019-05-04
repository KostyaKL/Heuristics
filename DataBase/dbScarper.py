import pickle
import random
import requests
from time import gmtime, strftime, time

test = requests.get("https://www.gsmarena.com/alcatel-phones-f-5-0-p10.php")

url = "https://www.gsmarena.com/"

source = requests.get(url + "makers.php3")

makers = {}

not_connected = []


class ModelCount:
    count = 0
    models = 0
    acquired = 0

    def __init__(self):
        self.count = 0
        self.models = 0
        self.acquired = 0

    def count_inc(self):
        self.count += 1

    def count_reset(self):
        self.count = 0

    def models_add(self):
        self.models += self.count

    def acquired_inc(self):
        self.acquired += 1

    def get_count(self):
        return self.count

    def get_models(self):
        return self.models

    def get_acquired(self):
        return self.acquired


def save_obj(obj, name):
    with open(name + '.pkl', 'wb') as save_file:
        pickle.dump(obj, save_file, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    with open(name + '.pkl', 'rb') as load_file:
        return pickle.load(load_file)


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

            print(brand_name, brand_count, "at", strftime("%d-%m-%Y %H:%M:%S", gmtime()))

        if parsed == '<table>':
            table = True


def get_models(brand, model_count):
    if brand in not_connected:
        not_connected.remove(brand)
    model_count.count_reset()
    source = requests.get(makers[brand]["url"])
    model_class_found = False
    page_class_found = True
    work = False
    # print(brand, makers[brand]["count"], source)
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

                    print(brand, model_name, "at", strftime("%d-%m-%Y %H:%M:%S", gmtime()))
                    model_count.count_inc()

                    makers[brand]["models"][model_name] = {}
                    makers[brand]["models"][model_name]["url"] = model_url
                    makers[brand]["models"][model_name]["img"] = model_img
                    makers[brand]["models"][model_name]["specs"] = {}
                work = False

            if parsed == "<div class=\"nav-pages\">":
                page_class_found = True

            if parsed.find("<a class=") == 0 and page_class_found is True:
                next_page = parsed[(parsed.find("class=\"pages-next\" href=") + 25):(parsed.find("\" title=\"Ne"))]
                if parsed.find("disabled pages-next") >= 0:
                    page_class_found = False
                    break
                else:
                    source = requests.get(url + next_page)


def get_specs(brand, model, model_count):
    if brand + " " + model in not_connected:
        not_connected.remove(brand + " " + model)
    source = requests.get(makers[brand]["models"][model]["url"])

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
    makers[brand]["models"][model]["specs"][
        "os"] = 0  # 1 android, 2 apple, 3 microsoft, 4 blackberry, 5 firefox, 6 symbian, 0 other
    makers[brand]["models"][model]["specs"]["chipset"] = no_data
    makers[brand]["models"][model]["specs"]["cpu"] = 0
    makers[brand]["models"][model]["specs"]["gpu"] = no_data
    makers[brand]["models"][model]["specs"]["memoryslot"] = 0
    makers[brand]["models"][model]["specs"]["maxextmemory"] = 0
    makers[brand]["models"][model]["specs"]["RAM"] = 0
    makers[brand]["models"][model]["specs"]["cam1MP"] = 0
    makers[brand]["models"][model]["specs"]["cam1video"] = 0
    makers[brand]["models"][model]["specs"]["cam2MP"] = 0
    makers[brand]["models"][model]["specs"]["cam2video"] = 0
    makers[brand]["models"][model]["specs"]["ir"] = 0
    makers[brand]["models"][model]["specs"]["radio"] = 0
    makers[brand]["models"][model]["specs"]["usb"] = 0  # 1 type c/iphone, 2 mini, 3 micro, 0 else
    makers[brand]["models"][model]["specs"]["nfc"] = 0
    makers[brand]["models"][model]["specs"]["fingerprint"] = 0
    makers[brand]["models"][model]["specs"]["price"] = 0
    makers[brand]["models"][model]["specs"]["basemark"] = 0
    makers[brand]["models"][model]["specs"]["loudspeaker"] = 0
    makers[brand]["models"][model]["specs"]["audioquality"] = 0
    makers[brand]["models"][model]["specs"]["endurance"] = 0
    makers[brand]["models"][model]["specs"]["waterproof"] = 0

    specs_list_found = False
    ir = False
    for line in source.iter_lines():
        parsed = str(line, 'utf-8', 'ignore')

        if ir is True:
            ir = False
            try:
                if parsed.find("Yes") >= 0:
                    makers[brand]["models"][model]["specs"]["ir"] = 1
                else:
                    makers[brand]["models"][model]["specs"]["ir"] = 0
            except Exception as e:
                print(e, 1)
                makers[brand]["models"][model]["specs"]["ir"] = 0

        if parsed.find("<div id=\"specs-list\">") == 0:
            specs_list_found = True

        if parsed.find("<p class=\"note\">") == 0:
            break

        if parsed.find("batsize") >= 0:
            try:
                makers[brand]["models"][model]["specs"]["battery"] = int(
                    parsed[parsed.find("spec=\"batsize-hl\">") + 18:parsed.find("</span>")])
            except Exception as e:
                print(e,2)
                makers[brand]["models"][model]["specs"]["battery"] = 0

        if specs_list_found is True:
            if parsed.find("data-spec=\"year\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["year"] = int(parsed[parsed.find(">") + 1:parsed.find(",")])
                except Exception as e:
                    print(e,3)
                    makers[brand]["models"][model]["specs"]["year"] = 0
            if parsed.find("data-spec=\"dimensions\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["height"] = float(
                        parsed[parsed.find(">") + 1:parsed.find(" x ")])
                    parsed = parsed[parsed.find(" x ") + 3:]
                    makers[brand]["models"][model]["specs"]["width"] = float(parsed[:parsed.find(" x ")])
                except Exception as e:
                    print(e,4)
                    makers[brand]["models"][model]["specs"]["height"] = 0
                    makers[brand]["models"][model]["specs"]["width"] = 0
            if parsed.find("data-spec=\"weight\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["weight"] = float(
                        parsed[parsed.find(">") + 1:parsed.find(" g ")])
                except Exception as e:
                    print(e,5)
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
                    elif makers[brand]["models"][model]["specs"]["sim"].find("Single") >= 0 or \
                            makers[brand]["models"][model]["specs"]["sim"].find("Yes") >= 0:
                        makers[brand]["models"][model]["specs"]["numofsim"] = 1
                    else:
                        makers[brand]["models"][model]["specs"]["numofsim"] = 0
                except Exception as e:
                    print(e,6)
                    makers[brand]["models"][model]["specs"]["sim"] = no_data
            if parsed.find("data-spec=\"displaysize\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["displaysize"] = float(
                        parsed[parsed.find(">") + 1:parsed.find(" inches")])
                except Exception as e:
                    print(e,7)
                    makers[brand]["models"][model]["specs"]["displaysize"] = 0
            if parsed.find("data-spec=\"displayresolution\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["displayresolution"] = parsed[
                                                                                   parsed.find(">") + 1:parsed.find(
                                                                                       " pixels")]
                    try:
                        a = makers[brand]["models"][model]["specs"]["displayresolution"][
                            :makers[brand]["models"][model]["specs"]["displayresolution"].find(" x ")]
                        b = makers[brand]["models"][model]["specs"]["displayresolution"][
                            makers[brand]["models"][model]["specs"]["displayresolution"].find(" x ") + 3:]
                        makers[brand]["models"][model]["specs"]["displayresolution"] = int(a) * int(b)
                    except Exception as e:
                        print(e,8)
                        makers[brand]["models"][model]["specs"]["displayresolution"] = 0
                except Exception as e:
                    print(e,9)
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
                    elif makers[brand]["models"][model]["specs"]["os"].find("Firefox") >= 0:
                        makers[brand]["models"][model]["specs"]["os"] = 5
                    elif makers[brand]["models"][model]["specs"]["os"].find("Symbian") >= 0:
                        makers[brand]["models"][model]["specs"]["os"] = 6
                    else:
                        makers[brand]["models"][model]["specs"]["os"] = 0
                except Exception as e:
                    print(e,10)
                    makers[brand]["models"][model]["specs"]["os"] = 0
            if parsed.find("data-spec=\"chipset\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["chipset"] = parsed[parsed.find(">") + 1:parsed.find("</")]
                except Exception as e:
                    print(e,11)
                    makers[brand]["models"][model]["specs"]["chipset"] = no_data
            if parsed.find("data-spec=\"cpu\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["cpu"] = parsed[parsed.find(">") + 1:parsed.find("</")]
                    if makers[brand]["models"][model]["specs"]["cpu"].find("Deca") >= 0:
                        makers[brand]["models"][model]["specs"]["cpu"] = 10
                    elif makers[brand]["models"][model]["specs"]["cpu"].find("Octa") >= 0:
                        makers[brand]["models"][model]["specs"]["cpu"] = 8
                    elif makers[brand]["models"][model]["specs"]["cpu"].find("Hexa") >= 0:
                        makers[brand]["models"][model]["specs"]["cpu"] = 6
                    elif makers[brand]["models"][model]["specs"]["cpu"].find("Quad") >= 0:
                        makers[brand]["models"][model]["specs"]["cpu"] = 4
                    elif makers[brand]["models"][model]["specs"]["cpu"].find("Dual") >= 0:
                        makers[brand]["models"][model]["specs"]["cpu"] = 2
                    else:
                        makers[brand]["models"][model]["specs"]["cpu"] = 1
                except Exception as e:
                    print(e,12)
                    makers[brand]["models"][model]["specs"]["cpu"] = 0
            if parsed.find("data-spec=\"gpu\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["gpu"] = parsed[parsed.find(">") + 1:parsed.find("</")]
                except Exception as e:
                    print(e,13)
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
                            makers[brand]["models"][model]["specs"]["maxextmemory"] = \
                            makers[brand]["models"][model]["specs"]["memoryslot"][start + 5:end]
                            makers[brand]["models"][model]["specs"]["memoryslot"] = 1
                        else:
                            makers[brand]["models"][model]["specs"]["memoryslot"] = 1
                            makers[brand]["models"][model]["specs"]["maxextmemory"] = 0
                except Exception as e:
                    print(e,14)
                    makers[brand]["models"][model]["specs"]["memoryslot"] = 0
            if parsed.find("data-spec=\"internalmemory\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["RAM"] = parsed[parsed.find(">") + 1:parsed.find("</")]
                    makers[brand]["models"][model]["specs"]["RAM"] = int(makers[brand]["models"][model]["specs"]["RAM"][makers[brand]["models"][model]["specs"]["RAM"].find(", ", makers[brand]["models"][model]["specs"]["RAM"].find(" GB RAM") - 8) + 2:makers[brand]["models"][model]["specs"]["RAM"].find(" GB RAM")])
                    if makers[brand]["models"][model]["specs"]["RAM"] > 12:
                        makers[brand]["models"][model]["specs"]["RAM"] = 0
                except Exception as e:
                    print(e,15)
                    makers[brand]["models"][model]["specs"]["RAM"] = 0
            if parsed.find("data-spec=\"cam1modules\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["cam1MP"] = int(
                        parsed[parsed.find(">") + 1:parsed.find(" MP")])
                except Exception as e:
                    # print(e,16)
                    makers[brand]["models"][model]["specs"]["cam1MP"] = 0
            if parsed.find("data-spec=\"cam1video\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["cam1video"] = int(
                        parsed[parsed.find(">") + 1:parsed.find("p", parsed.find(">"))])
                except Exception as e:
                    # print(e,17)
                    makers[brand]["models"][model]["specs"]["cam1video"] = 0
            if parsed.find("data-spec=\"cam2modules\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["cam2MP"] = int(
                        parsed[parsed.find(">") + 1:parsed.find(" MP")])
                except Exception as e:
                    # print(e,18)
                    makers[brand]["models"][model]["specs"]["cam2MP"] = 0
            if parsed.find("data-spec=\"cam2video\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["cam2video"] = int(
                        parsed[parsed.find(">") + 1:parsed.find("p@")])
                except Exception as e:
                    # print(e,19)
                    makers[brand]["models"][model]["specs"]["cam2video"] = 0
            if parsed.find(">Infrared port<") >= 0:
                makers[brand]["models"][model]["specs"]["radio"] = 1
            if parsed.find(">Infrared port<") >= 0:
                ir = True
            if parsed.find("data-spec=\"radio\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["radio"] = parsed[parsed.find(">") + 1:parsed.find("</")]
                    if makers[brand]["models"][model]["specs"]["radio"].find("Radio") >= 0 or \
                            makers[brand]["models"][model]["specs"]["radio"].find("radio") >= 0:
                        makers[brand]["models"][model]["specs"]["radio"] = 1
                    else:
                        makers[brand]["models"][model]["specs"]["radio"] = 0
                except Exception as e:
                    print(e,20)
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
                except Exception as e:
                    print(e,21)
                    makers[brand]["models"][model]["specs"]["usb"] = 0
            if parsed.find("Fingerprint ") >= 0 or parsed.find("fingerprint ") >= 0:
                makers[brand]["models"][model]["specs"]["fingerprint"] = 1
            if parsed.find("nfc") >= 0 or parsed.find("Nfc") >= 0 or parsed.find("NFC") >= 0:
                makers[brand]["models"][model]["specs"]["nfc"] = 1
            if parsed.find("data-spec=\"price\"") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["price"] = parsed[
                                                                       parsed.find(">About ") + 7:parsed.find("</")]
                    price = parsed[parsed.find(">About ") + 7:parsed.find(" ", parsed.find(">About ") + 7)]
                    currency = makers[brand]["models"][model]["specs"]["price"]
                    if currency.find("USD") >= 0:
                        makers[brand]["models"][model]["specs"]["price"] = price
                    elif currency.find("EUR") >= 0:
                        makers[brand]["models"][model]["specs"]["price"] = int(price) * 1.12
                    elif currency.find("INR") >= 0:
                        makers[brand]["models"][model]["specs"]["price"] = int(price) * 0.014
                    else:
                        makers[brand]["models"][model]["specs"]["price"] = 0
                except Exception as e:
                    print(e,22)
                    makers[brand]["models"][model]["specs"]["price"] = 0
            if parsed.find("Basemark X: ") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["basemark"] = int(
                        parsed[parsed.find("Basemark X: ") + 12:parsed.find("</")])
                except Exception as e:
                    print(e,23)
                    makers[brand]["models"][model]["specs"]["basemark"] = 0
            if parsed.find(">Voice ") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["loudspeaker"] = float(
                        parsed[parsed.find(">Voice ") + 7:parsed.find("dB ")])
                except Exception as e:
                    print(e,24)
                    makers[brand]["models"][model]["specs"]["loudspeaker"] = 0
            if parsed.find("Crosstalk") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["audioquality"] = float(
                        parsed[parsed.find(">Noise -") + 8:parsed.find("dB ")])
                except Exception as e:
                    print(e,25)
                    makers[brand]["models"][model]["specs"]["audioquality"] = 0
            if parsed.find(">Endurance rating") >= 0:
                try:
                    makers[brand]["models"][model]["specs"]["endurance"] = int(
                        parsed[parsed.find(">Endurance rating ") + 18:parsed.find("h<")])
                except Exception as e:
                    print(e,26)
                    makers[brand]["models"][model]["specs"]["endurance"] = 0
            if parsed.find("water") >= 0 or parsed.find("Water") >= 0:
                makers[brand]["models"][model]["specs"]["waterproof"] = 1

    print(brand, model, "specs acquired at", strftime("%d-%m-%Y %H:%M:%S", gmtime()))
    model_count.acquired_inc()


# makers = load_obj("db")

print("scarper started at:", strftime("%d-%m-%Y %H:%M:%S", gmtime()))

start_time = time()

model_count = ModelCount()

get_brands()

print(strftime("%d-%m-%Y %H:%M:%S", gmtime()))

print("total number of models:", sum(int(makers[brand]["count"]) for brand in makers))

for brand in makers:
    for retry in range(0, 5):
        try:
            get_models(brand, model_count)
            model_count.models_add()
            break
        except Exception as e:
            print(e,27)
            print(brand, "not connected -------------------------------------->",
                  strftime("%d-%m-%Y %H:%M:%S", gmtime()))
            not_connected.append(brand)

print(strftime("%d-%m-%Y %H:%M:%S", gmtime()))

print("not connected:", not_connected)

print("expected", sum(int(makers[brand]["count"]) for brand in makers), "models, found", model_count.get_models())

save_obj(makers, "db")

for brand in makers:
    for model in makers[brand]["models"]:
        for retry in range(0, 5):
            try:
                get_specs(brand, model, model_count)
                break
            except Exception as e:
                print(e,28)
                print(brand, model, "not connected -------------------------------------->",
                      strftime("%d-%m-%Y %H:%M:%S", gmtime()))
                not_connected.append(brand + " " + model)

print(strftime("%d-%m-%Y %H:%M:%S", gmtime()))

print("not connected:", not_connected)

print("expected", sum(int(makers[brand]["count"]) for brand in makers), "models, number of models",
      model_count.get_models(), "acquired",
      model_count.get_acquired())

end_time = time()

total_time = end_time - start_time

print("scarper finished at", strftime("%d-%m-%Y %H:%M:%S", gmtime()))

print("worked for", strftime("%H:%M:%S", gmtime(total_time)))

save_obj(makers, "db")

with open('phoneDB.csv', 'w') as f:
    printout = "brand,model"
    rand_brand = random.choice(list(makers))
    rand_model = random.choice(list(makers[rand_brand]["models"]))
    for key in makers[rand_brand]["models"][rand_model]["specs"]:
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
