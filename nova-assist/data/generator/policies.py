"""Nova Bank policy & FAQ library (fictional). Each doc: id, title, category, effective_date, body (markdown)."""

POLICIES = [
("POL-01", "Account fees – personal accounts", "fees", """
## §1 Monthly maintenance fee
| Plan | Monthly fee | Waiver |
| --- | --- | --- |
| Basic | EGP 25 | Waived when the average monthly balance is EGP 5,000 or more |
| Plus | EGP 15 | No waiver |
| Premier | EGP 0 | — |

The fee is charged on the 1st of each month for the previous month and appears as "Nova Bank Fee – Monthly maintenance".

## §2 SMS alerts
SMS transaction alerts cost EGP 5 per month for Basic and Plus customers who opt in. Premier customers receive SMS alerts free. In-app push notifications are always free.

## §3 Paper statements
E-statements in the app are free. Each paper statement mailed to the customer costs EGP 30 (see POL-14).

## §4 Where fees appear
Every fee is a separate line in the transaction history with the prefix "Nova Bank Fee –" and the fee name.
"""),
("POL-02", "Card fees", "fees", """
## §1 Debit cards
- First debit card: free.
- Replacement for a lost or stolen debit card: EGP 100.
- Replacement for a damaged or expired debit card: free.

## §2 Credit cards
- Annual fee: Classic credit card EGP 300; Premier credit card free.
- Replacement for a lost or stolen credit card: EGP 150.
- Late payment fee: EGP 150 when the minimum payment is not received by the due date.

## §3 Express delivery
Standard card delivery is free (5–7 business days). Express delivery (2 business days, Cairo, Giza and Alexandria only) costs EGP 75.
"""),
("POL-03", "ATM and transfer fees", "fees", """
## §1 ATM withdrawals in Egypt
- Nova Bank ATMs: free.
- Other banks' ATMs in Egypt: EGP 5 per withdrawal. Plus customers get their first 5 other-bank withdrawals each month free. Premier customers pay no other-bank ATM fees.
- Balance inquiry at another bank's ATM: EGP 2.

## §2 ATM withdrawals abroad
EGP 40 per withdrawal, plus the 3% international transaction fee in POL-04.

## §3 Transfers
- Transfers between Nova Bank accounts: free.
- Instant transfers to other Egyptian banks: 0.1% of the amount, minimum EGP 1, maximum EGP 20.
"""),
("POL-04", "International and foreign-currency transactions", "fees", """
## §1 International transaction fee
Card payments in a foreign currency, or with a merchant registered outside Egypt, carry a 3% international transaction fee on the EGP amount.

## §2 How it appears
The fee is posted as a separate line, "Nova Bank Fee – International transaction 3%", on the same day as the purchase or the next business day.

## §3 Exchange rate
Foreign-currency amounts are converted at Nova Bank's card exchange rate on the day the transaction posts. Pending amounts may change slightly when they post.
"""),
("POL-05", "Overdraft rules", "overdraft", """
## §1 Eligibility
Overdraft Protection is available to Plus and Premier customers who opt in through the app. Limit: up to EGP 5,000, set by the credit team.

## §2 Overdraft fee
EGP 50 for each day the account ends the day below zero, up to 3 overdraft fees per calendar month. No fee is charged if the account is overdrawn by EGP 100 or less.

## §3 Without Overdraft Protection
Card payments that would overdraw the account are declined. There is no fee for a declined payment.

## §4 Bringing the account back
Any deposit or incoming transfer is applied to the overdrawn balance first.
"""),
("POL-06", "Transaction dispute process", "disputes", """
## §1 Who can dispute
A customer can dispute a card transaction they do not recognise, were charged twice for, did not receive goods or services for, or that differs from the agreed amount.

## §2 Time limit
Disputes must be raised within 60 days of the transaction date.

## §3 How to raise a dispute
Through the app (Transaction → Report a problem), web, chat or phone. The customer is asked for the reason and any evidence (receipt, cancellation email).

## §4 Timeline
- Acknowledgement: within 2 business days.
- Provisional credit for suspected fraud: within 10 business days, while the investigation continues.
- Final decision: within 45 days of filing. Complex merchant cases can take up to 90 days; the customer is told if this applies.

## §5 Decisions
Only Nova Bank's Disputes Operations team can approve or reject a dispute. Contact-center agents and the digital assistant can report status and file a dispute request but cannot approve, reject or promise an outcome.
"""),
("POL-07", "Dispute statuses explained", "disputes", """
## §1 Statuses
| Status | Meaning for the customer |
| --- | --- |
| Submitted | We received the dispute; it will be acknowledged within 2 business days. |
| Under review | Disputes Operations is investigating and may contact the merchant. |
| Provisional credit issued | A temporary credit was added while we investigate. It becomes final if the dispute is decided in your favour. |
| Resolved – in your favour | The dispute was accepted. Any provisional credit is now final, or a credit is posted within 5 business days. |
| Resolved – not upheld | The evidence supported the merchant. Any provisional credit is reversed with 5 business days' notice. |

## §2 Appeals
A customer who disagrees with a "not upheld" decision can ask for a review within 30 days by contacting the contact center with new evidence.
"""),
("POL-08", "Unauthorised and fraudulent transactions", "disputes", """
## §1 What to do first
If a transaction looks like fraud, block the card immediately in the app (Cards → Block card) or by calling the contact center, then raise a dispute (POL-06).

## §2 Customer liability
Customers are not liable for unauthorised transactions reported within 60 days, unless they shared their PIN, OTP or card details.

## §3 Nova Bank will never ask
Nova Bank staff and the digital assistant will never ask for a full card number, PIN, OTP or password.
"""),
("POL-09", "Card replacement – lost or stolen", "cards", """
## §1 Steps
1. Block the card immediately (app: Cards → Block card, or the contact center 24/7).
2. Request a replacement in the app or through the contact center.
3. Cards Operations confirms the request and issues a new card with a new number.

## §2 Fees and delivery
Replacement fee: EGP 100 (debit) or EGP 150 (credit), see POL-02. Standard delivery 5–7 business days; express 2 business days for EGP 75.

## §3 After replacement
Recurring payments linked to the old card must be updated by the customer. The old card cannot be reactivated once reported lost or stolen.
"""),
("POL-10", "Card replacement – damaged or expired", "cards", """
## §1 Damaged cards
A damaged card is replaced free of charge with the same card number and a new expiry date and CVV. The old card keeps working until the new one is activated.

## §2 Expiring cards
Cards are renewed automatically and sent 30 days before expiry, free of charge, to the address on file.

## §3 Activation
New cards are activated in the app (Cards → Activate) or at any Nova Bank ATM with the PIN.
"""),
("POL-11", "Blocking and unblocking cards", "cards", """
## §1 Temporary block
Customers can freeze a card in the app and unfreeze it at any time. Pending transactions still post.

## §2 Permanent block
A card reported lost or stolen is permanently blocked and cannot be unblocked. A replacement is needed (POL-09).

## §3 Bank-initiated blocks
Nova Bank may block a card for suspected fraud. The customer is notified by push notification and SMS and must contact the contact center to verify recent transactions.
"""),
("POL-12", "Pending and posted transactions", "transactions", """
## §1 Pending
A pending transaction is authorised but not yet settled by the merchant. It reduces the available balance. Most pending card transactions post within 1–3 business days.

## §2 Amount changes
Hotels, fuel stations and foreign merchants may post a different final amount from the pending amount.

## §3 Dropped authorisations
If a merchant does not settle within 7 days, the pending amount is released automatically.

## §4 Disputes on pending transactions
A pending transaction cannot be disputed until it posts.
"""),
("POL-13", "Fee review and refund policy", "fees", """
## §1 Who can refund a fee
- Contact-center agents may refund one fee of up to EGP 100 per customer in any 12-month period, for a first occurrence.
- Supervisors may refund fees up to EGP 500.
- Larger amounts need Branch Operations approval.

## §2 Digital assistant
The digital assistant cannot refund or waive fees. It can explain a fee and submit a fee review request, which an agent decides within 3 business days.

## §3 Not refundable
Card replacement fees for lost or stolen cards and fees older than 90 days are not refundable.
"""),
("POL-14", "Account statements", "accounts", """
## §1 E-statements
Monthly e-statements are available in the app and web for the last 24 months, free.

## §2 Paper and stamped statements
Paper statements by mail: EGP 30 each. Stamped statements for embassies or official use: EGP 50, ready at a branch within 2 business days.

## §3 Custom periods
Customers can download a statement for any custom date range in the app (Accounts → Statements).
"""),
("POL-15", "Service plans", "accounts", """
## §1 Plans
| Plan | Monthly fee | Other-bank ATM | Overdraft Protection | SMS alerts |
| --- | --- | --- | --- | --- |
| Basic | EGP 25 (waived at EGP 5,000 average balance) | EGP 5 each | Not available | EGP 5/month |
| Plus | EGP 15 | 5 free a month, then EGP 5 | Optional | EGP 5/month |
| Premier | Free | Free | Optional | Free |

## §2 Changing plans
Customers can change plan in the app. The new plan starts on the 1st of the next month.
"""),
("POL-16", "Customer identity and data privacy in support", "privacy", """
## §1 Identity
Customers using chat in the app or web are already verified by their login. Phone customers are verified with security questions and an OTP.

## §2 Only your own data
Support staff and the digital assistant may only discuss the verified customer's own accounts, cards and transactions. Information about any other customer, including family members, is never shared without that customer's written authorisation on file.

## §3 Sensitive data
Full card numbers, PINs, OTPs and passwords are never requested or displayed. Card numbers are shown as the last 4 digits only.

## §4 Records
Support conversations are recorded and retained according to Nova Bank's records policy.
"""),
("POL-17", "Complaints and escalation", "service", """
## §1 Raising a complaint
Customers can complain through any channel. Every complaint gets a reference number.

## §2 Timeline
Acknowledgement within 1 business day; response within 10 business days.

## §3 Escalation
If the customer is not satisfied, they can ask for escalation to a supervisor and then to Nova Bank's Customer Advocacy team.

## §4 Talking to a person
A customer can ask to speak to an agent at any time; the digital assistant must hand over with a summary of the conversation.
"""),
("POL-18", "SMB business account fees", "fees", """
## §1 Monthly fee
SMB Business accounts: EGP 75 per month, charged on the 1st.

## §2 Included
Unlimited transfers between Nova accounts, 20 instant transfers to other banks per month, two debit cards.

## §3 Additional fees
Instant transfers beyond 20 per month follow POL-03 §3. Extra debit cards: EGP 100 each. Cheque books: EGP 60.
"""),
("POL-19", "Personal and SMB loans – product information", "loans", """
## §1 Personal loans
Unsecured personal loans up to EGP 500,000, terms from 12 to 60 months.

## §2 How decisions are made
All loan and credit decisions are made by Nova Bank's credit team after a full assessment. Neither contact-center agents nor the digital assistant can approve, pre-approve, or promise a loan, limit or rate.

## §3 SMB financing
SMB loan applications are reviewed by the SMB credit team. Current average review time is 9 business days.

## §4 Applying
Customers apply in the app (Loans → Apply) or at a branch.
"""),
("POL-20", "Contact channels and service hours", "service", """
## §1 Channels
- In-app and web chat: digital assistant 24/7; agents 8:00–22:00 daily.
- Phone: 24/7 for lost or stolen cards and fraud; other requests 8:00–22:00.
- Branches: Sunday–Thursday, 8:30–15:00.

## §2 Response times
Chat: typically under 5 minutes during agent hours. Requests handed over outside agent hours are answered the next morning.
"""),
]

EFFECTIVE = {
    "POL-05": "2026-03-01", "POL-06": "2026-01-15", "POL-13": "2026-05-01", "POL-16": "2026-02-01",
}
