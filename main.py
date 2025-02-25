import argparse
from agents.manager_agent import ManagerAgent
from workflows.press_kit_workflow import press_kit_workflow
from dotenv import load_dotenv

load_dotenv()

def main():
    parser = argparse.ArgumentParser(description="Press Kit Automatic Generation and Quality Review AI Agent.")

    parser.add_argument(
        'company_info',
        type=str,
        help="""Company name, flagship product/service, major achievements, brand attributes, etc.
                Example: "Tesla, Inc.; Flagship product: Electric vehicles; Achievements: Leading innovation in renewable energy." """
    )
    parser.add_argument(
        '-t', '--topic',
        type=str,
        default=None,
        required=True,
        help="""Press kit topic
                Example: "Launch of a new AI-driven analysis platform targeting global markets" """
    )
    parser.add_argument(
        '--tone',
        type=str,
        default="Professional",
        help="""Tone
                Example: "Professional" """
    )

    args = parser.parse_args()
    manager = ManagerAgent()
    press_kit_workflow(manager, args.company_info, args.topic, args.tone)

if __name__ == '__main__':
    main()

    # python .\main.py "Tesla, Inc.; Flagship product: Electric vehicles; Achievements: Leading innovation in renewable energy." -t "Launch of a new AI-driven analysis platform targeting global markets" --tone "Professional"