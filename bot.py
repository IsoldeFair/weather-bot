from argparse import ArgumentParser, RawDescriptionHelpFormatter
import sys
from bot.weather_bot import WeatherBot
from bot.tts import tts
from bot.asr import asr, list_mics

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

        parser.add_argument('-k', '--apikey', action='store', dest='apikey',
                            help='API key to OpenWeather')

        parser.add_argument('-n', '--no_asr', action='store_true', dest='no_asr')

        # Process arguments
        args = parser.parse_args()

        weather_check = WeatherBot("./grammars/weather.jsgf", args.apikey)

        selected_mic_id = None
        user_input = ""

        while user_input != "quit":
            if args.no_asr:
                user_input = input("Type your command: ")
            else:
                if not selected_mic_id:
                    mic_list = list_mics()
                    print(mic_list)
                    selected_mic_id = input("Please choose the mic number you want to use: ")
                user_input = asr(int(selected_mic_id))
            response = weather_check.response(user_input)
            print(response)
            tts(response)

    except KeyboardInterrupt:
        # handle keyboard interrupt ###
        return 0


if __name__ == "__main__":
    sys.exit(main())
