# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/164?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/164
- Title: A resolution supporting the goals and ideals of National Public Safety Telecommunicators Week.
- Congress: 119
- Bill type: SRES
- Bill number: 164
- Origin chamber: Senate
- Introduced date: 2025-04-09
- Update date: 2025-12-05T21:46:40Z
- Update date including text: 2025-12-05T21:46:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-09: Introduced in Senate
- 2025-04-09 - IntroReferral: Introduced in Senate
- 2025-04-09 - IntroReferral: Referred to the Committee on Commerce, Science, and Transportation. (text: CR S2528)
- Latest action: 2025-04-09: Introduced in Senate

## Actions

- 2025-04-09 - IntroReferral: Introduced in Senate
- 2025-04-09 - IntroReferral: Referred to the Committee on Commerce, Science, and Transportation. (text: CR S2528)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-09",
    "latestAction": {
      "actionDate": "2025-04-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/164",
    "number": "164",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "A resolution supporting the goals and ideals of National Public Safety Telecommunicators Week.",
    "type": "SRES",
    "updateDate": "2025-12-05T21:46:40Z",
    "updateDateIncludingText": "2025-12-05T21:46:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Commerce, Science, and Transportation. (text: CR S2528)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-09",
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
          "date": "2025-04-09T15:44:18Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres164is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 164\nIN THE SENATE OF THE UNITED STATES\nApril 9, 2025 Ms. Klobuchar (for herself and Mr. Budd ) submitted the following resolution; which was referred to the Committee on Commerce, Science, and Transportation\nRESOLUTION\nSupporting the goals and ideals of National Public Safety Telecommunicators Week.\nThat the Senate\u2014\n**(1)**\nsupports the goals and ideals of National Public Safety Telecommunicators Week;\n**(2)**\nhonors and recognizes the important and lifesaving contributions of public safety telecommunications professionals in the United States; and\n**(3)**\nencourages the people of the United States to remember the value of the work performed by public safety telecommunications professionals.",
      "versionDate": "2025-04-09",
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
        "actionDate": "2025-04-09",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "322",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Supporting the goals and ideals of National Public Safety Telecommunicators Week.",
      "type": "HRES"
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-05-01T12:30:48Z"
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
      "date": "2025-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres164is.xml"
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
      "title": "A resolution supporting the goals and ideals of National Public Safety Telecommunicators Week.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-12T02:48:15Z"
    },
    {
      "title": "A resolution supporting the goals and ideals of National Public Safety Telecommunicators Week.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-10T10:56:24Z"
    }
  ]
}
```
