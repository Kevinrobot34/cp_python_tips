import argparse


def get_args():
    """This function manages the arguments in this main function"""

    # Define aguments
    parser = argparse.ArgumentParser()
    parser.add_argument('num', type=int, default=10**2)

    args = parser.parse_args()

    return args


def main():
    args = get_args()

    print(args.num)
    for i in range(args.num):
        print(i)


if __name__ == '__main__':
    main()
