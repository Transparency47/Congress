# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3268?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3268
- Title: Federal Bird Safe Buildings Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3268
- Origin chamber: House
- Introduced date: 2025-05-08
- Update date: 2025-12-16T09:05:47Z
- Update date including text: 2025-12-16T09:05:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-08: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-08 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-05-08: Introduced in House

## Actions

- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-08 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-08",
    "latestAction": {
      "actionDate": "2025-05-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3268",
    "number": "3268",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "G000568",
        "district": "9",
        "firstName": "H.",
        "fullName": "Rep. Griffith, H. Morgan [R-VA-9]",
        "lastName": "Griffith",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Federal Bird Safe Buildings Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-16T09:05:47Z",
    "updateDateIncludingText": "2025-12-16T09:05:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-08",
      "committees": {
        "item": {
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-08",
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
      "actionDate": "2025-05-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-08",
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
          "date": "2025-05-08T13:02:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-05-08T21:15:39Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
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
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "IL"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-08-29",
      "state": "NJ"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "NV"
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
      "sponsorshipDate": "2025-10-21",
      "state": "VA"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3268ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3268\nIN THE HOUSE OF REPRESENTATIVES\nMay 8, 2025 Mr. Griffith (for himself and Mr. Quigley ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 40, United States Code, to direct the Administrator of General Services to incorporate practices and strategies to reduce bird fatalities resulting from collisions with certain public buildings, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federal Bird Safe Buildings Act of 2025 .\n#### 2. Use of bird-safe features, practices, and strategies in public buildings\n##### (a) In general\nChapter 33 of title 40, United States Code, is amended by adding at the end the following:\n3319. Use of bird-safe features, practices, and strategies in public buildings (a) Construction, alteration, and acquisition of public buildings The Administrator of General Services shall incorporate, to the extent practicable, features, practices, and strategies to reduce bird fatality resulting from collisions with public buildings for each public building\u2014 (1) constructed; (2) acquired; or (3) of which more than 50 percent of the facade is substantially altered (in the opinion of the Commissioner of Public Buildings). (b) Design guide The Administrator shall develop a design guide to carry out subsection (a) that includes the following: (1) Features for reducing bird fatalities resulting from collisions with public buildings throughout all construction phases, taking into account the risks and available information on bird fatalities that occur at different types of public buildings. (2) Methods and strategies for reducing bird fatalities resulting from collisions with public buildings during the operation and maintenance of such buildings, including installing interior, exterior, and site lighting. (3) Best practices for reducing bird fatalities resulting from collisions with public buildings, including\u2014 (A) a description of the reasons for adopting such practices; and (B) an explanation for the omission of a best practice identified pursuant to subsection (c). (c) Identifying best practices To carry out subsection (b)(3), the Administrator may identify best practices for reducing bird fatalities resulting from collisions with public buildings, including best practices recommended by\u2014 (1) Federal agencies with expertise in bird conservation; (2) nongovernmental organizations with expertise in bird conservation; and (3) representatives of green building certification systems. (d) Dissemination of design guide The Administrator shall disseminate the design guide developed pursuant to subsection (b) to all Federal agencies, subagencies, and departments with independent leasing authority from the Administrator. (e) Update to design guide The Administrator shall, on a regular basis, update the design guide developed pursuant to subsection (b) with respect to the priorities of the Administrator for reducing bird fatalities resulting from collisions with public buildings. (f) Exempt buildings This section shall not apply to\u2014 (1) any building or site listed, or eligible for listing, on the National Register of Historic Places; (2) the White House and the grounds of the White House; (3) the Supreme Court building and the grounds of the Supreme Court; or (4) the United States Capitol and any building on the grounds of the Capitol. (g) Compliance Not later than October 1 of each fiscal year, the Administrator, acting through the Commissioner, shall gather information on compliance with and certify to Congress that the Administrator uses the design guide developed pursuant to subsection (b) for each public building described in subsection (a). (h) Report Not later than October 1 of each fiscal year, the Administrator shall submit to Congress a report that includes\u2014 (1) the information under subsection (g); (2) to the extent practicable, an assessment of bird fatalities that occurred as a result of a collision with the public buildings occupied by the respective head of each Federal agency; and (3) any recommendations to reduce the risk of bird fatalities in and around public buildings occupied by Federal agencies. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of chapter 33 of title 40, United States Code, is amended by adding at the end the following new item:\n3319. Use of bird-safe features, practices, and strategies in public buildings. .",
      "versionDate": "2025-05-08",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-06-23T18:05:14Z"
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
      "date": "2025-05-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3268ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 40, United States Code, to direct the Administrator of General Services to incorporate practices and strategies to reduce bird fatalities resulting from collisions with certain public buildings, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-16T09:05:47Z"
    },
    {
      "title": "Federal Bird Safe Buildings Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-18T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Federal Bird Safe Buildings Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-18T05:23:16Z"
    }
  ]
}
```
