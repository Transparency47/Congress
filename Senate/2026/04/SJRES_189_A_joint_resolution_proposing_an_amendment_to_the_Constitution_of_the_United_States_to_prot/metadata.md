# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sjres/189?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-joint-resolution/189
- Title: A joint resolution proposing an amendment to the Constitution of the United States to protect United States citizenship.
- Congress: 119
- Bill type: SJRES
- Bill number: 189
- Origin chamber: Senate
- Introduced date: 2026-04-29
- Update date: 2026-05-15T15:52:33Z
- Update date including text: 2026-05-15T15:52:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-29: Introduced in Senate
- 2026-04-29 - IntroReferral: Introduced in Senate
- 2026-04-29 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-04-29: Introduced in Senate

## Actions

- 2026-04-29 - IntroReferral: Introduced in Senate
- 2026-04-29 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-29",
    "latestAction": {
      "actionDate": "2026-04-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-joint-resolution/189",
    "number": "189",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "P000603",
        "district": "",
        "firstName": "Rand",
        "fullName": "Sen. Paul, Rand [R-KY]",
        "lastName": "Paul",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "A joint resolution proposing an amendment to the Constitution of the United States to protect United States citizenship.",
    "type": "SJRES",
    "updateDate": "2026-05-15T15:52:33Z",
    "updateDateIncludingText": "2026-05-15T15:52:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-04-29",
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
          "date": "2026-04-29T22:02:23Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sjres/BILLS-119sjres189is.xml",
      "text": "IIA\n119th CONGRESS\n2d Session\nS. J. RES. 189\nIN THE SENATE OF THE UNITED STATES\nApril 29, 2026 Mr. Paul introduced the following joint resolution; which was read twice and referred to the Committee on the Judiciary\nJOINT RESOLUTION\nProposing an amendment to the Constitution of the United States to protect United States citizenship.\nThat the following article is proposed as an amendment to the Constitution of the United States, which shall be valid to all intents and purposes as part of the Constitution when ratified by the legislatures of three-fourths of the several States within seven years after the date of its submission for ratification:\n\u2014 1. For purposes of the 14th article of amendment to the Constitution of the United States, a person may be considered to be subject to the jurisdiction of the United States only in accordance with section 2. 2. A person born in the United States may only be considered \u2018subject to the jurisdiction of the United States' if the person is born in the United States of parents, one of whom is\u2014 (1) a citizen or national of the United States; (2) an alien lawfully admitted for permanent residence in the United States whose residence is in the United States; or (3) an alien with lawful status under the immigration laws performing active service in the Armed Forces. 3. Congress shall have the power to carry out this article through appropriate legislation. .",
      "versionDate": "2026-04-29",
      "versionType": "IS"
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
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-05-04",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "172",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Proposing an amendment to the Constitution of the United States to protect United States citizenship.",
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
        "updateDate": "2026-05-15T15:49:11Z"
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
      "date": "2026-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sjres/BILLS-119sjres189is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A joint resolution proposing an amendment to the Constitution of the United States to protect United States citizenship.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-02T03:33:30Z"
    },
    {
      "title": "A joint resolution proposing an amendment to the Constitution of the United States to protect United States citizenship.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T10:56:21Z"
    }
  ]
}
```
