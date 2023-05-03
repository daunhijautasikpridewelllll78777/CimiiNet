import colorama
import time
import re
import os

print("[KarssDev] Loading Banner System...")


def _str_to_tuple(string: str) -> tuple:
  '''
        Turns a string into an Tuple
        '''
  x = string.split(',' if ',' in string else '/')
  return (x[0], x[1], x[2])


def _tfx_fade(start: str,
              end: str,
              text: str,
              ignore: bool = False,
              text_color: str = "\033[0m") -> str:
  '''
        Helper function for the _fade function
        '''
  start = _str_to_tuple(start)
  end = _str_to_tuple(end)

  return _fade(start, end, text, ignore, text_color)


print("[KarssDev] Added fade.init() to Banner System")


def _fade(start: tuple,
          end: tuple,
          text: str,
          ignore_alpha: bool = False,
          text_color: str = "\033[0m") -> str:
  '''
        Gives a line of text a cool ANSI fade
        '''
  result = ""

  changer = int((int(end[0]) - int(start[0])) / len(text))
  changeg = int((int(end[1]) - int(start[1])) / len(text))
  changeb = int((int(end[2]) - int(start[2])) / len(text))
  r, g, b = int(start[0]), int(start[1]), int(start[2])

  for letter in text:
    if letter == "\n":  # don't bother fading newlines
      pass

    if ignore_alpha:
      if letter.isalpha() or letter.isnumeric():
        result += text_color + letter

        r += changer
        g += changeg
        b += changeb
        continue

    result += "\x1b[40;38;2;%s;%s;%sm%s\033[0m" % (r, g, b, letter
                                                   )  # ANSI escape sequence
    r += changer
    g += changeg
    b += changeb

  return result


print("[KarssDev] Added fade.fade() to Banner System")


def parse_in_fader(banner: str,
                   target="",
                   t_port="",
                   t_ip="",
                   t_method="",
                   username="",
                   plan="",
                   expire="",
                   cons="",
                   maxtime=""):
  #remove the colors
  banner = banner.replace("<<red>>", "").replace("<<green>>", "").replace(
    "<<yellow>>",
    "").replace("<<blue>>", "").replace("<<magenta>>", "").replace(
      "<<cyan>>", "").replace("<<white>>", "").replace("<<reset>>", "")
  #parse the vars but they are in ::var:: format
  banner = banner.replace("::target::", target).replace(
    "::port::",
    t_port).replace("::ip::", t_ip).replace("::method::", t_method).replace(
      "::username::", username).replace("::plan::", plan).replace(
        "::expire::", expire).replace("::cons::",
                                      cons).replace("::maxtime::", maxtime)


print("[KarssDev] Added parse.parse_in_fader() to Banner System")


def parse_only_vars(banner: str,
                    target="",
                    t_port="",
                    t_ip="",
                    t_method="",
                    username="",
                    plan="",
                    expire="",
                    cons="",
                    maxtime=""):
  #remove the colors
  banner = banner.replace("<<red>>", "").replace("<<green>>", "").replace(
    "<<yellow>>",
    "").replace("<<blue>>", "").replace("<<magenta>>", "").replace(
      "<<cyan>>", "").replace("<<white>>", "").replace("<<reset>>", "")
  #parse the vars
  banner = banner.replace("<<target>>", target).replace(
    "<<port>>",
    t_port).replace("<<ip>>", t_ip).replace("<<method>>", t_method).replace(
      "<<username>>", username).replace("<<plan>>", plan).replace(
        "<<expire>>", expire).replace("<<cons>>",
                                      cons).replace("<<maxtime>>", maxtime)
  return banner.replace("<>", "")  #remove the <> from the vars


print("[KarssDev] Added parse.parse_only_vars() to Banner System")


def parse_banner(banner: str,
                 target="",
                 t_port="",
                 t_ip="",
                 t_method="",
                 username="",
                 plan="",
                 expire="",
                 cons="",
                 maxtime="",
                 network="",
                 sec=""):
  #parse the vars
  banner = banner.replace("<<target>>", target).replace(
    "</Network/>",
    network).replace("<<port>>", t_port).replace("<<time>>", sec).replace(
      "<<ip>>", t_ip).replace("<<method>>", t_method).replace(
        "<<username>>", username).replace("<<plan>>", plan).replace(
          "<<expire>>", expire).replace("<<cons>>",
                                        cons).replace("<<maxtime>>", maxtime)
  #parse the colors
  banner = banner.replace("<<red>>", colorama.Fore.RED).replace(
    "<<green>>",
    colorama.Fore.GREEN).replace("<<yellow>>", colorama.Fore.YELLOW).replace(
      "<<blue>>", colorama.Fore.BLUE).replace(
        "<<magenta>>",
        colorama.Fore.MAGENTA).replace("<<cyan>>", colorama.Fore.CYAN).replace(
          "<<white>>", colorama.Fore.WHITE).replace("<<reset>>",
                                                    colorama.Fore.RESET)
  #parse the effects
  banner = banner.replace("<<bold>>", colorama.Style.BRIGHT).replace(
    "<<reset>>", colorama.Style.RESET_ALL)
  #parse special chars
  banner = banner.replace("<<newline>>", "\n").replace("<<same_line>>", "\r")
  #parse clearing chars
  banner = banner.replace("<<clear_line>>", "[K").replace(
    "<<clear_screen>>", "[2J").replace("<<clear_all>>", "[2J[1;1H")
  #parse vars in ::var:: format
  banner = banner.replace("::target::", target).replace(
    "::port::",
    t_port).replace("::ip::", t_ip).replace("::method::", t_method).replace(
      "::username::", username).replace("::plan::", plan).replace(
        "::expire::", expire).replace("::cons::",
                                      cons).replace("::maxtime::", maxtime)
  #parse the fade effect between <<fade>> and </fade>
  banner = re.sub(r'<<fade:(.*?)>>(.*?)<</fade:(.*?)>>',
                  lambda m: _tfx_fade(m.group(1), m.group(3), m.group(2)),
                  banner).replace("<>", "")
  #parse the fade effect between <<fade>> and </fade> but with the fade in the middle
  banner = re.sub(
    r'<<fade2:(.*?)>>(.*?)<</fade2:(.*?)>>(.*?)<</fade2:(.*?)>>',
    lambda m: _tfx_fade(m.group(1), m.group(3), m.group(2)) + _tfx_fade(
      m.group(3), m.group(5), m.group(4)), banner).replace("<>", "")
  return banner.replace("<>",
                        "")  #clean up the leftover <> from something wrong XD


print("[KarssDev] Added parse.parse_banner() to Banner System")
print(
  "Finished loading Banner System | Thanks for using KarssDev's Banner System!")
