# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8018?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8018
- Title: ISLET Act
- Congress: 119
- Bill type: HR
- Bill number: 8018
- Origin chamber: House
- Introduced date: 2026-03-19
- Update date: 2026-05-12T08:05:43Z
- Update date including text: 2026-05-12T08:05:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-19: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-03-19: Introduced in House

## Actions

- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-19",
    "latestAction": {
      "actionDate": "2026-03-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8018",
    "number": "8018",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "N000190",
        "district": "5",
        "firstName": "Ralph",
        "fullName": "Rep. Norman, Ralph [R-SC-5]",
        "lastName": "Norman",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "ISLET Act",
    "type": "HR",
    "updateDate": "2026-05-12T08:05:43Z",
    "updateDateIncludingText": "2026-05-12T08:05:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-19",
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
      "actionDate": "2026-03-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-19",
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
          "date": "2026-03-19T13:00:15Z",
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
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "NE"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "KS"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "TX"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8018ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8018\nIN THE HOUSE OF REPRESENTATIVES\nMarch 19, 2026 Mr. Norman (for himself and Mr. Bacon ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo regulate human cadaveric islets for transplantation as organs.\n#### 1. Short title\nThis Act may be cited as the Increase Support for Life-saving Endocrine Transplantation Act or the ISLET Act .\n#### 2. Regulation of human cadaveric islet transplants\n##### (a) In general\nSection 374(d)(2) of the Public Health Service Act ( 42 U.S.C. 274b(d)(2) ) is amended by striking pancreas, and inserting and pancreas, human cadaveric islets, .\n##### (b) Clarification\nNotwithstanding any other provision of law, none of the following terms includes human cadaveric islets:\n**(1)**\nThe term drug , as defined in section 201(g) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321(g) ).\n**(2)**\nThe term biological product , as defined in section 351(i) of the Public Health Service Act ( 42 U.S.C. 262(i) ).\n**(3)**\nThe term human cells, tissues, or cellular or tissue-based products (HCT/Ps) , as defined in section 1271.3 of title 21, Code of Federal Regulations (or any successor regulations).\n##### (c) Regulations\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the Secretary of Health and Human Services (referred to in this section as the Secretary ) shall update regulations promulgated under parts F, G, and H of title III of the Public Health Service Act ( 42 U.S.C. 262 et seq. , 264 et seq., 273 et seq.) and the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 301 et seq. ), and such other regulations as the Secretary determines appropriate, to carry out the amendment made by subsection (a).\n**(2) Report**\nNot later than 6 months after the date of enactment of this Act, the Secretary shall report to Congress on the progress made in updating regulations as required under paragraph (1).",
      "versionDate": "2026-03-19",
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
        "actionDate": "2025-11-05",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "3105",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "ISLET Act",
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
        "updateDate": "2026-04-03T20:29:31Z"
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
      "date": "2026-03-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8018ih.xml"
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
      "title": "ISLET Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-02T12:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ISLET Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-02T12:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Increase Support for Life-saving Endocrine Transplantation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-02T12:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To regulate human cadaveric islets for transplantation as organs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-02T12:03:26Z"
    }
  ]
}
```
