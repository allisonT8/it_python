
def banner(subject, author):
    subject_length = len(subject)
    by_line = f"By {author}"
    banner_length = max(subject_length, by_line_length)
    print(f"{'=' * banner_length}")
    print(f"{subject:^{banner_length}}")
    print(f"{by_line:^{banner_length}}")
    print(f"{'=' * banner_length}")
    print("")

if __name__ = "__main__":
    banner("BANNER", "Allison.T")
    subject = input("What's the suject?")
    author = input("Who's the author?")
    banner(subject,author)
