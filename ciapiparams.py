#!/usr/bin/python

import argparse
import jenkinsapi
from jenkinsapi.jenkins import Jenkins

def main():
    parser = argparse.ArgumentParser(description='ciapiparams - get build parameters from build number')
    parser.add_argument('build_number', type=int, help="Build number, i.e. 28945")
    args = parser.parse_args()

    print "build_number: {}".format(args.build_number)

    j = Jenkins('http://ci.suse.de')
    job = j.get_job("openstack-mkcloud")
    build = job.get_build(args.build_number)
    parameters = build.get_actions()['parameters']

    for parameter in parameters:
        if isinstance(parameter['value'], bool):
            if parameter['value']:
                value="1"
            else:
                value="0"
        else:
            value=parameter['value']

        print "export " + parameter['name'] + "=\"" + value + "\""
    

if __name__ == '__main__':
    main()

