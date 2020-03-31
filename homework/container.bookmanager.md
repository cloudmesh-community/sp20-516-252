# E.container.bookmanager.1

1. Make sure Docker is running
2. create an image using Makefile

```
$ git clone https://github.com/cyberaide/bookmanager.git
$ cd bookmanager
$ make image
```
Now use bookmanager to compile proceedings
```
$ mkdir -p cm/pub/docs
$ cd cm
$ git clone https://github.com/cloudmesh-community/book.git
$ git clone https://github.com/cyberaide/bookmanager.git
$ cd bookmanager
$ make image
$ make cm
```

Now we have cm container, run the command below
```buildoutcfg
 /cm# cd book
 /cm/book# cd books/cd 516-sp20/
 :/cm/book/books/516-sp20# time make proceedings
```
This will generate an epub book in the folder /cm/pub/docs.

# E.container.bookmanager.2

Remove all the sections not needed in the `e516-sp20-proceedings.yaml` file
, and verify that we can see our own chapter.

Before that, I created a pull request to add the links to our chapters to
 [this yaml file](https://github.com/cloudmesh-community/book/blob/master/books/516-sp20/e516-sp20-proceedings.yaml).
 
The edited yaml file I used to generate the book is in the same folder. See
 `homework/e516-sp20-proceedings.yaml`.
  