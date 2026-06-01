# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1316?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1316
- Title: Expressing the sense of the House of Representatives to reduce traffic fatalities to zero by 2050.
- Congress: 119
- Bill type: HRES
- Bill number: 1316
- Origin chamber: House
- Introduced date: 2026-05-21
- Update date: 2026-05-22T10:18:40Z
- Update date including text: 2026-05-22T10:18:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-21: Introduced in House
- 2026-05-21 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-05-21 - IntroReferral: Submitted in House
- Latest action: 2026-05-21: Submitted in House

## Actions

- 2026-05-21 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-05-21 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-21",
    "latestAction": {
      "actionDate": "2026-05-21",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1316",
    "number": "1316",
    "originChamber": "House",
    "policyArea": {},
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
    "title": "Expressing the sense of the House of Representatives to reduce traffic fatalities to zero by 2050.",
    "type": "HRES",
    "updateDate": "2026-05-22T10:18:40Z",
    "updateDateIncludingText": "2026-05-22T10:18:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
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
          "date": "2026-05-21T14:04:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
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
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "NV"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "NJ"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "DC"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "NY"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "CA"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "IL"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "NM"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "TN"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "MO"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "IL"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1316ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1316\nIN THE HOUSE OF REPRESENTATIVES\nMay 21, 2026 Ms. Schakowsky (for herself, Ms. Titus , Mrs. McIver , Ms. Norton , Ms. Meng , Mr. Huffman , Mr. Garc\u00eda of Illinois , Ms. Stansbury , Mr. Cohen , Mr. Cleaver , Mr. Krishnamoorthi , and Ms. Jayapal ) submitted the following resolution; which was referred to the Committee on Transportation and Infrastructure\nRESOLUTION\nExpressing the sense of the House of Representatives to reduce traffic fatalities to zero by 2050.\nThat the House of Representatives\u2014\n**(1)**\ncommits to advancing policies that will end roadway fatalities by 2050;\n**(2)**\ncalls on Congress and the Department of Transportation to commit to working together to achieve zero roadway fatalities by the year 2050;\n**(3)**\nsupports efforts to address disparities related to transportation safety;\n**(4)**\ncalls on the Department of Transportation, and the agencies within the Department of Transportation, to improve data gathering and tracking of traffic crashes and other issues related to transportation safety;\n**(5)**\ncalls on the Department of Transportation, and the agencies within the Department of Transportation, to commit to the implementation of proven countermeasures and interventions to prioritize transportation safety;\n**(6)**\nrecognizes the need for a safe system approach to transportation in the United States to improve access, safety, and mobility; and\n**(7)**\nsupports the use of the term crash , instead of accident , when describing traffic incidents and encourages all agencies of the Federal Government to use this term.",
      "versionDate": "2026-05-21",
      "versionType": "IH"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1316ih.xml"
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
      "title": "Expressing the sense of the House of Representatives to reduce traffic fatalities to zero by 2050.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-22T10:18:40Z"
    },
    {
      "title": "Expressing the sense of the House of Representatives to reduce traffic fatalities to zero by 2050.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T08:08:30Z"
    }
  ]
}
```
