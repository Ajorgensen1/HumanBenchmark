import pyautogui

def main():
    # Coordinates to look at/click, change to your needs
    x, y = 1196, 414
    # Click to start game
    pyautogui.click(x, y)
    # Game runs for five rounds
    for i in range(5):
        # Continue until round is over
        while True:
            # Take screenshot of screen and check if pixel is green
            screenshot = pyautogui.screenshot()
            current_green_val = screenshot.getpixel((x,y))[1]
            # If pixel is green, click
            if current_green_val > 100:
                pyautogui.click(x, y)
                break
        pyautogui.click(x,y)

if __name__ == "__main__":
    main()        
                     
