package day2.solution;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class Day_2 {

    public static void main(String[] args) {
        List<List<Long>> ranges = calculateRanges(input);
        System.out.println(ranges);

        long result = 0;
        Stack<Character> temp = new Stack<>();

        for (List<Long> range : ranges){
           for (long n = range.getFirst(); n <= range.getLast(); n++){
                String toTest = String.valueOf(n);
                long len = toTest.length();

               for (int q = 2; q <= len ; q++){
                   if (len % q != 0) {
                       continue;
                   }

                   for (long i = 0; i <= len / q - 1; i++) {
                       temp.push(toTest.charAt((int) i));
                   }

                   boolean isAtLeastDouble = true;
                   while (true) {
                       if (temp.isEmpty()) {
                           break;
                       } else if (temp.pop().equals(toTest.charAt((int) (len / 2 + temp.size())))) {
                           continue;
                       } else {
                           isAtLeastDouble = false;
                           break;
                       }
                   }

                   if (isAtLeastDouble) {
                       System.out.println(n);
                       result += n;
                   }
                   temp.removeAllElements();
               }

            }
        }

        System.out.println(result);
    }

    public static boolean isTopStackMultipleTimesInString(Stack<Character> stack, String toTest, int q){
        Character testChar = stack.pop();

        for (int mult = 0; mult < q; mult++){
            if(testChar.equals(toTest.charAt((stack.size()+1) + toTest.length()/q))){
                continue;
            }
            return false;
        }

        return true;
    }

    public static List<List<Long>> calculateRanges(String input) {
        List<List<Long>> result = new ArrayList<>();
        String[] splitInput = input.split(",");
        for (String range : splitInput){
            result.add(new ArrayList<>());
            for (String num : range.split("-")){
                result.getLast().add(Long.parseLong(num));
            }
        }
        return result;
    }

    static String input = "8284583-8497825,7171599589-7171806875,726-1031,109709-251143,1039-2064,650391-673817," +
            "674522-857785,53851-79525,8874170-8908147,4197684-4326484,22095-51217,92761-107689,23127451-23279882," +
            "4145708930-4145757240,375283-509798,585093-612147,7921-11457,899998-1044449,3-19,35-64,244-657," +
            "5514-7852,9292905274-9292965269,287261640-287314275,70-129,86249864-86269107,5441357-5687039,2493-5147,"+
            "93835572-94041507,277109-336732,74668271-74836119,616692-643777,521461-548256,3131219357-3131417388";
}