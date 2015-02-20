<label><?php


$verz="1.0";
#$stat1="red.jpg";
#$stat2="red.jpg";
#$stat3="red.jpg";
#$comPort = "C:\Users\mickael\Partage_VirtualBOX\Domotic_Server\DomoticServer\log\command.log"; /*change to correct com port */
$comPort = "command.log"; /*change to correct com port */
$Image1 = "image1.txt";
$Image2 = "image2.txt";
$Image3 = "image3.txt";
$socket1 = "socket1.txt";
$socket2 = "socket2.txt";
$socket3 = "socket3.txt";

$PHP_SELF="index.php";
if (isset($_POST["rcmd"])) {
$rcmd = $_POST["rcmd"];

switch ($rcmd) {
     case "ON1":
        $fp =fopen($comPort, "ab");
		$date = date('d m Y H:i:s');
  fwrite($fp, $date.">3.$.S0N1.S2N2.RELAY1ON.#\n"); /* this is the number that it will write */
  fclose($fp);
  $Image1Open = fopen($Image1, "ab");
  ftruncate($Image1Open, 0);
  fwrite($Image1Open,"green.jpg");
  fclose($Image1Open);
  break;
     case "OFF1":
        $fp =fopen($comPort, "ab");
		$date = date('d m Y H:i:s');
  fwrite($fp, $date.">3.$.S0N1.S2N2.RELAY1OFF.#\n"); /* this is the number that it will write */
  fclose($fp);
  $Image1Open = fopen($Image1, "ab");
  ftruncate($Image1Open, 0);
  fwrite($Image1Open,"red.jpg");
  fclose($Image1Open);
  break;
  case "ON2":
        $fp =fopen($comPort, "ab");
		$date = date('d m Y H:i:s');
  fwrite($fp, $date.">3.$.S0N1.S2N2.RELAY2ON.#\n"); /* this is the number that it will write */
  fclose($fp);
  $Image2Open = fopen($Image2, "ab");
  ftruncate($Image2Open, 0);
  fwrite($Image2Open,"green.jpg");
  fclose($Image2Open);
  break;
  case "OFF2":
       $fp =fopen($comPort, "ab");
		$date = date('d m Y H:i:s');
  fwrite($fp, $date.">3.$.S0N1.S2N2.RELAY2OFF.#\n"); /* this is the number that it will write */
  fclose($fp);
  $Image2Open = fopen($Image2, "ab");
  ftruncate($Image2Open, 0);
  fwrite($Image2Open,"red.jpg");
  fclose($Image2Open);
  break;
case "ON3":
        $fp =fopen($comPort, "ab");
		$date = date('d m Y H:i:s');
  fwrite($fp, $date.">3.$.S0N1.S2N2.RELAY3ON.#\n"); /* this is the number that it will write */
  fclose($fp);
  $Image3Open = fopen($Image3, "ab");
  ftruncate($Image3Open, 0);
  fwrite($Image3Open,"green.jpg");
  fclose($Image3Open);
  break;
case "OFF3":
        $fp =fopen($comPort, "ab");
		$date = date('d m Y H:i:s');
  fwrite($fp, $date.">3.$.S0N1.S2N2.RELAY3OFF.#\n"); /* this is the number that it will write */
  fclose($fp);
  $Image3Open = fopen($Image3, "ab");
  ftruncate($Image3Open, 0);
  fwrite($Image3Open,"red.jpg");
  fclose($Image3Open);
  break;
default:
  die('Crap, something went wrong. The page just puked.');
}
}
$handle = fopen($Image1, "r");
$stat1 = fread($handle, filesize($Image1));
fclose($handle);
$handle = fopen($Image2, "r");
$stat2 = fread($handle, filesize($Image2));
fclose($handle);
$handle = fopen($Image3, "r");
$stat3 = fread($handle, filesize($Image3));
fclose($handle);

$handle = fopen($socket1, "r");
$statSocket1 = fread($handle, filesize($socket1));
fclose($handle);
$handle = fopen($socket2, "r");
$statSocket2 = fread($handle, filesize($socket2));
fclose($handle);
$handle = fopen($socket3, "r");
$statSocket3 = fread($handle, filesize($socket3));
fclose($handle);
?></label>
<html>
<style type="text/css">
body{width:100%;}
</style>
<meta http-equiv="refresh" content="5;">
<style type="text/css">
<!--
.Style3 {color: #FFFFFF}
#apDiv16 {
	position:absolute;
	left:1196px;
	top:54px;
	width:176px;
	height:240px;
	z-index:13;
}
#apDiv17 {
	position:absolute;
	left:986px;
	top:422px;
	width:238px;
	height:234px;
	z-index:13;
}
#apDiv20 {
	position:absolute;
	left:398px;
	top:436px;
	width:66px;
	height:34px;
	z-index:14;
}
#apDiv21 {
	position:absolute;
	left:138px;
	top:436px;
	width:78px;
	height:38px;
	z-index:15;
}
#apDiv22 {
	position:absolute;
	left:680px;
	top:438px;
	width:48px;
	height:36px;
	z-index:16;
}
-->

</style>
<head>

<style type="text/css">
#apDiv1 {
	position:absolute;
	left:587px;
	top:206px;
	width:40px;
	height:24px;
	z-index:2;
}
#apDiv2 {
	position:absolute;
	left:57px;
	top:204px;
	width:37px;
	height:230px;
	z-index:3;
}
#apDiv3 {
	position:absolute;
	left:43px;
	top:143px;
	width:255px;
	height:25px;
	z-index:4;
}
#apDiv4 {
	position:absolute;
	left:318px;
	top:205px;
	width:46px;
	height:21px;
	z-index:5;
}
#apDiv5 {
	position:absolute;
	left:330px;
	top:143px;
	width:247px;
	height:24px;
	z-index:6;
}
#apDiv6 {
	position:absolute;
	left:602px;
	top:144px;
	width:267px;
	height:24px;
	z-index:8;
}
#apDiv7 {
	position:absolute;
	left:131px;
	top:345px;
	width:290px;
	height:241px;
	z-index:1;
}
#apDiv8 {
	position:absolute;
	left:577px;
	top:275px;
	width:69px;
	height:18px;
	z-index:9;
}
#apDiv9 {
	position:absolute;
	left:581px;
	top:376px;
	width:69px;
	height:18px;
	z-index:9;
}
#apDiv10 {
	position:absolute;
	left:584px;
	top:471px;
	width:65px;
	height:18px;
	z-index:9;
}
#apDiv11 {
	position:absolute;
	left:265px;
	top:24px;
	width:342px;
	height:44px;
	z-index:10;
}
.Style2 {
	font-size: 36px;
	font-weight: bold;
}
#apDiv12 {
	position:absolute;
	left:408px;
	top:82px;
	width:152px;
	height:44px;
	z-index:10;
}
#apDiv13 {
	position:absolute;
	left:387px;
	top:261px;
	width:39px;
	height:42px;
	z-index:11;
}
#apDiv14 {
	position:absolute;
	left:628px;
	top:347px;
	width:41px;
	height:41px;
	z-index:12;
}
#apDiv15 {
	position:absolute;
	left:631px;
	top:437px;
	width:41px;
	height:41px;
	z-index:12;
}
.Style4 {font-size: 36px; font-weight: bold; color: #FFFFFF; }
</style>
</head>

<body  bgcolor="black">
<div id="apDiv1"><img src="<?php echo $statSocket3; ?>" alt="SOCKET" width="230" height="232"></div>
<div id="apDiv20"><span class="Style2">
  <input type="image" name="RELAY2" id="RELAY2" src="<?php echo $stat2; ?>">
</span></div>
<div id="apDiv21"><span class="Style2">
<input type="image" name="RELAY1" id="RELAY1" src="<?php echo $stat1; ?>">
</span></div>
<div id="apDiv22"><span class="Style2">
  <input type="image" name="RELAY3" id="RELAY3" src="<?php echo $stat3; ?>">
</span></div>
<div id="apDiv19"></div>
<div id="apDiv18"></div>
<form method="post" action="<?php echo $PHP_SELF;?>">
<div id="apDiv3"><span class="Style2">
  <input name="rcmd" type="submit" class="Style2" value="ON1">
  <input name="rcmd" type="submit" class="Style2" value="OFF1">
</span></div>
<div class="Style2" id="apDiv5">
  <input name="rcmd" type="submit" class="Style2" value="ON2">
  <input name="rcmd" type="submit" class="Style2" value="OFF2">
</div>
<div class="Style2" id="apDiv6">
  <input type="submit" class="Style2" value="ON3" name="rcmd">
  <input name="rcmd" type="submit" class="Style2" value="OFF3">
</div>
<div class="Style2 Style3" id="apDiv11">DOMOTIC SERVER</div>

<div align="justify"></div>
<div class="Style4" id="apDiv12">ROOM 1</div>

<div id="apDiv2"><img src="<?php echo $statSocket1; ?>" alt="SOCKET" width="230" height="232"></div>
<div id="apDiv4"><img src="<?php echo $statSocket2; ?>" alt="SOCKET" width="230" height="232"></div>
</body>
</html>