# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/117?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/117
- Title: A resolution providing for members on the part of the Senate of the Joint Committee on Printing and the Joint Committee of Congress on the Library.
- Congress: 119
- Bill type: SRES
- Bill number: 117
- Origin chamber: Senate
- Introduced date: 2025-03-06
- Update date: 2025-05-14T17:55:37Z
- Update date including text: 2025-05-14T17:55:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-06: Introduced in Senate
- 2025-03-06 - IntroReferral: Introduced in Senate
- 2025-03-06 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent.
- 2025-03-06 - Floor: Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent. (consideration: CR S1616; text: CR S1609)
- Latest action: 2025-03-06: Introduced in Senate

## Actions

- 2025-03-06 - IntroReferral: Introduced in Senate
- 2025-03-06 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent.
- 2025-03-06 - Floor: Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent. (consideration: CR S1616; text: CR S1609)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/117",
    "number": "117",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "M000355",
        "district": "",
        "firstName": "Mitch",
        "fullName": "Sen. McConnell, Mitch [R-KY]",
        "lastName": "McConnell",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "A resolution providing for members on the part of the Senate of the Joint Committee on Printing and the Joint Committee of Congress on the Library.",
    "type": "SRES",
    "updateDate": "2025-05-14T17:55:37Z",
    "updateDateIncludingText": "2025-05-14T17:55:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-06",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent. (consideration: CR S1616; text: CR S1609)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-03-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-06",
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
      "sponsorshipDate": "2025-03-06",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres117ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 117\nIN THE SENATE OF THE UNITED STATES\nMarch 6, 2025 Mr. McConnell (for himself and Mr. Padilla ) submitted the following resolution; which was considered and agreed to\nRESOLUTION\nProviding for members on the part of the Senate of the Joint Committee on Printing and the Joint Committee of Congress on the Library.\nThat the following named Members be, and they are hereby, elected members of the following joint committees of Congress:\nJoint Committee on Printing:\nMr. McConnell, Mrs. Fischer, Mr. Hagerty, Mr. Padilla, and Mr. Merkley.\nJoint Committee of Congress on the Library:\nMr. McConnell, Mrs. Fischer, Mrs. Hyde-Smith, Mr. Padilla, and Ms. Klobuchar.",
      "versionDate": "2025-03-06",
      "versionType": "ATS"
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
        "name": "Congress",
        "updateDate": "2025-05-14T17:55:37Z"
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
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres117ats.xml"
        }
      ],
      "type": "ATS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "A resolution providing for members on the part of the Senate of the Joint Committee on Printing and the Joint Committee of Congress on the Library.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-07T11:56:15Z"
    },
    {
      "title": "A resolution providing for members on the part of the Senate of the Joint Committee on Printing and the Joint Committee of Congress on the Library.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-07T11:56:15Z"
    }
  ]
}
```
