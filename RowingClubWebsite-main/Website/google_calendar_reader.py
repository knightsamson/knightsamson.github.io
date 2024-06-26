import json
import urllib.request
import datetime
import dateutil.relativedelta
from dateutil.parser import *
from dateutil.rrule import *
from dateutil.tz import UTC

unix_epoch = datetime.datetime(1970,1,1)

# Some debugging/error prevention notes:
#	- Try to always compare dates by timestamps.
#	- Try to always set things up to ignore timezone details.

# get the next (at most) five google calendar events
def get_next_five_events():
	# load api key from file
	keyFile = open("API_KEY", "r")
	key = keyFile.read()
	keyFile.close()

	# get data from google api
	url = "https://www.googleapis.com/calendar/v3/calendars/c5fe0447d1a0e4d944df3016fb3743627f21dbccacf4f4b8c38c145effbc6e83@group.calendar.google.com/events?key="+key
	f = urllib.request.urlopen(url)

	# convert output json data to a python dictionary
	out = json.loads(f.read())

	# set up output data
	events = []
	for a in out["items"]:
		# fields for the event list
		summary = ""
		description = ""
		location = ""
		date = "" 

		# get event summary
		if "summary" in a.keys():
			summary += a["summary"]
		else:
			summary += "n/a"

		# get event description
		if "description" in a.keys():
			description += a["description"]
		else:
			description += "n/a"

		# get event location
		if "location" in a.keys():
			location += a["location"]
		else:
			location += "n/a"

		# if the event is recurring get the next five dates
		# otherwise just get the next date
		print(a['start'].keys())
		if "recurrence" in a.keys():
			now = datetime.datetime.now()
			for i in range(5):
				# Check first if now was set to None object by a previous iteration
				if now is None:
					break
				# We need to set the start time for the recurrence or it will use whatever
				# the default value is
				start = parse(a['start']['dateTime'],ignoretz=True,default=unix_epoch)
				now = rrulestr(a["recurrence"][0],dtstart=start,ignoretz=True).after(now)
				date += str(now)
				events.append((summary,description,location,date))
				date=""
		elif "dateTime" in a["start"].keys(): # the date and time are present
			date += a["start"]["dateTime"]	
			# chop up the date into the required format for sorting
			date1 = date.split("T")[0]
			date2 = date.split("T")[1]
			date2 = date2.split("-")[0]
			date = date1+" "+date2
			events.append((summary,description,location,date))
			date=""
		elif "date" in a["start"].keys(): # just the date is present
			date += a["start"]["date"]	
			#date += " 00:00:00" # a dummy time
			events.append((summary,description,location,date))
			date=""
		else: #in this case we cannot parse the event
			print("DEBUG: "+str(a))	

	# Replace all nonpareseable event date/time strings with the unix epoch
	tmp = []
	for i in events:
		newEvent = []
		newEvent = list(i)
		try: 
			parse(newEvent[3],default=unix_epoch)
		except:
			newEvent[3] = "1970-01-01 00:00:00"
		tmp.append(newEvent)
	events = tmp

	# sort events by date entry in format year-month-day hours:minutes:seconds
	events = sorted(events,key=lambda x: parse(x[3],default=unix_epoch))
	cnt = 1
	out = []
	for i in events:
		# we're only printing the next five upcoming events
		if cnt > 5:
			break

		# here we are just printing events, but this general structure can be used to build a list of the
		# next five events or to do processing on the next five events.
		eventDate = parse(i[3],default=unix_epoch)
		# it might make sense to set this to another day so that events today remain on the website all day?
		nowDate = datetime.datetime.now() 
		if eventDate.timestamp() > nowDate.timestamp(): # only print events after the current date
			out.append(i)
			cnt += 1 # increment the counter of events
	print(out)
	return out

# get the previous (at most) five google calendar events that have already ended
def get_last_five_events():
	# load api key from file
	keyFile = open("API_KEY", "r")
	key = keyFile.read()
	keyFile.close()

	# get data from google api
	url = "https://www.googleapis.com/calendar/v3/calendars/c5fe0447d1a0e4d944df3016fb3743627f21dbccacf4f4b8c38c145effbc6e83@group.calendar.google.com/events?key="+key
	f = urllib.request.urlopen(url)

	# convert output json data to a python dictionary
	out = json.loads(f.read())

	# set up output data
	events = []
	for a in out["items"]:
		# fields for the event list
		summary = ""
		description = ""
		location = ""
		date = ""

		# get event summary
		if a.keys()   and "summary" in a.keys():
			summary += a["summary"]
		else:
			summary += "n/a"

		# get event description
		if "description" in a.keys():
			description += a["description"]
		else:
			description += "n/a"

		# get event location
		if "location" in a.keys():
			location += a["location"]
		else:
			location += "n/a"

		# if the event is recurring get the next five dates
		# otherwise just get the next date
		if "recurrence" in a.keys():
			# get the start time of this recurrence	
			start = parse(a['start']['dateTime'],ignoretz=True,default=unix_epoch)
			now = datetime.datetime.now()
			last_month = now + dateutil.relativedelta.relativedelta(months=-1)
			# update the last_month variable with the correct times for this event
			last_month = last_month.replace(hour=start.hour,minute=start.minute)
			start = rrulestr(a["recurrence"][0],dtstart=last_month,ignoretz=True).after(last_month)
			for i in range(5):
				if start.timestamp() < now.timestamp():	# only include dates before the current date
					date += str(start).split(".")[0]
					events.append((summary,description,location,date))
					date=""
					start = rrulestr(a["recurrence"][0],dtstart=last_month,ignoretz=True).after(start)
		elif a["start"] and "dateTime" in a["start"].keys(): # the date and time are present
			date += a["start"]["dateTime"]	
			# chop up the date into the required format for sorting
			date1 = date.split("T")[0]
			date2 = date.split("T")[1]
			date2 = date2.split("-")[0]
			date = date1+" "+date2
			#eventDate = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
			eventDate = parse(date)
			if eventDate.timestamp() < datetime.datetime.now().timestamp(): # only include dates before the current date
				events.append((summary,description,location,date))
			date=""
		elif a["start"] and "date" in a["start"].keys(): # just the date is present
			date += a["start"]["date"]	
			date += " 00:00:00" # a dummy time
			#eventDate = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
			eventDate = parse(date)
			if eventDate.timestamp() < datetime.datetime.now().timestamp(): # only include dates before the current date
				events.append((summary,description,location,date))
			date=""
		else: #in this case we cannot parse the event
			print("DEBUG: "+str(a))	

	# Replace all nonpareseable event date/time strings with the unix epoch
	tmp = []
	for i in events:
		newEvent = []
		newEvent = list(i)
		try: 
			parse(newEvent[3])
		except:
			newEvent[3] = "1970-01-01 00:00:00"
		tmp.append(newEvent)
	events = tmp

	# sort events by date entry in format year-month-day hours:minutes:seconds
	events = sorted(events,key=lambda x: parse(x[3]).timestamp())
	cnt = 1
	out = []
	
	events.reverse() # we iterate across old events backwards
	for i in events:
		# we're only printing the next THREE past events
		if cnt > 5:
			break

		# here we are just printing events, but this general structure can be used to build a list of the
		# next five events or to do processing on the next five events.
		#eventDate = datetime.datetime.strptime(i[3], "%Y-%m-%d %H:%M:%S")
		eventDate = parse(i[3])
		# it might make sense to set this to another day so that events today remain on the website all day?
		nowDate = datetime.datetime.now() 
		#if eventDate.timestamp() > nowDate.timestamp(): # only print events after the current date
		#if eventDate < nowDate: # only print events after the current date
		if eventDate.timestamp() < nowDate.timestamp(): # only print events after the current date
			out.append(i)
			cnt += 1 # increment the counter of events
	return out


# driver function for testing
#def main():
#	print("Printing the next five upcoming events.")
#	events = get_next_five_events()
#	for i in events:
#		print("summary: "+i[0])
#		print("\tdescription: "+i[1])
#		print("\tlocation: "+i[2])
#		print("\tdate: "+i[3])
#	print("Printing the previous five past events.")
#	events = get_last_five_events()
#	for i in events:
#		print("summary: "+i[0])
#		print("\tdescription: "+i[1])
#		print("\tlocation: "+i[2])
#		print("\tdate: "+i[3])
#	
#if __name__ == "__main__":
#	main()
