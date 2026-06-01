# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4867?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4867
- Title: PHDs First Act
- Congress: 119
- Bill type: HR
- Bill number: 4867
- Origin chamber: House
- Introduced date: 2025-08-01
- Update date: 2025-09-18T16:57:09Z
- Update date including text: 2025-09-18T16:57:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-01: Introduced in House
- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-08-01: Introduced in House

## Actions

- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Referred to the House Committee on the Judiciary.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4867",
    "number": "4867",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "T000488",
        "district": "13",
        "firstName": "Shri",
        "fullName": "Rep. Thanedar, Shri [D-MI-13]",
        "lastName": "Thanedar",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "PHDs First Act",
    "type": "HR",
    "updateDate": "2025-09-18T16:57:09Z",
    "updateDateIncludingText": "2025-09-18T16:57:09Z"
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
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-01",
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
          "date": "2025-08-01T14:06:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "NY"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4867ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4867\nIN THE HOUSE OF REPRESENTATIVES\nAugust 1, 2025 Mr. Thanedar (for himself and Mr. Lawler ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo provide lawful permanent resident status and authorized dual intent for certain doctoral degree holders.\n#### 1. Short title\nThis Act may be cited as the Putting Highest Degrees First Act of 2025 or the PHDs First Act .\n#### 2. Exemption from numerical limitations on permanent residents for certain doctoral degree holders\n##### (a) In general\nSection 201(b)(1) of the Immigration and Nationality Act ( 8 U.S.C. 1151(b)(1) ) is amended by adding at the end the following:\n(F) Aliens who\u2014 (i) have earned a doctoral degree in a field of study (or the terminal highest degree awarded in a field of study for which a doctoral degree or its equivalent is not available) while physically present in the United States from a United States institution of higher education (as defined in section 101(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) )) accredited by a nationally recognized accrediting agency or association recognized by the Secretary of Education pursuant to part H of title IV of the Higher Education Act of 1965 ( 20 U.S.C. 1099a et seq. ); (ii) have an offer of employment from, or are employed by, a United States employer in a field related to such degree at a rate of pay that is higher than the median wage level for the occupational classification in the area of employment, as determined by the Secretary of Labor; and (iii) are admissible pursuant to an approved labor certification under section 212(a)(5)(A)(i). .\n##### (b) Procedure for Granting Immigration Status\nSection 204(a)(1)(F) of the Immigration and Nationality Act ( 8 U.S.C. 1154(a)(1)(F) ) is amended by striking 203(b)(2) and all that follows through Attorney General and inserting 203(b)(2), 203(b)(3), or 201(b)(1)(F) may file a petition with the Secretary of Homeland Security .\n##### (c) Dual Intent for F Nonimmigrants Seeking doctoral degrees at United States Institutions of Higher Education\nNotwithstanding sections 101(a)(15)(F)(i) and 214(b) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15)(F)(i) , 1184(b)), an alien who is a bona fide student admitted to a program in a field for a doctoral degree or the terminal highest degree awarded in a field of study for which a doctoral degree or its equivalent is not available at a United States institution of higher education (as defined in section 101(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) )) accredited by a nationally recognized accrediting agency or association recognized by the Secretary of Education pursuant to part H of title IV of the Higher Education Act of 1965 ( 20 U.S.C. 1099a et seq. ) may obtain a student visa or extend or change nonimmigrant status to pursue such degree even if such alien intends to seek lawful permanent resident status in the United States.",
      "versionDate": "2025-08-01",
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
        "name": "Immigration",
        "updateDate": "2025-09-18T16:57:09Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4867ih.xml"
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
      "title": "PHDs First Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T03:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PHDs First Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Putting Highest Degrees First Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide lawful permanent resident status and authorized dual intent for certain doctoral degree holders.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:33:24Z"
    }
  ]
}
```
