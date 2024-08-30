class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> str = new ArrayList<>();
        String value = "";
        for (int i=1; i <=n; i++){
            value = "";
            if (i%3 == 0 && i%5 ==0)
                value = "FizzBuzz";
            else if (i%3 == 0)
                value = "Fizz";
            else if (i%5 == 0)
                value = "Buzz";
            else
                value = String.valueOf(i);
            str.add(value);
        }
        return str;
    }
}