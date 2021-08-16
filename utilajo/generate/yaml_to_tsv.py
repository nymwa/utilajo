import sys
import yaml

def main():
    yml = yaml.safe_load(sys.stdin)

    for hypos_dict in yml:
        hypos = hypos_dict['hypos']
        source = hypos_dict['source']
        for sent in hypos:
            text = sent['text']
            print(source + '\t' + text)

