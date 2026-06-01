# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2272?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2272
- Title: FAFSA Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2272
- Origin chamber: House
- Introduced date: 2025-03-21
- Update date: 2026-03-16T19:10:31Z
- Update date including text: 2026-03-16T19:10:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-21: Introduced in House
- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-03-21: Introduced in House

## Actions

- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-21",
    "latestAction": {
      "actionDate": "2025-03-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2272",
    "number": "2272",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "P000048",
        "district": "11",
        "firstName": "August",
        "fullName": "Rep. Pfluger, August [R-TX-11]",
        "lastName": "Pfluger",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "FAFSA Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-16T19:10:31Z",
    "updateDateIncludingText": "2026-03-16T19:10:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-21",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-21",
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
          "date": "2025-03-21T20:01:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "NC"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "FL"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "WI"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "NE"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
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
      "sponsorshipDate": "2025-05-08",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2272ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2272\nIN THE HOUSE OF REPRESENTATIVES\nMarch 21, 2025 Mr. Pfluger (for himself and Mr. Edwards ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo make certain individuals ineligible to receive any Federal financial aid under title IV of the Higher Education Act of 1965.\n#### 1. Short title\nThis Act may be cited as the Freeze Aid For Student Assaulters Act of 2025 or the FAFSA Act of 2025 .\n#### 2. In general\n##### (a) Termination of eligibility for title IV assistance\nBeginning with the first award year that begins after the date of the enactment of the Freeze Aid For Student Assaulters Act of 2025 , an individual shall not be eligible to receive any grant, loan (other than a loan described in subsection (b)), or work assistance under title IV of the Higher Education Act of 1965 ( 20 U.S.C. 1070 et seq. ) and shall repay, in accordance with subsection (b), the sum of the amounts of any grant received under such title, if the individual has been convicted of a criminal offense\u2014\n**(1)**\nof assault against a police officer; or\n**(2)**\nof rioting, the elements of which may include\u2014\n**(A)**\ninciting a riot;\n**(B)**\norganizing, promoting, encouraging, participating in, or carrying on a riot;\n**(C)**\ncommitting any act of violence in furtherance of a riot; or\n**(D)**\naiding or abetting any person in inciting or participating in or carrying on a riot or committing any act of violence in furtherance of a riot.\n##### (b) Conversion of grants to loans\n**(1) In general**\nIf an individual who is subject to the termination of eligibility described in subsection (a) has received any grants under title IV of the Higher Education Act of 1965 ( 20 U.S.C. 1070 et seq. ) for a program of study in which the individual is enrolled as of the date on which the criminal offense occurred, such grant shall be treated as a Federal Direct Unsubsidized Stafford Loan under part D of such title, and shall be subject to repayment, together with interest thereon accruing from the date of the grant award.\n**(2) No repayment assistance**\nSuch loans may not be eligible for any loan forgiveness, cancellation, discharge, or reduction programs under the Higher Education Act of 1965 ( 20 U.S.C. 1001 et seq. ), any other provision of law, or any administrative action or program.",
      "versionDate": "2025-03-21",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Assault and harassment offenses",
            "updateDate": "2026-03-16T19:10:31Z"
          },
          {
            "name": "Government lending and loan guarantees",
            "updateDate": "2026-03-16T19:10:24Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2026-03-16T19:10:14Z"
          },
          {
            "name": "Student aid and college costs",
            "updateDate": "2026-03-16T19:10:19Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-04-01T16:13:45Z"
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
      "date": "2025-03-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2272ih.xml"
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
      "title": "FAFSA Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-01T04:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FAFSA Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-01T04:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Freeze Aid For Student Assaulters Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-01T04:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To make certain individuals ineligible to receive any Federal financial aid under title IV of the Higher Education Act of 1965.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-01T04:18:30Z"
    }
  ]
}
```
