from textwrap import dedent

head = dedent("""\
    <!-- Last updated for Version 2.1 -->
    
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title>ཚིག་གསུམ་གནད་བརྡེག།</title>
        <link rel="stylesheet" href="css/hyperaudio-lite-player.css">
          <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Jomolhari">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/velocity/1.5.0/velocity.js"></script>
        <style>
          /* uncomment the following CSS for active parent / word indicator */ 
          
          
          .hyperaudio-transcript .active{
            background-color: #efefef;
          }
      
          .hyperaudio-transcript .active > .active {
            background-color: #ccf;
            text-decoration:  #00f underline;
            text-decoration-thickness: 3px;
          }
          
          #popover {
          position: absolute;
          background-color: #f9f9f9;
          
          border: 1px solid #ccc;
          padding: 10px;
          border-radius: 4px;
          box-shadow: 0 2px 5px rgba(0,0,0,0.2);
          display: none;
          z-index: 1;
          font-size: small;
          font-family: Jomolhari, Arial,Helvetica Neue,Helvetica,sans-serif;
        }
    
        #popover a {
          text-decoration: none; 
          color: #303030;
          cursor: pointer;
        }
    
        #clipboard-text {
          font-family: Jomolhari, Courier New,Courier,Lucida Sans Typewriter,Lucida Typewriter,monospace; 
        }
    
        #clipboard-confirm {
          font-size: medium;
        }
        </style>
      </head>""")

body_beginning = dedent("""\
      <body>
          <p style="font-size: 32pt; text-align: center; color: brown;">Tsiksum Nedek teachings synchronized with the text</p>

<p style="font-size: 25pt; color: brown;">Four complete teachings of the commentary</p>        
                <p style="font-size: 20pt;">Teaching of the commentary - 1</p>
          <p style="font-size: 20pt;">  <a href="#tsiksum1">Session 1</a><span style="font-family:arial; font-size: 20px;">27:38</span> 
                                        <a href="#tsiksum2">Session 2</a><span style="font-family:arial; font-size: 20px;">14:05</span> 
                                        <a href="#tsiksum3">Session 3</a><span style="font-family:arial; font-size: 20px;">9:51</span></p>

                <p><p style="font-size: 20pt;">Teaching of the commentary - 3</p>
          <p style="font-size: 20pt;">  <a href="#tsiksum4">Session 1</a><span style="font-family:arial; font-size: 20px;">17:51</span> 
                                        <a href="#tsiksum5">Session 2</a><span style="font-family:arial; font-size: 20px;">17:16</span> 
                                        <a href="#tsiksum6">Session 3</a><span style="font-family:arial; font-size: 20px;">11:25</span></p>
                                        
                <p style="font-size: 20pt;">Teaching of the commentary - 6</p>
          <p style="font-size: 20pt;">  <a href="#tsiksum7">Session 1</a><span style="font-family:arial; font-size: 20px;">2:34</span> 
                                        <a href="#tsiksum8">Session 2</a><span style="font-family:arial; font-size: 20px;">7:51</span> 
                                        <a href="#tsiksum9">Session 3</a><span style="font-family:arial; font-size: 20px;">10:08</span> 
                                        <a href="#tsiksum10">Session 4</a><span style="font-family:arial; font-size: 20px;">6:46</span></p>
                                        
                <p style="font-size: 20pt;">Teaching of the commentary - 10</p>
          <p style="font-size: 20pt;">  <a href="#tsiksum11">Session 1</a><span style="font-family:arial; font-size: 20px;">31:52</span> 
                                        <a href="#tsiksum12">Session 2</a><span style="font-family:arial; font-size: 20px;">14:27</span> 
                                        <a href="#tsiksum13">Session 3</a><span style="font-family:arial; font-size: 20px;">4:26</span> 
                                        <a href="#tsiksum14">Session 4</a><span style="font-family:arial; font-size: 20px;">9:17</span> 
                                        <a href="#tsiksum15">Session 5</a><span style="font-family:arial; font-size: 20px;">6:43</span></p>

<p style="font-size: 25pt; color: brown;">Five incomplete teachings of the commentary (excepting the teaching transcribed by Sengdrag Rinpoche</p>                                        
                <p style="font-size: 20pt;">Teaching of the commentary - 4</p>
          <p style="font-size: 20pt;">  <a href="#tsiksum16">Session 1</a><span style="font-family:arial; font-size: 20px;">17:07</span> 
                                        <a href="#tsiksum17">Session 2-from point 1 until the end</a><span style="font-family:arial; font-size: 20px;">9:00</span></p>
          
                <p style="font-size: 20pt;">Teaching of the commentary - 8</p>
          <p style="font-size: 20pt;"><a href="#tsiksum18">From intro of the three points until the end of point 1</a><span style="font-family:arial; font-size: 20px;">40:58</span></p>

                <p style="font-size: 20pt;">Teaching of the commentary - 7</p>
          <p style="font-size: 20pt;"><a href="#tsiksum19">From middle of point 2 until the end</a><span style="font-family:arial; font-size: 20px;">18:50</span></p>

                <p style="font-size: 20pt;">Teaching of the commentary - 2</p>
          <p style="font-size: 20pt;"><a href="#tsiksum20">Point 3 and conclusion</a><span style="font-family:arial; font-size: 20px;">11:10</span></p>

                <p style="font-size: 20pt;">Teaching of the commentary - 5</p>
          <p style="font-size: 20pt;"><a href="#tsiksum21">Only the beginning of point 3</a><span style="font-family:arial; font-size: 20px;">2:19</span></p>

<p style="font-size: 25pt; color: brown;">One teaching of the commentary not following the words of the text</p>
                <p style="font-size: 20pt;">General overview of the commentary</p>
          <p style="font-size: 20pt;">  <a href="#tsiksum22">Session 1</a><span style="font-family:arial; font-size: 20px;">15:26</span> 
                                        <a href="#tsiksum23">Session 2</a><span style="font-family:arial; font-size: 20px;">31:00</span> 
                                        <a href="#tsiksum24">Session 3</a><span style="font-family:arial; font-size: 20px;">12:57</span> 
                                        <a href="#tsiksum25">Session 4</a><span style="font-family:arial; font-size: 20px;">18:40</span> 
                                        <a href="#tsiksum26">Session 5</a><span style="font-family:arial; font-size: 20px;">14:49</span> 
                                        <a href="#tsiksum27">Session 6</a><span style="font-family:arial; font-size: 20px;">13:44</span> 
                                        <a href="#tsiksum28">Session 7</a><span style="font-family:arial; font-size: 20px;">10:28</span> 
                                        <a href="#tsiksum29">Session 8</a><span style="font-family:arial; font-size: 20px;">21:30</span> 
                                        <a href="#tsiksum30">Session 9</a><span style="font-family:arial; font-size: 20px;">22:28</span> 
                                        <a href="#tsiksum31">Session 10</a><span style="font-family:arial; font-size: 20px;">14:45</span></p>

<p style="font-size: 25pt; color: brown;">Two lungs of the commentary with occasional commentary</p>
                <p style="font-size: 20pt;">Lung of the commentary with occasional commentary - 1</p>
          <p style="font-size: 20pt;">  <a href="#tsiksum32">Session 1</a><span style="font-family:arial; font-size: 20px;">24:53</span> 
                                        <a href="#tsiksum33">Session 2</a><span style="font-family:arial; font-size: 20px;">1:31</span> 
                                        <a href="#tsiksum34">Session 3</a><span style="font-family:arial; font-size: 20px;">10:21</span> 
                                        <a href="#tsiksum35">Session 4</a><span style="font-family:arial; font-size: 20px;">8:30</span> 
                                        <a href="#tsiksum36">Session 5</a><span style="font-family:arial; font-size: 20px;">6:44</span></p>
                                        
                <p style="font-size: 20pt;">Lung of the commentary with occasional commentary - 2</p>
          <p style="font-size: 20pt;"><a href="#tsiksum37">Session 1</a><span style="font-family:arial; font-size: 20px;">35:02</span> 
                                        <a href="#tsiksum38">Session 2</a><span style="font-family:arial; font-size: 20px;">8:11</span> 
                                        <a href="#tsiksum39">Session 3</a><span style="font-family:arial; font-size: 20px;">8:09</span> 
                                        <a href="#tsiksum40">Session 4</a><span style="font-family:arial; font-size: 20px;">4:13</span></p>

<p style="font-size: 25pt; color: brown;">Two lungs of the root text with occasional commentary</p>
                <p style="font-size: 20pt;">Lung of the root text with sparse commentaries</p>
          <p style="font-size: 20pt;">  <a href="#tsiksum41">Session 1</a><span style="font-family:arial; font-size: 20px;">41:18</span></p>
          
                <p style="font-size: 20pt;">Lung of the root text with sparse commentaries</p>
          <p style="font-size: 20pt;"><a href="#tsiksum42">Session 1</a><span style="font-family:arial; font-size: 20px;">21:51</span></p>

<p style="font-size: 25pt; color: brown;">One Lung of the root text with a condensed presentation of each point</p>
                <p style="font-size: 20pt;">Lung of the root text with a condensed presentation of each point</p>
          <p style="font-size: 20pt;"><a href="#tsiksum43">Session 1</a><span style="font-family:arial; font-size: 20px;">7:14</span><br></p><br><br><br>
          """)

players = [
        dedent("""\
          <p id="tsiksum1" style="font-size: 26pt; color: brown;">Teaching of the commentary - 1 Session 1</p>         
          <audio id="hyperplayer1" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_a_1.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f615f312e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum2" style="font-size: 26pt; color: brown;">Teaching of the commentary - 1 Session 2</p>         
          <audio id="hyperplayer2" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_a_2.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f615f322e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum3" style="font-size: 26pt; color: brown;">Teaching of the commentary - 1 Session 3</p>         
          <audio id="hyperplayer3" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_a_3.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f615f332e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <audio id="hyperplayer4" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_c_1.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f635f312e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
          <p id="tsiksum4" style="font-size: 26pt; color: brown;">Teaching of the commentary - 3 Session 1</p>         
        """),
        dedent("""\
          <p id="tsiksum5" style="font-size: 26pt; color: brown;">Teaching of the commentary - 3 Session 2</p>         
          <audio id="hyperplayer5" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_c_2.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f635f322e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum6" style="font-size: 26pt; color: brown;">Teaching of the commentary - 3 Session 3</p>         
          <audio id="hyperplayer6" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_c_3.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f635f332e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <audio id="hyperplayer7" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_f_1.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f665f312e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
          <p id="tsiksum7" style="font-size: 26pt; color: brown;">Teaching of the commentary - 6 Session 1</p>         
        """),
        dedent("""\
          <p id="tsiksum8" style="font-size: 26pt; color: brown;">Teaching of the commentary - 6 Session 2</p>         
          <audio id="hyperplayer8" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_f_2.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f665f322e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum9" style="font-size: 26pt; color: brown;">Teaching of the commentary - 6 Session 3</p>         
          <audio id="hyperplayer9" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_f_3.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f665f332e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum10" style="font-size: 26pt; color: brown;">Teaching of the commentary - 6 Session 4</p>         
          <audio id="hyperplayer10" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_f_4.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f665f342e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum11" style="font-size: 26pt; color: brown;">Teaching of the commentary - 10 Session 1</p>         
          <audio id="hyperplayer11" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_k_1.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f6b5f312e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum12" style="font-size: 26pt; color: brown;">Teaching of the commentary - 10 Session 2</p>         
          <audio id="hyperplayer12" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_k_2.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f6b5f322e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum13" style="font-size: 26pt; color: brown;">Teaching of the commentary - 10 Session 3</p>         
          <audio id="hyperplayer13" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_k_3.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f6b5f332e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum14" style="font-size: 26pt; color: brown;">Teaching of the commentary - 10 Session 4</p>         
          <audio id="hyperplayer14" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_k_4.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f6b5f342e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum15" style="font-size: 26pt; color: brown;">Teaching of the commentary - 10 Session 5</p>         
          <audio id="hyperplayer15" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_k_5.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f6b5f352e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum16" style="font-size: 26pt; color: brown;">Teaching of the commentary - 4 Session 1</p>         
          <audio id="hyperplayer16" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_d_1.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f645f312e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum17" style="font-size: 26pt; color: brown;">Teaching of the commentary - 4 Session 2</p>         
          <audio id="hyperplayer17" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_d_2_unfinished.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f645f325f756e66696e69736865642e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum18" style="font-size: 26pt; color: brown;">Teaching of the commentary - 8, From intro of the three points until the end of point 1</p>         
          <audio id="hyperplayer18" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_h_onlybeginning.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f685f6f6e6c79626567696e6e696e672e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum19" style="font-size: 26pt; color: brown;">Teaching of the commentary - 7, From middle of point 2 until the end</p>         
          <audio id="hyperplayer19" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_g_nobeginning.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f675f6e6f626567696e6e696e672e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum20" style="font-size: 26pt; color: brown;">Teaching of the commentary - 2, Point 3 and conclusion</p>         
          <audio id="hyperplayer20" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_b_onlyend.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f625f6f6e6c79656e642e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum21" style="font-size: 26pt; color: brown;">Teaching of the commentary - 5, Only the beginning of point 3</p>         
          <audio id="hyperplayer21" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_e_unfinished.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f655f756e66696e69736865642e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum22" style="font-size: 26pt; color: brown;">General overview of the commentary, Session 1</p>         
          <audio id="hyperplayer22" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_l_1.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f6c5f312e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum23" style="font-size: 26pt; color: brown;">General overview of the commentary, Session 2</p>         
          <audio id="hyperplayer23" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_l_2.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f6c5f322e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum24" style="font-size: 26pt; color: brown;">General overview of the commentary, Session 3</p>         
          <audio id="hyperplayer24" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_l_3.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f6c5f332e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum25" style="font-size: 26pt; color: brown;">General overview of the commentary, Session 4</p>         
          <audio id="hyperplayer25" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_l_4.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f6c5f342e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum26" style="font-size: 26pt; color: brown;">General overview of the commentary, Session 5</p>         
          <audio id="hyperplayer26" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_l_5.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f6c5f352e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum27" style="font-size: 26pt; color: brown;">General overview of the commentary, Session 6</p>         
          <audio id="hyperplayer27" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_l_6.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f6c5f362e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum28" style="font-size: 26pt; color: brown;">General overview of the commentary, Session 7</p>         
          <audio id="hyperplayer28" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_l_7.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f6c5f372e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum29" style="font-size: 26pt; color: brown;">General overview of the commentary, Session 8</p>         
          <audio id="hyperplayer29" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_l_8.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f6c5f382e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum30" style="font-size: 26pt; color: brown;">General overview of the commentary, Session 9</p>         
          <audio id="hyperplayer30" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_l_9.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f6c5f392e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum31" style="font-size: 26pt; color: brown;">General overview of the commentary, Session 10</p>         
          <audio id="hyperplayer31" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_l_10.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f6c5f31302e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum32" style="font-size: 26pt; color: brown;">Lung of the commentary with occasional commentary - 1, Session 1</p>         
          <audio id="hyperplayer32" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_thrilung_b_1.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f746872696c756e675f625f312e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum33" style="font-size: 26pt; color: brown;">Lung of the commentary with occasional commentary - 1, Session 2</p>         
          <audio id="hyperplayer33" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_thrilung_b_2.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f746872696c756e675f625f322e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum34" style="font-size: 26pt; color: brown;">Lung of the commentary with occasional commentary - 1, Session 3</p>         
          <audio id="hyperplayer34" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_thrilung_b_3.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f746872696c756e675f625f332e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum35" style="font-size: 26pt; color: brown;">Lung of the commentary with occasional commentary - 1, Session 4</p>         
          <audio id="hyperplayer35" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_thrilung_b_4.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f746872696c756e675f625f342e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum36" style="font-size: 26pt; color: brown;">Lung of the commentary with occasional commentary - 1, Session 5</p>         
          <audio id="hyperplayer36" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_thrilung_b_5.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f746872696c756e675f625f352e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum37" style="font-size: 26pt; color: brown;">Lung of the commentary with occasional commentary - 2, Session 1</p>         
          <audio id="hyperplayer37" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_j_1.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f6a5f312e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum38" style="font-size: 26pt; color: brown;">Lung of the commentary with occasional commentary - 2, Session 2</p>         
          <audio id="hyperplayer38" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_j_2.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f6a5f322e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum39" style="font-size: 26pt; color: brown;">Lung of the commentary with occasional commentary - 2, Session 3</p>         
          <audio id="hyperplayer39" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_j_3.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f6a5f332e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum40" style="font-size: 26pt; color: brown;">Lung of the commentary with occasional commentary - 2, Session 4</p>         
          <audio id="hyperplayer40" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_j_4.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f6a5f342e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum41" style="font-size: 26pt; color: brown;">Lung of the root text with sparse commentaries Session 1</p>         
          <audio id="hyperplayer41" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_thrilung_a.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f746872696c756e675f612e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum42" style="font-size: 26pt; color: brown;">Lung of the root text with sparse commentaries Session 1</p>         
          <audio id="hyperplayer42" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_roottext_thrilung_a_1.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f726f6f74746578745f746872696c756e675f615f312e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum43" style="font-size: 26pt; color: brown;">Lung of the root text with a condensed presentation of each point Session 1</p>         
          <audio id="hyperplayer43" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_roottext_overview_a.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f726f6f74746578745f6f766572766965775f612e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
]

transcript_start = """\
          <div id="hypertranscript###" class="hyperaudio-transcript" style="resize: vertical; overflow-y:scroll; height:800px; width: 97%; scrollbar-gutter: stable; position:relative; border-style:dashed; border-width: 1px; border-color:#999; padding: 8px">
          <article><section>"""


transcript_end = dedent("""\
          </section></article>
          </div>""")

body_end = dedent("""\
          <script src="https://w.soundcloud.com/player/api.js"></script>
          <script src="js/hyperaudio-lite.js"></script>
          <script src="js/hyperaudio-lite-extension.js"></script>
          <script>
          // minimizedMode is still experimental - it aims to show the current words in the title, which can be seen on the browser tab.
          let minimizedMode = false;
          let autoScroll = true;
          let doubleClick = false;
          let webMonetization = false;
    
          new HyperaudioLite("hypertranscript1", "hyperplayer1", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript2", "hyperplayer2", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript3", "hyperplayer3", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript4", "hyperplayer4", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript5", "hyperplayer5", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript6", "hyperplayer6", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript7", "hyperplayer7", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript8", "hyperplayer8", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript9", "hyperplayer9", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript10", "hyperplayer10", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript11", "hyperplayer11", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript12", "hyperplayer12", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript13", "hyperplayer13", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript14", "hyperplayer14", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript15", "hyperplayer15", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript16", "hyperplayer16", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript17", "hyperplayer17", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript18", "hyperplayer18", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript19", "hyperplayer19", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript20", "hyperplayer20", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript21", "hyperplayer21", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript22", "hyperplayer22", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript23", "hyperplayer23", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript24", "hyperplayer24", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript25", "hyperplayer25", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript26", "hyperplayer26", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript27", "hyperplayer27", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript28", "hyperplayer28", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript29", "hyperplayer29", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript30", "hyperplayer30", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript31", "hyperplayer31", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript32", "hyperplayer32", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript33", "hyperplayer33", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript34", "hyperplayer34", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript35", "hyperplayer35", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript36", "hyperplayer36", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript37", "hyperplayer37", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript38", "hyperplayer38", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript39", "hyperplayer39", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript40", "hyperplayer40", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript41", "hyperplayer41", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript42", "hyperplayer42", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript43", "hyperplayer43", minimizedMode, autoScroll, doubleClick, webMonetization);
          </script>
          <script>
            var coll = document.getElementsByClassName("collapsible");
            var i;
            
            for (i = 0; i < coll.length; i++) {
              coll[i].addEventListener("click", function() {
                this.classList.toggle("active");
                var content = this.nextElementSibling;
                if (content.style.display === "block") {
                  content.style.display = "none";
                } else {
                  content.style.display = "block";
                }
              });
            }
          </script>
      </body>
    </html>""")