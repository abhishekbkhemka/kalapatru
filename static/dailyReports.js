console.log("loaded");
	var SALECOUNT = 0;
	var PURCHASECOUNT = 0;
	var EXPENSECOUNT = 0;

	var saleList ={};
	var purchaseList = {};
	var expenseList = {};
	var totalCashPurchase = 0;
	var totalCreditPurchase = 0;
	var otherExpense = 0;
	var otherCashIn = 0;
	var diffinCash = 0
	
			$(document).ready(function(){
				
				var todayDate = new Date();
				$("#todaydate").text(todayDate)
  $("input").focusout(function(){
    calcuateDayDifference();
  });



			});
			
		
$(document).on('submit', '#miscsaleform', function() { 
			SALECOUNT = SALECOUNT +1
			var rowId = SALECOUNT
			var td = "<tr id='sale"+rowId+"'><td><label>Sale Name :  "+$("#miscSaleType").val()+"&nbsp;&nbsp;&nbsp;&nbsp; Rs :"+$("#miscSale").val() +"</tr>"
			var input = "<td><a onclick='removeMiscSale("+rowId+")' class='ui-input-clear ui-btn ui-icon-delete ui-btn-icon-notext ui-corner-all' /></td>"

			$("#miscSaleTable").append(td)
			$("#sale"+rowId).append(input)
			saleList[rowId] ={miscCashInName:$("#miscSaleType").val(),miscCashInAmount:parseInt($("#miscSale").val())} 
			otherCashIn = otherCashIn + parseInt($("#miscSale").val())
			$("#otherCashIn").text(otherCashIn)
			$("#miscSaleType").val('') ;
			$("#miscSale").val('') ;
			calcuateDayDifference();
 			return false
})
		
		
		
		$(document).on('submit', '#purchaseform', function() { 
					PURCHASECOUNT = PURCHASECOUNT +1
					var rowId = PURCHASECOUNT
					var td = "<tr id='purchase"+rowId+"'><td><label> Supplier Name : "+$("#purchasePartyName").val()+"&nbsp;&nbsp;&nbsp;&nbsp; Rs : "+$("#purchasePartyAmount").val() +" &nbsp;&nbsp;&nbsp;&nbsp; Type - "+$("#transactionType").val()+"</tr>"
					var input = "<td><a onclick='removePurchase("+rowId+")' class='ui-input-clear ui-btn ui-icon-delete ui-btn-icon-notext ui-corner-all' /></td>"

					$("#purchaseTable").append(td)
					$("#purchase"+rowId).append(input)
					purchaseList[rowId] ={supplierName:$("#purchasePartyName").val() ,purchaseAmount:parseInt($("#purchasePartyAmount").val()),transactionType:$("#transactionType").val()}
					if($("#transactionType").val() == 'Cash'){
						totalCashPurchase = totalCashPurchase + parseInt($("#purchasePartyAmount").val())
						$("#totalCashPurchase").text(totalCashPurchase)

					}else{
						totalCreditPurchase = totalCreditPurchase + parseInt($("#purchasePartyAmount").val())
						$("#totalCreditPurchase").text(totalCreditPurchase)
					}
				
					$("#purchasePartyName").val('') ;
					$("#purchasePartyAmount").val('') ;
					calcuateDayDifference();
				
		 			return false
		})
		
		$(document).on('submit', '#expenseform', function() {
                       
					EXPENSECOUNT = EXPENSECOUNT +1
					var rowId = EXPENSECOUNT
					var td = "<tr id='expense"+rowId+"'><td><label> Expense Name : "+$("#expenseName").val()+"&nbsp;&nbsp;&nbsp;&nbsp; Rs : "+$("#expenseAmount").val() +"</tr>"
					var input = "<td><a onclick='removeExpense("+rowId+")' class='ui-input-clear ui-btn ui-icon-delete ui-btn-icon-notext ui-corner-all' /></td>"

					$("#expenseTable").append(td)
					$("#expense"+rowId).append(input)
					expenseList[rowId] ={expenseAmount:parseInt($("#expenseAmount").val()),expenseName:$("#expenseName").val() }
					otherExpense = otherExpense + parseInt($("#expenseAmount").val())  ;
					$("#otherExpense").text(otherExpense) 
					$("#expenseName").val('') ;
					$("#expenseAmount").val('') ;
					calcuateDayDifference();
					

		 			return false
		})
		

			function removeMiscSale(Id){
				$("#sale"+Id).remove();
				var miscCash = saleList[Id+''] 
				otherCashIn = otherCashIn - miscCash.miscCashInAmount  ;
			$("#otherCashIn").text(otherCashIn)
				delete saleList[Id+''] 
				
				SALECOUNT = SALECOUNT -1
			calcuateDayDifference()

			}
			
			function removePurchase(Id){
				$("#purchase"+Id).remove();
				var purchase = purchaseList[Id+''] 
				if(purchase.transactionType == 'Cash'){
					totalCashPurchase = totalCashPurchase - purchase.purchaseAmount
					$("#totalCashPurchase").text(totalCashPurchase)
					
				}else{
					totalCreditPurchase = totalCreditPurchase - purchase.purchaseAmount
					$("#totalCreditPurchase").text( totalCreditPurchase)
				}
					
					delete purchaseList[Id+''] 
					PURCHASECOUNT = PURCHASECOUNT -1;
			calcuateDayDifference()
			

			}
			
			function removeExpense(Id){
				
				
				$("#expense"+Id).remove();
				var expense = expenseList[Id+''] 
				otherExpense = otherExpense - expense.expenseAmount  ;
				$("#otherExpense").text(otherExpense)
				delete expenseList[Id+''] 
				EXPENSECOUNT = EXPENSECOUNT -1;
			calcuateDayDifference()
			

			}
			
			
			
			function submitPage(){
                document.getElementById("orderSubmitButton").disabled = true
				if(diffinCash < 0 ){
					var onclick = confirm('Your day difference is in negative. You sure you want to continue ?')
					
					if(onclick){
						return send()
					}
					
				}else{
					return send()
				}
				
				
			}
			
			function send(){
					requestList = {};
					requestList['Date'] = $("#todaydate").text()
					requestList['BranchName'] = $("#branchName").val() 
                                       

					requestList['openingBalance'] = parseInt($("#openingBalance").val());
										requestList['dayCashSale'] = parseInt($("#cashsale").val());
										requestList['dayCreditSale'] = parseInt($("#creditsale").val());
										requestList['dayCardSale'] = parseInt($("#cardsale").val());
										requestList['TotalMiscCashIn'] = otherCashIn;
										requestList['miscCashInDetails'] = saleList;
										
										requestList['totalCashPurchase'] = parseInt($("#totalCashPurchase").text());
										requestList['totalCreditPurchase'] = parseInt($("#totalCreditPurchase").text());
										requestList['cashInhand'] = parseInt($("#cashInhand").val());
										requestList['DayCashDifference'] = parseInt($("#differenceAmount").text());
										requestList['purchaseDetail'] = purchaseList;
										requestList['expensesDetail'] = expenseList;
                                        requestList['totalExpense'] = otherExpense;
                                        requestList['bankDeposit'] = parseInt($("#bankDeposit").val());
                                      
					
					
					
					
					
					$.ajax({
					        url: "http://localhost:8000/dailyreport/",
					        type: "POST",
					        headers: { "X-CSRFToken": token },
                            data: {data:JSON.stringify(requestList),
                                csrfmiddlewaretoken: '{{ csrf_token }}'},
							dataType:"json",
					        success:function(data){
					           if(data.status == 'success'){
													window.location = "thankyoureport.html"
																					}else{
																							window.location = "error.html"
																					}

					        

					        }
					    });
			}
			function calcuateDayDifference(){
		//		try{
			
				var totalCashSale = parseInt($("#cashsale").val());
				if(isNaN(totalCashSale)){
					totalCashSale = 0
				}
					var openingBalance = parseInt($("#openingBalance").val())
				if(isNaN(openingBalance)){
					openingBalance = 0;
				}
		
				
				var totalCashExpense = otherExpense + totalCashPurchase;
				// alert(totalCashExpense)
				var totalCashToBe =  (totalCashSale +openingBalance+otherCashIn) ;
				var cashInHand = parseInt($("#cashInhand").val()) 
				var bankDeposit = parseInt($("#bankDeposit").val()) 
                                bankDeposit = isNaN(bankDeposit) ? 0 : bankDeposit
				if(isNaN(cashInHand)){
					cashInHand = 0;
				}
			     
				diffinCash = (cashInHand+totalCashExpense+bankDeposit)- totalCashToBe
				var color = 'black'
				if(diffinCash < 0){
					color = 'red'
				}
				$("#differenceAmount").text(diffinCash);
				$("#differenceAmount").css('color',color);
				
		//	}catch(err){
		//		
		//	}
				
				
			}
		