# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/449?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/449
- Title: Supports the designation of "ALS Awareness Month".
- Congress: 119
- Bill type: HRES
- Bill number: 449
- Origin chamber: House
- Introduced date: 2025-05-29
- Update date: 2025-05-30T14:27:44Z
- Update date including text: 2025-05-30T14:27:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-29: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-05-29 - IntroReferral: Submitted in House
- 2025-05-29 - IntroReferral: Submitted in House
- Latest action: 2025-05-29: Submitted in House

## Actions

- 2025-05-29 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-05-29 - IntroReferral: Submitted in House
- 2025-05-29 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-29",
    "latestAction": {
      "actionDate": "2025-05-29",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/449",
    "number": "449",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001121",
        "district": "6",
        "firstName": "Jason",
        "fullName": "Rep. Crow, Jason [D-CO-6]",
        "lastName": "Crow",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Supports the designation of \"ALS Awareness Month\".",
    "type": "HRES",
    "updateDate": "2025-05-30T14:27:44Z",
    "updateDateIncludingText": "2025-05-30T14:27:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-29",
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
      "actionDate": "2025-05-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-05-29",
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
          "date": "2025-05-29T15:02:20Z",
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
      "bioguideId": "C000059",
      "district": "41",
      "firstName": "Ken",
      "fullName": "Rep. Calvert, Ken [R-CA-41]",
      "isOriginalCosponsor": "True",
      "lastName": "Calvert",
      "party": "R",
      "sponsorshipDate": "2025-05-29",
      "state": "CA"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "AL"
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
      "sponsorshipDate": "2025-05-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres449ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 449\nIN THE HOUSE OF REPRESENTATIVES\nMay 29, 2025 Mr. Crow (for himself, Mr. Calvert , Ms. Sewell , and Mr. Fitzpatrick ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nSupports the designation of ALS Awareness Month .\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of ALS Awareness Month ;\n**(2)**\naffirms the dedication of the House of Representatives to ensuring people with ALS have access to effective treatments as soon as possible and identifying risk factors and causes of ALS to prevent new cases;\n**(3)**\naffirms the dedication of the House of Representatives to empowering people with ALS to engage with the world in the way they want;\n**(4)**\naffirms the dedication of the House of Representatives to reducing physical, emotional, and financial burdens of living with ALS;\n**(5)**\naffirms the dedication of the House of Representatives to ensuring all people with ALS and their caregivers receive high-quality services and supports that benefit them; and\n**(6)**\ncommends the dedication of the family members, friends, organizations, volunteers, researchers, and caregivers across the United States that are working to improve the quality and length of life of ALS patients and the development of treatments and cures that reach patients as soon as possible.",
      "versionDate": "2025-05-29",
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
        "updateDate": "2025-05-30T14:27:44Z"
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
      "date": "2025-05-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres449ih.xml"
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
      "title": "Supports the designation of \"ALS Awareness Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-30T08:18:19Z"
    },
    {
      "title": "Supports the designation of \"ALS Awareness Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-30T08:05:22Z"
    }
  ]
}
```
