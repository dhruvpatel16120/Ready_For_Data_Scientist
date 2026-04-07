import configparser
import os

def configparser_demo():
    print("--- Python Configuration Parsing (configparser) ---")
    
    config = configparser.ConfigParser()
    config_file = "settings.ini"

    # 1. Create a configuration structure (dictionary-like)
    config['DEFAULT'] = {
        'ServerAliveInterval': '45',
        'Compression': 'yes',
        'CompressionLevel': '9'
    }
    
    config['bitbucket.org'] = {}
    config['bitbucket.org']['User'] = 'hg'
    
    config['topsecret.server.com'] = {
        'Port': '50022',
        'ForwardX11': 'no'
    }

    # 2. Write to a file
    with open(config_file, 'w') as f:
        config.write(f)
    print(f"Created configuration file: {config_file}")

    # 3. Read from a file
    new_config = configparser.ConfigParser()
    new_config.read(config_file)

    print("\nReading data from INI file:")
    print(f"Sections found: {new_config.sections()}")
    
    print(f"User for bitbucket: {new_config['bitbucket.org']['User']}")
    print(f"Port for topsecret: {new_config.getint('topsecret.server.com', 'Port')}")
    print(f"Default Compression: {new_config['DEFAULT']['Compression']}")

    # Clean up
    # os.remove(config_file)
    
    print("\nConfigparser demo completed.\n")

if __name__ == "__main__":
    configparser_demo()
