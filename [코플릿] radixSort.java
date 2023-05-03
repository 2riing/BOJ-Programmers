package com.codestates.coplit; 

public class Solution { 
	public int[] radixSort(int[] arr) {
		// length
		int N = arr.length;
		// max 
		int max = arr[0];
		for (int i = 1; i < N; i++) {
				if (max < arr[i]) max = arr[i];
		}

		// Time Complexity O(numN)
		// Counting Sort, 자리별(num) sort, until max num
		for (int num = 1; num <= max; num *= 10) {
				int temp[] = new int[N];
				int counting[] = new int[10];

				// 현재 자리(num) counting
				for(int i = 0; i < N; i++) counting[(arr[i] / num) % 10]++;

				// couting -> prefix sum 
				for(int i = 1; i < 10; i++) counting[i] += counting[i - 1];
				
				// 거꾸로 돌면서 fill temp
				for(int i = N - 1; i >= 0; i--) {
					int cur = (arr[i] / num) % 10;
					int idx = counting[cur];
					temp[idx - 1] = arr[i];
					counting[cur]--;
				}
				// copy temp into arr
				for(int i=0; i < N ; i++) arr[i] = temp[i];
		}
		return arr;
	} 
}
