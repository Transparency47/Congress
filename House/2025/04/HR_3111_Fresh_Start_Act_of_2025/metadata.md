# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3111?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3111
- Title: Fresh Start Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3111
- Origin chamber: House
- Introduced date: 2025-04-30
- Update date: 2026-04-21T08:06:03Z
- Update date including text: 2026-04-21T08:06:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-30: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-04-30: Introduced in House

## Actions

- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-30",
    "latestAction": {
      "actionDate": "2025-04-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3111",
    "number": "3111",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "L000597",
        "district": "15",
        "firstName": "Laurel",
        "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
        "lastName": "Lee",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Fresh Start Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-21T08:06:03Z",
    "updateDateIncludingText": "2026-04-21T08:06:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-30",
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
      "actionDate": "2025-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-30",
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
          "date": "2025-04-30T14:04:30Z",
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
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "CA"
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
      "sponsorshipDate": "2025-04-30",
      "state": "DC"
    },
    {
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "KY"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "NE"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "TX"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "FL"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary Gay",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Scanlon",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "PA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-06-02",
      "state": "VA"
    },
    {
      "bioguideId": "S001223",
      "district": "13",
      "firstName": "Emilia",
      "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Sykes",
      "middleName": "Strong",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "OH"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "DE"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "FL"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3111ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3111\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2025 Ms. Lee of Florida (for herself, Ms. Kamlager-Dove , Ms. Norton , Mr. McGarvey , Mr. Bacon , Mr. Crenshaw , Mr. Rutherford , and Ms. Scanlon ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Brady Handgun Violence Prevention Act to establish grants for States for purposes of modernizing criminal justice data infrastructure to facilitate automated record sealing and expungement, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fresh Start Act of 2025 .\n#### 2. Implementation of expungement laws\nSection 106(b) of the Brady Handgun Violence Prevention Act ( 34 U.S.C. 40302(b) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (C), by striking and at the end;\n**(B)**\nin subparagraph (D), by striking the period and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(E) to implement a covered expungement law. ; and\n**(2)**\nby adding at the end the following:\n(3) Covered expungement laws In this subsection: (A) The term automatic means, with regard to the expungement or sealing of a criminal record, that such expungement or sealing occurs without any action required on the part of the State from an eligible individual. (B) The term covered expungement law means a law of a State providing for the automatic expungement or sealing, subject to such requirements as the State may impose (including provisions ensuring continued access to the expunged or sealed material by courts and law enforcement agencies), of a criminal record of an individual, without delay by reason of a failure to pay a fee or fine. (4) Reporting requirements (A) In general A State receiving a grant under this section shall report to the Attorney General, each year of the grant term, pursuant to guidelines established by the Attorney General, information regarding the following: (i) The number of individuals eligible for automatic expungement or sealing under the covered expungement law of that State, disaggregated by race, ethnicity, and gender. (ii) The number of individuals whose records have been expunged or sealed annually since the enactment of such law, disaggregated by race, ethnicity, and gender. (iii) The number of individuals whose application for expungement or sealing under such law are still pending, disaggregated by race, ethnicity, and gender. (B) Inaccessibility of data for reporting In the event that elements of the data on expungement and sealing required to be reported under subparagraph (A)(i) are not able to be compiled and reported, the State shall develop and report a comprehensive plan to obtain as much of the unavailable data as possible not later than the date that is one year after the first year of the grant being awarded. (C) Publication Not later than 1 year after the date of enactment of this paragraph, and each year thereafter, the Attorney General shall publish, and make available to the public, a report containing the data reported to the Attorney General under this subparagraph. .",
      "versionDate": "2025-04-30",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-05-21T12:34:23Z"
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
      "date": "2025-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3111ih.xml"
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
      "title": "Fresh Start Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:31:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fresh Start Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T05:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Brady Handgun Violence Prevention Act to establish grants for States for purposes of modernizing criminal justice data infrastructure to facilitate automated record sealing and expungement, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T05:18:39Z"
    }
  ]
}
```
