# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/779?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/779
- Title: EARLY Minds Act
- Congress: 119
- Bill type: S
- Bill number: 779
- Origin chamber: Senate
- Introduced date: 2025-02-27
- Update date: 2025-12-05T21:54:53Z
- Update date including text: 2025-12-05T21:54:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-27: Introduced in Senate
- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (Sponsor introductory remarks on measure: CR S1430-1431)
- Latest action: 2025-02-27: Introduced in Senate

## Actions

- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (Sponsor introductory remarks on measure: CR S1430-1431)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/779",
    "number": "779",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "P000145",
        "district": "",
        "firstName": "Alex",
        "fullName": "Sen. Padilla, Alex [D-CA]",
        "lastName": "Padilla",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "EARLY Minds Act",
    "type": "S",
    "updateDate": "2025-12-05T21:54:53Z",
    "updateDateIncludingText": "2025-12-05T21:54:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (Sponsor introductory remarks on measure: CR S1430-1431)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T17:33:19Z",
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
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "NC"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "VA"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s779is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 779\nIN THE SENATE OF THE UNITED STATES\nFebruary 27, 2025 Mr. Padilla (for himself, Mr. Tillis , Mr. Kaine , and Ms. Murkowski ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend title XIX of the Public Health Service Act to provide for prevention and early intervention services under the Block Grants for Community Mental Health Services program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Early Action and Responsiveness Lifts Youth Minds Act or the EARLY Minds Act .\n#### 2. Early intervention\n##### (a) State plan option\nSection 1912(b)(1)(A)(vii) of the Public Health Service Act ( 42 U.S.C. 300x\u20131(b)(1)(A)(vii) ) is amended\u2014\n**(1)**\nin subclause (III), by striking and at the end;\n**(2)**\nin subclause (IV), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(V) a description of any evidence-based prevention and early intervention strategies and programs the State provides to prevent, delay, or reduce the severity and onset of mental illness and behavioral problems, including for children and adolescents, irrespective of experiencing a serious mental illness or serious emotional disturbance, as defined under subsection (c)(1). .\n##### (b) Allocation allowance; reports\nSection 1920 of the Public Health Service Act ( 42 U.S.C. 300x\u20139 ) is amended by adding at the end the following:\n(e) Prevention and early intervention services In the case of a State with a State plan that provides for strategies and programs specified in section 1912(b)(1)(A)(vii)(V), such State may expend not more than 5 percent of the amount of the allotment of the State pursuant to a funding agreement under section 1911 for each fiscal year to support such strategies and programs. (f) Reports to congress Not later than 1 year after the date of enactment of the EARLY Minds Act , and biennially thereafter, the Secretary shall submit to Congress a report on the prevention and early intervention strategies and programs pursued by States pursuant to subsection (e). Each such report shall include\u2014 (1) a list of the States that utilized the option to provide prevention and early intervention services; (2) a description of the prevention and early intervention activities of each such State; (3) the population served, including information on demographics, including age; (4) the outcomes of such activities, including\u2014 (A) how such activities reduced delays in access to mental and behavioral health care for children and adults; and (B) how such activities reduced the severity of onset of serious mental illness and serious emotional disturbance; and (5) any other relevant information the Secretary determines necessary. .",
      "versionDate": "2025-02-27",
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
        "actionDate": "2025-02-27",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "1735",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Early Action and Responsiveness Lifts Youth Minds Act",
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
        "name": "Health",
        "updateDate": "2025-03-21T16:38:35Z"
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
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s779is.xml"
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
      "title": "EARLY Minds Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:08:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "EARLY Minds Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Early Action and Responsiveness Lifts Youth Minds Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XIX of the Public Health Service Act to provide for prevention and early intervention services under the Block Grants for Community Mental Health Services program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:03:48Z"
    }
  ]
}
```
