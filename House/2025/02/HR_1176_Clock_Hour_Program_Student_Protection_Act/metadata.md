# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1176?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1176
- Title: Clock Hour Program Student Protection Act
- Congress: 119
- Bill type: HR
- Bill number: 1176
- Origin chamber: House
- Introduced date: 2025-02-10
- Update date: 2026-01-23T18:27:10Z
- Update date including text: 2026-01-23T18:27:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-10: Introduced in House
- 2025-02-10 - IntroReferral: Introduced in House
- 2025-02-10 - IntroReferral: Introduced in House
- 2025-02-10 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-02-10: Introduced in House

## Actions

- 2025-02-10 - IntroReferral: Introduced in House
- 2025-02-10 - IntroReferral: Introduced in House
- 2025-02-10 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-10",
    "latestAction": {
      "actionDate": "2025-02-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1176",
    "number": "1176",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "S001199",
        "district": "11",
        "firstName": "Lloyd",
        "fullName": "Rep. Smucker, Lloyd [R-PA-11]",
        "lastName": "Smucker",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Clock Hour Program Student Protection Act",
    "type": "HR",
    "updateDate": "2026-01-23T18:27:10Z",
    "updateDateIncludingText": "2026-01-23T18:27:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-10",
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
      "actionDate": "2025-02-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-10",
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
          "date": "2025-02-10T17:03:15Z",
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
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "UT"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "PA"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "PA"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "WI"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1176ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1176\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 10, 2025 Mr. Smucker (for himself, Mr. Owens , Mr. Meuser , Mr. Thompson of Pennsylvania , and Mr. Van Orden ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Higher Education Act of 1965 to clarify the clock hour requirements for certain eligible programs under title IV of such Act.\n#### 1. Short title\nThis Act may be cited as the Clock Hour Program Student Protection Act .\n#### 2. Clock hour requirements for certain programs of training\n##### (a) In general\nSection 481(b) of the Higher Education Act of 1965 ( 20 U.S.C. 1088(b) ) is amended by adding at the end the following:\n(5) An otherwise eligible program that provides a program of training to prepare students for gainful employment in a recognized profession in a State, and for which the number of clock hours of instruction exceeds the minimum number of clock hours of instruction required by such State for training in the recognized profession for which the otherwise eligible program prepares students, shall be determined to be an eligible program under this subsection if the number of clock hours of instruction provided by such otherwise eligible program does not exceed the greater of\u2014 (A) 150 percent of the minimum number of clock hours required by such State for training in the recognized profession for which the otherwise eligible program prepares students; or (B) 150 percent of the minimum number of clock hours required by a Federal agency for such training. .\n##### (b) Effective date\nThe amendment made by this section shall take effect on the date of enactment of this Act, and shall apply with respect to award year 2024\u20132025, and each succeeding award year.",
      "versionDate": "2025-02-10",
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
            "name": "Employment and training programs",
            "updateDate": "2026-01-23T18:27:10Z"
          },
          {
            "name": "Government lending and loan guarantees",
            "updateDate": "2026-01-23T18:27:06Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2026-01-23T18:26:57Z"
          },
          {
            "name": "Student aid and college costs",
            "updateDate": "2026-01-23T18:27:01Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-03-17T14:31:09Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-10",
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
          "measure-id": "id119hr1176",
          "measure-number": "1176",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-10",
          "originChamber": "HOUSE",
          "update-date": "2025-07-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1176v00",
            "update-date": "2025-07-28"
          },
          "action-date": "2025-02-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Clock Hour Program Student Protection Act</strong></p><p>This bill provides statutory authority for the 150% rule, which allows an educational program that prepares students for gainful employment in a recognized occupation to maintain eligibility for federal student aid funding if the program operates within 150% of the state's minimum hours requirement for licensure.\u00a0</p><p>The Department of Education (ED) previously enforced the 150% rule through regulations.\u00a0ED proposed a new regulation to rescind the 150% rule and instead limit the length of these programs to 100% of the state's minimum required hours. This revised regulation was set to take effect on July 1, 2024; however, a court imposed a temporary injunction to halt the regulation from taking effect.</p>"
        },
        "title": "Clock Hour Program Student Protection Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1176.xml",
    "summary": {
      "actionDate": "2025-02-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Clock Hour Program Student Protection Act</strong></p><p>This bill provides statutory authority for the 150% rule, which allows an educational program that prepares students for gainful employment in a recognized occupation to maintain eligibility for federal student aid funding if the program operates within 150% of the state's minimum hours requirement for licensure.\u00a0</p><p>The Department of Education (ED) previously enforced the 150% rule through regulations.\u00a0ED proposed a new regulation to rescind the 150% rule and instead limit the length of these programs to 100% of the state's minimum required hours. This revised regulation was set to take effect on July 1, 2024; however, a court imposed a temporary injunction to halt the regulation from taking effect.</p>",
      "updateDate": "2025-07-28",
      "versionCode": "id119hr1176"
    },
    "title": "Clock Hour Program Student Protection Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Clock Hour Program Student Protection Act</strong></p><p>This bill provides statutory authority for the 150% rule, which allows an educational program that prepares students for gainful employment in a recognized occupation to maintain eligibility for federal student aid funding if the program operates within 150% of the state's minimum hours requirement for licensure.\u00a0</p><p>The Department of Education (ED) previously enforced the 150% rule through regulations.\u00a0ED proposed a new regulation to rescind the 150% rule and instead limit the length of these programs to 100% of the state's minimum required hours. This revised regulation was set to take effect on July 1, 2024; however, a court imposed a temporary injunction to halt the regulation from taking effect.</p>",
      "updateDate": "2025-07-28",
      "versionCode": "id119hr1176"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1176ih.xml"
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
      "title": "Clock Hour Program Student Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T06:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Clock Hour Program Student Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T06:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Higher Education Act of 1965 to clarify the clock hour requirements for certain eligible programs under title IV of such Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T06:18:32Z"
    }
  ]
}
```
