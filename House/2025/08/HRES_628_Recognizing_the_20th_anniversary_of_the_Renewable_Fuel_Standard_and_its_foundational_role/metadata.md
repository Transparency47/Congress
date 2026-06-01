# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/628?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/628
- Title: Recognizing the 20th anniversary of the Renewable Fuel Standard and its foundational role in strengthening United States energy security, supporting rural communities, growing the United States economy, and improving environmental performance.
- Congress: 119
- Bill type: HRES
- Bill number: 628
- Origin chamber: House
- Introduced date: 2025-08-01
- Update date: 2025-09-12T16:15:35Z
- Update date including text: 2025-09-12T16:15:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-08-01: Introduced in House
- 2025-08-01 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-08-01 - IntroReferral: Submitted in House
- 2025-08-01 - IntroReferral: Submitted in House
- Latest action: 2025-08-01: Submitted in House

## Actions

- 2025-08-01 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-08-01 - IntroReferral: Submitted in House
- 2025-08-01 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-01",
    "latestAction": {
      "actionDate": "2025-08-01",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/628",
    "number": "628",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "M001222",
        "district": "7",
        "firstName": "Max",
        "fullName": "Rep. Miller, Max L. [R-OH-7]",
        "lastName": "Miller",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Recognizing the 20th anniversary of the Renewable Fuel Standard and its foundational role in strengthening United States energy security, supporting rural communities, growing the United States economy, and improving environmental performance.",
    "type": "HRES",
    "updateDate": "2025-09-12T16:15:35Z",
    "updateDateIncludingText": "2025-09-12T16:15:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-01",
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
      "actionDate": "2025-08-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-08-01",
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
          "date": "2025-08-01T14:02:45Z",
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
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "IL"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "NE"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "MN"
    },
    {
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "NE"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "NE"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "IL"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "IA"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "IA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-08-08",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres628ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 628\nIN THE HOUSE OF REPRESENTATIVES\nAugust 1, 2025 Mr. Miller of Ohio (for himself, Ms. Budzinski , Mr. Smith of Nebraska , Ms. Craig , Mr. Flood , Mr. Bacon , Mr. Bost , Mr. Feenstra , and Mrs. Miller-Meeks ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nRecognizing the 20th anniversary of the Renewable Fuel Standard and its foundational role in strengthening United States energy security, supporting rural communities, growing the United States economy, and improving environmental performance.\nThat the House of Representatives\u2014\n**(1)**\nrecognizes the 20th anniversary of the Renewable Fuel Standard ( RFS ) as a milestone in the commitment of the United States to strengthening energy security, supporting rural communities, growing the economy, and improving environmental performance;\n**(2)**\ncommends the contributions of the RFS in building a robust and innovative domestic renewable fuels industry;\n**(3)**\nrecognizes the positive impacts of the RFS on United States energy policy, the agricultural sector, and the environment over the past 20 years;\n**(4)**\naffirms the continued importance of the RFS in advancing the Nation\u2019s energy, economic, and environmental goals;\n**(5)**\nbelieves that diversifying the United States fuel supply with an increasing percentage of domestic renewable fuel strengthens the Nation\u2019s economy, increases security, and improves environmental performance; and\n**(6)**\nsupports continued implementation of the RFS as enacted in 2007 to achieve this goal.",
      "versionDate": "2025-08-01",
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
        "actionDate": "2025-08-01",
        "text": "Referred to the Committee on Environment and Public Works. (text: CR S5211-5212)"
      },
      "number": "364",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution recognizing the 20th anniversary of the Renewable Fuel Standard and its foundational role in strengthening American energy security, supporting rural communities, growing the United States economy, and improving environmental performance.",
      "type": "SRES"
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
        "name": "Energy",
        "updateDate": "2025-09-12T16:15:35Z"
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
      "date": "2025-08-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres628ih.xml"
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
      "title": "Recognizing the 20th anniversary of the Renewable Fuel Standard and its foundational role in strengthening United States energy security, supporting rural communities, growing the United States economy, and improving environmental performance.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-02T08:18:29Z"
    },
    {
      "title": "Recognizing the 20th anniversary of the Renewable Fuel Standard and its foundational role in strengthening United States energy security, supporting rural communities, growing the United States economy, and improving environmental performance.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-02T08:05:22Z"
    }
  ]
}
```
