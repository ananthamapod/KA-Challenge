# Total and Limited Infection - Khan Academy Challenge
>This project is part of an interview coding challenge, and it models the deployment of new features in the Khan Academy environment.

**From the assignment prompt**: "When rolling out big new features, we like to enable them slowly, starting with just the KA team, then a handful of users, then some more users, and so on, until we’ve ramped up to 100%. This insulates the majority of users from bad bugs that crop up early in the life of a feature.

This strategy can cause problems somewhat unique to our user base. It’s not uncommon for a classroom of students to be using the site together, so it would be confusing to show half of them a completely different version of the site. Children are not software engineers and often have a poor understanding of deployment and a/b testing, so inconsistent colors, layout, and interactions effectively mean the site is broken."

It is desired to keep the deployment of new features to the Khan Academy environment as consistent as possible among the users in a classroom. Therefore, two methods of spreading deployment of new features are examined.

## Methods
#### Total Infection

Using the heuristic that every student-teacher pair must be on the same version of the site, when a new feature is rolled out to a user, all students coached by the user and all teachers coaching the user shall also receive the new feature. Essentially the connected component originating from the user is "totally infected".


#### Limited Infection

Using the same heuristic as total infection, but limiting the number of users "infected", a certain number of users alone in the connected component originating from a starting user receive the new feature, a "limited infection".

**From the assignment prompt**: "The problem with infection is lack of control over the number of users that eventually become infected. Starting an infection could cause only that person to become infected or at the opposite (unrealistic) extreme it could cause all users to become infected.

We would like to be able to infect close to a given number of users. Ideally we’d like a coach and all of their students to either have a feature or not. However, that might not always be possible."

## Graph Design

If users represent nodes in a graph, there are 2 kinds of relationships or edges to be modeled. There are both coaching and coached by relations. Therefore, a graph with colored edges would be the most applicable. Using an adjacency matrix would be the most convenient, as colored edges can be represented with different edge values. However, given that this is a graph of all a huge userbase, and adjacency matrix would be a spatial nightmare.

Therefore, an adjacency list representation is used, where the edges for each user are organized into roles. In the role of teacher, a user has 'students', and in the role of student, a user has 'teachers'. The graph therefore has a dictionary of vertices representing users and a dictionary of edges representing the relations. These are indexed by username, since a username is assumed to be unique.

* KA-Graph

  * v

    * [username]

    * ...

  * e

    * [username]

      * 'students'

        * [username] -> Relation

        * ...

      * 'teachers'

        * [username] -> Relation

        * ...

    * ...
