# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4333?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4333
- Title: VOICE Act
- Congress: 119
- Bill type: S
- Bill number: 4333
- Origin chamber: Senate
- Introduced date: 2026-04-16
- Update date: 2026-05-13T18:12:51Z
- Update date including text: 2026-05-13T18:12:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-04-16: Introduced in Senate
- 2026-04-16 - IntroReferral: Introduced in Senate
- 2026-04-16 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-04-16: Introduced in Senate

## Actions

- 2026-04-16 - IntroReferral: Introduced in Senate
- 2026-04-16 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-16",
    "latestAction": {
      "actionDate": "2026-04-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4333",
    "number": "4333",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "L000570",
        "district": "",
        "firstName": "Ben",
        "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
        "lastName": "Luj\u00e1n",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "VOICE Act",
    "type": "S",
    "updateDate": "2026-05-13T18:12:51Z",
    "updateDateIncludingText": "2026-05-13T18:12:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-16",
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
      "actionDate": "2026-04-16",
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
          "date": "2026-04-16T19:54:25Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4333is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4333\nIN THE SENATE OF THE UNITED STATES\nApril 16 (legislative day, April 14), 2026 Mr. Luj\u00e1n introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo provide a civil remedy for any individual whose rights have been violated by a Federal law enforcement officer carrying out an immigration-related enforcement action.\n#### 1. Short title\nThis Act may be cited as the Victims of Immigration Conduct Enforcement Act or the VOICE Act .\n#### 2. Civil remedy for victims of unlawful immigration-related enforcement actions\nSection 2674 of title 28, United States Code, is amended\u2014\n**(1)**\nby inserting (a) before The United States shall be liable, respecting ;\n**(2)**\nby inserting (b) before If, however, ;\n**(3)**\nby inserting (c) before With respect to any claim under this chapter, ;\n**(4)**\nby inserting (d) before With respect to any claim to which this section applies, ; and\n**(5)**\nby adding at the end the following:\n(e) (1) In this subsection, the term Federal law enforcement officer has the meaning given the term law enforcement officer in section 1515 of title 18. (2) If, while acting under color of law to carry out an immigration-related enforcement action, a Federal law enforcement officer, or any other person acting under the direction of a Federal law enforcement officer, subjects, or causes to be subjected, any individual within the jurisdiction of the United States to the deprivation of any rights, privileges, or immunities secured by the Constitution or laws of the United States, the United States shall be liable to the aggrieved party in an action at law, a suit in equity, or any other proper proceeding for redress, regardless of whether the officer or other person was acting consistent with an official policy, practice, or custom. (3) Monetary damages awarded in a case authorized under paragraph (2) shall be paid by the Federal agency that employed the Federal law enforcement officer who subjected or caused to be subjected, or under whose direction another person subjected or caused to be subjected, an individual to the deprivation of rights, privileges, or immunities secured by the Constitution or laws of the United States. (4) Section 2675(a) shall not apply to a civil action authorized under paragraph (2) of this subsection. (5) Notwithstanding subsection (a) or any other provision of law, if the United States is found liable in a case authorized under paragraph (2) of this subsection, the claimant shall be awarded $2,000,000 in punitive damages. (6) Nothing in this subsection may be construed to limit or preclude any legal, equitable, or other remedy that is otherwise available against an individual Federal law enforcement officer or other person. .",
      "versionDate": "2026-04-16",
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
        "name": "Immigration",
        "updateDate": "2026-05-13T18:12:51Z"
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
      "date": "2026-04-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4333is.xml"
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
      "title": "VOICE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-29T04:53:37Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "VOICE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-29T04:53:34Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Victims of Immigration Conduct Enforcement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-29T04:53:34Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide a civil remedy for any individual whose rights have been violated by a Federal law enforcement officer carrying out an immigration-related enforcement action.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-29T04:48:54Z"
    }
  ]
}
```
