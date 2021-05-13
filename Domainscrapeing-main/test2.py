from bs4 import *

testtr = """<tr class="srRow1" id="s_tr1_347793720f" onmouseout="s_tr_setBgColor('347793720f','white');" onmouseover="s_tr_setBgColor('347793720f','#E4EFC5');">
<td align="center" class="srCol1" style="border-left:1px solid #CECECE;"><input id="hidMS347793720f" name="hidMS347793720" type="hidden" value="O"/><input id="chkMS347793720f" onclick="chkMS_Click('347793720f', '$1750 oder mehr anbieten', 1750);" type="checkbox"/></td>
<td class="srCol1" style="border-right:0px;"> </td>
<td align="left" class="srCol1" onclick="RecordClick(event, '37020', '');s_ShowAuctionDetails('347793720f', 'Featured');" style="padding-left:0px;min-width:297px;font-size:14px;"><span class="OneLinkNoTx" style="cursor:pointer;color:black;text-decoration:none;font-weight:700;" title="Details anzeigen für gettherapeutics.com"><img align="left" alt="" height="14" id="imgDomDet_347793720f" src="https://img5.wsimg.com/dna/5/hp/btn_grey_plus.png" style="margin-right:5px;" width="14"/>gettherapeutics.com</span></td>
<td align="right" class="srCol1"> 0</td>
<td align="right" class="srCol1">-  </td>
<td align="right" class="srCol1">-  </td>
<td align="right" class="srCol1">€15.423 *</td><td align="center" class="srCol1" style="padding-left:25px;height:46px;"><div id="s_bid_div1_347793720f" style="display:inline;"><span style="white-space:nowrap;">USD$ <input class="input-sm" id="s_bid347793720f" onblur="s_bid_blur('347793720f', '$1,750 oder mehr anbieten', 1750);" onfocus="s_bid_focus('347793720f');" onkeydown="var keyCode = event.keyCode ? event.keyCode : event.which ? event.which : event.charCode;if(keyCode == 13){s_reviewSelectedGo();return false;}" onkeyup="validateItem(this,1750);" style="color:gray;font:11px Arial;width:auto;" type="text" value="$1,750 oder mehr anbieten"/></span><br/>  oder <a href="javascript:void(0);" onclick="s_buyNow_click('347793720f', true);">Sofortkauf</a> für $18,830 *</div><div id="s_bid_div2_347793720f" style="display:none;">Kaufen für $18,830 * <a href="javascript:void(0);" onclick="RecordClick(event, '45052', 'GoToCart');s_gotocart_click();">Zum Warenkorb</a><br/>oder <a href="javascript:void(0);" onclick="s_buyNow_click('347793720f', false);">Stattdessen Angebot abgeben</a></div></td>
<td align="right" class="srCol1" style="border-right:1px solid #CECECE;">1D 8H  </td>
</tr>"""

soup = BeautifulSoup(testtr, "html.parser")

#print(soup.prettify())
tds = soup.find_all("td")
print(len(tds))
#get domainname
print(tds[2])

#get bids
#print(tds[3].get_text())

#get traffic
#print(tds[4].get_text())

#get estimated value
#print(tds[5].get_text())

#get price
#print(tds[6].get_text())

#get time left
#print(tds[8].get_text())


def tr_processing(tr_html):

    soup = BeautifulSoup(tr_html, "html.parser")
    tds = soup.find_all("td")

    domainname = tds[2].find("span").get_text().replace("\xa0", "")
    bids = tds[3].get_text().replace("\xa0", "")
    traffic = tds[4].get_text().replace("\xa0", "")
    estimated_value = tds[5].get_text().replace("\xa0", "")
    price = tds[6].get_text().replace("\xa0", "")
    time_left = tds[8].get_text().replace("\xa0", "")

    info_list =[domainname, bids, traffic, estimated_value, price, time_left]

    return info_list

#print(tr_processing(testtr))
