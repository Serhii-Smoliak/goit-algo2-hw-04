from trie import Trie

class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        if not isinstance(pattern, str):
            raise ValueError("Pattern must be a string.")
        
        if not pattern:
            return 0
        
        count = 0
        
        def dfs(node, current_word):
            nonlocal count
            if node.value is not None and current_word.endswith(pattern):
                count += 1
            for char, child_node in node.children.items():
                dfs(child_node, current_word + char)
        
        dfs(self.root, "")
        return count

    def has_prefix(self, prefix) -> bool:
        if not isinstance(prefix, str):
            raise ValueError("Prefix must be a string.")
        
        if not prefix:
            return False

        def dfs(node, current_word):
            if current_word.startswith(prefix):
                return True
            for char, child_node in node.children.items():
                if dfs(child_node, current_word + char):
                    return True
            return False
        
        return dfs(self.root, "")


if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    print(trie.count_words_with_suffix("e"))  # 1
    print(trie.count_words_with_suffix("ion"))  # 1
    print(trie.count_words_with_suffix("a"))  # 1
    print(trie.count_words_with_suffix("at"))  # 1

    print(trie.has_prefix("app"))  # True
    print(trie.has_prefix("bat"))  # False
    print(trie.has_prefix("ban"))  # True
    print(trie.has_prefix("ca"))  # True
