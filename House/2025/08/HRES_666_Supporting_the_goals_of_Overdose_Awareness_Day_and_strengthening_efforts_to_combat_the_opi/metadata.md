# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/666?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/666
- Title: Supporting the goals of Overdose Awareness Day and strengthening efforts to combat the opioid crisis in the United States.
- Congress: 119
- Bill type: HRES
- Bill number: 666
- Origin chamber: House
- Introduced date: 2025-08-29
- Update date: 2025-09-19T17:17:12Z
- Update date including text: 2025-09-19T17:17:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-29: Introduced in House
- 2025-08-29 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-08-29 - IntroReferral: Submitted in House
- 2025-08-29 - IntroReferral: Submitted in House
- Latest action: 2025-08-29: Submitted in House

## Actions

- 2025-08-29 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-08-29 - IntroReferral: Submitted in House
- 2025-08-29 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-29",
    "latestAction": {
      "actionDate": "2025-08-29",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/666",
    "number": "666",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "T000482",
        "district": "3",
        "firstName": "Lori",
        "fullName": "Rep. Trahan, Lori [D-MA-3]",
        "lastName": "Trahan",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Supporting the goals of Overdose Awareness Day and strengthening efforts to combat the opioid crisis in the United States.",
    "type": "HRES",
    "updateDate": "2025-09-19T17:17:12Z",
    "updateDateIncludingText": "2025-09-19T17:17:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-29",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-08-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-08-29T17:32:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-08-29",
      "state": "CO"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-08-29",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres666ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 666\nIN THE HOUSE OF REPRESENTATIVES\nAugust 29, 2025 Mrs. Trahan (for herself, Ms. Pettersen , and Mr. Fitzpatrick ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nSupporting the goals of Overdose Awareness Day and strengthening efforts to combat the opioid crisis in the United States.\nThat the House of Representatives\u2014\n**(1)**\nrecognizes Overdose Awareness Day in the United States;\n**(2)**\ncommits to advancing and passing bipartisan policies that reduce the stigma surrounding substance use disorders and overdoses; and\n**(3)**\nis dedicated to collaborating with States, localities, businesses, nongovernmental organizations, health care providers, patients, and families to support a comprehensive system that promotes prevention, treatment, harm reduction, and recovery from opioid use disorder.",
      "versionDate": "2025-08-29",
      "versionType": "IH"
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
        "updateDate": "2025-09-19T17:17:12Z"
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
      "date": "2025-08-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres666ih.xml"
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
      "title": "Supporting the goals of Overdose Awareness Day and strengthening efforts to combat the opioid crisis in the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-30T08:18:20Z"
    },
    {
      "title": "Supporting the goals of Overdose Awareness Day and strengthening efforts to combat the opioid crisis in the United States.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-30T08:05:24Z"
    }
  ]
}
```
