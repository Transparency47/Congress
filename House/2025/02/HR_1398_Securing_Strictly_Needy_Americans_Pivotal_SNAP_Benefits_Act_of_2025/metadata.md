# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1398?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1398
- Title: Securing Strictly Needy Americans’ Pivotal (SNAP) Benefits Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1398
- Origin chamber: House
- Introduced date: 2025-02-18
- Update date: 2025-12-17T09:06:31Z
- Update date including text: 2025-12-17T09:06:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-18: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-03-20 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.
- Latest action: 2025-02-18: Introduced in House

## Actions

- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-03-20 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-18",
    "latestAction": {
      "actionDate": "2025-02-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1398",
    "number": "1398",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "R000603",
        "district": "7",
        "firstName": "David",
        "fullName": "Rep. Rouzer, David [R-NC-7]",
        "lastName": "Rouzer",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Securing Strictly Needy Americans\u2019 Pivotal (SNAP) Benefits Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-17T09:06:31Z",
    "updateDateIncludingText": "2025-12-17T09:06:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-20",
      "committees": {
        "item": {
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Nutrition and Foreign Agriculture.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-18",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-18",
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
          "date": "2025-02-18T18:02:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-20T20:39:28Z",
              "name": "Referred to"
            }
          },
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "systemCode": "hsag00",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "NE"
    },
    {
      "bioguideId": "S001189",
      "district": "8",
      "firstName": "Austin",
      "fullName": "Rep. Scott, Austin [R-GA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "GA"
    },
    {
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "MO"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1398ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1398\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 18, 2025 Mr. Rouzer (for himself, Mr. Bacon , Mr. Austin Scott of Georgia , and Mr. Alford ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Consolidated Appropriations Act, 2023, to limit the conditions applicable to the use of electronic benefit transfer (EBT) cards to purchase food, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Securing Strictly Needy Americans\u2019 Pivotal (SNAP) Benefits Act of 2025 .\n#### 2. Amendment to Consolidated Appropriations Act, 2023\nSection 501 of title IV of division HH of the Consolidated Appropriations Act, 2023, is amended by adding at the end the following:\n(f) Exclusively out-of-State purchases The State agency shall suspend the accounts of households for which EBT card transactions are made exclusively out-of-State for a period longer than 60 days, until\u2014 (1) the household affirmatively provides substantiating evidence that the members of the household who are program participants still reside in the state from which they receive benefits; or (2) an investigation is conducted and conclusively determines that the members of the household who are program participants still reside in the state from which they receive benefits. .\n#### 3. Limitation on redemption of supplemental nutrition assistance program benefits by owners of approved retail food stores and wholesale food concerns\nSection 9 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2020 ) is amended by adding at the end the following:\n(k) Limitation on redemption of supplemental nutrition assistance program benefits by households that include members who are owners of approved retail food stores or wholesale food concerns (1) A household that includes a member who is an owner of an approved retail food store or wholesale food concern may not redeem supplemental nutrition assistance program benefits at such store or such concern. (2) Paragraph (1) shall not apply with respect to a retail food store, or a wholesale food concern, that is owned by a publicly owned corporation or by a government. .\n#### 4. Effective date\nThis Act and the amendments made by this Act shall take effect 1 year after the date of the enactment of this Act.",
      "versionDate": "2025-02-18",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-03-20T19:57:30Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-18",
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
          "measure-id": "id119hr1398",
          "measure-number": "1398",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-18",
          "originChamber": "HOUSE",
          "update-date": "2025-06-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1398v00",
            "update-date": "2025-06-02"
          },
          "action-date": "2025-02-18",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Securing Strictly Needy Americans\u2019 Pivotal (SNAP) Benefits Act of 2025</strong></p><p>This bill establishes additional limitations on the use of\u00a0Supplemental Nutrition Assistance Program (SNAP) benefits.</p><p>The bill requires that a state agency suspend a SNAP household account when the Electronic Benefits Transfer (EBT) card transactions are made exclusively out-of-state for a period longer than 60 days. The state agency must maintain the suspension until (1) the household affirmatively provides substantiating evidence that the participating household members still reside in the state from which they receive benefits, or (2) an investigation conclusively determines that the participating\u00a0household members still reside in the state from which they receive benefits.</p><p>In addition, a SNAP household may not redeem SNAP benefits at a SNAP-approved retail food store or wholesale food concern that is owned by a household member. This does not apply to a retail food store or a wholesale food concern that is owned by a publicly owned corporation or a government.</p>"
        },
        "title": "Securing Strictly Needy Americans\u2019 Pivotal (SNAP) Benefits Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1398.xml",
    "summary": {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Securing Strictly Needy Americans\u2019 Pivotal (SNAP) Benefits Act of 2025</strong></p><p>This bill establishes additional limitations on the use of\u00a0Supplemental Nutrition Assistance Program (SNAP) benefits.</p><p>The bill requires that a state agency suspend a SNAP household account when the Electronic Benefits Transfer (EBT) card transactions are made exclusively out-of-state for a period longer than 60 days. The state agency must maintain the suspension until (1) the household affirmatively provides substantiating evidence that the participating household members still reside in the state from which they receive benefits, or (2) an investigation conclusively determines that the participating\u00a0household members still reside in the state from which they receive benefits.</p><p>In addition, a SNAP household may not redeem SNAP benefits at a SNAP-approved retail food store or wholesale food concern that is owned by a household member. This does not apply to a retail food store or a wholesale food concern that is owned by a publicly owned corporation or a government.</p>",
      "updateDate": "2025-06-02",
      "versionCode": "id119hr1398"
    },
    "title": "Securing Strictly Needy Americans\u2019 Pivotal (SNAP) Benefits Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Securing Strictly Needy Americans\u2019 Pivotal (SNAP) Benefits Act of 2025</strong></p><p>This bill establishes additional limitations on the use of\u00a0Supplemental Nutrition Assistance Program (SNAP) benefits.</p><p>The bill requires that a state agency suspend a SNAP household account when the Electronic Benefits Transfer (EBT) card transactions are made exclusively out-of-state for a period longer than 60 days. The state agency must maintain the suspension until (1) the household affirmatively provides substantiating evidence that the participating household members still reside in the state from which they receive benefits, or (2) an investigation conclusively determines that the participating\u00a0household members still reside in the state from which they receive benefits.</p><p>In addition, a SNAP household may not redeem SNAP benefits at a SNAP-approved retail food store or wholesale food concern that is owned by a household member. This does not apply to a retail food store or a wholesale food concern that is owned by a publicly owned corporation or a government.</p>",
      "updateDate": "2025-06-02",
      "versionCode": "id119hr1398"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1398ih.xml"
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
      "title": "Securing Strictly Needy Americans\u2019 Pivotal (SNAP) Benefits Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-19T03:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Securing Strictly Needy Americans\u2019 Pivotal (SNAP) Benefits Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-19T03:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Consolidated Appropriations Act, 2023, to limit the conditions applicable to the use of electronic benefit transfer (EBT) cards to purchase food, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-19T03:03:29Z"
    }
  ]
}
```
