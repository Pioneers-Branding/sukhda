window.addEventListener('load',function(){setTimeout(function(){
function rgb(s){var m=s.match(/[\d.]+/g);return m?m.map(Number):null}
function lum(c){var a=c.slice(0,3).map(function(v){v/=255;return v<=0.03928?v/12.92:Math.pow((v+0.055)/1.055,2.4)});return .2126*a[0]+.7152*a[1]+.0722*a[2]}
function bgOf(el){while(el&&el!==document.documentElement){var cs=getComputedStyle(el);var c=rgb(cs.backgroundColor);if(c&&(c.length<4||c[3]>0.5))return c;var bi=cs.backgroundImage;if(bi&&bi.indexOf('gradient')>-1){var m=bi.match(/rgba?\([^)]*\)|#[0-9a-f]{6}/gi);if(m){var x=m[m.length-1];if(x[0]=='#')return [parseInt(x.substr(1,2),16),parseInt(x.substr(3,2),16),parseInt(x.substr(5,2),16)];var r=rgb(x);if(!r[3]||r[3]>0.5)return r;}}el=el.parentElement}return [255,255,255]}
var out=[],seen={};
document.querySelectorAll('body *').forEach(function(el){
 if(el.closest('.ss-overlay,footer,.top,.top-bar,.nav,header'))return;
 var t=Array.prototype.some.call(el.childNodes,function(n){return n.nodeType==3&&n.textContent.trim().length>1});
 if(!t||!el.offsetParent)return;
 var c=rgb(getComputedStyle(el).color); if(!(c[1]>c[0]+30&&c[1]>c[2]+30))return;
 var b=bgOf(el);var L1=lum(c),L2=lum(b);var r=(Math.max(L1,L2)+.05)/(Math.min(L1,L2)+.05);
 if(r<3.5){var k=el.className+'|'+el.textContent.trim().slice(0,40);if(!seen[k]){seen[k]=1;out.push(r.toFixed(2)+' <'+el.tagName.toLowerCase()+' class="'+el.className+'"> '+el.textContent.trim().replace(/\s+/g,' ').slice(0,50))}}
});
var p=document.createElement('pre');p.id='zzscan';p.textContent='ZZ'+JSON.stringify(out);document.body.appendChild(p);
},1500)});
