class Solution {
    public boolean checkIfPangram(String sentence) {
        Map<Character, Integer> letterCount = new HashMap<>();
        for(char ch:sentence.toLowerCase().toCharArray()){
            if(ch>='a' && ch<='z'){
                if(letterCount.containsKey(ch)){
                    int oldCount = letterCount.get(ch);
                    letterCount.put(ch, oldCount+1);
                }
                else{
                    letterCount.put(ch, 1);
                }
            }
        }
    return letterCount.size() == 26;
    }
}