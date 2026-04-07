import logging

def logging_demo():
    print("--- Python Logging Module ---")
    
    # Configure basic logging
    # Levels: DEBUG < INFO < WARNING < ERROR < CRITICAL
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename='app.log', # Logs will be written to this file
        filemode='w'        # 'w' for overwrite, 'a' for append
    )

    # Creating a logger
    logger = logging.getLogger("LibraryDemo")

    print("Logging messages at different levels...")
    logger.debug("This is a debug message (diagnostic info)")
    logger.info("This is an info message (confirmation of operation)")
    logger.warning("This is a warning (indicator of something unexpected)")
    logger.error("This is an error (problem occurred)")
    logger.critical("This is a critical error (program may stop)")

    print("Check 'app.log' in the current directory to see the output.")

    # Logging exceptions
    try:
        1 / 0
    except ZeroDivisionError:
        logger.exception("We caught an exception!")

    print("\nLogging demo completed.\n")

if __name__ == "__main__":
    logging_demo()
