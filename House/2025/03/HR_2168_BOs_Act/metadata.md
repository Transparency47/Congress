# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2168?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2168
- Title: BO’s Act
- Congress: 119
- Bill type: HR
- Bill number: 2168
- Origin chamber: House
- Introduced date: 2025-03-14
- Update date: 2026-04-29T08:06:52Z
- Update date including text: 2026-04-29T08:06:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-14: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-03-14: Introduced in House

## Actions

- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-14",
    "latestAction": {
      "actionDate": "2025-03-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2168",
    "number": "2168",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "Y000067",
        "district": "2",
        "firstName": "Rudy",
        "fullName": "Rep. Yakym, Rudy [R-IN-2]",
        "lastName": "Yakym",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "BO\u2019s Act",
    "type": "HR",
    "updateDate": "2026-04-29T08:06:52Z",
    "updateDateIncludingText": "2026-04-29T08:06:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-14",
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
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-14",
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
          "date": "2025-03-14T13:02:50Z",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "NE"
    },
    {
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2025-08-08",
      "state": "NE"
    },
    {
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2025-08-08",
      "state": "OH"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "WV"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-09-08",
      "state": "GA"
    },
    {
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "UT"
    },
    {
      "bioguideId": "E000235",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Ezell, Mike [R-MS-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Ezell",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "MS"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "MS"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "TX"
    },
    {
      "bioguideId": "D000628",
      "district": "2",
      "firstName": "Neal",
      "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Dunn",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2168ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2168\nIN THE HOUSE OF REPRESENTATIVES\nMarch 14, 2025 Mr. Yakym introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Secretary of Health and Human Services to conduct a study and submit to Congress a report on the use of home cardiorespiratory monitors for infants, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Baby Observation Act or the BO\u2019s Act .\n#### 2. Study and report on home cardiorespiratory monitors for infants\n##### (a) Study\nThe Secretary of Health and Human Services (in this section referred to as the Secretary ), pursuant to section 1121(a) of the Public Health Service Act ( 42 U.S.C. 300c\u201311(a) ), shall conduct a study on the use of home cardiorespiratory monitors for infants in relation to the prevention of sudden unexpected infant death (as defined in section 1121(e) of such Act ( 42 U.S.C. 300c\u201311(e) )).\n##### (b) Report\nNot later than 1 year after the date of enactment of this Act, the Secretary shall submit to Congress a report describing the results of the study under subsection (a). Such report shall include the following:\n**(1)**\nEvidence on the effectiveness, performance, and accuracy of home cardiorespiratory monitors that track the heart rate, blood oxygen levels, and other vital signs of an infant.\n**(2)**\nNew models of care to improve the home sleeping environment of an infant, including the use of cardiorespiratory monitors.\n**(3)**\nHealth care plan criteria for medically appropriate coverage for a home cardiorespiratory monitor.\n**(4)**\nRecommendations on whether home cardiorespiratory monitors have shown product efficacy supporting coverage under public or private health insurance plans.",
      "versionDate": "2025-03-14",
      "versionType": "Introduced in House"
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
        "actionDate": "2026-01-28",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "3712",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "BO\u2019s Act",
      "type": "S"
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
        "updateDate": "2025-03-31T16:16:46Z"
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
      "date": "2025-03-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2168ih.xml"
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
      "title": "BO\u2019s Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:13:40Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "BO\u2019s Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-29T02:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Baby Observation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-29T02:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Health and Human Services to conduct a study and submit to Congress a report on the use of home cardiorespiratory monitors for infants, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-29T02:48:37Z"
    }
  ]
}
```
