public class Main {

    public static boolean safeEqual(String a, String b) {
        if (a.length() != b.length()) {
            return false;
        }

        int equal = 0;

        for (int i = 0; i < a.length(); i++) {
            equal |= a.charAt(i) ^ b.charAt(i);
        }

        return equal == 0;
    }

    public static void main(String[] args) {
        String input = "abdd";
        String correct = "abcd";
        System.out.println(safeEqual(input, correct));

        int a = 5;
        int b = 2;
        b ^= a;

        System.out.print(b);
    }
}