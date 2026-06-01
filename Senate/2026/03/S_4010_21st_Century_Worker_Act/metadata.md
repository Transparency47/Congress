# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4010?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4010
- Title: 21st Century Worker Act
- Congress: 119
- Bill type: S
- Bill number: 4010
- Origin chamber: Senate
- Introduced date: 2026-03-05
- Update date: 2026-03-24T16:48:21Z
- Update date including text: 2026-03-24T16:48:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-05: Introduced in Senate
- 2026-03-05 - IntroReferral: Introduced in Senate
- 2026-03-05 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-03-05: Introduced in Senate

## Actions

- 2026-03-05 - IntroReferral: Introduced in Senate
- 2026-03-05 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-05",
    "latestAction": {
      "actionDate": "2026-03-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4010",
    "number": "4010",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "21st Century Worker Act",
    "type": "S",
    "updateDate": "2026-03-24T16:48:21Z",
    "updateDateIncludingText": "2026-03-24T16:48:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-05",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2026-03-05T18:58:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "AL"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4010is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4010\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2026 Mr. Lee introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo clarify the classification of service provider payees as employees or independent contractors in Federal law.\n#### 1. Short title\nThis Act may be cited as the 21st Century Worker Act .\n#### 2. Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title.\nSec. 2. Table of contents.\nTITLE I\u2014Classification of service provider payees\nSec. 101. Definitions.\nSec. 102. Classification.\nSec. 103. Mandatory independent contractor classification.\nSec. 104. Mandatory employee classification.\nSec. 105. Elective classification service provider payees.\nSec. 106. Change in classification; periodic classification review.\nTITLE II\u2014Application to other laws\nSec. 201. Fair Labor Standards Act of 1938.\nSec. 202. National Labor Relations Act.\nSec. 203. Tax classification.\nSec. 204. GAO study on changes needed to other Federal laws.\nI\nClassification of service provider payees\n#### 101. Definitions\nIn this title:\n**(1) Bona fide sole proprietor**\nThe term bona fide sole proprietor means a service provider payee who\u2014\n**(A)**\nhas entered into a written contract governing the terms of the goods or services provided to a service recipient payor and the contract is not an employment by agreement;\n**(B)**\nis not required to provide the goods or services exclusively for the service recipient payor; and\n**(C)**\nhas not had a substantial economic relationship or employment by agreement with the service recipient payor as described in section 104 during the previous calendar year.\n**(2) Business entity**\nThe term business entity \u2014\n**(A)**\nmeans a corporation, limited liability company, limited partnership, limited liability partnership, limited liability limited partnership, statutory business trust, or a similar entity formed under the laws of the United States, under the law of a State or United States territory (including the District of Columbia), or under the laws of a foreign country; and\n**(B)**\nincludes a general partnership not described in subparagraph (A) that has registered to do business under State or local law.\n**(3) Compensation**\n**(A) In general**\nThe term compensation \u2014\n**(i)**\nmeans consideration paid by a service recipient payor to a service provider payee for goods or services provided; and\n**(ii)**\nincludes payments in money, payments in property, wages, salaries, benefits, and other types of payment.\n**(B) Fair market value**\nFor purposes of determining the amount of compensation, the value of payments in a form other than legal tender shall be determined by the fair market value of the payment on the date of payment.\n**(4) Direct sales service provider payee**\nThe term direct sales service provider payee means a service provider payee who is a direct seller, as defined in section 3508(b) of the Internal Revenue Code of 1986.\n**(5) Elective classification service provider payee**\nThe term elective classification service provider payee means a service provider payee who is not classified as either\u2014\n**(A)**\na mandatory independent contractor under section 103; or\n**(B)**\na mandatory employee under section 104.\n**(6) Employee**\nThe term employee means an individual who\u2014\n**(A)**\nis a service provider payee; and\n**(B)**\nis\u2014\n**(i)**\nclassified as a mandatory employee under section 104; or\n**(ii)**\nclassified as an employee under section 105.\n**(7) Employer**\nThe term employer means a service recipient payor\u2014\n**(A)**\nthat is in a substantial economic relationship with a service provider payee who is classified as an employee under section 104 with respect to the service recipient payor;\n**(B)**\nthat has entered into employment by agreement under section 104 with a service provider payee; or\n**(C)**\nfor whom a service recipient payee has elected to be classified as an employee under section 105.\n**(8) Employment by agreement**\nThe term employment by agreement means an agreement, whether written or otherwise, between a service recipient payor and a service provider payee that demonstrably expresses their mutual intent to form an employer-employee relationship.\n**(9) Formal bona fide contractor**\nThe term formal bona fide contractor , when used with respect to a service provider payee providing goods or services to a service recipient payor, means a service provider payee who\u2014\n**(A)**\nis recognized as a contractor under applicable State law; or\n**(B)**\nis not required to provide the goods or services exclusively for the service recipient payor and has\u2014\n**(i)**\nentered into a written contract governing the terms of the goods or services provided to the service recipient payor that is not designated as an employment by agreement;\n**(ii)**\nincurred unreimbursed expenses related to providing the goods or services to the service recipient payor annually that exceed 5 percent of the total compensation made to the service provider payee by the service recipient payor; and\n**(iii)**\nnot had a substantial economic relationship or employment by agreement with the service recipient payor as described in section 104 during the previous calendar year.\n**(10) Independent contractor**\nThe term independent contractor means a service provider payee who\u2014\n**(A)**\nis classified as a mandatory independent contractor under section 103; or\n**(B)**\nis classified as an independent contractor under section 105.\n**(11) Licensed profession, trade, or occupation**\nThe term licensed profession, trade, or occupation means a profession, trade, or occupation that may not be lawfully engaged in unless a license from a Federal, State, or local government is obtained.\n**(12) Limited economic relationship**\nThe term limited economic relationship means an economic relationship between a service recipient payor and a service provider payee under which\u2014\n**(A)**\nthe compensation to the service provider payee by the service recipient payor is based on a period of time worked;\n**(B)**\nthe period of time worked for which the service provider payee is compensated by the service recipient payor is less than 30 days per calendar quarter; and\n**(C)**\nthe service provider payee is not required to provide the goods or services exclusively for the service recipient payor.\n**(13) Money**\nThe term money means any legal tender as defined in section 5103 of title 31, United States Code.\n**(14) Period of time worked**\nThe term period of time worked includes any specified period of time worked, including hourly, daily, weekly, bi-weekly, bi-monthly, monthly, quarterly, or annually periods of time.\n**(15) Sales commission**\nThe term sales commission means compensation based on sales made by the service provider payee or by individuals managed, supervised, advised, or recruited by the service provider payee.\n**(16) Secretary**\nThe term Secretary means the Secretary of Labor.\n**(17) Service provider payee**\nThe term service provider payee means an individual providing goods or services to a service recipient payor in return for compensation paid to the individual by the service recipient payor.\n**(18) Service recipient payor**\nThe term service recipient payor means a person receiving goods or services from a service provider payee in return for compensation paid by the person to the service provider payee.\n**(19) Substantial economic relationship**\nThe term substantial economic relationship means an economic relationship between a service recipient payor and a service provider payee where\u2014\n**(A)**\nthe service provider payee is a natural person;\n**(B)**\nmore than 75 percent of the compensation to the service provider payee by the service recipient payor is based on a period of time worked;\n**(C)**\nthe service recipient payor determines the hours of work; and\n**(D)**\nthe service recipient payor requires the service provider payee to work substantially full-time for the service recipient payor for a period of 4 consecutive weeks or more.\n**(20) Substantially full-time**\nThe term substantially full-time means an average of 30 or more hours per week during the relevant period of time worked.\n**(21) Written contract**\nThe term written contract means writing sufficient to indicate that a contract has been made between the parties that is legally enforceable in the jurisdiction or jurisdictions where the services by the service provider payee are performed or to be performed.\n#### 102. Classification\n##### (a) Bifurcated classification\nFor purposes of this title, a service provider payee shall be classified as either an employee or an independent contractor in accordance with the following:\n**(1) Mandatory independent contractors**\nA service provider payee meeting the requirements of section 103 shall be classified as an independent contractor.\n**(2) Mandatory employee classification**\nA service provider payee meeting the requirements of section 104 shall be classified as an employee.\n**(3) Elective classification service provider payees**\nA service provider payee that meets neither the requirements of section 103 nor the requirements of section 104 shall be classified as the service provider payee elects in accordance with section 105.\n##### (b) Responsibility for initial determination\n**(1) General rule**\nSubject to paragraph (2), the service recipient payor is responsible for determining whether a service provider payee is properly classified as a mandatory independent contractor, a mandatory employee, or an elective classification service provider payee, for purposes of subsection (a).\n**(2) Exceptions**\nThe service provider payee is responsible for determining whether the service provider payee is properly classified as a mandatory independent contractor if the classification of the service provider payee as an independent contractor is based on meeting the requirements of\u2014\n**(A)**\nsection 103(2)(A) (relating to licensed professions, trades, or occupations);\n**(B)**\nsection 103(2)(B) (relating to business entities);\n**(C)**\nsection 103(2)(E) (relating to bona fide sole proprietors); or\n**(D)**\nsection 103(2)(F) (relating to formal bona fide contractors).\n**(3) Timing**\nThe classification determination of a service provider payee shall be made by the service recipient payor or service provider payee (as required under this subsection) immediately upon entering into an economic relationship between the service recipient payor and the service provider payee.\n##### (c) Reclassifications and periodic review\nA service provider payee or a service recipient payor, as applicable, shall reclassify or review the classification determination under this section in accordance with section 106.\n#### 103. Mandatory independent contractor classification\nA service provider payee shall be classified as an independent contractor if the service provider payee\u2014\n**(1)**\nis not classified as an employee pursuant to section 104; and\n**(2)**\nmeets one or more of the following requirements:\n**(A) Licensed profession, trade, or occupation**\nThe service provider payee\u2014\n**(i)**\nis engaged in a licensed profession, trade, or occupation; and\n**(ii)**\nholds himself or herself out as providing services to the public.\n**(B) Business entity**\nThe service provider payee is a business entity.\n**(C) Limited economic relationship**\nThe economic relationship between a service recipient payor and a service provider payee is a limited economic relationship.\n**(D) Direct sales**\nThe service provider payee is a direct sales service provider payee.\n**(E) Bona fide sole proprietor**\nThe service provider payee is a bona fide sole proprietor.\n**(F) Formal bona fide contractor**\nThe service provider payee is a formal bona fide contractor.\n#### 104. Mandatory employee classification\nA service provider payee shall be classified as an employee if the service provider payee meets one or more of the following requirements:\n**(1) Substantial economic relationship**\nThe economic relationship between a service recipient payor and a service provider payee is a substantial economic relationship.\n**(2) Employment by agreement**\nThere is employment by agreement.\n#### 105. Elective classification service provider payees\n##### (a) Elective classification service provider payees; election required\nA service provider payee that does not meet either of the requirements of section 103 or section 104 is an elective classification service provider payee. Each elective classification service provider payee shall elect whether to be classified as an employee or an independent contractor in accordance with this section.\n##### (b) Method of election\nThe elective classification service provider payee shall make the election required by this section in writing upon entering into an economic relationship with a service recipient payor. Subject to subsection (c), the election need not be in any particular form as long as the election\u2014\n**(1)**\nclearly indicates the service provider payee\u2019s intent regarding whether to be classified as an independent contractor or an employee;\n**(2)**\nis dated;\n**(3)**\nis signed by the elective classification service provider payee; and\n**(4)**\nis countersigned by the service recipient payor.\n##### (c) Service recipient payor counter signature required\nThe elective classification service provider payee shall secure the counter-signature of the service recipient payor acknowledging that the service recipient payor knows the classification election made by the service provider payee. The election required under subsection (a) is not effective until the counter-signature of the service recipient payor is secured, subject to subsection (f).\n##### (d) Timing of election\nThe election required under subsection (a) shall be made by the elective classification service provider payee upon entering into an economic relationship with a service recipient payor. Failure by the elective classification service provider payee to make the election required by subsection (a) within 14 days of entering into an economic relationship with a service recipient payor shall be subject to a penalty under subsection (g)(1), subject to subsection (f).\n##### (e) Record-keeping retention requirement\nBoth the elective classification service provider payee and the service recipient payor are required to maintain a copy of the countersigned election required under subsection (b) for a period of 3 years following its countersignature. Failure by the elective classification service provider payee or the service recipient payor to maintain a copy of the countersigned election required by this section shall be subject to a penalty under subsection (g)(2).\n##### (f) Absence of countersignature; default rule\nIn the event that an elective classification service provider payee makes the election required under subsection (a) except that the elective classification service provider payee requests, but does not receive, the countersignature required by subsection (c) within 14 days of entering into an economic relationship with a service recipient payor, the elective classification service provider payee shall be classified as an independent contractor and shall not be in violation of subsection (g)(1).\n##### (g) Penalties\n**(1) Penalty for failure to make election**\nThe Secretary shall impose a penalty not to exceed $100 on an elective classification service provider payee who fails to make the election required by subsection (a) within 14 days of entering into an economic relationship with a service recipient payor.\n**(2) Penalty for failure to keep records relating to election**\nThe Secretary shall impose a penalty not to exceed $100 on elective classification service provider payees or service recipient payors who fail to maintain the records required by subsection (e).\n**(3) Willful or reckless misclassification**\nThe Secretary shall impose a penalty on a service recipient payor or service provider payee responsible for a classification determination under this section who willfully or recklessly misclassifies a service provider payee as an independent contractor in an amount equal to 15 percent of the compensation paid to the independent contractor.\n##### (h) No requirement To enter into economic relationship\nNothing in this title shall be read as a requirement by a service provider payee or a service recipient payor to enter into an economic relationship.\n#### 106. Change in classification; periodic classification review\n##### (a) Major change in the nature of the economic relationship\n**(1) In general**\nIf there is a major change in the nature of the economic relationship between a service provider payee and a service recipient payor, then a new classification determination shall be made by the service recipient payor or service provider payee responsible for classification determination pursuant to section 102(b) upon the major change in the nature of the economic relationship.\n**(2) Major change described**\nFor purposes of this section, a major change in the nature of the economic relationship means an increase or decrease of 25 percent or more in the hours worked by, or the compensation paid to, the service provider payee by the service recipient payor in the most recent calendar quarter compared to the previous calendar quarter.\n**(3) Effective date**\nIf a reclassification determination is made, it shall be effective beginning on the first day of the first month that immediately follows the determination.\n##### (b) Change in classification for other reasons\n**(1) In general**\nIf there is a change in the nature of the economic relationship between a service provider payee and a service recipient payor other than a major change in the nature of the economic relationship described in subsection (a) that a reasonable person should anticipate could change the classification of a service provider payee, then the service recipient payor or service provider payee responsible for classification determination pursuant to section 102(b) shall make a classification determination upon the change in the nature of the economic relationship.\n**(2) Examples**\nChanges in the nature of the economic relationship included under paragraph (1) include, without limitation\u2014\n**(A)**\nthe loss of a license by a service recipient payee;\n**(B)**\nthe forfeiture of a business entity charter by a service recipient payee;\n**(C)**\na change in the relative importance of sales commissions in compensating a direct sales service provider payee; or\n**(D)**\na change in the requirement, or lack thereof, to perform services exclusively for the service recipient payor.\n**(3) Reclassification timing**\nIf a reclassification determination is made, then it shall be made effective with respect to the calendar quarter that begins immediately after the date on which the event giving rise to the change in the nature of the economic relationship occurred.\n##### (c) Periodic review requirement; frequency\n**(1) In general**\nThe service recipient payor or service provider payee responsible for a classification determination under subsection (a) or (b) shall make annual determinations for any continuing economic relationships with service recipient payors or service provider payees, as the case may be. These periodic reviews shall be completed by January 31 with respect to continuing economic relationships as of December 31 of the previous calendar year.\n**(2) Effective date of determination changes**\nIf a reclassification determination is made as a result of this review, it shall be made effective beginning on the first day of the first month that immediately follows the determination.\n##### (d) Exemption\nFor purposes of this section, if a service provider payee does not have more than 100 hours worked or been compensated more than a total of $10,000 during a calendar quarter in which the reclassification determination is made, then the service provider payor or service provider payee, as the case may be, is exempt from the requirements of this section.\nII\nApplication to other laws\n#### 201. Fair Labor Standards Act of 1938\nSection 3 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203 ) is amended\u2014\n**(1)**\nby striking subsection (d) and inserting the following:\n(d) Employer \u2014 (1) except as otherwise provided in this subsection, has the meaning given the term in section 101 of the 21st Century Worker Act ; (2) includes any person (including a public agency) acting directly or indirectly in the interest of an employer in relation to an employee; and (3) does not include any labor organization (other than when acting as an employer) or anyone acting in the capacity of officer or agent of such labor organization. ;\n**(2)**\nby striking paragraph (1) of subsection (e) and inserting the following:\n(1) Except as provided in paragraphs (2), (3), (4), and (5), the term employee has the meaning given the term employee in section 101 of the 21st Century Worker Act . ; and\n**(3)**\nby striking subsection (g) and inserting the following:\n(g) (1) Employ includes to suffer or permit to work under a substantial economic relationship (as defined in section 101 of the 21st Century Worker Act ) between an employer and employee. (2) Employment means the provision of goods or services by an employee for an employer. .\n#### 202. National Labor Relations Act\nSection 2 of the National Labor Relations Act ( 29 U.S.C. 152 ) is amended\u2014\n**(1)**\nby striking paragraph (2) and inserting the following:\n(2) The term employer \u2014 (A) except as otherwise provided in this paragraph, has the meaning given the term in section 101 of the 21st Century Worker Act ; (B) includes any person acting as an agent of an employer, directly or indirectly; and (C) does not include the United States or any wholly owned Government corporation, or any Federal Reserve Bank, or any State or political subdivision thereof, or any person subject to the Railway Labor Act, as amended from time to time, or any labor organization (other than when acting as an employer), or anyone acting in the capacity of officer or agent of such labor organization. ;\n**(2)**\nin paragraph (3), by striking shall include any employee, and shall not be limited to the employees of a particular employer, unless the Act explicitly states otherwise, and shall and inserting , except as otherwise provided in this paragraph, has the meaning given the term employee in section 101 of the 21st Century Worker Act . The term shall include any employee, and shall not be limited to the employees of a particular employer. The term shall ; and\n**(3)**\nby adding at the end the following:\n(15) The term employment means the provision of goods or services by an employee for an employer. .\n#### 203. Tax classification\n##### (a) Employee and employer\nSection 7701(a)(20) of the Internal Revenue Code of 1986 is amended to read as follows:\n(20) Employee and employer The terms employee and employer have the same meaning given such terms in section 101 of the 21st Century Worker Act . .\n##### (b) Employment\nSection 3121(b) of the Internal Revenue Code of 1986 is amended to read as follows:\n(b) The term employment means any services performed by an employee for an employer. .\n##### (c) Conforming amendments\n**(1)**\nSection 3121 of the Internal Revenue Code of 1986 is amended by striking subsection (d).\n**(2)**\nSection 3306(a) of such Code is amended by striking paragraph (3).\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.\n#### 204. GAO study on changes needed to other Federal laws\n##### (a) In general\nNot later than 2 years after the date of enactment of this Act, the Comptroller General of the United States shall prepare and submit to Congress a report that identifies\u2014\n**(1)**\nall covered Federal laws that utilize the terms employee , employer , employ , and employment in ways that do not correspond with the definitions of the terms employee and employer under section 101 of this Act; and\n**(2)**\nhow harmonizing the definitions of employee , employer , employ , and employment across all covered Federal laws would alter each covered Federal law.\n##### (b) Definition of covered Federal law\nIn this section, the term covered Federal law means each of the following:\n**(1)**\nThe Age Discrimination in Employment Act of 1967 ( 29 U.S.C. 621 et seq. ), including subsections (b) and (f) of section 11, and section 15(a), of such Act ( 29 U.S.C. 630(b) and (f); 29 U.S.C. 633a(a) ).\n**(2)**\nThe Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 et seq. ), including paragraphs (4) and (5) of section 101, and section 510, of such Act ( 42 U.S.C. 12111(4) and (5); 42 U.S.C. 12209 ).\n**(3)**\nTitle VII of the Civil Rights Act of 1964 ( 42 U.S.C. 2000e et seq. ), including subsections (b) and (f) of section 701, and section 717(a), of such title ( 42 U.S.C. 2000e(b) and (f); 42 U.S.C. 2000e\u201316(a) ).\n**(4)**\nSection 304(a) of the Civil Rights Act of 1991 (42 U.S.C. 2000e\u201316c(a)).\n**(5)**\nThe Congressional Accountability Act of 1995 ( 2 U.S.C. 1301 et seq. ), including section 201 of such Act ( 2 U.S.C. 1311 ).\n**(6)**\nThe Employee Polygraph Protection Act of 1988 ( 29 U.S.C. 2001 et seq. ), including section 2(2) of such Act ( 29 U.S.C. 2001(2) ).\n**(7)**\nThe Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1001 et seq. ), including paragraphs (5) and (6) of section 3 of such Act ( 29 U.S.C. 1002(5) , (6)) and part 6 of subtitle B of title I of such Act (relating to health insurance continuation by employees) ( 29 U.S.C. 1161 et seq. ).\n**(8)**\nThe Family and Medical Leave Act of 1993 ( 29 U.S.C. 2601 et seq. ), including paragraphs (3) and (4) of section 101 of such Act ( 29 U.S.C. 2611(3) and (4)).\n**(9)**\nThe Fair Credit Reporting Act ( 15 U.S.C. 1681 et seq. ), including section 603(h) of such Act ( 15 U.S.C. 1681a(h) ).\n**(10)**\nTitle II of the Genetic Information Nondiscrimination Act of 2008 ( 42 U.S.C. 2000ff et seq. ), including section 201(2) of such Act ( 42 U.S.C. 2000ff(2) ).\n**(11)**\nThe Government Employee Rights Act of 1991 (42 U.S.C. 2000e\u201316a et seq.).\n**(12)**\nThe Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ).\n**(13)**\nThe Labor-Management Reporting and Disclosure Act of 1959 ( 29 U.S.C. 401 et seq. ), including subsections (e) and (f) of section 3 of such Act ( 29 U.S.C. 402(e) and (f)).\n**(14)**\nThe Occupational Safety and Health Act of 1970 ( 29 U.S.C. 651 et seq. ), including paragraphs (5) and (6) of section 3 of such Act ( 29 U.S.C. 652(5) and (6)).\n**(15)**\nSubtitle B of title I of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18001 et seq. ).\n**(16)**\nThe Rehabilitation Act of 1973 ( 29 U.S.C. 701 et seq. ), including section 501 of such Act ( 29 U.S.C. 791 ).\n**(17)**\nThe Worker Adjustment and Retraining Notification Act ( 29 U.S.C. 2101 et seq. ), including section 2(a) of such Act ( 29 U.S.C. 2101(a) ).\n**(18)**\nSection 1977A of the Revised Statutes ( 42 U.S.C. 1981a ).\n**(19)**\nSection 411 of title 3, United States Code.\n**(20)**\nChapter 81 of title 5, United States Code (commonly known as the Federal Employees\u2019 Compensation Act ), including paragraphs (1) and (12) of section 8101 of such title.\n**(21)**\nSubchapter IV of chapter 31 of title 40, United States Code (commonly known as the Davis-Bacon Act ).\n**(22)**\nChapter 43 of title 38, United States Code (commonly known as the Uniformed Services Employment and Reemployment Rights Act ), including paragraphs (3) and (4) of section 4303 of such title.\n**(23)**\nChapter 37 of title 40, United States Code (commonly known as the Contract Work Hours and Safety Standards Act ), including section 3701(b)(2) of such title.\n**(24)**\nChapter 67 of title 41, United States Code (commonly known as the McNamara-O\u2019Hara Service Contract Act ), including section 6701(3) of such title.\n**(25)**\nChapter 81 of title 41, United States Code (commonly referred to as the Drug-Free Workplace Act ), including section 8101(a)(6) of such title.",
      "versionDate": "2026-03-05",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Labor and Employment",
        "updateDate": "2026-03-24T16:48:21Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4010is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "21st Century Worker Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T02:38:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "21st Century Worker Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-20T02:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to clarify the classification of service provider payees as employees or independent contractors in Federal law.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-20T02:33:36Z"
    }
  ]
}
```
