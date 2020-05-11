from argparse import ArgumentParser, RawDescriptionHelpFormatter
import sys
from bot.weather_bot import WeatherBot

__version__ = '0.1.0'

def main(argv=None):
    '''Command line options.'''

    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

    try:
        # Setup argument parser
        parser = ArgumentParser(formatter_class=RawDescriptionHelpFormatter)

        parser.add_argument('-v', '--version', action='version',
                            version=__version__)

        # Process arguments
        args = parser.parse_args()

        weather_check = WeatherBot("./grammars/weather.jsgf")

        user_input = ""
        while user_input != "quit":
            user_input = input("Type your command:")
            response = weather_check.response(user_input)
            print(response)

    except KeyboardInterrupt:
        # handle keyboard interrupt ###
        return 0


if __name__ == "__main__":
    sys.exit(main())
