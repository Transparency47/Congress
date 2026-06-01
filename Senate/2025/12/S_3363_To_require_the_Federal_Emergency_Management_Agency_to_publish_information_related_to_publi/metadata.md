# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3363?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3363
- Title: TRACK Act
- Congress: 119
- Bill type: S
- Bill number: 3363
- Origin chamber: Senate
- Introduced date: 2025-12-04
- Update date: 2026-01-07T23:23:00Z
- Update date including text: 2026-01-07T23:23:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in Senate
- 2025-12-04 - IntroReferral: 
- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-12-04: Introduced in Senate

## Actions

- 2025-12-04 - IntroReferral: 
- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3363",
    "number": "3363",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "M001244",
        "district": "",
        "firstName": "Ashley",
        "fullName": "Sen. Moody, Ashley [R-FL]",
        "lastName": "Moody",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "TRACK Act",
    "type": "S",
    "updateDate": "2026-01-07T23:23:00Z",
    "updateDateIncludingText": "2026-01-07T23:23:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-04",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-S",
      "actionDate": "2025-12-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-04",
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
          "date": "2025-12-04T18:44:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3363is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3363\nIN THE SENATE OF THE UNITED STATES\nDecember 4, 2025 Mrs. Moody (for herself and Ms. Alsobrooks ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo require the Federal Emergency Management Agency to publish information related to public assistance awards, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Transparency in Recovery Assistance and Claims Knowledge Act or the TRACK Act .\n#### 2. Public assistance dashboard\nSection 430(a) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5189h(a) ) is amended\u2014\n**(1)**\nby redesignating paragraphs (1) through (7) as subparagraphs (A) through (G), respectively, and adjusting the margins accordingly;\n**(2)**\nby striking Not later than and inserting the following:\n(1) Section 406 grants Not later than ; and\n**(3)**\nby adding at the end the following:\n(2) Public assistance dashboard (A) Public assistance defined In this paragraph, the term public assistance means assistance provided under section 402, 403, 406, 407, 418, or 419. (B) Dashboard For each major disaster declared by the President, the Administrator of the Federal Emergency Management Agency shall make publicly available on the website of the Federal Emergency Management Agency an interactive dashboard that tracks the following information with respect to public assistance awards related to each such major disaster: (i) The damage category code. (ii) For each proposed grant award, information on each cost estimate, applicant ID, the date of each submission, the descriptions for each project, and the cost of each project with a breakdown of the Federal cost-share and non-Federal cost-share. (iii) Status of the Agency review and approval of each cost estimate submitted, including the date on which a project is approved and the date on which the grant is issued. (iv) An explanation for any cost estimate that is not approved, or if the grant is not provided in the timeline as required, and any corrective action taken by the Agency. (v) Project-level progress updates. (vi) Information on requests for assistance made, including dates and amounts of each request, timelines for submissions of required information, and dates of approval and disbursement of awards. (vii) Any other information the Administrator determines to be appropriate to ensure transparency and accountability in the administration of public assistance. .",
      "versionDate": "2025-12-04",
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
        "name": "Emergency Management",
        "updateDate": "2026-01-07T23:23:00Z"
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
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3363is.xml"
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
      "title": "TRACK Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-30T05:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "TRACK Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-30T05:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Transparency in Recovery Assistance and Claims Knowledge Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-30T05:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Federal Emergency Management Agency to publish information related to public assistance awards, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-30T05:33:23Z"
    }
  ]
}
```
