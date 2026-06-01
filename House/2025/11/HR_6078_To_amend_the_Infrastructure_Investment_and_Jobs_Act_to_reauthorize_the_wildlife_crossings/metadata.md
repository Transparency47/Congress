# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6078?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6078
- Title: Wildlife Road Crossings Program Reauthorization Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6078
- Origin chamber: House
- Introduced date: 2025-11-18
- Update date: 2026-05-13T08:06:07Z
- Update date including text: 2026-05-13T08:06:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-18: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-11-19 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-11-18: Introduced in House

## Actions

- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-11-19 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-18",
    "latestAction": {
      "actionDate": "2025-11-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6078",
    "number": "6078",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "B001292",
        "district": "8",
        "firstName": "Donald",
        "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
        "lastName": "Beyer",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Wildlife Road Crossings Program Reauthorization Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:07Z",
    "updateDateIncludingText": "2026-05-13T08:06:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-19",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-18",
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
      "actionCode": "Intro-H",
      "actionDate": "2025-11-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-18",
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
          "date": "2025-11-18T15:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-19T18:20:40Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
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
      "bioguideId": "Z000018",
      "district": "1",
      "firstName": "Ryan",
      "fullName": "Rep. Zinke, Ryan K. [R-MT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Zinke",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-11-18",
      "state": "MT"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-12-05",
      "state": "CA"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "False",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "CA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "PA"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "NV"
    },
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "CO"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6078ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6078\nIN THE HOUSE OF REPRESENTATIVES\nNovember 18, 2025 Mr. Beyer (for himself and Mr. Zinke ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend the Infrastructure Investment and Jobs Act to reauthorize the wildlife crossings program.\n#### 1. Short title\nThis Act may be cited as the Wildlife Road Crossings Program Reauthorization Act of 2025 .\n#### 2. Wildlife crossings program\n##### (a) Authorization of appropriations\nSection 11101(d) of the Infrastructure Investment and Jobs Act ( 23 U.S.C. 101 note) is amended\u2014\n**(1)**\nin the heading by striking pilot and inserting additional ;\n**(2)**\nin paragraph (1)\u2014\n**(A)**\nin the heading by striking pilot ; and\n**(B)**\nby striking pilot program under and inserting program under ; and\n**(3)**\nby striking United States Code and all that follows through the period at the end and inserting United States Code, $200,000,000 for each of fiscal years 2026 through 2031 .\n##### (b) Wildlife crossing safety\n**(1) In general**\nSection 171 of title 23, United States Code, is amended\u2014\n**(A)**\nin the heading by striking pilot ;\n**(B)**\nby striking pilot program each place it appears and inserting Program ;\n**(C)**\nby redesignating subsections (h) and (i) as subsections (l) and (m), respectively; and\n**(D)**\nby inserting after subsection (g) the following:\n(h) Federal cost share for Indian tribes In the case of a grant submitted by a entity described in subsection (c)(6), the Federal share of the cost of the project shall be 100 percent. (i) Tribal technical assistance (1) In general The Secretary may use an amount equal to not more than \u00bd of 1 percent of the funds authorized under this section to improve the ability of entities described in subsection (c)(6) to access funding for projects under this subsection in an efficient and expeditious manner by providing to such entities application assistance, technical assistance, and assistance in reducing the period of time between the selection of the project and the obligation of funds for the project. (2) Use of Funds Amounts used under paragraph (1) may be expended\u2014 (A) by the Secretary; or (B) through contracts with\u2014 (i) a Federal, Tribal, regional, or State government entity; (ii) a private entity; or (iii) a nonprofit entity. (j) Grant administration The Secretary may retain not more than a total of \u00bd of 1 percent of the funds made available to carry out this section to\u2014 (1) review applications for grants under this section; (2) obligate and administer grant awards selected under this section; and (3) carry out the requirements of\u2014 (A) section 172 of title 23, United States Code; and (B) subsections (b)(6) and (i)(3) of section 144 of title 23, United States Code. (k) Unobligated funds If for any fiscal year the total of all obligations to carry out this section is less than the amount authorized to be obligated for the fiscal year, the unobligated balance of that amount shall\u2014 (1) remain available until expended; and (2) be in addition to amounts otherwise available to carry out this section for each year. .\n**(2) Clerical amendment**\nThe item relating to section 171 in the analysis for chapter 1 of title 23, United States Code, is amended by striking pilot .",
      "versionDate": "2025-11-18",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-12-01T16:30:56Z"
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
      "date": "2025-11-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6078ih.xml"
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
      "title": "Wildlife Road Crossings Program Reauthorization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-29T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Wildlife Road Crossings Program Reauthorization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-29T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Infrastructure Investment and Jobs Act to reauthorize the wildlife crossings program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-29T05:18:17Z"
    }
  ]
}
```
