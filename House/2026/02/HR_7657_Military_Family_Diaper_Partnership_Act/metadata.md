# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7657?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7657
- Title: Military Family Diaper Partnership Act
- Congress: 119
- Bill type: HR
- Bill number: 7657
- Origin chamber: House
- Introduced date: 2026-02-24
- Update date: 2026-05-13T08:06:10Z
- Update date including text: 2026-05-13T08:06:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-24: Introduced in House
- 2026-02-24 - IntroReferral: Introduced in House
- 2026-02-24 - IntroReferral: Introduced in House
- 2026-02-24 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2026-02-24: Introduced in House

## Actions

- 2026-02-24 - IntroReferral: Introduced in House
- 2026-02-24 - IntroReferral: Introduced in House
- 2026-02-24 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-24",
    "latestAction": {
      "actionDate": "2026-02-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7657",
    "number": "7657",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "F000477",
        "district": "4",
        "firstName": "Valerie",
        "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
        "lastName": "Foushee",
        "party": "D",
        "state": "NC"
      }
    ],
    "title": "Military Family Diaper Partnership Act",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:10Z",
    "updateDateIncludingText": "2026-05-13T08:06:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-24",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-24",
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
          "date": "2026-02-24T15:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "PA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "DC"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7657ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7657\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 24, 2026 Mrs. Foushee (for herself and Mr. Mackenzie ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo direct the Secretary of Defense to provide funds to the National Diaper Bank Network for the establishment of a Military Family Diaper Fund to provide diapers and diapering supplies to military families in need, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Military Family Diaper Partnership Act .\n#### 2. Provision of funds for establishment of Military Family Diaper Fund\n##### (a) Provision of Funds\nThe Secretary of Defense shall seek to enter an agreement with the National Diaper Bank Network to provide to the Network $1,000,000 for each of fiscal years 2027 through 2030 for the purpose of establishing a military family diaper fund to distribute diapers and diapering supplies to military families.\n##### (b) Use of funds\nAn agreement under subsection (a) shall provide that\u2014\n**(1)**\nthe National Diaper Bank Network shall establish a military family diaper fund and deposit funds received from the Secretary under the agreement into such fund;\n**(2)**\nthe National Diaper Bank Network shall deposit into the military family diaper fund matching funds or in-kind contributions from non-Federal Government sources that are of a value equal or greater to the amount of funds provided by the Secretary under the agreement;\n**(3)**\nfunds or in-kind contributions in the military family diaper fund shall only be provided to members of the National Diaper Bank Network who have engaged in the distribution of diapers or diapering supplies in an area located within 20 miles of a military installation for a period of not less than five years;\n**(4)**\nsuch funds or in-kind contributions shall only be used\u2014\n**(A)**\nto provide diapers and diapering supplies to military families in need of diapers or diapering supplies; or\n**(B)**\nfor technical assistance and evaluation provided by the National Diaper Bank Network; and\n**(5)**\nthe National Diaper Bank Network shall submit to the Secretary of Defense an annual report on the activities carried out using the military family diaper fund during the preceding fiscal year.",
      "versionDate": "2026-02-24",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-03-12T15:09:46Z"
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
      "date": "2026-02-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7657ih.xml"
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
      "title": "Military Family Diaper Partnership Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-11T03:38:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Military Family Diaper Partnership Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-11T03:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Defense to provide funds to the National Diaper Bank Network for the establishment of a Military Family Diaper Fund to provide diapers and diapering supplies to military families in need, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-11T03:33:36Z"
    }
  ]
}
```
