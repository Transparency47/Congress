# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5775?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5775
- Title: FCRA Liability Harmonization Act
- Congress: 119
- Bill type: HR
- Bill number: 5775
- Origin chamber: House
- Introduced date: 2025-10-17
- Update date: 2026-03-26T08:06:42Z
- Update date including text: 2026-03-26T08:06:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-17: Introduced in House
- 2025-10-17 - IntroReferral: Introduced in House
- 2025-10-17 - IntroReferral: Introduced in House
- 2025-10-17 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-17 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-10-17: Introduced in House

## Actions

- 2025-10-17 - IntroReferral: Introduced in House
- 2025-10-17 - IntroReferral: Introduced in House
- 2025-10-17 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-17 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-17",
    "latestAction": {
      "actionDate": "2025-10-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5775",
    "number": "5775",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "L000583",
        "district": "11",
        "firstName": "Barry",
        "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
        "lastName": "Loudermilk",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "FCRA Liability Harmonization Act",
    "type": "HR",
    "updateDate": "2026-03-26T08:06:42Z",
    "updateDateIncludingText": "2026-03-26T08:06:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-17",
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
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-17",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-17",
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
          "date": "2025-10-17T18:02:20Z",
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
          "date": "2025-10-17T18:02:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "MO"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "WI"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "PA"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "CA"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "MI"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5775ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5775\nIN THE HOUSE OF REPRESENTATIVES\nOctober 17, 2025 Mr. Loudermilk (for himself, Mrs. Wagner , Mr. Fitzgerald , Mr. Meuser , Mrs. Kim , and Mr. Huizenga ) introduced the following bill; which was referred to the Committee on Financial Services , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the civil liability requirements under the Fair Credit Reporting Act to include requirements relating to class actions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the FCRA Liability Harmonization Act .\n#### 2. Maintaining consistency in civil liability under the Fair Credit Reporting Act for class actions\n##### (a) Willful noncompliance\nSection 616 of the Fair Credit Reporting Act ( 15 U.S.C. 1681n ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1)(B), by inserting and after the semicolon;\n**(B)**\nby striking paragraph (2);\n**(C)**\nby redesignating paragraph (3) as paragraph (2); and\n**(D)**\nin paragraph (2), as redesignated by subparagraph (C), by striking as determined by the court. and inserting\nas determined by the court, in an amount that does not exceed the lesser of\u2014 (A) $100,000; or (B) the amount that is 40 percent of any damages awarded under paragraph (1)(A). ;\n**(2)**\nby redesignating subsection (d) as subsection (e); and\n**(3)**\nby inserting after subsection (c) the following new subsection:\n(d) Class action lawsuits With respect to a class action brought by a class made up of consumers against a person who willfully fails to comply with a requirement imposed under this title, such person shall be liable to such consumers in such an amount as a court may determine, except that\u2014 (1) the court may not apply a minimum amount of damages for each member of the class; (2) the total recovery (excluding reasonable attorney\u2019s fees as determined by the court) of the class may not exceed the lesser of\u2014 (A) $500,000; or (B) 1 percent of the net worth of such person; and (3) the costs of the action together with reasonable attorney\u2019s fees, as determined by the court, may not exceed the lesser\u2014 (A) of $100,000; (B) the amount that is 40 percent of any damages awarded by a court under this subsection; or (C) the sum of the costs of the action and reasonable attorney\u2019s fees, as determined by the court, not to exceed the lower of $100,000 or an amount equal to 40 percent of actual damages. .\n##### (b) Negligent noncompliance\nSection 617 of the Fair Credit Reporting Act ( 15 U.S.C. 1681o ) is amended\u2014\n**(1)**\nin subsection (a)(2), by striking the period at the end and inserting\n, not to exceed the lesser of\u2014 (A) $100,000; or (B) 40 percent of any actual damages determined by the court. ; and\n**(2)**\nby adding at the end the following new subsection:\n(c) Class action lawsuits With respect to a class action brought by consumers against a person who negligently fails to comply with any requirement imposed under this title, such person is liable to such consumers in an amount equal to the sum of any actual damages sustained by the consumers as a result of the failure, except that the total recovery (excluding reasonable attorney\u2019s fees as determined by the court) of the class shall not exceed the lesser of\u2014 (1) $500,000; (2) 1 percent of the net worth of such person; or (3) the sum of the costs of the action and reasonable attorney\u2019s fees, as determined by the court, not to exceed the lower of $100,000 or an amount equal to 40 percent of actual damages. .",
      "versionDate": "2025-10-17",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-12-08T16:58:37Z"
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
      "date": "2025-10-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5775ih.xml"
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
      "title": "FCRA Liability Harmonization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-22T06:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FCRA Liability Harmonization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-22T06:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the civil liability requirements under the Fair Credit Reporting Act to include requirements relating to class actions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-22T06:03:19Z"
    }
  ]
}
```
