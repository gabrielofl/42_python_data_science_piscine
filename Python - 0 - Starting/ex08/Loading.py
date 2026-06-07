import time
import os


def ft_tqdm(lst: range) -> None:
    """ft_tqdm(range) -> None
        Progress bar
        Implementation of tqdm function."""

    total = len(lst)
    start_time = time.time()

    blocks = [' ', '▏', '▎', '▍', '▌', '▋', '▊', '▉', '█']

    for i, item in enumerate(lst):
        now = time.time()
        elapsed = now - start_time
        it_per_sec = (i + 1) / elapsed if elapsed > 0 else 0
        eta = (total - (i + 1)) / it_per_sec if it_per_sec > 0 else 0

        try:
            width = os.get_terminal_size().columns
        except OSError:
            width = 80

        percent = (i + 1) / total
        bar_width = width - 45
        filled_total = bar_width * percent
        filled_chars = int(filled_total)

        bar = '█' * filled_chars + blocks[int((filled_total
                                               - filled_chars) * 9)]
        bar = bar.ljust(bar_width)

        print(f"\r{percent:3.0%}|{bar}| {i+1}/{total} \
              [{elapsed:02.0f}<{eta:02.0f}, {it_per_sec:.2f}it/s]",
              end="", flush=True)

        yield item

    print()
