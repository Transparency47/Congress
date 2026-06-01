# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6858?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6858
- Title: Veteran Suicide Prevention Act
- Congress: 119
- Bill type: HR
- Bill number: 6858
- Origin chamber: House
- Introduced date: 2025-12-18
- Update date: 2026-05-15T08:07:50Z
- Update date including text: 2026-05-15T08:07:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-12-18: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-22 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-12-18: Introduced in House

## Actions

- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-22 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-18",
    "latestAction": {
      "actionDate": "2025-12-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6858",
    "number": "6858",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "G000597",
        "district": "2",
        "firstName": "Andrew",
        "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
        "lastName": "Garbarino",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Veteran Suicide Prevention Act",
    "type": "HR",
    "updateDate": "2026-05-15T08:07:50Z",
    "updateDateIncludingText": "2026-05-15T08:07:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-22",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-18",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-18",
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
          "date": "2025-12-18T14:08:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-22T15:19:08Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "H001047",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Himes, James A. [D-CT-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Himes",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CT"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "NY"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CO"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "NJ"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "NC"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "UT"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2026-03-16",
      "state": "CA"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-03-16",
      "state": "DE"
    },
    {
      "bioguideId": "R000600",
      "district": "0",
      "firstName": "Aumua Amata",
      "fullName": "Del. Radewagen, Aumua Amata Coleman [R-AS-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Radewagen",
      "middleName": "Coleman",
      "party": "R",
      "sponsorshipDate": "2026-03-16",
      "state": "AS"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "CT"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "VA"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "NH"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "NH"
    },
    {
      "bioguideId": "F000485",
      "district": "14",
      "firstName": "Clay",
      "fullName": "Rep. Fuller, Clay [R-GA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Fuller",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6858ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6858\nIN THE HOUSE OF REPRESENTATIVES\nDecember 18, 2025 Mr. Garbarino (for himself, Mr. Himes , Mr. Lawler , Mr. Neguse , Mr. Kean , and Mr. Davis of North Carolina ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo direct the Secretary of Veterans Affairs to conduct a review of the deaths of certain veterans who died by suicide, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veteran Suicide Prevention Act .\n#### 2. Department of Veterans Affairs review of certain veterans\u2019 deaths by suicide\n##### (a) Review required\nNot later than 18 months after the date of the enactment of this Act, the Secretary of Veterans Affairs shall complete a review of the deaths of all covered veterans who died by suicide during the five-year period preceding the date of the enactment of this Act. Such review shall include\u2014\n**(1)**\nthe total number of veterans who died by suicide during the five-year period preceding the date of the enactment of this Act;\n**(2)**\na summary of such veterans that includes the age, gender, and race of such veterans;\n**(3)**\na comprehensive list of the medications prescribed to, and found in the systems of, such veterans at the time of their deaths, specifically listing any medications that carried a black box warning, were off-label, psychotropic, or carried warnings that included suicidal ideation;\n**(4)**\na summary of medical diagnoses by Department of Veterans Affairs physicians which led to the prescribing of the medications referred to in paragraph (3);\n**(5)**\nthe number of instances in which the veteran who died by suicide was concurrently on multiple medications prescribed by Department of Veterans Affairs physicians;\n**(6)**\nthe percentage of veterans who died by suicide who were not taking any medication prescribed by a Department of Veterans Affairs physician;\n**(7)**\nthe percentage of veterans referred to in paragraph (1) with combat experience or trauma (including, but not limited to military sexual trauma, traumatic brain injury, and post-traumatic stress);\n**(8)**\nVeteran Health Administration facilities with markedly high prescription and suicide rates of patients being treated at those facilities;\n**(9)**\na description of Department of Veterans Affairs policies governing the prescribing of medications referred to in paragraph (3);\n**(10)**\nany patterns apparent to the Secretary based on the review; and\n**(11)**\nrecommendations for further action that would improve the safety and well-being of veterans.\n##### (b) Public availability\nNot later than 30 days after the completion of the review required under subsection (a), the Secretary shall\u2014\n**(1)**\nsubmit to Congress a report on the results of the review; and\n**(2)**\nmake such report publicly available.\n##### (c) Covered veteran\nIn this section:\n**(1)**\nThe term covered veteran means any veteran who received hospital care or medical services furnished by the Department of Veterans Affairs during the five-year period preceding the death of the veteran.\n**(2)**\nThe term black box warning means a warning displayed within a box in the prescribing information for drugs that have special problems, particularly ones that may lead to death or serious injury.",
      "versionDate": "2025-12-18",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-01-21T16:06:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-12-18",
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
          "measure-id": "id119hr6858",
          "measure-number": "6858",
          "measure-type": "hr",
          "orig-publish-date": "2025-12-18",
          "originChamber": "HOUSE",
          "update-date": "2026-04-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6858v00",
            "update-date": "2026-04-10"
          },
          "action-date": "2025-12-18",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Veteran Suicide Prevention Act</b></p> <p>This bill requires the Department of Veterans Affairs (VA) to complete a review of the deaths of all covered veterans who died by suicide during the five-year period preceding the enactment of this bill. Covered veterans are those who received VA hospital care or medical services during the five-year period preceding the death of the veteran. </p> <p>The VA shall report on the results of the review and make such report publicly available.</p>"
        },
        "title": "Veteran Suicide Prevention Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6858.xml",
    "summary": {
      "actionDate": "2025-12-18",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Veteran Suicide Prevention Act</b></p> <p>This bill requires the Department of Veterans Affairs (VA) to complete a review of the deaths of all covered veterans who died by suicide during the five-year period preceding the enactment of this bill. Covered veterans are those who received VA hospital care or medical services during the five-year period preceding the death of the veteran. </p> <p>The VA shall report on the results of the review and make such report publicly available.</p>",
      "updateDate": "2026-04-10",
      "versionCode": "id119hr6858"
    },
    "title": "Veteran Suicide Prevention Act"
  },
  "summaries": [
    {
      "actionDate": "2025-12-18",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Veteran Suicide Prevention Act</b></p> <p>This bill requires the Department of Veterans Affairs (VA) to complete a review of the deaths of all covered veterans who died by suicide during the five-year period preceding the enactment of this bill. Covered veterans are those who received VA hospital care or medical services during the five-year period preceding the death of the veteran. </p> <p>The VA shall report on the results of the review and make such report publicly available.</p>",
      "updateDate": "2026-04-10",
      "versionCode": "id119hr6858"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6858ih.xml"
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
      "title": "Veteran Suicide Prevention Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veteran Suicide Prevention Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T05:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Veterans Affairs to conduct a review of the deaths of certain veterans who died by suicide, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T05:18:39Z"
    }
  ]
}
```
