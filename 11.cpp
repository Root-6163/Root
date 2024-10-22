#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Job {
    int id;          // Job ID
    int priority;    // Job priority

    // For sorting jobs by priority
    bool operator<(const Job& other) const {
        return priority < other.priority; // Lower value means higher priority
    }
};

class JobQueue {
private:
    vector<Job> queue; // Vector to store jobs

public:
    void insert(int id, int priority); // Insert job into the queue
    void removeHighestPriority();       // Remove job with the highest priority
    Job getHighestPriority();           // Get job with the highest priority
    bool isEmpty();                     // Check if the queue is empty
    void display();                     // Display all jobs in the queue
};

// Insert job into the priority queue
void JobQueue::insert(int id, int priority) {
    Job newJob = {id, priority};
    queue.push_back(newJob); // Add job to the vector
    sort(queue.begin(), queue.end()); // Sort jobs based on priority
    cout << "Job " << id << " with priority " << priority << " added to the queue." << endl;
}

// Remove the job with the highest priority
void JobQueue::removeHighestPriority() {
    if (isEmpty()) {
        cout << "Queue is empty! Cannot remove job." << endl;
        return;
    }
    cout << "Removing job " << queue.front().id << " with priority " << queue.front().priority << "." << endl;
    queue.erase(queue.begin()); // Remove the first job (highest priority)
}

// Get the job with the highest priority
Job JobQueue::getHighestPriority() {
    if (isEmpty()) {
        cout << "Queue is empty!" << endl;
        return {-1, -1}; // Return invalid job
    }
    return queue.front(); // Return the job at the front of the queue
}

// Check if the queue is empty
bool JobQueue::isEmpty() {
    return queue.empty(); // Use the vector's empty method
}

// Display all jobs in the queue
void JobQueue::display() {
    if (isEmpty()) {
        cout << "Queue is empty!" << endl;
        return;
    }

    cout << "Current jobs in the queue:" << endl;
    for (const auto& job : queue) {
        cout << "Job ID: " << job.id << ", Priority: " << job.priority << endl;
    }
}

// Main function
int main() {
    JobQueue jobQueue; // Create a job queue

    jobQueue.insert(101, 3); // Add jobs
    jobQueue.insert(102, 1);
    jobQueue.insert(103, 2);
    jobQueue.insert(104, 4);
    jobQueue.insert(105, 0); // This will be the highest priority

    jobQueue.display(); // Display jobs in the queue

    Job highestPriorityJob = jobQueue.getHighestPriority();
    cout << "Highest priority job ID: " << highestPriorityJob.id << ", Priority: " << highestPriorityJob.priority << endl;

    jobQueue.removeHighestPriority(); // Remove job with the highest priority
    jobQueue.display(); // Display remaining jobs

    return 0;
}

