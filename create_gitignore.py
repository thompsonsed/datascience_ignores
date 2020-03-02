import logging
import pathlib
import argparse


def read_default_data() -> str:
    """
    Reads the default data from *default_ignores*

    :return: the default ignore data
    """
    default_ignores_path = pathlib.Path(pathlib.Path(__file__).parent, "default_ignores")
    if not default_ignores_path.exists():
        raise FileNotFoundError(f"Default ignores template file not found at {default_ignores_path.absolute()}.")
    with default_ignores_path.open("r") as d_path:
        return d_path.read()


def check_existing_defaults(gitignore_path: pathlib.Path) -> bool:
    """
    Checks if the existing gitignore has the defaults already.

    If the gitignore path does not exist, returns false.

    Checks for the following pattern:

    ############################
    # Start of default ignores #
    ############################

    :param gitignore_path: the path of the existing .gitignore file.
    :return: true if the defaults already exist.
    """
    if gitignore_path.exists():
        expected_pattern = (
            """############################\n# Start of default ignores #\n############################\n"""
        )
        with gitignore_path.open("r") as git_file:
            return expected_pattern in git_file.read()
    return False


def main():
    """Runs the argument parsing and creation of the gitignore."""
    args = argparse.ArgumentParser(description="Create or add to an existing .gitignore with data science defaults.")
    args.add_argument(
        "-d",
        dest="dest_path",
        required=False,
        action="store",
        help="The path to the new .gitignore file, or the directory in which to create the new .gitignore file (default, current directory)",
        default=None,
    )
    args.add_argument("-v", dest="verbose", action="store_true", help="Provide verbose logging.", default=False)
    p_args = args.parse_args()
    if p_args.verbose:
        logging.getLogger().setLevel(20)
    else:
        logging.getLogger().setLevel(40)
    if p_args.dest_path is None:
        dest_path = pathlib.Path(".gitignore")
        logging.info("No destination path provided, using current working directory.")
        logging.info(f"Writing to {dest_path.absolute()}")
    else:
        dest_path = pathlib.Path(p_args.dest_path)
        if dest_path.is_dir():
            dest_path = pathlib.Path(dest_path, ".gitignore")
        logging.info(f"Writing to destination .gitignore at {dest_path}.")
        if not dest_path.parent.exists():
            raise IOError(f"Directory does not exist at {dest_path.parent}")
    if check_existing_defaults(dest_path):
        logging.info(f"Defaults already exist in {dest_path}, exiting")
    else:
        with dest_path.open("a") as d_path:
            d_path.write(read_default_data())
        logging.info(f".gitignore defaults written to {dest_path}.")


if __name__ == "__main__":
    main()
