import xml.dom.minidom
from ncclient import manager
import requests

def fetch_running_config1(host, port, username, password):
    try:
        with manager.connect(
            host=host,
            port=port,
            username=username,
            password=password,
            hostkey_verify=False,
        ) as m:

            netconf_filter = """
            <filter>
                <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
            </filter>
            """

            netconf_reply = m.get_config(source="running", filter=netconf_filter)

            pretty_config = xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml()
            print("Running Configuration:")
            print(pretty_config)

    except Exception as e:
        print(f"An error occurred (fetch_running_config1): {e}")

def change_hostname(host, port, username, password):
    try:
        with manager.connect(
            host=host,
            port=port,
            username=username,
            password=password,
            hostkey_verify=False,
        ) as m:

            netconf_edit = """
            <config>
                <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                    <hostname>cisco121</hostname>
                </native>
            </config>
            """

            m.edit_config(target="running", config=netconf_edit)

            print("Hostname changed to 'cisco121'")

    except Exception as e:
        print(f"An error occurred (change_hostname): {e}")

def change_ip_gigabit_ethernet(host, port, username, password):
    try:
        with manager.connect(
            host=host,
            port=port,
            username=username,
            password=password,
            hostkey_verify=False,
        ) as m:

            netconf_edit = """
            <config>
                <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                    <interface>
                        <GigabitEthernet>
                            <name>1</name>
                            <ip>
                                <address>
                                    <primary>
                                        <address>192.168.56.122</address>
                                        <mask>255.255.255.0</mask>
                                    </primary>
                                </address>
                            </ip>
                        </GigabitEthernet>
                    </interface>
                </native>
            </config>
            """

            m.edit_config(target="running", config=netconf_edit)

            print("IP address of GigabitEthernet1 changed to '192.168.56.122'")

    except Exception as e:
        print(f"An error occurred (change_ip_gigabit_ethernet): {e}")

def add_loopback(port, username, password):
    host="192.168.56.122"
    
    try:
        with manager.connect(
            host=host,
            port=port,
            username=username,
            password=password,
            hostkey_verify=False,
        ) as m:

            netconf_edit = """
            <config>
                <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                    <interface>
                        <Loopback>
                            <name>3</name>
                            <ip>
                                <address>
                                    <primary>
                                        <address>10.2.2.2</address>
                                        <mask>255.255.255.0</mask>
                                    </primary>
                                </address>
                            </ip>
                        </Loopback>
                    </interface>
                </native>
            </config>
            """

            m.edit_config(target="running", config=netconf_edit)

            print("Loopback1 added with IP address '10.2.2.2'")

    except Exception as e:
        print(f"An error occurred (add_loopback): {e}")

def fetch_running_config2(port, username, password):
    host="192.168.56.122"
    
    try:
        with manager.connect(
            host=host,
            port=port,
            username=username,
            password=password,
            hostkey_verify=False,
        ) as m:

            netconf_filter = """
            <filter>
                <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
            </filter>
            """

            netconf_reply = m.get_config(source="running", filter=netconf_filter)

            pretty_config = xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml()
            print("Running Configuration:")
            print(pretty_config)

    except Exception as e:
        print(f"An error occurred (fetch_running_config2): {e}")

def send_webex_message(token, room_id, message):
    api_url = "https://webexapis.com/v1/meetings"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "roomId": room_id,
        "text": message
    }

    response = requests.post(api_url, headers=headers, json=payload)

    if response.status_code == 200:
        print("Message sent successfully")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    host = "192.168.56.121"
    port = 830
    username = "cisco"
    password = "cisco123!"
    webex_token = "NzVkNGM1MzctYzc3My00NTMwLTk0NDQtYWEwOGI1NjE0ODVjMzUxYjkwMGEtMTBj_P0A1_d0b19fc5-a717-4064-90e2-8d88b3acad9c"
    webex_room_id = "14723988dbb24b1ea7b0b774c0fe145d"

    fetch_running_config1(host, port, username, password)
    change_hostname(host, port, username, password)
    change_ip_gigabit_ethernet(host, port, username, password)
    add_loopback(port, username, password)
    fetch_running_config2(port, username, password)
    
    message_text = "Changes have been made to the network configuration."
    send_webex_message(webex_token, webex_room_id, message_text)
