def count_vowels_consonants(text):
  vowels_list = ['A', 'E', 'I', 'O', 'U']
  consonants = 0
  vowels = 0
  for character in text:
    if character.isalpha():
      if character.upper() in vowels_list:
        vowels += 1
      else:
        consonants += 1
  return (vowels, consonants)