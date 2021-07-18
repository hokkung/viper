import click
import signal
import sys
from processor.processor import Processor

def signal_handler(signo: int) -> None:
    sys.exit()

def init_sentry(env: str) -> None:
    pass

def init_logger() -> None:
    pass

def init_server() -> None:
    Processor.run()

@click.command()
@click.option("--env", required=True)
def app() -> None:
    signal.signal(signal.SIGTERM, signal_handler)

    init_sentry()
    init_logger()
    init_server()

if __name__ == "__main__":
    app()
