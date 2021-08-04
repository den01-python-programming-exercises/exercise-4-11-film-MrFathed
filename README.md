[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=5383245&assignment_repo_type=AssignmentRepo)
# Exercise 4.11 Film

Create a film class with the instance variables `name` and `age_rating`. Write the constructor `def __init__(self, film_name, film_age_rating)` for the class, and also the methods `def name(self)` and `def age_rating(self)`. The first of these returns the film title and the second returns its rating.

Below is an example use case of the class.

```python
chipmunks = Film("Alvin and the Chipmunks: The Squeakquel", 0)
age = int(input("How old are you?"))

if (age >= chipmunks.age_rating):
    print("You may watch the film " + chipmunks.name)
else:
    print("You may not watch the film " + chipmunks.name)
```

```plaintext
How old are you?
**7**
You may watch the film Alvin and the Chipmunks: The Squeakquel
```
