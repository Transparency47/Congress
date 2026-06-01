# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/172?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/172
- Title: Proposing an amendment to the Constitution of the United States to protect United States citizenship.
- Congress: 119
- Bill type: HJRES
- Bill number: 172
- Origin chamber: House
- Introduced date: 2026-05-04
- Update date: 2026-05-22T08:08:13Z
- Update date including text: 2026-05-22T08:08:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-05-04: Introduced in House
- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-05-04: Introduced in House

## Actions

- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-04",
    "latestAction": {
      "actionDate": "2026-05-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/172",
    "number": "172",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "F000485",
        "district": "14",
        "firstName": "Clay",
        "fullName": "Rep. Fuller, Clay [R-GA-14]",
        "lastName": "Fuller",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Proposing an amendment to the Constitution of the United States to protect United States citizenship.",
    "type": "HJRES",
    "updateDate": "2026-05-22T08:08:13Z",
    "updateDateIncludingText": "2026-05-22T08:08:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-04",
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
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-04",
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
          "date": "2026-05-04T14:32:10Z",
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
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "TX"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hjres/BILLS-119hjres172ih.xml",
      "text": "IA\n119th CONGRESS\n2d Session\nH. J. RES. 172\nIN THE HOUSE OF REPRESENTATIVES\nMay 4, 2026 Mr. Fuller submitted the following joint resolution; which was referred to the Committee on the Judiciary\nJOINT RESOLUTION\nProposing an amendment to the Constitution of the United States to protect United States citizenship.\nThat the following article is proposed as an amendment to the Constitution of the United States, which shall be valid to all intents and purposes as part of the Constitution when ratified by the legislatures of three-fourths of the several States within seven years after the date of its submission for ratification:\n\u2014 1. For purposes of the 14th article of amendment to the Constitution of the United States, a person may be considered to be subject to the jurisdiction of the United States only in accordance with section 2. 2. A person born in the United States may only be considered subject to the jurisdiction of the United States if the person is born in the United States of parents, one of whom is\u2014 (1) a citizen or national of the United States; (2) an alien lawfully admitted for permanent residence in the United States whose residence is in the United States; or (3) an alien with lawful status under the immigration laws performing active service in the Armed Forces. 3. Congress shall have the power to carry out this article through appropriate legislation. .",
      "versionDate": "2026-05-04",
      "versionType": "IH"
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
        "actionDate": "2026-04-29",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "189",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A joint resolution proposing an amendment to the Constitution of the United States to protect United States citizenship.",
      "type": "SJRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-06-30",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "103",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Proposing an amendment to the Constitution to protect American citizenship.",
      "type": "HJRES"
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
        "name": "Immigration",
        "updateDate": "2026-05-15T15:53:04Z"
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
      "date": "2026-05-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hjres/BILLS-119hjres172ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Proposing an amendment to the Constitution of the United States to protect United States citizenship.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-05T08:18:37Z"
    },
    {
      "title": "Proposing an amendment to the Constitution of the United States to protect United States citizenship.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-05T08:05:35Z"
    }
  ]
}
```
