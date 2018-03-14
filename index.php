<?php
	include('/var/www/twiverse.php');

	$filename = $_GET['stamp'];
	exec('curl https://pbs.twimg.com/media/'.$filename.' > /tmp/'.$filename);
	`sync`;
	exec('blender --background --python stamp.py /tmp/'.$filename);
	`sync`;
	header('Content-Type: application/force-download');
	header('Content-Length: '.filesize('/tmp/'.$filename));
	header('Content-Disposition: attachment; filename="stamp.stl"');
	readfile('/tmp/'.$filename);
	unlink('/tmp/'.$filename);
?>
