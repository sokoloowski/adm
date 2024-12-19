# Results analysis and conclusion {#sec:conclusion}

We started our work with almost no knowledge of text data mining, and it seemed like a good idea to do unsupervised learning, i.e. clustering. However, it quickly became clear that text data, which comes from a social network and is therefore written by a wide variety of internet users, is not suitable for this purpose - their topics mix and the resulting clusters overlap, making such a process ineffective.

Having failed in this area, we decided to try supervised learning, i.e. classification. We used the names of subreddits as labels for our data. The first attempts were promising, so we started adding more configurations and algorithms. The results we achieved, an accuracy of 70%, led us to adjust the process of preparing the data for learning. In this way, our models achieved around 80% accuracy.

However, one class that overlapped with the others was still problematic. To improve the results, we used the Hidden Markov Model, the dense network and the Long Short-Term Memory network. These methods did not allow us to break the 80% accuracy barrier, but still produced decent results.

At the outset of the project, we were uncertain as to the objective we wished to pursue. The subsequent stages of the project revealed that the formulation of a specific goal was unnecessary; the comparison of machine learning models was a sufficiently intriguing topic in itself. The process provided valuable insights into the preparation of text data for processing and demonstrated the impact of model parameters on classification outcomes. A multitude of experiments were conducted, with a consistent focus on enhancing the precision of class assignments and identifying avenues for further improvement.
