import argparse
from proxy_server import run_server, empty_cache

def main():
    #Getting all the arguments from the command line
    parser = argparse.ArgumentParser(description="Caching proxy CLI")
    parser.add_argument("--port", type=int, required=False, help="Port number")
    parser.add_argument("--origin", required=False, help="Origin server URL")
    parser.add_argument("--clear-cache", action="store_true", help="Clear the cache")

    args = parser.parse_args()

    if args.clear_cache:
        #clear the cache
        empty_cache()
    else:
        #run the caching server
        run_server(args.port, args.origin)


if __name__ == "__main__":
   main()