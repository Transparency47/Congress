# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/710?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/710
- Title: Regulation Decimation Act
- Congress: 119
- Bill type: HR
- Bill number: 710
- Origin chamber: House
- Introduced date: 2025-01-23
- Update date: 2026-03-17T08:05:36Z
- Update date including text: 2026-03-17T08:05:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-23 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-01-23: Introduced in House

## Actions

- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-23 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/710",
    "number": "710",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "T000490",
        "district": "2",
        "firstName": "David",
        "fullName": "Rep. Taylor, David [R-OH-2]",
        "lastName": "Taylor",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Regulation Decimation Act",
    "type": "HR",
    "updateDate": "2026-03-17T08:05:36Z",
    "updateDateIncludingText": "2026-03-17T08:05:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-23",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-23",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-01-23T15:02:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-23T15:02:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "NC"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "OH"
    },
    {
      "bioguideId": "S001188",
      "district": "3",
      "firstName": "Marlin",
      "fullName": "Rep. Stutzman, Marlin A. [R-IN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Stutzman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "IN"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "GA"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham [R-AZ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "AZ"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "WI"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "TX"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TX"
    },
    {
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "NE"
    },
    {
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "WI"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "MI"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2026-03-16",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr710ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 710\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2025 Mr. Taylor (for himself, Mr. Harris of North Carolina , Mr. Rulli , Mr. Stutzman , Mr. Collins , Mr. Hamadeh of Arizona , Mr. Wied , and Mr. Gill of Texas ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require agencies to repeal ten existing regulations before issuing a new regulation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Regulation Decimation Act .\n#### 2. Repeal of regulations required before issuance of a new rule\n**(1) Requirement for rule**\nAn agency may not issue a rule unless such agency has repealed ten or more rules described in paragraph (4) that, to the extent practicable, are related to the rule.\n**(2) Requirement for major rule**\n**(A) Repeal required**\nAn agency may not issue a major rule unless\u2014\n**(i)**\nsuch agency has repealed ten or more rules described in paragraph (4) that, to the extent practicable, are related to the major rule; and\n**(ii)**\nthe cost of the new major rule is less than or equal to the cost of the rules repealed.\n**(B) Certified cost**\nFor any rule issued in accordance with subparagraph (A), the Administrator of the Office of Information and Regulatory Affairs of the Office of Management and Budget must have certified that the cost of the new major rule is equal to or less that the cost of the rules repealed.\n**(3) Publication required**\nAny rule repealed under paragraph (1) or (2) shall be published in the Federal Register.\n**(4) Applicability**\nThis section\u2014\n**(A)**\napplies to any rule or major rule that imposes a cost or responsibility on a nongovernmental person or a State or local government; and\n**(B)**\nshall not apply to any rule or major rule\u2014\n**(i)**\nthat relates to the internal policy or practice of an agency or procurement by the agency; or\n**(ii)**\nthat is being revised to be less burdensome to decrease requirements imposed by the rule or cost of compliance.\n**(5) Review of agency rules**\nNot later than 90 days after the date of the enactment of this Act, the head of each agency shall submit to Congress and the Director of the Office of Management and Budget a report that includes a review of each rule of the agency that identifies whether that rule is costly, ineffective, duplicative, or outdated, including a list of any other unnecessary regulatory restriction of the agency that is costly, ineffective, duplicative, or outdated.\n**(6) Report on rules**\nNot later than 5 years after the date of the enactment of this Act, the President shall submit to Congress a report on the number of rules in effect and the status of the reduction of rules over the previous 5 years.\n**(7) Definitions**\nIn this section:\n**(A) Agency**\nThe term agency has the meaning given that term in section 551 of title 5, United States Code.\n**(B) Major rule**\nThe term major rule has the meaning given that term in section 804 of title 5, United States Code.\n**(C) Rule**\nThe term rule has the meaning given that term in section 551 of title 5, United States Code.\n**(D) State**\nThe term State means each of the several States, the District of Columbia, each territory or possession of the United States, and each federally recognized Indian Tribe.",
      "versionDate": "2025-01-23",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-02-25",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "712",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Regulation Decimation Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-14",
        "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "377",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Regulation Reduction Act of 2025",
      "type": "HR"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-03-06T16:48:19Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-03-06T16:48:19Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-03-06T16:48:19Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-01T21:06:29Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr710",
          "measure-number": "710",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-23",
          "originChamber": "HOUSE",
          "update-date": "2025-05-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr710v00",
            "update-date": "2025-05-27"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Regulation Decimation Act</strong></p><p>This bill requires federal agencies to repeal certain existing rules prior to issuing a new rule.</p><p>Specifically, the bill prohibits an agency from issuing a rule that imposes a cost or responsibility on a nongovernmental person or a state or local government unless it repeals ten or more related rules.</p><p>Additionally, an agency may not issue a major rule that imposes such a cost or responsibility unless (1) the agency has repealed ten or more related rules, and (2) the cost of the new rule is less than or equal to the cost of the rules being repealed.\u00a0A\u00a0<em>major rule</em> is a rule that has resulted in or is likely to result in (1) an annual economic effect of at least $100 million; (2) a major increase in costs or prices for consumers, individual industries, government agencies, or geographic regions; or (3) significant adverse effects on competition, employment, investment, productivity, or innovation.</p><p>Any such repealed rule must be published in the Federal Register.</p><p>This bill does not apply to a rule or major rule that (1) relates to an internal agency policy\u00a0or practice, (2) relates to\u00a0procurement, or (3) is being revised to be less burdensome to decrease requirements imposed or compliance costs.</p><p>Additionally, each federal agency must submit to Congress and the Office of Management and Budget a report that includes a review of each rule of the agency and that identifies whether each rule is costly, ineffective, duplicative, or outdated.</p>"
        },
        "title": "Regulation Decimation Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr710.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Regulation Decimation Act</strong></p><p>This bill requires federal agencies to repeal certain existing rules prior to issuing a new rule.</p><p>Specifically, the bill prohibits an agency from issuing a rule that imposes a cost or responsibility on a nongovernmental person or a state or local government unless it repeals ten or more related rules.</p><p>Additionally, an agency may not issue a major rule that imposes such a cost or responsibility unless (1) the agency has repealed ten or more related rules, and (2) the cost of the new rule is less than or equal to the cost of the rules being repealed.\u00a0A\u00a0<em>major rule</em> is a rule that has resulted in or is likely to result in (1) an annual economic effect of at least $100 million; (2) a major increase in costs or prices for consumers, individual industries, government agencies, or geographic regions; or (3) significant adverse effects on competition, employment, investment, productivity, or innovation.</p><p>Any such repealed rule must be published in the Federal Register.</p><p>This bill does not apply to a rule or major rule that (1) relates to an internal agency policy\u00a0or practice, (2) relates to\u00a0procurement, or (3) is being revised to be less burdensome to decrease requirements imposed or compliance costs.</p><p>Additionally, each federal agency must submit to Congress and the Office of Management and Budget a report that includes a review of each rule of the agency and that identifies whether each rule is costly, ineffective, duplicative, or outdated.</p>",
      "updateDate": "2025-05-27",
      "versionCode": "id119hr710"
    },
    "title": "Regulation Decimation Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Regulation Decimation Act</strong></p><p>This bill requires federal agencies to repeal certain existing rules prior to issuing a new rule.</p><p>Specifically, the bill prohibits an agency from issuing a rule that imposes a cost or responsibility on a nongovernmental person or a state or local government unless it repeals ten or more related rules.</p><p>Additionally, an agency may not issue a major rule that imposes such a cost or responsibility unless (1) the agency has repealed ten or more related rules, and (2) the cost of the new rule is less than or equal to the cost of the rules being repealed.\u00a0A\u00a0<em>major rule</em> is a rule that has resulted in or is likely to result in (1) an annual economic effect of at least $100 million; (2) a major increase in costs or prices for consumers, individual industries, government agencies, or geographic regions; or (3) significant adverse effects on competition, employment, investment, productivity, or innovation.</p><p>Any such repealed rule must be published in the Federal Register.</p><p>This bill does not apply to a rule or major rule that (1) relates to an internal agency policy\u00a0or practice, (2) relates to\u00a0procurement, or (3) is being revised to be less burdensome to decrease requirements imposed or compliance costs.</p><p>Additionally, each federal agency must submit to Congress and the Office of Management and Budget a report that includes a review of each rule of the agency and that identifies whether each rule is costly, ineffective, duplicative, or outdated.</p>",
      "updateDate": "2025-05-27",
      "versionCode": "id119hr710"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr710ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Regulation Decimation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-21T12:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Regulation Decimation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T12:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require agencies to repeal ten existing regulations before issuing a new regulation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T12:03:26Z"
    }
  ]
}
```
