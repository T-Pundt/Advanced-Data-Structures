import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children;
    boolean isEndOfWord;

    public TrieNode() {
        children = new HashMap<>();
        isEndOfWord = false;
    }
}

class Trie {
    private TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    public void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            node.children.putIfAbsent(c, new TrieNode());
            node = node.children.get(c);
        }
        node.isEndOfWord = true;
    }

    public boolean search(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            if (!node.children.containsKey(c)) {
                return false;
            }
            node = node.children.get(c);
        }
        return node.isEndOfWord;
    }

    public List<String> findSuggestions(String prefix) {
        List<String> suggestions = new ArrayList<>();
        TrieNode node = root;
        for (char c : prefix.toCharArray()) {
            if (!node.children.containsKey(c)) {
                return suggestions;
            }
            node = node.children.get(c);
        }
        findSuggestionsHelper(node, prefix, suggestions);
        return suggestions;
    }

    private void findSuggestionsHelper(TrieNode node, String prefix, List<String> suggestions) {
        if (node.isEndOfWord) {
            suggestions.add(prefix);
        }
        for (char c : node.children.keySet()) {
            findSuggestionsHelper(node.children.get(c), prefix + c, suggestions);
        }
    }
}

//This is the dictionary where Trie is the type and dictionary is the name
public class SpellChecker {
    private Trie dictionary;

    public SpellChecker(String[] words) {
        dictionary = new Trie();
        for (String word : words) {
            dictionary.insert(word);
        }
    }

    public boolean isCorrect(String word) {
        return dictionary.search(word);
    }

    public List<String> getSuggestions(String word) {
        return dictionary.findSuggestions(word);
    }


    public static void main(String[] args) {
        String[] words = {"apple", "banana", "cherry", "date", "elderberry", "ban"};
        SpellChecker spellChecker = new SpellChecker(words);

        String[] testWords = {"apple", "ban", "cherr", "dat", "elderberr"};
        for (String word : testWords) {
            if (spellChecker.isCorrect(word)) {
                System.out.println(word + " is spelled correctly.");
            } else {
                List<String> suggestions = spellChecker.getSuggestions(word);
                System.out.println(word + " is misspelled. Suggestions: " + suggestions);
            }
        }
    }
}