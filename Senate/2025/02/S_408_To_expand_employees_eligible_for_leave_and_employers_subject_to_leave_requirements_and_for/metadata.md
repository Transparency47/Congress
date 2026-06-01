# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/408?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/408
- Title: Job Protection Act
- Congress: 119
- Bill type: S
- Bill number: 408
- Origin chamber: Senate
- Introduced date: 2025-02-05
- Update date: 2025-12-06T06:52:08Z
- Update date including text: 2025-12-06T06:52:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-05: Introduced in Senate
- 2025-02-05 - IntroReferral: Introduced in Senate
- 2025-02-05 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-02-05: Introduced in Senate

## Actions

- 2025-02-05 - IntroReferral: Introduced in Senate
- 2025-02-05 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-05",
    "latestAction": {
      "actionDate": "2025-02-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/408",
    "number": "408",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "S001203",
        "district": "",
        "firstName": "Tina",
        "fullName": "Sen. Smith, Tina [D-MN]",
        "lastName": "Smith",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Job Protection Act",
    "type": "S",
    "updateDate": "2025-12-06T06:52:08Z",
    "updateDateIncludingText": "2025-12-06T06:52:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-05",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-05",
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
          "date": "2025-02-05T18:46:03Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "MA"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "IL"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "CT"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "CA"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "WA"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "NY"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernard",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-02-05",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s408is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 408\nIN THE SENATE OF THE UNITED STATES\nFebruary 5, 2025 Ms. Smith (for herself, Ms. Warren , Mr. Durbin , Mr. Blumenthal , Mr. Padilla , Mrs. Murray , Mrs. Gillibrand , and Mr. Sanders ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo expand employees eligible for leave and employers subject to leave requirements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Job Protection Act .\n#### 2. Expansion of employees eligible for leave\n##### (a) In general\nSection 101(2) of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2611(2) ) is amended\u2014\n**(1)**\nin subparagraph (A), by striking employed\u2014 and all that follows through the end of the subparagraph and inserting employed for not less than 90 days by the employer with respect to whom leave is requested under section 102. ;\n**(2)**\nin subparagraph (B), by striking does not include\u2014 and all that follows through the end of the subparagraph and inserting does not include any Federal officer or employee covered under subchapter V of chapter 63 of title 5, United States Code (as added by title II of this Act). ;\n**(3)**\nby striking subparagraphs (C) and (D); and\n**(4)**\nby redesignating subparagraph (E) as subparagraph (C).\n##### (b) Federal employees\n**(1) Title 5**\nSubchapter V of chapter 63 of title 5, United States Code, is amended\u2014\n**(A)**\nin section 6381(1)(B), by striking 12 months and inserting 90 days ; and\n**(B)**\nin section 6382(d)(2)(E), by striking 12 months and inserting 90 days .\n**(2) Presidential employees**\nSection 412(a)(2)(B) of title 3, United States Code, is amended by striking 12 months and for at least 1,250 hours of employment during the previous 12 months and inserting 90 days .\n**(3) Congressional employees**\nSection 202(a)(2)(B) of the Congressional Accountability Act of 1995 ( 2 U.S.C. 1312(a)(2)(B) ) is amended by striking 12 months and for at least 1,250 hours of employment during the previous 12 months and inserting 90 days .\n#### 3. Expansion of employers subject to leave requirements\nSection 101(4)(A)(i) of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2611(4)(A)(i) ) is amended by striking 50 or more employees and all that follows through the end of the clause and inserting 1 or more employees .\n#### 4. Applicability\nThis Act, and the amendments made by this Act, shall apply with respect to leave taken on or after the date of enactment of this Act.",
      "versionDate": "2025-02-05",
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
        "actionDate": "2025-02-05",
        "text": "Referred to the Committee on Education and Workforce, and in addition to the Committees on House Administration, and Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1035",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Job Protection Act",
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
            "name": "Employee benefits and pensions",
            "updateDate": "2025-04-15T14:10:24Z"
          },
          {
            "name": "Employee leave",
            "updateDate": "2025-04-15T14:10:24Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-04-15T14:10:24Z"
          }
        ]
      },
      "policyArea": {
        "name": "Labor and Employment",
        "updateDate": "2025-03-12T14:37:51Z"
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
      "date": "2025-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s408is.xml"
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
      "title": "Job Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T02:23:34Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Job Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to expand employees eligible for leave and employers subject to leave requirements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:18:50Z"
    }
  ]
}
```
