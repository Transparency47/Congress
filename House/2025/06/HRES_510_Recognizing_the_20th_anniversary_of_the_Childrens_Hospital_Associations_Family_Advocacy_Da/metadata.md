# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/510?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/510
- Title: Recognizing the 20th anniversary of the Children's Hospital Association's Family Advocacy Day and honoring the contributions of children's hospitals and their patients and families.
- Congress: 119
- Bill type: HRES
- Bill number: 510
- Origin chamber: House
- Introduced date: 2025-06-12
- Update date: 2025-06-27T13:05:06Z
- Update date including text: 2025-06-27T13:05:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-06-12: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-06-12 - IntroReferral: Submitted in House
- 2025-06-12 - IntroReferral: Submitted in House
- Latest action: 2025-06-12: Submitted in House

## Actions

- 2025-06-12 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-06-12 - IntroReferral: Submitted in House
- 2025-06-12 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/510",
    "number": "510",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001066",
        "district": "14",
        "firstName": "Kathy",
        "fullName": "Rep. Castor, Kathy [D-FL-14]",
        "lastName": "Castor",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Recognizing the 20th anniversary of the Children's Hospital Association's Family Advocacy Day and honoring the contributions of children's hospitals and their patients and families.",
    "type": "HRES",
    "updateDate": "2025-06-27T13:05:06Z",
    "updateDateIncludingText": "2025-06-27T13:05:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-12",
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
      "actionDate": "2025-06-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-06-12",
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
          "date": "2025-06-12T14:03:15Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres510ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 510\nIN THE HOUSE OF REPRESENTATIVES\nJune 12, 2025 Ms. Castor of Florida submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nRecognizing the 20th anniversary of the Children\u2019s Hospital Association\u2019s Family Advocacy Day and honoring the contributions of children\u2019s hospitals and their patients and families.\nThat the House of Representatives\u2014\n**(1)**\nhonors the children and families who bravely share their stories to advocate for policies that strengthen pediatric care;\n**(2)**\ncommends the Children\u2019s Hospital Association for 20 years of Family Advocacy Day and its continued dedication to improving pediatric health care;\n**(3)**\nrecognizes the vital role of children\u2019s hospitals in delivering specialized, family-centered care to children across the nation; and\n**(4)**\nsupports continued federal investment in pediatric health care to ensure every child has timely access to the highest quality care.",
      "versionDate": "2025-06-12",
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
        "updateDate": "2025-06-27T13:05:06Z"
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
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres510ih.xml"
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
      "title": "Recognizing the 20th anniversary of the Children's Hospital Association's Family Advocacy Day and honoring the contributions of children's hospitals and their patients and families.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-14T04:18:17Z"
    },
    {
      "title": "Recognizing the 20th anniversary of the Children's Hospital Association's Family Advocacy Day and honoring the contributions of children's hospitals and their patients and families.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-13T08:06:20Z"
    }
  ]
}
```
