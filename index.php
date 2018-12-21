<?php
	include('/var/www/twiverse.php');

	try{
		mysql_start();
		$set = mysql_fetch_assoc(mysql_throw(mysql_query("select stamp_height from user where id=".$_SESSION['twitter']['id'])));
		mysql_close();

		$filename = $_GET['stamp'];
		//$filename = 'DSG2cHQWkAYCk5h.png';
		exec('curl https://pbs.twimg.com/media/'.$filename.' > /tmp/'.$filename);
		`sync`;
		exec('mogrify -trim /tmp/'.$filename);
		`sync`;
		exec('python imgread.py /tmp/'.$filename);
		`sync`;
		exec('blender --background --python genstamp.py /tmp/'.$filename.' '.$set['stamp_height']);
		`sync`;
		header('Content-Type: application/force-download');
		header('Content-Length: '.filesize('/tmp/'.$filename));
		header('Content-Disposition: attachment; filename="'.pathinfo($filename)['filename'].'.stl"');
		readfile('/tmp/'.$filename);
		unlink('/tmp/'.$filename);
	}catch(Exception $e){
		catch_default($e);
	}
?>
