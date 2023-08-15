<h2><a href="https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst">1692. Number of Ways to Reorder Array to Get Same BST</a></h2><h3>Hard</h3><hr><p>Given an array <code>self</code> that represents a permutation of integers from <code>1</code> to <code>n</code>. We are going to construct a binary search tree (BST) by inserting the elements of <code>self</code> in order into an initially empty BST. Find the number of different ways to reorder <code>self</code> so that the constructed BST is identical to that formed from the original array <code>self</code>.</p>

<ul>
	<li>For example, given <code>self = [2,1,3]</code>, we will have 2 as the root, 1 as a left child, and 3 as a right child. The array <code>[2,3,1]</code> also yields the same BST but <code>[3,2,1]</code> yields a different BST.</li>
</ul>

<p>Return <em>the number of ways to reorder</em> <code>self</code> <em>such that the BST formed is identical to the original BST formed from</em> <code>self</code>.</p>

<p>Since the answer may be very large, <strong>return it modulo </strong><code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/12/bb.png" style="width: 121px; height: 101px;" />
<pre>
<strong>Input:</strong> self = [2,1,3]
<strong>Output:</strong> 1
<strong>Explanation:</strong> We can reorder self to be [2,3,1] which will yield the same BST. There are no other ways to reorder self which will yield the same BST.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/12/ex1.png" style="width: 241px; height: 161px;" />
<pre>
<strong>Input:</strong> self = [3,4,5,1,2]
<strong>Output:</strong> 5
<strong>Explanation:</strong> The following 5 arrays will yield the same BST: 
[3,1,2,4,5]
[3,1,4,2,5]
[3,1,4,5,2]
[3,4,1,2,5]
[3,4,1,5,2]
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/12/ex4.png" style="width: 121px; height: 161px;" />
<pre>
<strong>Input:</strong> self = [1,2,3]
<strong>Output:</strong> 0
<strong>Explanation:</strong> There are no other orderings of self that will yield the same BST.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= self.length &lt;= 1000</code></li>
	<li><code>1 &lt;= self[i] &lt;= self.length</code></li>
	<li>All integers in <code>self</code> are <strong>distinct</strong>.</li>
</ul>
