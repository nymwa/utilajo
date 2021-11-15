def make_main(fn, parse_args = None):

    def main():
        try:
            if parse_args is None:
                fn()
            else:
                args = parse_args()
                fn(args)
        except BrokenPipeError:
            pass
        except KeyboardInterrupt:
            pass

    return main

