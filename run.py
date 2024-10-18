if __name__ == '__main__':
	import sys
	from pathlib import Path
	sys.path[0] = str(Path(__file__).resolve().parent)
	from settings import BASE_DIR, DJANGO_DIR, DJANGO_MANAGE_FILE
	sys.path.insert(1, str(DJANGO_DIR))
	import os
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ration.settings')
	import django
	django.setup()
	from db import db
	import time
	import requests
	import subprocess
	import warnings
	# arguments validation
	if len(sys.argv) > 2:
		raise Exception(f'Unrecognized arguments {sys.argv[1:]}!')
	try:
		# open django subprocess
		dj_pr = subprocess.Popen([sys.executable, DJANGO_MANAGE_FILE, 'runserver', '8000'])
		# wait for django
		start_time, timeout = time.time(), 30
		while True:
			try:
				response = requests.get(f'http://localhost:8000')
				if response.status_code:
					break
			except requests.ConnectionError:
				pass
			# stop waiting
			if time.time() - start_time > timeout:
				raise Exception(f'Django server did not start within {timeout} seconds!')
			time.sleep(1)
		if len(sys.argv) == 2:
			if sys.argv[1] == '--rebuild-db':
				# flush db
				db_pr = subprocess.Popen([sys.executable, DJANGO_MANAGE_FILE, 'flush', '--noinput'])
				db_pr.wait()
				# rebuild db
				db.rebuild()
				# end program
				sys.exit(0)
			else:
				warning.warn(f'Unrecognized argument {sys.argv[1]}!')
		# wait for subprocess to complete
		dj_pr.wait()
	except KeyboardInterrupt:
		# close subprocess
		dj_pr.terminate()
		# wait for subprocess to close
		dj_pr.wait()
		# end program
		sys.exit(0)
	# end program with error
	sys.exit(-1)
