# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/167?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/167
- Title: To establish uniform standards for flag displays in the House of Representatives facilities.
- Congress: 119
- Bill type: HRES
- Bill number: 167
- Origin chamber: House
- Introduced date: 2025-02-26
- Update date: 2026-02-24T09:05:26Z
- Update date including text: 2026-02-24T09:05:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-26: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the House Committee on House Administration.
- 2025-02-26 - Committee: Submitted in House
- Latest action: 2025-02-26: Submitted in House

## Actions

- 2025-02-26 - IntroReferral: Referred to the House Committee on House Administration.
- 2025-02-26 - Committee: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-26",
    "latestAction": {
      "actionDate": "2025-02-26",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/167",
    "number": "167",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "H001098",
        "district": "8",
        "firstName": "Abraham",
        "fullName": "Rep. Hamadeh, Abraham [R-AZ-8]",
        "lastName": "Hamadeh",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "To establish uniform standards for flag displays in the House of Representatives facilities.",
    "type": "HRES",
    "updateDate": "2026-02-24T09:05:26Z",
    "updateDateIncludingText": "2026-02-24T09:05:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-26",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-02-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
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
          "date": "2025-02-26T15:03:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "NY"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "TN"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison [R-NC-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "NC"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "WI"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "TX"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John J. [R-VA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "VA"
    },
    {
      "bioguideId": "T000490",
      "district": "2",
      "firstName": "David",
      "fullName": "Rep. Taylor, David J. [R-OH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Taylor",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "OH"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig A. [R-TX-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "TX"
    },
    {
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "KY"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-07-25",
      "state": "TN"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres167ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 167\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 26, 2025 Mr. Hamadeh of Arizona (for himself, Ms. Tenney , Mrs. Harshbarger , and Mr. McDowell ) submitted the following resolution; which was referred to the Committee on House Administration\nRESOLUTION\nTo establish uniform standards for flag displays in the House of Representatives facilities.\n#### 1. Scope and application\n##### (a) Application\nThis resolution shall apply to the following:\n**(1)**\nOffice buildings of the House of Representatives;\n**(2)**\nAny office or facility used by the leadership of the House of Representatives for official purposes.\n**(3)**\nAny locations used for official purposes by a committee of the House of Representatives.\n**(4)**\nAny other area under the jurisdiction of the House of Representatives.\n##### (b) Exception\nNothing in this resolution shall apply to the individual personal office space of a Member of the House of Representatives.\n#### 2. Authorized flag displays\nIn any location covered by section 1, the only flags that may be displayed are the following:\n**(1)**\nThe United States flag, as defined in section 700(b) of title 18, United States Code.\n**(2)**\nThe official House of Representatives flags and insignia.\n**(3)**\nThe State flag of the represented district of a Member of the House of Representatives, displayed adjacent to the office of such Member.\n**(4)**\nA military service flag.\n**(5)**\nThe POW/MIA flag.\n**(6)**\nAny flag eligible to be displayed in the Hall of Tribal Nations of the Bureau of Indian Affairs Museum Program.\n**(7)**\nThe flags of visiting foreign dignitaries during an official visit.\n#### 3. Oversight\nThe Administration Committee of the House of Representatives and the Sergeant of Arms shall oversee the application of this resolution, including by\u2014\n**(1)**\nestablishing a process for reviewing and approving temporary exceptions; and\n**(2)**\nimplementing a timeline for compliance with the requirements of this resolution, including an initial implementation date that is not later than 30 days after the date of enactment of this resolution.",
      "versionDate": "2025-02-26",
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
        "name": "Congress",
        "updateDate": "2025-03-04T16:45:19Z"
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
      "date": "2025-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres167ih.xml"
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
      "title": "To establish uniform standards for flag displays in the House of Representatives facilities.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:12:37Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish uniform standards for flag displays in the House of Representatives facilities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-01T09:06:20Z"
    }
  ]
}
```
