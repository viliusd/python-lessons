from argparse import Action, ArgumentParser
import time

known_drivers = ['local', 's3']

class DriverAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        if driver.lower() not in known_drivers:
            parser.error("Unknjown driver. avialable drivers are 'local' and 's3' ")
        namespace.driver = driver.lower()
        namespace.destination = destination

def create_parser():
    parser = ArgumentParser()
    parser.add_argument('url', help="URL postgress database to backup")
    parser.add_argument('--driver', '-d',
                help="how and where to store backup",
                nargs=2,
                action=DriverAction,
                metavar=('driver','destination'),
                required=True)
    return parser

def main():
    import boto3
    from pgbackup import pgdump, storage
    
    args = create_parser().parse_args()
    dump = pgdump.dump(args.url)
    if args.driver == 's3':
        client = boto3.client('s3')
        timestamp = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())
        file_name = pgdump.dump_file_name(args.url, timestamp)
        print(f"Backing database up locally to {args.destination} in S3 as {file_name}")
        storage.s3(client, dump.stdout, args.destination, file_name)
    else:
        outfile = open(args.destination, 'wb')
        storage.local(dump.stdout, outfile)