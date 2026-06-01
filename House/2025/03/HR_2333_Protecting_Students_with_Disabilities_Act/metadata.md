# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2333?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2333
- Title: Protecting Students with Disabilities Act
- Congress: 119
- Bill type: HR
- Bill number: 2333
- Origin chamber: House
- Introduced date: 2025-03-25
- Update date: 2026-05-30T08:06:05Z
- Update date including text: 2026-05-30T08:06:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-25: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-03-25: Introduced in House

## Actions

- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-25",
    "latestAction": {
      "actionDate": "2025-03-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2333",
    "number": "2333",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "M001231",
        "district": "22",
        "firstName": "John",
        "fullName": "Rep. Mannion, John [D-NY-22]",
        "lastName": "Mannion",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Protecting Students with Disabilities Act",
    "type": "HR",
    "updateDate": "2026-05-30T08:06:05Z",
    "updateDateIncludingText": "2026-05-30T08:06:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-25",
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
      "actionDate": "2025-03-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-25",
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
          "date": "2025-03-25T14:00:30Z",
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
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "CT"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "GA"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "NV"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "CA"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "MN"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "OH"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "CA"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "False",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "CA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "CA"
    },
    {
      "bioguideId": "R000599",
      "district": "25",
      "firstName": "Raul",
      "fullName": "Rep. Ruiz, Raul [D-CA-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Ruiz",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "CA"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "CA"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "CA"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "CA"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "CA"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "PA"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "CA"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "WA"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "IL"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "IL"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "CA"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "False",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "CA"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "CA"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-11-25",
      "state": "CO"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CA"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "AZ"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "OR"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "CA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "CA"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2333ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2333\nIN THE HOUSE OF REPRESENTATIVES\nMarch 25, 2025 Mr. Mannion (for himself, Mrs. Hayes , and Mrs. McBath ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo prohibit the use of appropriated funds to eliminate, consolidate, or otherwise restructure any office within the Department of Education that administers or enforces programs under the Individuals with Disabilities Education Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Students with Disabilities Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nSection 1402 of the Individuals with Disabilities Education Act explicitly states that the Office of Special Education Programs shall be housed within the Department of Education and tasked with administering and carrying out programs and activities concerning the education of children with disabilities.\n**(2)**\nThe executive branch does not have the unilateral authority to alter this statutory framework. This Act reaffirms Congress\u2019s intent and ensures compliance with existing statute.\n#### 3. Prohibition\nNone of the funds made available by Acts making appropriations may be used to\u2014\n**(1)**\neliminate, consolidate, or otherwise restructure any office within the Department of Education that administers or enforces programs under the Individuals with Disabilities Education Act ( 20 U.S.C. 1400 et seq. );\n**(2)**\nterminate, reassign, or alter the responsibilities of any personnel of any such office; or\n**(3)**\ncontract with, or delegate to, any entity outside of the Department of Education to administer or enforce such programs.",
      "versionDate": "2025-03-25",
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
        "name": "Education",
        "updateDate": "2025-04-04T16:53:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-25",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr2333",
          "measure-number": "2333",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-25",
          "originChamber": "HOUSE",
          "update-date": "2025-09-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2333v00",
            "update-date": "2025-09-04"
          },
          "action-date": "2025-03-25",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Protecting Students with Disabilities Act</strong></p><p>This bill prohibits the use of appropriated funds to eliminate the Department of Education's (ED's) oversight of the Individuals with Disabilities Education Act (IDEA). (The IDEA authorizes grant programs that support special education and early intervention services for children with disabilities. Currently, the IDEA is administered by the Office of Special Education Programs\u00a0in the Office of Special Education and Rehabilitative Services\u00a0in ED.)</p><p>Specifically, the bill prohibits the use of appropriated funds to eliminate, consolidate, or otherwise restructure any office within ED that administers or enforces programs under the IDEA.</p><p>Further, appropriated funds may not be used to (1) terminate, reassign, or alter the responsibilities of any personnel of any such office; or (2) contract with, or delegate to, any entity outside of ED to administer or enforce IDEA programs.</p><p>(On March 20, 2025, President Donald Trump signed an executive order titled <em>Improving Education</em> <em>Outcomes by Empowering Parents, States, and Communities</em>, calling for the closure of ED and giving authority over education to the states. Further, the Trump Administration has announced plans to transfer ED's oversight of services for students with disabilities to the Department of Health and Human Services.)</p>"
        },
        "title": "Protecting Students with Disabilities Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2333.xml",
    "summary": {
      "actionDate": "2025-03-25",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Students with Disabilities Act</strong></p><p>This bill prohibits the use of appropriated funds to eliminate the Department of Education's (ED's) oversight of the Individuals with Disabilities Education Act (IDEA). (The IDEA authorizes grant programs that support special education and early intervention services for children with disabilities. Currently, the IDEA is administered by the Office of Special Education Programs\u00a0in the Office of Special Education and Rehabilitative Services\u00a0in ED.)</p><p>Specifically, the bill prohibits the use of appropriated funds to eliminate, consolidate, or otherwise restructure any office within ED that administers or enforces programs under the IDEA.</p><p>Further, appropriated funds may not be used to (1) terminate, reassign, or alter the responsibilities of any personnel of any such office; or (2) contract with, or delegate to, any entity outside of ED to administer or enforce IDEA programs.</p><p>(On March 20, 2025, President Donald Trump signed an executive order titled <em>Improving Education</em> <em>Outcomes by Empowering Parents, States, and Communities</em>, calling for the closure of ED and giving authority over education to the states. Further, the Trump Administration has announced plans to transfer ED's oversight of services for students with disabilities to the Department of Health and Human Services.)</p>",
      "updateDate": "2025-09-04",
      "versionCode": "id119hr2333"
    },
    "title": "Protecting Students with Disabilities Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-25",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Students with Disabilities Act</strong></p><p>This bill prohibits the use of appropriated funds to eliminate the Department of Education's (ED's) oversight of the Individuals with Disabilities Education Act (IDEA). (The IDEA authorizes grant programs that support special education and early intervention services for children with disabilities. Currently, the IDEA is administered by the Office of Special Education Programs\u00a0in the Office of Special Education and Rehabilitative Services\u00a0in ED.)</p><p>Specifically, the bill prohibits the use of appropriated funds to eliminate, consolidate, or otherwise restructure any office within ED that administers or enforces programs under the IDEA.</p><p>Further, appropriated funds may not be used to (1) terminate, reassign, or alter the responsibilities of any personnel of any such office; or (2) contract with, or delegate to, any entity outside of ED to administer or enforce IDEA programs.</p><p>(On March 20, 2025, President Donald Trump signed an executive order titled <em>Improving Education</em> <em>Outcomes by Empowering Parents, States, and Communities</em>, calling for the closure of ED and giving authority over education to the states. Further, the Trump Administration has announced plans to transfer ED's oversight of services for students with disabilities to the Department of Health and Human Services.)</p>",
      "updateDate": "2025-09-04",
      "versionCode": "id119hr2333"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2333ih.xml"
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
      "title": "Protecting Students with Disabilities Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-04T05:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Students with Disabilities Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T05:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the use of appropriated funds to eliminate, consolidate, or otherwise restructure any office within the Department of Education that administers or enforces programs under the Individuals with Disabilities Education Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T05:03:42Z"
    }
  ]
}
```
