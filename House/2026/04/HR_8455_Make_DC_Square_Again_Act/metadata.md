# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8455?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8455
- Title: Make DC Square Again Act
- Congress: 119
- Bill type: HR
- Bill number: 8455
- Origin chamber: House
- Introduced date: 2026-04-22
- Update date: 2026-05-04T22:12:40Z
- Update date including text: 2026-05-04T22:12:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-22: Introduced in House
- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-22 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-04-22: Introduced in House

## Actions

- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-22 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-22",
    "latestAction": {
      "actionDate": "2026-04-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8455",
    "number": "8455",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "M001218",
        "district": "7",
        "firstName": "Richard",
        "fullName": "Rep. McCormick, Richard [R-GA-7]",
        "lastName": "McCormick",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Make DC Square Again Act",
    "type": "HR",
    "updateDate": "2026-05-04T22:12:40Z",
    "updateDateIncludingText": "2026-05-04T22:12:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-22",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-22",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-22",
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
          "date": "2026-04-22T15:04:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-04-22T15:04:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "GA"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2026-04-23",
      "state": "FL"
    },
    {
      "bioguideId": "F000485",
      "district": "14",
      "firstName": "Clay",
      "fullName": "Rep. Fuller, Clay [R-GA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Fuller",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8455ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8455\nIN THE HOUSE OF REPRESENTATIVES\nApril 22, 2026 Mr. McCormick (for himself and Mr. Carter of Georgia ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Oversight and Government Reform , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo repeal an Act entitled An Act to retrocede the county of Alexandria, in the District of Columbia, to the State of Virginia, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Make DC Square Again Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nArticle I, section 8, clause 17 of the Constitution known as the Enclave Clause enumerates the power of the Federal Government to exercise exclusive legislation in all cases whatsoever over such District (not exceeding ten miles square) as may, by cession of particular States, and the acceptance of Congress, become the seat of government of the United States .\n**(2)**\nThe Constitution does not enumerate authority for the Federal Government to retrocede portions of such a district back to states.\n**(3)**\nAn Act of Congress approved July 16, 1790, ten miles square of territory was accepted from the States of Maryland and Virginia to serve the permanent seat of government subsequently being known as the District of Columbia.\n**(4)**\nAct of Congress approved on July 9, 1846, the portion of the District of Columbia lying south of the Potomac River was ceded back to the State of Virginia in violation of the intent and meaning of the Constitution of the United States.\n**(5)**\nSenator Benjamin Wade of Ohio introduced S. 280 to repeal the 1846 Act of retrocession on April 23, 1866, during the 1st Session of the 39th Congress.\n#### 3. Repeal of retrocession and restoration of territory\n##### (a) Repeal\nThe Act of July 9, 1846 (9 Stat. 35, Chapter 35), entitled An Act to Retrocede the County of Alexandria, in the District of Columbia, to the State of Virginia , is repealed.\n##### (b) Restoration\nThe territory retroceded under the Act repealed by subsection (a), consisting of the area now comprising Arlington County, Virginia, and the independent City of Alexandria, Virginia, is restored to, and shall constitute part of, the District of Columbia.\n##### (c) Governing law\nEffective on the date of enactment of this Act, the laws of the District of Columbia shall apply to the territory restored under subsection (b), and the laws of the Commonwealth of Virginia shall cease to apply to such territory, except that\u2014\n**(1)**\nall rights, titles, and interests in property held by any person on such date shall remain undisturbed; and\n**(2)**\nany civil or criminal proceeding pending in a court of the Commonwealth of Virginia on such date arising in such territory may be concluded in that court as if this Act had not been enacted.\n##### (d) Effective date\nThis Act shall take effect on the first day of the first fiscal year beginning after the date of the enactment of this Act.",
      "versionDate": "2026-04-22",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-05-04T22:12:40Z"
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
      "date": "2026-04-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8455ih.xml"
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
      "title": "Make DC Square Again Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-01T08:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Make DC Square Again Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-01T08:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To repeal an Act entitled \"An Act to retrocede the county of Alexandria, in the District of Columbia, to the State of Virginia,\" and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-01T08:48:44Z"
    }
  ]
}
```
