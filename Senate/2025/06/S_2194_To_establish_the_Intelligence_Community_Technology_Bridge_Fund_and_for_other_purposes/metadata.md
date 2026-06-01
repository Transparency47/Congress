# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2194?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2194
- Title: Intelligence Community Technology Bridge Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2194
- Origin chamber: Senate
- Introduced date: 2025-06-26
- Update date: 2025-10-01T01:04:13Z
- Update date including text: 2025-10-01T01:04:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-26: Introduced in Senate
- 2025-06-26 - IntroReferral: Introduced in Senate
- 2025-06-26 - IntroReferral: Read twice and referred to the Select Committee on Intelligence.
- Latest action: 2025-06-26: Introduced in Senate

## Actions

- 2025-06-26 - IntroReferral: Introduced in Senate
- 2025-06-26 - IntroReferral: Read twice and referred to the Select Committee on Intelligence.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-26",
    "latestAction": {
      "actionDate": "2025-06-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2194",
    "number": "2194",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Intelligence Community Technology Bridge Act of 2025",
    "type": "S",
    "updateDate": "2025-10-01T01:04:13Z",
    "updateDateIncludingText": "2025-10-01T01:04:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-26",
      "committees": {
        "item": {
          "name": "Intelligence (Select) Committee",
          "systemCode": "slin00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Select Committee on Intelligence.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-26",
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
          "date": "2025-06-26T21:29:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Intelligence (Select) Committee",
      "systemCode": "slin00",
      "type": "Select"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "VA"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "AZ"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2194is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2194\nIN THE SENATE OF THE UNITED STATES\nJune 26 (legislative day, June 24), 2025 Mr. Cornyn (for himself, Mr. Warner , Mr. Kelly , and Mr. Lankford ) introduced the following bill; which was read twice and referred to the Select Committee on Intelligence\nA BILL\nTo establish the Intelligence Community Technology Bridge Fund, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Intelligence Community Technology Bridge Act of 2025 .\n#### 2. Intelligence Community Technology Bridge Fund\n##### (a) Definitions\nIn this section:\n**(1) Congressional intelligence committees**\nThe term congressional intelligence committees has the meaning given such term in section 3 of the National Security Act of 1947 ( 50 U.S.C. 3003 ).\n**(2) Intelligence community**\nThe term intelligence community has the meaning given such term in such section.\n**(3) Nonprofit organization**\nThe term nonprofit organization means an organization that is described in section 501(c)(3) of the Internal Revenue Code of 1986 and that is exempt from tax under section 501(a) of such Code.\n##### (b) Establishment of fund\nThere is established in the Treasury of the United States a fund to be known as the Intelligence Community Technology Bridge Fund (in this subsection referred to as the Fund ) to assist in the transitioning of products or services from the research and development phase to the prototype or production phase.\n##### (c) Contents of Fund\nThe Fund shall consist of amounts appropriated to the Fund, and amounts in the Fund shall remain available until expended.\n##### (d) Availability and use of Fund\n**(1) In general**\nSubject to paragraph (3), amounts in the Fund shall be available to the Director of National Intelligence to make available to the heads of the elements of the intelligence community to provide assistance to a business or nonprofit organization that is transitioning a product or service to the prototype or production phase as a means of advancing government acquisitions of the product or service.\n**(2) Types of assistance**\nAssistance provided under paragraph (1) may be distributed as funds in the form of a grant, a payment for a product or service, or a payment for equity.\n**(3) Requirements for funds**\nAssistance may be provided under paragraph (1) to a business or nonprofit organization that is transitioning a product or service only if\u2014\n**(A)**\nthe business or nonprofit organization is under contract, agreement, or other engagement with an element of the intelligence community for research and development; and\n**(B)**\nthe Director of National Intelligence or the head of an element of the intelligence community attests that the product or service will be utilized by an element of the intelligence community for a mission need, such as because it would be valuable in addressing a needed capability, fill or complement a technology gap, or increase the supplier base or price-competitiveness for the Federal Government.\n**(4) Priority for small business concerns and nontraditional contractors**\nIn providing assistance under paragraph (1), the Director shall limit the provision of assistance to small business concerns (as defined under section 3(a) of the Small Business Act ( 15 U.S.C. 632(a) )) and nontraditional defense contractors (as defined in section 3014 of title 10, United States Code).\n##### (e) Administration of Fund\n**(1) In general**\nThe Fund shall be administered by the Director of National Intelligence.\n**(2) Consultation**\nIn administering the Fund, the Director\u2014\n**(A)**\nshall consult with the heads of the elements of the intelligence community; and\n**(B)**\nmay consult with the Defense Advanced Research Projects Agency, Intelligence Advanced Research Projects Activity, National Laboratories intelligence community laboratories, the North Atlantic Treaty Organization Investment Fund, the Defense Innovation Unit, and such other entities as the Director deems appropriate.\n##### (f) Annual reports\n**(1) In general**\nNot later than September 30, 2026, and each fiscal year thereafter, the Director shall submit to the congressional intelligence committees a report on the Fund.\n**(2) Contents**\nEach report submitted pursuant to paragraph (1) shall include, for the period covered by the report, information about the following:\n**(A)**\nHow much was expended or obligated using amounts from the Fund.\n**(B)**\nFor what the amounts were expended or obligated.\n**(C)**\nThe effects of such expenditures and obligations.\n**(D)**\nA summary of annual transition activities and outcomes of such activities for the intelligence community.\n##### (g) Authorization of appropriations\n**(1) In general**\nSubject to paragraph (2), there is authorized to be appropriated to the Fund $75,000,000 for fiscal year 2026 and for each fiscal year thereafter.\n**(2) Limitation**\nThe amount in the Fund shall not exceed $75,000,000 at any time.",
      "versionDate": "2025-06-26",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-07-29",
        "text": "By Senator Cotton from Select Committee on Intelligence filed written report. Report No. 119-51. Minority views filed."
      },
      "number": "2342",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Intelligence Authorization Act for Fiscal Year 2026",
      "type": "S"
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-07-29T21:11:16Z"
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
      "date": "2025-06-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2194is.xml"
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
      "title": "Intelligence Community Technology Bridge Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-16T03:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Intelligence Community Technology Bridge Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-16T03:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish the Intelligence Community Technology Bridge Fund, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-16T03:33:20Z"
    }
  ]
}
```
