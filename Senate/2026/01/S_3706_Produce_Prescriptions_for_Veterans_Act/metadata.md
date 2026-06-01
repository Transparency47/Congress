# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3706?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3706
- Title: Produce Prescriptions for Veterans Act
- Congress: 119
- Bill type: S
- Bill number: 3706
- Origin chamber: Senate
- Introduced date: 2026-01-27
- Update date: 2026-04-30T11:03:20Z
- Update date including text: 2026-04-30T11:03:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-27: Introduced in Senate
- 2026-01-27 - IntroReferral: Introduced in Senate
- 2026-01-27 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs. (text: CR S292)
- 2026-04-29 - Committee: Committee on Veterans' Affairs. Hearings held.
- Latest action: 2026-01-27: Introduced in Senate

## Actions

- 2026-01-27 - IntroReferral: Introduced in Senate
- 2026-01-27 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs. (text: CR S292)
- 2026-04-29 - Committee: Committee on Veterans' Affairs. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-27",
    "latestAction": {
      "actionDate": "2026-01-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3706",
    "number": "3706",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Produce Prescriptions for Veterans Act",
    "type": "S",
    "updateDate": "2026-04-30T11:03:20Z",
    "updateDateIncludingText": "2026-04-30T11:03:20Z"
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
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-27",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs. (text: CR S292)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-01-27",
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
            "date": "2026-04-29T21:37:26Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2026-01-27T23:36:09Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3706is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3706\nIN THE SENATE OF THE UNITED STATES\nJanuary 27, 2026 Mr. Durbin introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to authorize the provision of produce prescriptions to veterans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Produce Prescriptions for Veterans Act .\n#### 2. Provision of produce prescriptions to veterans\n##### (a) Inclusion as medical services\nParagraph (6) of section 1701 of title 38, United States Code, is amended by adding at the end the following new subparagraph:\n(J) The provision of produce prescriptions. .\n##### (b) Definition of produce prescription\nSuch section is further amended by adding at the end the following new paragraph:\n(11) The term produce prescription means a service in which the Secretary provides a benefit to a veteran who has a diet-related chronic condition and is food-insecure or refers such a veteran to receive a benefit, including a voucher or debit card, for the purchase of fruits and vegetables to improve a diet-related chronic condition. .",
      "versionDate": "2026-01-27",
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
        "actionDate": "2026-02-12",
        "text": "Referred to the Subcommittee on Health."
      },
      "number": "7267",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Produce Prescriptions for Veterans Act",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-02-23T17:17:48Z"
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
      "date": "2026-01-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3706is.xml"
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
      "title": "Produce Prescriptions for Veterans Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T11:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Produce Prescriptions for Veterans Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to authorize the provision of produce prescriptions to veterans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T03:48:26Z"
    }
  ]
}
```
