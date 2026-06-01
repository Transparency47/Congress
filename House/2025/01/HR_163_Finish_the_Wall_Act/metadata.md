# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/163?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/163
- Title: Finish the Wall Act
- Congress: 119
- Bill type: HR
- Bill number: 163
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2026-04-28T08:06:22Z
- Update date including text: 2026-04-28T08:06:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-01-03 - Committee: Referred to the Subcommittee on Border Security and Enforcement.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-01-03 - Committee: Referred to the Subcommittee on Border Security and Enforcement.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/163",
    "number": "163",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "H001077",
        "district": "3",
        "firstName": "Clay",
        "fullName": "Rep. Higgins, Clay [R-LA-3]",
        "lastName": "Higgins",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Finish the Wall Act",
    "type": "HR",
    "updateDate": "2026-04-28T08:06:22Z",
    "updateDateIncludingText": "2026-04-28T08:06:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-03",
      "committees": {
        "item": {
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Border Security and Enforcement.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Homeland Security.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:06:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-01-03T18:41:47Z",
              "name": "Referred to"
            }
          },
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "systemCode": "hshm00",
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
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "OK"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "MI"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "PA"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "VA"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "MI"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "TX"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "IA"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "FL"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "TN"
    },
    {
      "bioguideId": "E000235",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Ezell, Mike [R-MS-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ezell",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "MS"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "SC"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "IL"
    },
    {
      "bioguideId": "F000459",
      "district": "3",
      "firstName": "Charles",
      "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Fleischmann",
      "middleName": "J. \"Chuck\"",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "TN"
    },
    {
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "TX"
    },
    {
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "IN"
    },
    {
      "bioguideId": "K000392",
      "district": "8",
      "firstName": "David",
      "fullName": "Rep. Kustoff, David [R-TN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Kustoff",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "TN"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "FL"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "MI"
    },
    {
      "bioguideId": "C001137",
      "district": "5",
      "firstName": "Jeff",
      "fullName": "Rep. Crank, Jeff [R-CO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Crank",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "CO"
    },
    {
      "bioguideId": "T000490",
      "district": "2",
      "firstName": "David",
      "fullName": "Rep. Taylor, David [R-OH-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Taylor",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "OH"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "TN"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "MS"
    },
    {
      "bioguideId": "L000583",
      "district": "11",
      "firstName": "Barry",
      "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Loudermilk",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "GA"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "CO"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "KS"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "MN"
    },
    {
      "bioguideId": "C001108",
      "district": "1",
      "firstName": "James",
      "fullName": "Rep. Comer, James [R-KY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Comer",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "KY"
    },
    {
      "bioguideId": "M001216",
      "district": "7",
      "firstName": "Cory",
      "fullName": "Rep. Mills, Cory [R-FL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mills",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "FL"
    },
    {
      "bioguideId": "G000568",
      "district": "9",
      "firstName": "H.",
      "fullName": "Rep. Griffith, H. Morgan [R-VA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Griffith",
      "middleName": "Morgan",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr163ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 163\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Higgins of Louisiana (for himself, Mr. Brecheen , Mr. Bergman , Mr. Meuser , Mr. Cline , Mr. Moolenaar , Mr. Weber of Texas , Mr. Feenstra , Mr. Buchanan , Mr. Rose , Mr. Ezell , Ms. Mace , Mr. Bost , Mr. Fleischmann , Mr. Roy , Mrs. Houchin , Mr. Kustoff , Mrs. Luna , Mr. Huizenga , Mr. Crank , Mr. Taylor , Mrs. Harshbarger , and Mr. Guest ) introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo immediately resume construction of the border wall system along the international border between the United States and Mexico to secure the border, enforce the rule of law, and expend appropriated funds as mandated by Congress, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Finish the Wall Act .\n#### 2. Border wall system construction\n##### (a)\n**(1) Immediately resume border wall system construction**\nNot later than 24 hours after the date of the enactment of this Act, the Secretary of Homeland Security shall resume all activities related to the construction of the border barrier system (also known as, and referred to in this Act as, the border wall system ) along the international border between the United States and Mexico that were underway or being planned for prior to January 20, 2021.\n**(2) No cancellations**\nThe Secretary of Homeland Security may not cancel any contract for activities related to border wall system construction referred to in paragraph (1) that was entered into on or before January 20, 2021.\n**(3) Use of funds**\nThe Secretary of Homeland Security shall expend all funds appropriated or explicitly obligated for border wall system construction referred to in paragraph (1) that were appropriated or obligated, as the case may be, beginning on October 1, 2016, to carry out this Act.\n**(4) Implementation plan for border wall system**\nNot later than 30 days after the date of the enactment of this Act, the Secretary of Homeland Security shall submit to the appropriate congressional committees an implementation plan to complete, by not later than September 30, 2026, border wall system construction referred to in paragraph (1) and funded in accordance with paragraph (3).\n##### (b) Plan To complete tactical infrastructure and technology elements of border wall system\nNot later than 90 days after the date of the enactment of this Act, the Secretary of Homeland Security shall submit to the appropriate congressional committees an implementation plan, including quarterly benchmarks and cost estimates, for satisfying all requirements of border wall system construction referred to in subsection (a)(1), including tactical infrastructure, technology, and other elements as identified by the Department of Homeland Security prior to January 20, 2021, through the expenditure of funds appropriated or explicitly obligated, as the case may be, for use beginning on October 1, 2016, as well as any future funds appropriated by Congress.\n##### (c) Uphold negotiated agreements\nThe Secretary of Homeland Security shall ensure that all agreements executed in writing between the Department of Homeland Security and private citizens, State, local, and Tribal governments, and other stakeholders are honored by the Department relating to current and future border wall system construction as required by such agreements.\n#### 3. DNA collection consistent with Federal law\nNot later than 14 days after the date of the enactment of this Act, the Secretary of Homeland Security shall ensure and certify to the Committee on Homeland Security of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate that U.S. Customs and Border Protection is fully compliant with the DNA Fingerprint Act of 2005 at all border facilities that process adults, including as part of a family unit, in the custody of U.S. Customs and Border Protection at the border.\n#### 4. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means the Committee on Homeland Security and the Committee on Appropriations of the House of Representatives and the Committee on Homeland Security and Governmental Affairs and the Committee on Appropriations of the Senate.\n**(2) Tactical infrastructure**\nThe term tactical infrastructure includes boat ramps, access gates, checkpoints, lighting, and roads associated with a border wall system.\n**(3) Technology**\nThe term technology includes border surveillance and detection technology, including linear ground detection systems, associated with a border wall system.",
      "versionDate": "2025-01-03",
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
            "name": "Border security and unlawful immigration",
            "updateDate": "2025-09-18T15:11:48Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-09-18T15:11:48Z"
          },
          {
            "name": "Department of Homeland Security",
            "updateDate": "2025-09-18T15:11:48Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-09-18T15:11:48Z"
          },
          {
            "name": "Genetics",
            "updateDate": "2025-09-18T15:11:48Z"
          },
          {
            "name": "Immigration status and procedures",
            "updateDate": "2025-09-18T15:11:48Z"
          },
          {
            "name": "Public contracts and procurement",
            "updateDate": "2025-09-18T15:11:48Z"
          }
        ]
      },
      "policyArea": {
        "name": "Immigration",
        "updateDate": "2025-02-05T17:04:04Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr163",
          "measure-number": "163",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr163v00",
            "update-date": "2025-02-24"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Finish the Wall Act</strong></p> <p>This bill requires the Department of Homeland Security (DHS) to resume activities related to the construction of a barrier system along the U.S.-Mexico border and addresses other border-related issues.</p> <p>DHS must resume all such construction activities that were planned or underway prior to January 20, 2021. DHS must also expend all funds appropriated or explicitly obligated since October 1, 2016, for construction of this barrier system. DHS may not cancel contracts for activities related to such construction entered into on or before January 20, 2021. </p> <p>Furthermore, within 14 days of this bill's enactment, DHS must certify to Congress that U.S. Customs and Border Protection facilities that process adults taken into custody at the border are fully compliant with certain laws related to the collection of DNA. (Among other things, these laws allow for the collection of DNA samples from non-U.S. persons detained under U.S. authority.)</p>"
        },
        "title": "Finish the Wall Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr163.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Finish the Wall Act</strong></p> <p>This bill requires the Department of Homeland Security (DHS) to resume activities related to the construction of a barrier system along the U.S.-Mexico border and addresses other border-related issues.</p> <p>DHS must resume all such construction activities that were planned or underway prior to January 20, 2021. DHS must also expend all funds appropriated or explicitly obligated since October 1, 2016, for construction of this barrier system. DHS may not cancel contracts for activities related to such construction entered into on or before January 20, 2021. </p> <p>Furthermore, within 14 days of this bill's enactment, DHS must certify to Congress that U.S. Customs and Border Protection facilities that process adults taken into custody at the border are fully compliant with certain laws related to the collection of DNA. (Among other things, these laws allow for the collection of DNA samples from non-U.S. persons detained under U.S. authority.)</p>",
      "updateDate": "2025-02-24",
      "versionCode": "id119hr163"
    },
    "title": "Finish the Wall Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Finish the Wall Act</strong></p> <p>This bill requires the Department of Homeland Security (DHS) to resume activities related to the construction of a barrier system along the U.S.-Mexico border and addresses other border-related issues.</p> <p>DHS must resume all such construction activities that were planned or underway prior to January 20, 2021. DHS must also expend all funds appropriated or explicitly obligated since October 1, 2016, for construction of this barrier system. DHS may not cancel contracts for activities related to such construction entered into on or before January 20, 2021. </p> <p>Furthermore, within 14 days of this bill's enactment, DHS must certify to Congress that U.S. Customs and Border Protection facilities that process adults taken into custody at the border are fully compliant with certain laws related to the collection of DNA. (Among other things, these laws allow for the collection of DNA samples from non-U.S. persons detained under U.S. authority.)</p>",
      "updateDate": "2025-02-24",
      "versionCode": "id119hr163"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr163ih.xml"
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
      "title": "Finish the Wall Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-04T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Finish the Wall Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-04T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To immediately resume construction of the border wall system along the international border between the United States and Mexico to secure the border, enforce the rule of law, and expend appropriated funds as mandated by Congress, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-04T05:33:23Z"
    }
  ]
}
```
