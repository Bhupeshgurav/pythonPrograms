def hacker_speak(string):
    result = string.replace("a", "4").replace("e", "3").replace(
        "i", "1").replace("0", "0").replace("s", "5")
    return result


print(hacker_speak("hello"))
