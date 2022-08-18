

Java example -  README.md - apache, gson, java, json, license, maven











alvinalexander.com | career | drupal | java | mac | mysql | perl | scala | uml | unix


	 
    



















Java example source code file (README.md)

This example Java source code file (README.md) is included in the alvinalexander.com
"Java Source Code
Warehouse" project. The intent of this project is to help you "Learn
Java by Example" TM.
Learn more about this Java project at its project page.



Java - Java tags/keywords

allow, apache, generics, google, gson, java, json, license, maven, this, unless, you



The README.md Java example source code

# google-gson

[![Build Status](https://travis-ci.org/google/gson.svg?branch=master)](https://travis-ci.org/google/gson)
[![Maven Central](https://maven-badges.herokuapp.com/maven-central/com.google.code.gson/gson/badge.svg)](https://maven-badges.herokuapp.com/maven-central/com.google.code.gson/gson)
[![Javadoc](https://javadoc-emblem.rhcloud.com/doc/com.google.code.gson/gson/badge.svg)](http://www.javadoc.io/doc/com.google.code.gson/gson)

Gson is a Java library that can be used to convert Java Objects into their JSON representation. It can also be used to convert a JSON string to an equivalent Java object.
Gson can work with arbitrary Java objects including pre-existing objects that you do not have source-code of. 

There are a few open-source projects that can convert Java objects to JSON. However, most of them require that you place Java annotations in your classes; something that you can not do if you do not have access to the source-code. Most also do not fully support the use of Java Generics. Gson considers both of these as very important design goals. 

###*Gson Goals*
  * Provide simple `toJson()` and `fromJson()` methods to convert Java objects to JSON and vice-versa
  * Allow pre-existing unmodifiable objects to be converted to and from JSON
  * Extensive support of Java Generics
  * Allow custom representations for objects
  * Support arbitrarily complex objects (with deep inheritance hierarchies and extensive use of generic types)

###*Gson Download and Maven*
  * [Gson Download](https://maven-badges.herokuapp.com/maven-central/com.google.code.gson/gson) downloads at Maven Central
  * For Maven check "Dependency Information" tab, on the left side.

###*Gson Documentation*
  * Gson [API](http://www.javadoc.io/doc/com.google.code.gson/gson): Javadocs for the current Gson release
  * Gson [user guide](https://github.com/google/gson/blob/master/UserGuide.md): This guide contains examples on how to use Gson in your code.
  * Gson [Roadmap](https://github.com/google/gson/blob/master/CHANGELOG.md): Details of changes in the recent versions
  * Gson [design document](https://github.com/google/gson/blob/master/GsonDesignDocument.md): This document discusses issues we faced while designing Gson. It also include a comparison of Gson with other Java libraries that can be used for Json conversion

Please use the [google-gson Google group](http://groups.google.com/group/google-gson) to discuss Gson, or to post questions. 

###*Gson-related Content Created by Third Parties*
  * [Gson Tutorial](http://www.studytrails.com/java/json/java-google-json-introduction.jsp) by `StudyTrails`

###*License*

Gson is released under the [Apache 2.0 license](LICENSE).

```
Copyright 2008 Google Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```


Other Java examples (source code examples)
Here is a short list of links related to this Java README.md source code file:

 The search page
 Other Java source code examples at this package level
 Click here to learn more about this project











... this post is sponsored by my books ...





#1 New Release!



FP Best Seller



 


new blog posts


How to use `curl` scripts to test RESTful web services (GET, POST, etc.)
Using a SQLite date/time field with Flutter and Dart
Scala 3: Using Term Inference with Given and Using

Flutter 3 release, May, 2022
Your ego is writing checks your body can'''t cash
Scala 3 Unions: Simulating Dynamic Typing with Union Types

Scala 3: Using Java Collections in Scala
A User Story Mapping Example Using Facebook
How to read '''difficult''' Scala method type signatures





 
Copyright 1998-2021 Alvin Alexander, alvinalexander.com
All Rights Reserved.

A percentage of advertising revenue from
pages under the /java/jwarehouse 
URI on this website is
paid back to open source projects.


 

