#include <bits/stdc++.h>

using namespace std;

class MinHeapNode
{
    char data;                	// Input
    unsigned freq;             	// Frequency
    MinHeapNode *left, *right; 	// Children

    MinHeapNode(char data, unsigned freq)
    {
        left = right = NULL;
        this->data = data;
        this->freq = freq;
    }
	bool compare(MinHeapNode* l, MinHeapNode* r)
	{
		return (l->freq > r->freq);
	}
};

void HuffmanCodes(char data[], int freq[], int size)
{
    struct MinHeapNode *left, *right, *top;
	priority_queue < MinHeapNode*, vector < MinHeapNode* >, compare > minHeap;

	for (int i = 0; i < size; ++i)
        minHeap.push(new MinHeapNode(data[i], freq[i]));

	while (minHeap.size() != 1)
    {
		left = minHeap.top();
        minHeap.pop();
        right = minHeap.top();
        minHeap.pop();

		top = new MinHeapNode('#', left->freq + right->freq);
        top->left = left;
        top->right = right;
        minHeap.push(top);
    }
}
