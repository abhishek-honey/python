import pyautogui
from playsound import playsound

# pyautogui.click(100, 100)

s = """

package test;

import java.util.HashSet;
import java.util.Set;

public class TwoPlusTwo {
	public static void main(String[] args) {
		int[] arr = new int[] { 1, 3, 5, 8, 7, 6 };
		int requiredSum = 8;

		getIntegerForSum(arr, requiredSum);
	}

	private static void getIntegerForSum(int[] arr, int requiredSum) {
		Set<Integer> differenceSet = new HashSet<>();
		for (int i = 0; i < arr.length; i++) {
			if (differenceSet.contains(arr[i])) {
				System.out.println(arr[i] + ", " + (requiredSum - arr[i]));
			} else {
				differenceSet.add(requiredSum - arr[i]);
			}
		}
	}
}
"""

# pyautogui.press(s)
pyautogui.countdown(5)
for c in s:
    pyautogui.typewrite(c)
    playsound('/Users/apple/code/github/python/keyboard.mp3')

# pyautogui.typewrite(s, interval=0.01)
