from trie import Trie

class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        if not strings:
            return ""

        for word in strings:
            self.put(word)

        current_node = self.root
        longest_common_prefix = ""
        while current_node and len(current_node.children) == 1 and current_node.value is None:
            char, next_node = next(iter(current_node.children.items()))
            longest_common_prefix += char
            current_node = next_node

        return longest_common_prefix


if __name__ == "__main__":
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    print(trie.find_longest_common_word(strings))  # "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    print(trie.find_longest_common_word(strings))  # "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    print(trie.find_longest_common_word(strings))  # ""
