# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1019?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1019
- Title: Recognizing the roles and the contributions of America's Certified Registered Nurse Anesthetists (CRNAs) and their critical role in providing quality health care for the public and our Nation's Armed Forces, for more than 150 years and through multiple public health emergencies and beyond.
- Congress: 119
- Bill type: HRES
- Bill number: 1019
- Origin chamber: House
- Introduced date: 2026-01-23
- Update date: 2026-01-26T13:44:22Z
- Update date including text: 2026-01-26T13:44:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-23: Introduced in House
- 2026-01-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-01-23 - IntroReferral: Submitted in House
- 2026-01-23 - IntroReferral: Submitted in House
- Latest action: 2026-01-23: Submitted in House

## Actions

- 2026-01-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-01-23 - IntroReferral: Submitted in House
- 2026-01-23 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-23",
    "latestAction": {
      "actionDate": "2026-01-23",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1019",
    "number": "1019",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001145",
        "district": "9",
        "firstName": "Janice",
        "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
        "lastName": "Schakowsky",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Recognizing the roles and the contributions of America's Certified Registered Nurse Anesthetists (CRNAs) and their critical role in providing quality health care for the public and our Nation's Armed Forces, for more than 150 years and through multiple public health emergencies and beyond.",
    "type": "HRES",
    "updateDate": "2026-01-26T13:44:22Z",
    "updateDateIncludingText": "2026-01-26T13:44:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-23",
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
      "actionDate": "2026-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-01-23",
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
          "date": "2026-01-23T15:00:10Z",
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
      "bioguideId": "J000295",
      "district": "14",
      "firstName": "David",
      "fullName": "Rep. Joyce, David P. [R-OH-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Joyce",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-01-23",
      "state": "OH"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2026-01-23",
      "state": "NY"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2026-01-23",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1019ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1019\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2026 Ms. Schakowsky (for herself, Mr. Joyce of Ohio , Mr. Tonko , and Ms. Bonamici ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nRecognizing the roles and the contributions of America\u2019s Certified Registered Nurse Anesthetists (CRNAs) and their critical role in providing quality health care for the public and our Nation\u2019s Armed Forces, for more than 150 years and through multiple public health emergencies and beyond.\nThat the House of Representatives thanks and promotes the profession of Certified Registered Nurse Anesthetists (CRNAs) and their incredible, selfless, and dedicated service for over 150 years, by encouraging patients, hospital administrators, health care professionals, policymakers, and others to utilize CRNAs to their full potential and to recognize the work of CRNAs by participating in National CRNA Week.",
      "versionDate": "2026-01-23",
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
        "actionDate": "2025-01-24",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "67",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Recognizing the roles and the contributions of Americas Certified Registered Nurse Anesthetists (CRNAs) and their critical role in providing quality health care for the public and the Nation's Armed Forces for more than 150 years and through multiple public health emergencies and beyond.",
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
        "name": "Health",
        "updateDate": "2026-01-26T13:44:22Z"
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
      "date": "2026-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1019ih.xml"
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
      "title": "Recognizing the roles and the contributions of America's Certified Registered Nurse Anesthetists (CRNAs) and their critical role in providing quality health care for the public and our Nation's Armed Forces, for more than 150 years and through multiple public health emergencies and beyond.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-24T09:18:22Z"
    },
    {
      "title": "Recognizing the roles and the contributions of America's Certified Registered Nurse Anesthetists (CRNAs) and their critical role in providing quality health care for the public and our Nation's Armed Forces, for more than 150 years and through multiple public health emergencies and beyond.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-24T09:06:21Z"
    }
  ]
}
```
