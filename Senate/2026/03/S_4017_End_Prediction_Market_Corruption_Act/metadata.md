# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4017?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4017
- Title: End Prediction Market Corruption Act
- Congress: 119
- Bill type: S
- Bill number: 4017
- Origin chamber: Senate
- Introduced date: 2026-03-05
- Update date: 2026-03-24T16:54:06Z
- Update date including text: 2026-03-24T16:54:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-05: Introduced in Senate
- 2026-03-05 - IntroReferral: Introduced in Senate
- 2026-03-05 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2026-03-05: Introduced in Senate

## Actions

- 2026-03-05 - IntroReferral: Introduced in Senate
- 2026-03-05 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4017",
    "number": "4017",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "M001176",
        "district": "",
        "firstName": "Jeff",
        "fullName": "Sen. Merkley, Jeff [D-OR]",
        "lastName": "Merkley",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "End Prediction Market Corruption Act",
    "type": "S",
    "updateDate": "2026-03-24T16:54:06Z",
    "updateDateIncludingText": "2026-03-24T16:54:06Z"
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
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
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
          "date": "2026-03-05T19:46:46Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "MN"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "MD"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4017is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4017\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2026 Mr. Merkley (for himself, Ms. Klobuchar , Mr. Van Hollen , Mr. Schiff , and Mrs. Gillibrand ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Commodity Exchange Act to ban certain Government officials from trading event contracts, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the End Prediction Market Corruption Act .\n#### 2. Ban on trading event contracts by certain Government officials\nSection 5c of the Commodity Exchange Act ( 7 U.S.C. 7a\u20132 ) is amended by inserting after subsection (c) the following:\n(d) Ban on trading event contracts by certain Government officials (1) Definitions In this subsection: (A) Covered individual The term covered individual means\u2014 (i) the President; (ii) the Vice President; and (iii) a Member of Congress. (B) Event contract The term event contract means an agreement, contract, transaction, or swap in an excluded commodity that is based on an occurrence, extent of an occurrence of, or contingency. (C) Material nonpublic information The term material nonpublic information means information\u2014 (i) that a reasonable investor would consider important in making a decision regarding purchasing, selling, or otherwise exchanging an agreement or contract in a commodity or a commodity for future delivery; and (ii) that is not publicly available. (D) Member of Congress The term Member of Congress has the meaning given the term in section 13101 of title 5, United States Code. (E) Senior executive branch official The term senior executive branch official means any officer or employee described in any of paragraphs (3) through (8) of section 13103(f) of title 5, United States Code. (2) Ban on trading event contracts (A) Covered individuals No covered individual may purchase, sell, or otherwise exchange an event contract. (B) Senior executive branch officials No senior executive branch official may purchase, sell, or otherwise exchange an event contract the subject of which is a matter in which the senior executive branch official participates personally and substantially as a Government officer or employee, through decision, approval, disapproval, recommendation, the rendering of advice, investigation, or otherwise, in a judicial or other proceeding, application, request for a ruling or other determination, contract, claim, controversy, charge, accusation, arrest, or other particular matter. (3) Civil actions (A) In general The Attorney General may bring a civil action in the appropriate United States district court against any individual who engages in conduct in violation of paragraph (2). (B) Civil penalty In a civil action under subparagraph (A), if it is demonstrated by a preponderance of the evidence that the individual has violated paragraph (2), the individual shall be subject to a civil penalty of not more than the greater of\u2014 (i) $10,000 for each violation; and (ii) the amount of profit made through the purchase, sale, or exchange of the event contract in violation of paragraph (2). (C) No preclusion of alternative remedies The imposition of a civil penalty under this paragraph does not preclude any other criminal or civil statutory, common law, or administrative remedy that is available by law to the United States or any other person. (4) Foreign boards of trade (A) Definition of foreign board of trade In this paragraph, the term foreign board of trade means a board of trade that\u2014 (i) is organized under the laws of a non-United States jurisdiction or has its principal place of business outside the United States; and (ii) avails itself of any means or instrumentality of interstate commerce in the conduct of its business as a board of trade. (B) Quarterly reports Each foreign board of trade shall submit to the Commission quarterly reports describing each purchase, sale, or other exchange on the foreign board of trade in violation of paragraph (2). (C) Enforcement A foreign board of trade that fails to submit a report required by subparagraph (B) shall be subject to revocation of the registration of the foreign board of trade by the Commission. (5) Insider trading The Commission shall issue a rule to restrict the inappropriate use of material nonpublic information, in breach of an express or implied duty not to use or disclose such material nonpublic information, as a means of making a profit through the purchase, sale, or other exchange of an event contract, including by requiring designated contract markets to prohibit the purchase, sale, or other exchange of an event contract by such individuals as the Commission determines to be appropriate in the public interest. .\n#### 3. Financial disclosure reports\n##### (a) Annual and termination reports\nSection 13104(a) of title 5, United States Code, is amended by adding at the end the following:\n(9) Disclosure relating to event contracts (A) Definitions In this paragraph: (i) Covered reporting individual The term covered reporting individual means an individual described in paragraphs (1) through (10) of section 13103(f). (ii) Dependent child The term dependent child has the meaning given the term in section 13101. (iii) Event contract The term event contract has the meaning given the term in subsection (d)(1) of section 5c of the Commodity Exchange Act ( 7 U.S.C. 7a\u20132 ). (B) Requirement Each report filed pursuant to subsection (d) or (e) of section 13103 by a covered reporting individual shall include\u2014 (i) a statement of whether, during the period covered by the report, the covered reporting individual, or the spouse or dependent child of the covered reporting individual, purchased, sold, or otherwise exchanged an event contract; and (ii) with respect to any event contract described in clause (i), a description of the event contract and the value of the event contract. .\n##### (b) Periodic event contract transaction reports\nSection 13105 of title 5, United States Code, is amended by adding at the end the following:\n(m) Periodic event contract transaction reports (1) Definitions For purposes of this subsection, the terms covered reporting individual and event contract have the meanings given those terms in section 13104(a)(9)(A). (2) Requirement Not later than 30 days after receiving notification of any event contract transaction required to be reported under section 13104(a)(9), but in no case later than 45 days after such event contract transaction, a covered reporting individual shall file a report of the transaction that includes a description of the event contract that is the subject of the transaction and the value of the event contract. .",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2026-03-24T16:54:05Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4017is.xml"
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
      "title": "End Prediction Market Corruption Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T02:23:30Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "End Prediction Market Corruption Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-20T02:23:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Commodity Exchange Act to ban certain Government officials from trading event contracts, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-20T02:18:32Z"
    }
  ]
}
```
