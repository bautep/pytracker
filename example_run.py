#!/usr/bin/python
import argparse
try:
	from pytracker import Tracker
except ImportError:
	raise ImportError("Requires pytracker module.")

parser = argparse.ArgumentParser(description='example app for pytracker')
# get project and api token
parser.add_argument('--project', type=str,
                    help='project id')

parser.add_argument('--token', type=str,
                    help='your personal api token to connect to tracker.com')

parser.add_argument('story', type=int,
                    help='storyi number')

args = parser.parse_args()

project = args.project
token = args.token
storynr = args.story

tracker = Tracker(int(project), token)

activities = tracker.GetProjectActivity()
for act in activities:
    act.pprint()

# #story = tracker.GetStory(storynr)
# story = tracker.GetStory(storynr)
# print story.story_type

# activities = tracker.GetStoryActivity(storynr)

# story.pprint()
# print "==========="

# for act in activities:
    # act.pprint()
