# python-challenge

### Challenge:

#### I wrote a **short story** with the title "This is a short story !" and saved it in my Artifactory in the libs-release-local repository as a text file.

#### Someone hacked my account and renamed all my Artifacts in this repo.

#### Please help me to get my story back.

I want you to write a Python script to:

Go over the files in this repository

Create a CSV file with the details of the source file and the story.

| File Name | Story Txt (without the title) |
|-----------|-------------------------------|

Security is even more important to me now and I limited all active users in the system with the minimum permissions that are needed.

Please work only with short-lived access tokens <5 seconds. You can refresh it if needed.

The script should print start and end time, and the faster the run the more impressed I will be!

You should use at least 10 advanced python concepts

This relies on a jfrog platform with admin user and password access.
JFrog Platform details
jfrog_url = "URL"
jfrog_user = "USER"
jfrog_password = "PASS"
Jfrog_repo_name = “REPO“


The script body should be like:

   #!/usr/bin/env python3

   < YOUR CODE > 


   if __name__ == "__main__":

      start_time = perf_counter()

      < YOUR CODE > 


      end_time = perf_counter()
      print(f'It took {end_time-start_time: 0.4f} second(s) to complete.')



Share your instructions to execute and get the results.


Bonus: Share K8s Job to run it
