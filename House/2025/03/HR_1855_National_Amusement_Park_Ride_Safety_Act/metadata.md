# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1855?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1855
- Title: National Amusement Park Ride Safety Act
- Congress: 119
- Bill type: HR
- Bill number: 1855
- Origin chamber: House
- Introduced date: 2025-03-05
- Update date: 2025-11-05T09:05:42Z
- Update date including text: 2025-11-05T09:05:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-05: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-03-05 - IntroReferral: Sponsor introductory remarks on measure. (CR E186)
- Latest action: 2025-03-05: Introduced in House

## Actions

- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-03-05 - IntroReferral: Sponsor introductory remarks on measure. (CR E186)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1855",
    "number": "1855",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "C001072",
        "district": "7",
        "firstName": "Andr\u00e9",
        "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
        "lastName": "Carson",
        "party": "D",
        "state": "IN"
      }
    ],
    "title": "National Amusement Park Ride Safety Act",
    "type": "HR",
    "updateDate": "2025-11-05T09:05:42Z",
    "updateDateIncludingText": "2025-11-05T09:05:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-05",
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
      "actionCode": "Intro-H",
      "actionDate": "2025-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR E186)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-03-05T15:02:35Z",
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
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "MI"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NJ"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "LA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1855ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1855\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2025 Mr. Carson (for himself, Ms. Tlaib , and Mrs. McIver ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Consumer Product Safety Act to ensure amusement rides permanently fixed to a site are treated as consumer products, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the National Amusement Park Ride Safety Act .\n#### 2. Amusement rides permanently fixed to a site\n##### (a) In general\nSection 3(a)(5) of the Consumer Product Safety Act ( 15 U.S.C. 2052(a)(5) ) is amended by striking , and which is not permanently fixed to a site. Such term does not include such a device which is permanently fixed to a site. and inserting a period.\n##### (b) Authorization of appropriations\n**(1) In general**\nIn addition to amounts otherwise authorized to be appropriated to the Consumer Product Safety Commission, there is authorized to be appropriated to the Commission each fiscal year for activities relating to covered devices $11,500,000, of which\u2014\n**(A)**\n$5,000,000 each fiscal year is authorized to be appropriated exclusively for activities relating to covered devices not permanently fixed to a site; and\n**(B)**\n$6,500,000 each fiscal year is authorized to be appropriated exclusively for activities relating to covered devices permanently fixed to a site.\n**(2) Covered device defined**\nIn this subsection, the term covered device means a mechanical device which carries or conveys passengers along, around, or over a fixed or restricted route or course or within a defined area for the purpose of giving its passengers amusement, which is customarily controlled or directed by an individual who is employed for that purpose and who is not a consumer with respect to such device.",
      "versionDate": "2025-03-05",
      "versionType": "Introduced in House"
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
        "name": "Commerce",
        "updateDate": "2025-05-14T15:18:45Z"
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
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1855ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "National Amusement Park Ride Safety Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:08:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "National Amusement Park Ride Safety Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Consumer Product Safety Act to ensure amusement rides permanently fixed to a site are treated as consumer products, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:04:03Z"
    }
  ]
}
```
