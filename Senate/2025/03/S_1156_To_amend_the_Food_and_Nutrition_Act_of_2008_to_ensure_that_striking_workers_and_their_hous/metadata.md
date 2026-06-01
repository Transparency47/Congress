# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1156?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1156
- Title: Food Secure Strikers Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1156
- Origin chamber: Senate
- Introduced date: 2025-03-26
- Update date: 2026-04-16T11:03:24Z
- Update date including text: 2026-04-16T11:03:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-26: Introduced in Senate
- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-03-26: Introduced in Senate

## Actions

- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-26",
    "latestAction": {
      "actionDate": "2025-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1156",
    "number": "1156",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "F000479",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Fetterman, John [D-PA]",
        "lastName": "Fetterman",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Food Secure Strikers Act of 2025",
    "type": "S",
    "updateDate": "2026-04-16T11:03:24Z",
    "updateDateIncludingText": "2026-04-16T11:03:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-26",
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
      "actionDate": "2025-03-26",
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
        "item": [
          {
            "date": "2025-03-26T20:07:58Z",
            "name": "Referred To"
          },
          {
            "date": "2025-03-26T20:07:58Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "CA"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "CT"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "MN"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "MN"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "OR"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "NY"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "CA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "VT"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "NJ"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-03-26",
      "state": "VT"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "AZ"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "MI"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "NM"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "IL"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1156is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1156\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2025 Mr. Fetterman (for himself, Mr. Padilla , Mr. Blumenthal , Ms. Smith , Ms. Klobuchar , Mr. Wyden , Mrs. Gillibrand , Mr. Schiff , Mr. Welch , Mr. Booker , Mr. Sanders , Mr. Gallego , and Ms. Slotkin ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Food and Nutrition Act of 2008 to ensure that striking workers and their households do not become ineligible for benefits under the supplemental nutrition assistance program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Food Secure Strikers Act of 2025 .\n#### 2. Eligibility of striking workers\nSection 6(d) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2015(d) ) is amended\u2014\n**(1)**\nin paragraph (1)(D)\u2014\n**(A)**\nby striking clause (iv); and\n**(B)**\nby redesignating clauses (v) and (vi) as clauses (iv) and (v), respectively; and\n**(2)**\nin paragraph (3)\u2014\n**(A)**\nby striking participate in the supplemental nutrition assistance program at any time that and inserting be ineligible to participate in the supplemental nutrition assistance program as a result of ;\n**(B)**\nby striking is on strike and inserting being on strike ; and\n**(C)**\nby striking : Provided, That and all that follows through the period at the end and inserting a period.",
      "versionDate": "2025-03-26",
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
        "actionDate": "2025-04-18",
        "text": "Referred to the Subcommittee on Nutrition and Foreign Agriculture."
      },
      "number": "2357",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Food Secure Strikers Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Agriculture and Food",
        "updateDate": "2025-05-06T17:10:59Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-26",
    "originChamber": "Senate",
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
          "measure-id": "id119s1156",
          "measure-number": "1156",
          "measure-type": "s",
          "orig-publish-date": "2025-03-26",
          "originChamber": "SENATE",
          "update-date": "2026-02-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1156v00",
            "update-date": "2026-02-04"
          },
          "action-date": "2025-03-26",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Food Secure Strikers Act of 2025\u00a0</strong></p><p>This bill allows certain\u00a0striking workers\u00a0and their households\u00a0to\u00a0maintain their eligibility for the\u00a0Supplemental Nutrition Assistance Program (SNAP).</p><p>Specifically, the bill provides that a household that would otherwise be eligible to participate in SNAP is eligible for benefits\u00a0if any member of the household is\u00a0on strike because of a labor dispute. Current law generally prohibits a household from participating in SNAP if any member of the household is on strike unless the household was eligible for SNAP immediately prior to the strike. Also, under current law, households are not eligible for an increased SNAP allotment as a result of the decreased income of a striking member of the household. The bill expands SNAP eligibility for households with striking workers by repealing both of these restrictions.</p><p>The bill also allows\u00a0a government employee who is dismissed for\u00a0striking and their household\u00a0to maintain SNAP program eligibility. Specifically, current law prohibits certain individuals who voluntarily and without good cause quit a job from participating in SNAP. Further, a federal, state, or local government\u00a0employee who participates in a strike against the government that results in their dismissal is considered\u00a0to have voluntarily quit without good cause. The bill eliminates the provision that considers the\u00a0dismissed government employee to have voluntarily quit without good cause, thereby allowing the employee and their household\u00a0to maintain SNAP program eligibility if they are otherwise eligible for the program.</p>"
        },
        "title": "Food Secure Strikers Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1156.xml",
    "summary": {
      "actionDate": "2025-03-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Food Secure Strikers Act of 2025\u00a0</strong></p><p>This bill allows certain\u00a0striking workers\u00a0and their households\u00a0to\u00a0maintain their eligibility for the\u00a0Supplemental Nutrition Assistance Program (SNAP).</p><p>Specifically, the bill provides that a household that would otherwise be eligible to participate in SNAP is eligible for benefits\u00a0if any member of the household is\u00a0on strike because of a labor dispute. Current law generally prohibits a household from participating in SNAP if any member of the household is on strike unless the household was eligible for SNAP immediately prior to the strike. Also, under current law, households are not eligible for an increased SNAP allotment as a result of the decreased income of a striking member of the household. The bill expands SNAP eligibility for households with striking workers by repealing both of these restrictions.</p><p>The bill also allows\u00a0a government employee who is dismissed for\u00a0striking and their household\u00a0to maintain SNAP program eligibility. Specifically, current law prohibits certain individuals who voluntarily and without good cause quit a job from participating in SNAP. Further, a federal, state, or local government\u00a0employee who participates in a strike against the government that results in their dismissal is considered\u00a0to have voluntarily quit without good cause. The bill eliminates the provision that considers the\u00a0dismissed government employee to have voluntarily quit without good cause, thereby allowing the employee and their household\u00a0to maintain SNAP program eligibility if they are otherwise eligible for the program.</p>",
      "updateDate": "2026-02-04",
      "versionCode": "id119s1156"
    },
    "title": "Food Secure Strikers Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Food Secure Strikers Act of 2025\u00a0</strong></p><p>This bill allows certain\u00a0striking workers\u00a0and their households\u00a0to\u00a0maintain their eligibility for the\u00a0Supplemental Nutrition Assistance Program (SNAP).</p><p>Specifically, the bill provides that a household that would otherwise be eligible to participate in SNAP is eligible for benefits\u00a0if any member of the household is\u00a0on strike because of a labor dispute. Current law generally prohibits a household from participating in SNAP if any member of the household is on strike unless the household was eligible for SNAP immediately prior to the strike. Also, under current law, households are not eligible for an increased SNAP allotment as a result of the decreased income of a striking member of the household. The bill expands SNAP eligibility for households with striking workers by repealing both of these restrictions.</p><p>The bill also allows\u00a0a government employee who is dismissed for\u00a0striking and their household\u00a0to maintain SNAP program eligibility. Specifically, current law prohibits certain individuals who voluntarily and without good cause quit a job from participating in SNAP. Further, a federal, state, or local government\u00a0employee who participates in a strike against the government that results in their dismissal is considered\u00a0to have voluntarily quit without good cause. The bill eliminates the provision that considers the\u00a0dismissed government employee to have voluntarily quit without good cause, thereby allowing the employee and their household\u00a0to maintain SNAP program eligibility if they are otherwise eligible for the program.</p>",
      "updateDate": "2026-02-04",
      "versionCode": "id119s1156"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1156is.xml"
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
      "title": "Food Secure Strikers Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-16T11:03:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Food Secure Strikers Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-12T02:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Food and Nutrition Act of 2008 to ensure that striking workers and their households do not become ineligible for benefits under the supplemental nutrition assistance program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-12T02:48:20Z"
    }
  ]
}
```
