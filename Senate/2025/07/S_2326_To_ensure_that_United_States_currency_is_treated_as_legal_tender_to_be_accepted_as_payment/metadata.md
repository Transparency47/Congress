# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2326?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2326
- Title: Payment Choice Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2326
- Origin chamber: Senate
- Introduced date: 2025-07-17
- Update date: 2026-02-12T00:41:17Z
- Update date including text: 2026-02-12T00:41:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-17: Introduced in Senate
- 2025-07-17 - IntroReferral: Introduced in Senate
- 2025-07-17 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-07-17: Introduced in Senate

## Actions

- 2025-07-17 - IntroReferral: Introduced in Senate
- 2025-07-17 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2326",
    "number": "2326",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "C001096",
        "district": "",
        "firstName": "Kevin",
        "fullName": "Sen. Cramer, Kevin [R-ND]",
        "lastName": "Cramer",
        "party": "R",
        "state": "ND"
      }
    ],
    "title": "Payment Choice Act of 2025",
    "type": "S",
    "updateDate": "2026-02-12T00:41:17Z",
    "updateDateIncludingText": "2026-02-12T00:41:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-17",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-17",
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
          "date": "2025-07-17T17:17:48Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2326is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2326\nIN THE SENATE OF THE UNITED STATES\nJuly 17, 2025 Mr. Cramer (for himself and Mr. Fetterman ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo ensure that United States currency is treated as legal tender to be accepted as payment for purchases of goods and services at brick-and-mortar businesses throughout the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Payment Choice Act of 2025 .\n#### 2. Sense of Congress\nIt is the sense of Congress that United States currency should be treated as legal tender throughout the United States, and that every consumer should have the right to use cash as payment at retail businesses that accept in-person payments.\n#### 3. Retail businesses prohibited from refusing cash payments\n##### (a) In general\nSubchapter I of chapter 51 of title 31, United States Code, is amended by adding at the end the following:\n5104. Retail businesses prohibited from refusing cash payments (a) In general Any person engaged in the business of selling or offering goods or services at retail to the public who accepts in-person payments at a physical location (including a person accepting payments for telephone, mail, or internet-based transactions who is accepting in-person payments at a physical location)\u2014 (1) shall accept cash as a form of payment for sales made at such physical location in amounts up to and including $500 per transaction; and (2) may not charge cash-paying customers a higher price compared to the price charged to customers not paying with cash. (b) Exceptions (1) In general Subsection (a) shall not apply to a person if\u2014 (A) the person is unable to accept cash because of\u2014 (i) a sale system failure that temporarily prevents the processing of cash payments; or (ii) temporarily having insufficient cash on hand to make change; or (B) (i) the person provides customers with a device that converts cash into prepaid cards on the premises; (ii) there is no fee for the use of the device; (iii) the device does not require a minimum deposit of more than one dollar; (iv) any funds placed onto a prepaid card using the device do not expire, except as permitted under paragraph (2); (v) the device does not collect any personal identifying information from the customer; and (vi) there is no fee to use the prepaid card that the device produces. (2) Inactivity A person seeking exception from subsection (a) may charge an inactivity fee in association with a card offered by such person if\u2014 (A) there has been no activity with respect to the card during the 12-month period ending on the date on which the inactivity fee is imposed; (B) not more than 1 inactivity fee is imposed in any 1-month period; and (C) it is clearly and conspicuously stated, on the face of the mechanism that issues the card and on the card\u2014 (i) that an inactivity fee or charge may be imposed; (ii) the frequency at which such inactivity fee may be imposed; and (iii) the amount of such inactivity fee. (c) Right To not accept large bills (1) In general Notwithstanding subsection (a), for the 5-year period beginning on the date of enactment of this section, this section shall not require a person to accept cash payments in $50 bills or any larger bill. (2) Rulemaking (A) In general The Secretary shall issue a rule on the date that is 5 years after the date of the enactment of this section with respect to any bill denominations a person is not required to accept. (B) Requirement When issuing a rule under subparagraph (A), the Secretary shall require persons to accept $1, $5, $10 and $20 bills. (d) Enforcement (1) Preventative relief (A) In general Whenever any person has engaged, or there are reasonable grounds to believe that any person is about to engage, in any act or practice prohibited by this section, any customer or prospective customer of such person aggrieved by such violation or threatened violation may deliver to the retailer, or cause to be so delivered by certified mail, with proof of delivery, a notice describing, in reasonable detail, the conduct or events constituting the violation or threatened violation, and giving notice that, unless such conduct is corrected or cured within 45 days after the date of delivery of such notice, a civil action for preventative relief, including an application for a permanent or temporary injunction, restraining order, or other appropriate such relief, which may include a civil penalty under paragraph (2), may be brought against such person. (B) No violation If, within the 45-day period under subparagraph (A), the retailer establishes to the reasonable satisfaction of the customer, in a response provided in writing to the customer, that no violation occurred as alleged, or certifies that the violation alleged has been corrected or cured, and provides reasonable assurance that no such violation will be permitted to occur, no further proceedings under this section shall be undertaken. (C) Failure to respond If a retailer, having received a notice described in subparagraph (A), fails to respond in accordance with that subparagraph, or responds but fails to reasonably establish that the violation alleged did not occur or has been corrected or cured, the aggrieved customer may file a civil action against the retailer seeking relief under this subsection, and shall attach to the complaint in such action copies of the notice given to the retailer and any response from the retailer. (2) Damages and civil penalties Any person who violates this section shall\u2014 (A) be liable for actual damages, and, if actual damages are less than $250, liquidated damages of $250; and (B) a civil penalty of not more than $500 for a first offense and not more than $1,500 for a second or subsequent offense. (3) Jurisdiction An action under this section may be brought in any United States district court, or in any other court of competent jurisdiction. (4) Intervention of attorney general Upon timely application, a court may, in its discretion, permit the Attorney General to intervene in a civil action brought under this subsection, if the Attorney General certifies that the action is of general public importance. (5) Authority to appoint court-paid attorney Upon application by an individual and in such circumstances as the court may determine just, the court may appoint an attorney for such individual and may authorize the commencement of a civil action under this subsection without the payment of fees, costs, or security. (6) Attorney\u2019s fees In any action commenced pursuant to this section, the court, in its discretion, may allow the prevailing party, other than the United States, a reasonable attorney\u2019s fee, not to exceed $3,000, as part of the costs, and the United States shall be liable for costs the same as a private person. (7) Requirements in certain states and local areas In the case of an alleged act or practice prohibited by this section which occurs in a State, or political subdivision of a State, which has a State or local law prohibiting such act or practice and establishing or authorizing a State or local authority to grant or seek relief from such act or practice or to institute criminal proceedings with respect thereto upon receiving notice thereof, no civil action may be brought hereunder before the expiration of 30 days after written notice of such alleged act or practice has been given to the appropriate State or local authority by registered mail or in person, provided that the court may stay proceedings in such civil action pending the termination of State or local enforcement proceedings. (e) Greater protection under state law This section shall not preempt any law of a State, the District of Columbia, a Tribal government, or a territory of the United States if the protections that such law affords to consumers are greater than the protections provided under this section. (f) Rulemaking The Secretary shall issue such rules as the Secretary determines are necessary to implement this section, which may prescribe additional exceptions to the application of the requirements described in subsection (a). (g) Annual reports on the geographic distribution of automated teller machines owned by federally insured depository institutions Beginning on the date that is 1 year after the date of enactment of this section, and annually thereafter, the Federal Deposit Insurance Corporation, with respect to depository institutions insured by the Corporation, and the National Credit Union Administration, with respect to credit unions insured by the National Credit Union Share Insurance Fund, shall submit to the Committee on Banking, Housing, and Urban Affairs of the Senate and the Committee on Financial Services of the House of Representatives a report that provides\u2014 (1) the number of automated teller machines owned and in service by each institution insured by such agency; (2) the location of each such automated teller machine that is installed at a fixed site; and (3) the approximate geographic range or radius within which mobile automated teller machines owned by any such institution are deployed. .\n##### (b) Technical and conforming amendment\nThe table of contents for chapter 51 of title 31, United States Code, is amended by inserting after the item relating to section 5103 the following:\n5104. Retail businesses prohibited from refusing cash payments. .",
      "versionDate": "2025-07-17",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-09-05T15:41:19Z"
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
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2326is.xml"
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
      "title": "Payment Choice Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-01T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Payment Choice Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-01T03:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to ensure that United States currency is treated as legal tender to be accepted as payment for purchases of goods and services at brick-and-mortar businesses throughout the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-01T03:48:25Z"
    }
  ]
}
```
