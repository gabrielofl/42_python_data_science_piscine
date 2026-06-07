from time import strftime, time, gmtime

seconds = time()
date_str = strftime('%B %-d, %Y', gmtime(0))

print(f"Seconds since {date_str}: {seconds:,.4f} or {seconds:.2e} in scientific notation\n{strftime('%b %-d %Y', gmtime())}")

#January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
#Oct 21 2022$
