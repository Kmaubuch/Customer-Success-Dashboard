Synapse Workspace - Customer Success Datasets

Files:
1. support_tickets.csv
2. support_satisfaction.csv
3. customers.csv

Notes:
- All CSV files use UTF-8-SIG encoding for compatibility with Excel and analytics tools.
- Dates use YYYY-MM-DD format.

1. support_tickets.csv
Variable		Description
TicketID		Unique identifier for each support ticket.
CustomerID		Unique identifier for the customer who submitted the ticket.
SubscriptionPlan	Customer's current subscription plan.
TicketCategory		Primary issue or request category.
Priority		Ticket priority (Low, Medium, High, or Urgent).
Channel			Channel used to submit the request.
SubmittedDate		Date the ticket was submitted (YYYY-MM-DD).
ResolvedDate		Date the ticket was resolved (YYYY-MM-DD).
ResolutionDays		Number of days required to resolve the ticket.
Status			Current ticket status.

2. support_satisfaction.csv
Variable		Description
CustomerID		Unique identifier for each customer.
Industry		Customer industry.
CompanySize		Customer company size.
Country			Customer country.
CustomerSegment	        Customer segment.
SubscriptionPlan	Customer's current subscription plan.
TicketCount		Total number of support tickets submitted by the customer.
AvgResolutionDays	Mean ResolutionDays across the customer's tickets, rounded to two decimals.
HighPriorityTickets	Number of tickets with High or Urgent priority.
MostCommonCategory	Most frequently submitted ticket category. If categories are tied, one tied category is shown.
OverallSupportRating	Overall support satisfaction rating (1-5).
SupportRecommendScore	Likelihood of recommending Synapse Workspace based on the support experience (0-10).
SupportSentiment	Support feedback classification (Satisfied or Neutral).
SupportFeedbackDate	Date the customer submitted support feedback (YYYY-MM-DD).
SupportComment		Written feedback about the support experience.

3. customers.csv
Variable		Description
CustomerID		Unique identifier for each customer.
CompanyName		Name of the customer organization.
Industry		Primary industry of the customer organization.
CompanySize		Company size category (Small, Mid-Market, or Enterprise).
Country			Country where the customer organization is located.
CustomerSegment	Customer market segment served by Synapse Workspace.
JoinMonth		Month number within the 24-month customer acquisition window (1-24).
OnboardingScore	Overall onboarding success score. Higher values indicate a smoother onboarding experience.
