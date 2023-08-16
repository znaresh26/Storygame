#IMPORT LIBRARIES
import random

#ENTER YOUR DETAILS
Hero=input("Enter your Name: ")
Age=input("Enter your age: ")
Place=input("Enter your Place: ")

#MINI STORIES
story1=f"""
The Curious Pocket Watch:
In an antique shop at {Place}, young {Hero} stumbled upon a pocket watch that seemed to glow with an otherworldly light. Little did she know, the watch held the essence of a time-traveling inventor named Alexander. With each turn of the gears, {Hero} and Alexander journeyed through time, facing challenges that tested their bond."""
story2=f"""
The Whispering Grove:
In the heart of the Whispering Grove lived an ancient tree named {Hero}, who possessed the power to communicate with animals. When a group of young explorers sought her guidance, {Hero} granted them enchanted pendants that allowed them to understand and protect the creatures of the forest of {Place}."""
story3=f"""
The Masked Ball Masquerade:
In a grand mansion of {Place}, the annual Masked Ball Masquerade was a mysterious affair. Among the attendees, a charming thief named {Hero} stole more than just hearts. When he swiped an ornate key pendant, he unknowingly unlocked a hidden chamber containing a map to untold treasures."""
story4=f"""
The Clockwork Companions:
In a world where robotic companions were the norm, a lonely inventor named {Hero} created a clockwork bird named Percival. When Percival unexpectedly gained the ability to speak, he and {Hero} embarked on a journey to find the mythical Source of Voices, where all sentient machines originated."""
story5=f"""
The Celestial Compass:
{Hero}, a determined stargazer, stumbled upon a compass that pointed not to north, but to the constellations. With it, she unraveled the cosmic secrets of an ancient civilization at {Place}, uncovering a connection between the stars and a long-lost artifact that could reshape the world."""
story6=f"""
The Crystal Chronicles:
In the Kingdom of {Place}, Princess {Hero} possessed a crystal amulet that could record and replay memories. When a dark sorcerer threatened the kingdom, {Hero}'s amulet became the key to unearthing forgotten spells and uncovering the truth behind a generations-old curse."""
story7=f"""
The Scent of Enchantment:
In a bustling bazaar of {Place}, a perfumer named {Hero} crafted scents that held magical properties. When a wandering minstrel named Elara encountered one of {Hero}'s enchanting fragrances, she found herself able to communicate with her beloved cat and unearth a hidden realm of animal magic."""
story8=f"""
The Mechanical Marionette:
In a city ruled by technology, a gifted puppeteer named {Hero} created a mechanical marionette named Elise. When Elise's movements began to mimic human emotions, {Hero} realized he had inadvertently brought a sentient being to life, sparking a debate about the rights of artificial intelligence."""
story9=f"""
The Cursed Quill:
In an old library of {Place}, a struggling writer named {Hero} discovered a quill rumored to grant great storytelling abilities—at a steep price. With each tale he penned, {Hero}'s own life unraveled, and he raced against time to break the curse before his own story reached a tragic end."""
story10=f"""
The Elemental Medallions:
In a land where elemental magic ruled, four individuals from different walks of life—Aria, Zephyr, Terra, and {Hero}—uncovered medallions that granted them control over wind, earth, fire, and water. Together, they embarked on a quest to restore harmony to their realm, battling dark forces seeking to exploit their powers to save {Place}."""

#RANDOMLY PICKING A STORY
stories=[story1,story2,story3,story4,story5,story6,story7,story8,story9,story10]

#DISPLAYING THE STORY
print(random.choice(stories))
