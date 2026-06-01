# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1158?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1158
- Title: Freedom First Lend Lease Act
- Congress: 119
- Bill type: HR
- Bill number: 1158
- Origin chamber: House
- Introduced date: 2025-02-10
- Update date: 2025-10-25T08:05:46Z
- Update date including text: 2025-10-25T08:05:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-10: Introduced in House
- 2025-02-10 - IntroReferral: Introduced in House
- 2025-02-10 - IntroReferral: Introduced in House
- 2025-02-10 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-02-10: Introduced in House

## Actions

- 2025-02-10 - IntroReferral: Introduced in House
- 2025-02-10 - IntroReferral: Introduced in House
- 2025-02-10 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-10",
    "latestAction": {
      "actionDate": "2025-02-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1158",
    "number": "1158",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "W000795",
        "district": "2",
        "firstName": "Joe",
        "fullName": "Rep. Wilson, Joe [R-SC-2]",
        "lastName": "Wilson",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Freedom First Lend Lease Act",
    "type": "HR",
    "updateDate": "2025-10-25T08:05:46Z",
    "updateDateIncludingText": "2025-10-25T08:05:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-10",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-10",
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
          "date": "2025-02-10T17:03:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "TN"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "IL"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "PA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "CA"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "PA"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "False",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-14",
      "state": "TX"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "NJ"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "MA"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "NY"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "NE"
    },
    {
      "bioguideId": "H000874",
      "district": "5",
      "firstName": "Steny",
      "fullName": "Rep. Hoyer, Steny H. [D-MD-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoyer",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "MD"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "NY"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "AZ"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "NV"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1158ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1158\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 10, 2025 Mr. Wilson of South Carolina (for himself and Mr. Cohen ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo provide enhanced authority for the President to enter into agreements with the Government of Ukraine to lend or lease defense articles to that Government to protect civilian populations in Ukraine from Russian military invasion, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Freedom First Lend Lease Act .\n#### 2. Loan and lease of defense articles to the Governments of Ukraine and eastern flank countries\n##### (a) Authority To lend or lease defense articles to certain governments\n**(1) In general**\nSubject to paragraph (2), for fiscal years 2026 and 2027, the President may authorize the United States Government to lend or lease defense articles to the Government of Ukraine or to governments of Eastern European countries impacted by the Russian Federation\u2019s invasion of Ukraine to help bolster those countries\u2019 defense capabilities and protect their civilian populations from potential invasion or ongoing aggression by the armed forces of the Government of the Russian Federation.\n**(2) Exclusions**\nFor the purposes of the authority described in paragraph (1) as that authority relates to Ukraine, the following provisions of law shall not apply:\n**(A)**\nSection 503(b)(3) of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2311(b)(3) ).\n**(B)**\nSection 61 of the Arms Export Control Act ( 22 U.S.C. 2796 ).\n**(3) Condition**\nAny loan or lease of defense articles to the Government of Ukraine under paragraph (1) shall be subject to all applicable laws concerning the return of and reimbursement and repayment for defense articles loan or leased to foreign governments.\n**(4) Delegation of authority**\nThe President may delegate the enhanced authority under this subsection only to an official appointed by the President by and with the advice and consent of the Senate.\n##### (b) Procedures for delivery of defense articles\nNot later than 60 days after the date of the enactment of this Act, the President shall establish expedited procedures for the delivery of any defense article loaned or leased to the Government of Ukraine under an agreement entered into under subsection (a) to ensure timely delivery of the article to that Government.\n##### (c) Definition of defense article\nIn this Act, the term defense article has the meaning given that term in section 47 of the Arms Export Control Act ( 22 U.S.C. 2794 ).",
      "versionDate": "2025-02-10",
      "versionType": "Introduced in House"
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
        "name": "International Affairs",
        "updateDate": "2025-03-21T15:16:30Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-10",
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
          "measure-id": "id119hr1158",
          "measure-number": "1158",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-10",
          "originChamber": "HOUSE",
          "update-date": "2025-05-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1158v00",
            "update-date": "2025-05-01"
          },
          "action-date": "2025-02-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Freedom First Lend\u00a0Lease Act </strong></p><p>This bill temporarily waives certain requirements related to the President's authority to lend or lease defense articles if the defense articles are intended for Ukraine's government or the governments of other Eastern European countries affected by Russia's invasion of Ukraine.</p><p>For FY2026 and FY2027, an agreement to lend or lease defense articles under this bill shall not be subject to certain requirements and provisions that typically apply to such lend-lease agreements, including a requirement that generally prohibits a loan or lease period from exceeding five years.</p><p>The President must establish expedited procedures to ensure the timely delivery of defense articles loaned or leased to Ukraine under this bill.\u00a0Laws concerning the return of, reimbursement, and repayment for defense articles loaned or leased to foreign governments shall apply to any loan or lease to Ukraine.</p>"
        },
        "title": "Freedom First Lend Lease Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1158.xml",
    "summary": {
      "actionDate": "2025-02-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Freedom First Lend\u00a0Lease Act </strong></p><p>This bill temporarily waives certain requirements related to the President's authority to lend or lease defense articles if the defense articles are intended for Ukraine's government or the governments of other Eastern European countries affected by Russia's invasion of Ukraine.</p><p>For FY2026 and FY2027, an agreement to lend or lease defense articles under this bill shall not be subject to certain requirements and provisions that typically apply to such lend-lease agreements, including a requirement that generally prohibits a loan or lease period from exceeding five years.</p><p>The President must establish expedited procedures to ensure the timely delivery of defense articles loaned or leased to Ukraine under this bill.\u00a0Laws concerning the return of, reimbursement, and repayment for defense articles loaned or leased to foreign governments shall apply to any loan or lease to Ukraine.</p>",
      "updateDate": "2025-05-01",
      "versionCode": "id119hr1158"
    },
    "title": "Freedom First Lend Lease Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Freedom First Lend\u00a0Lease Act </strong></p><p>This bill temporarily waives certain requirements related to the President's authority to lend or lease defense articles if the defense articles are intended for Ukraine's government or the governments of other Eastern European countries affected by Russia's invasion of Ukraine.</p><p>For FY2026 and FY2027, an agreement to lend or lease defense articles under this bill shall not be subject to certain requirements and provisions that typically apply to such lend-lease agreements, including a requirement that generally prohibits a loan or lease period from exceeding five years.</p><p>The President must establish expedited procedures to ensure the timely delivery of defense articles loaned or leased to Ukraine under this bill.\u00a0Laws concerning the return of, reimbursement, and repayment for defense articles loaned or leased to foreign governments shall apply to any loan or lease to Ukraine.</p>",
      "updateDate": "2025-05-01",
      "versionCode": "id119hr1158"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1158ih.xml"
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
      "title": "Freedom First Lend Lease Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T04:23:36Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Freedom First Lend Lease Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T04:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide enhanced authority for the President to enter into agreements with the Government of Ukraine to lend or lease defense articles to that Government to protect civilian populations in Ukraine from Russian military invasion, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T04:20:43Z"
    }
  ]
}
```
