README


What circumstances may lead to false positives or false negatives when using solely this score?
  If a person forgets their password, they may register their IP address as a fraudulent. If someone
  happens to hack into another persons account, their IP address may be registered as LOGIN.

What challenges are there with computing distances based on latitude/longitude?
  There are challenges when the person travels across the globe for some time or moves.
  Then, their logins are more spread out so fraudulent attacks are harder to distinguish.
  Did the person simply forget their password a few times or is someone trying to hack into their account?


Further Considerations:
  The main issues I had while working on this challenge are the assumptions I made. To make sure I had some
  sort of running code, I made these assumptions for the time being. What should I do about IP addresses that
  overlap being FRAUD and LOGIN? If the person successfully logs in at some point in time and then someone
  else fails to hack into their account with the same IP address?

  Assumptions I made:
  FRAUD and LOGIN locations do not overlap. If an IP address is marked FRAUD, then it can't be marked LOGIN.


To use this program, run the input.py file. Then you will be prompted to input an IP address. Once you have
entered an IP address, press enter and a score will be printed. The program will continue running until it is
terminated. To edit the given IP addresses file, change IP.txt. The formal is "type(FRAUD/LOGIN) IP_ADDRESS"
