<?php
	include('/var/www/twiverse.php');

	$filename = $_GET['stamp'];
	//$filename = 'DSG2cHQWkAYCk5h.png';
	exec('curl https://pbs.twimg.com/media/'.$filename.' > /tmp/'.$filename);
	`sync`;
	exec('python imgread.py /tmp/'.$filename);
	`sync`;
	exec('blender --background --python genstamp.py /tmp/'.$filename);
	`sync`;
	header('Content-Type: application/force-download');
	header('Content-Length: '.filesize('/tmp/'.$filename));
	header('Content-Disposition: attachment; filename="stamp.stl"');
	readfile('/tmp/'.$filename);
	unlink('/tmp/'.$filename);
?>
