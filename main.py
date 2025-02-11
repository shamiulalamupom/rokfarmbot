import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con


def click(x, y):
    """Move the cursor to (x, y) and perform a left-click with a random delay."""
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(np.random.uniform(0.1, 0.3))  # Randomized click hold duration
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(np.random.uniform(1, 1.2))  # Randomized delay before the next action


def button_press(btn: str, iterations: int = 1):
    """Simulate key presses with random delays."""
    for _ in range(iterations):
        try:
            print(f"pressing {btn}")
            pyautogui.keyDown(btn)
            time.sleep(np.random.uniform(0.3, 0.5))
            print(f"releasing {btn}")
            pyautogui.keyUp(btn)
            time.sleep(np.random.uniform(1, 1.2))
        except Exception as e:
            print(e)


def scroll_a_bit():
    """Scroll the screen up and down to search for new nodes."""
    for _ in range(4):
        pyautogui.scroll(-1)
    pyautogui.scroll(1)
    pyautogui.scroll(-1)


def find_node() -> pyautogui.Point:
    """
    Continuously search for resource nodes on the screen
    until one is found, using images for detection.
    """
    while True:
        # Move the camera upward slightly to search for nodes
        pyautogui.keyDown('up')
        time.sleep(0.1)
        pyautogui.keyUp('up')
        time.sleep(np.random.uniform(4, 4.2))

        # Attempt to detect large, normal, or small nodes
        for image_name in ['gem_node_l.png', 'gem_node_ll.png']:
            try:
                node = pyautogui.locateCenterOnScreen(
                    f'images/{image_name}', grayscale=True, confidence=0.8
                )
                if node:
                    print(f"Node found: {image_name}")
                    return node
            except pyautogui.ImageNotFoundException:
                print("No node found.")
                continue

        # No node found, continue scanning


def main():
    """
    Main bot loop:
    - Press space if the map is visible.
    - Scroll the map to explore.
    - Locate a node and click it.
    """
    print("Bot started. Press 'q' to stop.")
    time.sleep(3)  # Delay before starting
    # button_press('r')
    # button_press('i')
    # button_press('s')
    # button_press('e')
    # button_press('space')
    # button_press('o')
    # button_press('f')
    # button_press('space')
    # button_press('k')
    # button_press('i')
    # button_press('n')
    # button_press('g')
    # button_press('d')
    # button_press('o', iterations=2)
    # button_press('m')
    

    while not keyboard.is_pressed('q'):  # Run until 'q' is pressed
        try:
            # Detect the map and press space if visible
            if pyautogui.locateCenterOnScreen('images/test.png', grayscale=True, confidence=0.8):
                print("Image found.")
                button_press('space')
        except pyautogui.ImageNotFoundException:
            print("Image not found")
            button_press('space', iterations=2)

        # Scroll the map to search for nodes
        scroll_a_bit()

        # Locate and click a node
        node_location = find_node()
        click(node_location.x, node_location.y)

        # Click on the center of a 1920x1080 window
        center_x, center_y = 1920 // 2, 1080 // 2
        click(center_x, center_y)

        # Wait after clicking the node
        time.sleep(np.random.uniform(10, 10.2))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Bot stopped.")
