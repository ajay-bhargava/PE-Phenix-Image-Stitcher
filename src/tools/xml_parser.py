'''
def parse_phenix_xml(xml_path):
    This is an internal function to parse XML files from the output of a database from perkinelmer
    This function can be improved to split by position or time (which isn't included right now)

    By: Ajay Bhargava
    Last Edit: 03/03/19
    
'''


def parse_phenix_xml(xml_path):
    import os, re
    from collections import defaultdict
    from xml.etree import ElementTree as ET

    # Open XML

    with open(xml_path, "rt") as f:
        tree = ET.parse(f)
        root = tree.getroot()

    # Get all the elements of the XML

    well_elements = root.findall('{http://www.perkinelmer.com/PEHH/HarmonyV5}Wells/{http://www.perkinelmer.com/PEHH/HarmonyV5}Well')
    id_elements = root.findall('{http://www.perkinelmer.com/PEHH/HarmonyV5}Images/{http://www.perkinelmer.com/PEHH/HarmonyV5}Image/{http://www.perkinelmer.com/PEHH/HarmonyV5}id')
    url_elements = root.findall('{http://www.perkinelmer.com/PEHH/HarmonyV5}Images/{http://www.perkinelmer.com/PEHH/HarmonyV5}Image/{http://www.perkinelmer.com/PEHH/HarmonyV5}URL')

    # Start building the parsable dictionary from the files using list - comprehension

    id_elements_list = [id_elements[i].text for i, num in enumerate(id_elements)]
    url_elements_list = [url_elements[i].text for i, num in enumerate(url_elements)]
    lookup_dict = dict(zip(id_elements_list, url_elements_list))
    id_keys = [value for found in root.iterfind('{http://www.perkinelmer.com/PEHH/HarmonyV5}Plates/{http://www.perkinelmer.com/PEHH/HarmonyV5}Plate/{http://www.perkinelmer.com/PEHH/HarmonyV5}Well') for i, value in found.items()]
    id_files = [[value.attrib['id'] for value in well_elements[i].findall('{http://www.perkinelmer.com/PEHH/HarmonyV5}Image')] for i, data in enumerate(well_elements)]

    # Replace ID's with file-paths for each file in each well

    def convert(l, d):
        return [convert(x, d) if isinstance(x, list) else d.get(x, x) for x in l]

    id_file_urls = convert(id_files, lookup_dict)

    # Create semi-finished dictionary ready to be parsed

    parsing_dictionary = dict(zip(id_keys, id_file_urls))

    # Split nested level dictionary by channel if the channel exists.

    def channel_extractor(my_string):
        my_string = my_string.split('-')[1][:3]
        return my_string

    img_dictionary = {}

    # Finally, assemble it all together as a neatly nested dictionary

    for key, value in parsing_dictionary.items():
        anything = {}
        ch_list = [channel_extractor(x) for x in value]
        for ch in set(ch_list):
            # list comprehension step where, a new key, value pair is created after each position of ch1-3 is determined from each key in parsing_dictionary
            anything[ch] = [value[index] for index, item in enumerate(ch_list) if item == ch]
        img_dictionary[key] = anything

    return img_dictionary
# Finished Function.
