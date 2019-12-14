import datetime
import xml.etree.ElementTree as ET

def parseXML(xmlfile):

    tree = ET.parse(xmlfile)

    root = tree.getroot()

    blogposts = []

    for item in root.findall('./PostItem'):
        # for child in item:
        #     print(child.tag)
        if item.find('type').text == 'Text':
            # print(item)
            post = {}
            post['title'] = item.find('title').text
            post['date'] = item.find('publishTime').text
            post['category'] = None
            post['content'] = item.find('content').text

            blogposts.append(post)

    return blogposts


def create_md_files(blog_list):
    for blog in blog_list:
        with open("./content/{}.md".format(blog['title'].replace('.', '_').replace("'", '_').replace('?', '_')), 'w', encoding='utf-8') as f:
            f.write("Title: {}\n".format(blog['title']))
            f.write("Date: {}\n".format(parse_timestamp(int(blog['date']))))
            f.write("\n")
            f.write("{}\n".format(blog['content']))

def process():
    create_md_files(parseXML("LOFTER-North Shore-2019.10.28.xml"))
    create_md_files(parseXML("LOFTER-methodology-2019.10.28.xml"))

def parse_timestamp(timestamp):
    # lofter timestamp 1197115140190 should multiple 0.001
    value = datetime.datetime.fromtimestamp(timestamp*0.001)
    exct_time = value.strftime('%Y-%m-%d %H:%M')
    return exct_time

if __name__ == "__main__":
    process()
