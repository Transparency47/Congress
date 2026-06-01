# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1905?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1905
- Title: Protecting American Students Act
- Congress: 119
- Bill type: HR
- Bill number: 1905
- Origin chamber: House
- Introduced date: 2025-03-06
- Update date: 2025-09-27T08:05:38Z
- Update date including text: 2025-09-27T08:05:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-06: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-03-06: Introduced in House

## Actions

- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1905",
    "number": "1905",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001260",
        "district": "16",
        "firstName": "Vern",
        "fullName": "Rep. Buchanan, Vern [R-FL-16]",
        "lastName": "Buchanan",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Protecting American Students Act",
    "type": "HR",
    "updateDate": "2025-09-27T08:05:38Z",
    "updateDateIncludingText": "2025-09-27T08:05:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-06",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-06",
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
          "date": "2025-03-06T14:08:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "NE"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "PA"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "WV"
    },
    {
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "NC"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "NY"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "TX"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "NY"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1905ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1905\nIN THE HOUSE OF REPRESENTATIVES\nMarch 6, 2025 Mr. Buchanan (for himself, Mr. Smith of Nebraska , Mr. Kelly of Pennsylvania , Mrs. Miller of West Virginia , Mr. Murphy , Ms. Tenney , and Ms. Van Duyne ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to exclude certain students from the calculation to determine if certain private colleges and universities are subject to the excise tax on net investment income, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting American Students Act .\n#### 2. Certain students not taken into account for purposes of calculation to determine if certain private colleges and universities are subject to excise tax on net investment income\n##### (a) In general\nSection 4968(b) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(3) Certain students not taken into account in determining endowment threshold For purposes of paragraph (1)(D), a student shall not be taken into account with respect to an eligible educational institution unless such student meets the student eligibility requirements under section 484(a)(5) of the Higher Education Act of 1965 ( 20 U.S.C. 1091(a)(5) ). .\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years beginning after December 31, 2025.\n#### 3. Requirement to report certain information with respect to application of excise tax based on investment income of private colleges and universities\n##### (a) In general\nSection 6033 of the Internal Revenue Code of 1986 is amended by redesignating subsection (o) as subsection (p) and by inserting after subsection (n) the following new subsection:\n(o) Requirement To report certain information with respect To excise tax based on investment income of private colleges and universities Each applicable educational institution described in section 4968(b) which is subject to the requirements of subsection (a) shall include on the return required under subsection (a)\u2014 (1) the number of students taken into account for purposes of the calculation in paragraph (1)(D) of section 4968(b) (determined before the application of paragraph (3) of such section), and (2) the number of students taken into account for purposes of the calculation in paragraph (1)(D) of section 4968(b) (determined after the application of paragraph (3) of such section). .\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-03-06",
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
        "name": "Taxation",
        "updateDate": "2025-05-07T18:21:45Z"
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
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1905ih.xml"
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
      "title": "Protecting American Students Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-20T07:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting American Students Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T07:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to exclude certain students from the calculation to determine if certain private colleges and universities are subject to the excise tax on net investment income, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T07:03:36Z"
    }
  ]
}
```
