# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2592?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2592
- Title: Aviation Medication Transparency Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2592
- Origin chamber: House
- Introduced date: 2025-04-02
- Update date: 2026-05-21T08:08:16Z
- Update date including text: 2026-05-21T08:08:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-02: Introduced in House
- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-04-02 - Committee: Referred to the Subcommittee on Aviation.
- Latest action: 2025-04-02: Introduced in House

## Actions

- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-04-02 - Committee: Referred to the Subcommittee on Aviation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-02",
    "latestAction": {
      "actionDate": "2025-04-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2592",
    "number": "2592",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "C001117",
        "district": "6",
        "firstName": "Sean",
        "fullName": "Rep. Casten, Sean [D-IL-6]",
        "lastName": "Casten",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Aviation Medication Transparency Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:16Z",
    "updateDateIncludingText": "2026-05-21T08:08:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-02",
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
      "actionDate": "2025-04-02",
      "committees": {
        "item": {
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Aviation.",
      "type": "Committee"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-02",
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
          "date": "2025-04-02T22:02:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-02T20:48:52Z",
              "name": "Referred to"
            }
          },
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
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
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "MN"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "VT"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "NY"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "MN"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "MI"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2026-05-07",
      "state": "NC"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "NJ"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "NC"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "CA"
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
      "sponsorshipDate": "2026-05-19",
      "state": "VA"
    },
    {
      "bioguideId": "D000594",
      "district": "15",
      "firstName": "Monica",
      "fullName": "Rep. De La Cruz, Monica [R-TX-15]",
      "isOriginalCosponsor": "False",
      "lastName": "De La Cruz",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "TX"
    },
    {
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "UT"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "WA"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "NY"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2592ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2592\nIN THE HOUSE OF REPRESENTATIVES\nApril 2, 2025 Mr. Casten (for himself and Mr. Stauber ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo require the Administrator of the Federal Aviation Administration to publish the list of medications that the Administrator has compiled for purposes of the medical certification of airmen, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Aviation Medication Transparency Act of 2025 .\n#### 2. List of approved medications\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Administrator of the Federal Aviation Administration shall publish and maintain on a publicly available website of the Administration the list of medications and treatments that may be safely prescribed to an airman to treat certain medical conditions that the Administrator has compiled for purposes of the issuance of a medical certification to an airman.\n##### (b) Requirements\nThe list required under subsection (a) shall\u2014\n**(1)**\nbe drafted in consultation with\u2014\n**(A)**\nthe Aeromedical Innovation and Modernization Working Group;\n**(B)**\nthe certified exclusive bargaining representatives of air traffic controllers of the Administration certified under section 7111 of title 5, United States Code;\n**(C)**\nthe principal organization representing the largest certified collective bargaining representative of airline pilots; and\n**(D)**\nany other stakeholder determined relevant by the task group, including any stakeholders described in section 411(d)(3)(B) of the FAA Reauthorization Act of 2024;\n**(2)**\nbe comprehensive;\n**(3)**\nbe drafted in a user-friendly and accessible manner and provided to airmen at the time when such airmen first seek a license and medical certification;\n**(4)**\nindicate what, if any, period of time, on average, an airman must have limited or no duties to stabilize on an approved medication;\n**(5)**\ninclude the list of medications that the Administrator has designated as Do Not Issue ;\n**(6)**\ninclude a mechanism for doctors or medical providers to contact the Federal Aviation Administration regarding questions related to such list;\n**(7)**\ninclude any additional information that the Administrator determines is appropriate to provide with respect to what conditions a certain medication may or may not be used to treat and any information to explain why a medication is allowed or prohibited by the Federal Aviation Administration; and\n**(8)**\ninclude any other information or clarification that the Administrator determines appropriate.\n##### (c) Annual update\nNot later than 1 year after the date of publication of the list required under subsection (a), and annually thereafter, the Administrator shall update such list, as appropriate.",
      "versionDate": "2025-04-02",
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
        "updateDate": "2025-04-08T16:35:02Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-02",
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
          "measure-id": "id119hr2592",
          "measure-number": "2592",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-02",
          "originChamber": "HOUSE",
          "update-date": "2026-05-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2592v00",
            "update-date": "2026-05-05"
          },
          "action-date": "2025-04-02",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Aviation Medication Transparency Act of 2025</strong></p><p>This bill directs the Federal Aviation Administration (FAA) to compile, publish, and annually update a list of medications that may be safely prescribed to pilots and air traffic controllers for the purposes of issuing a medical certification. The list must be publicly available on the FAA website and distributed to those seeking a license and medical\u00a0certification. </p><p>Currently, the FAA does not have a list of approved medications. However, the FAA does have lists for Aviation Medical Examiners of <em>Do Not Issue</em> medications and <em>Do Not Fly</em> medications.<em></em></p>"
        },
        "title": "Aviation Medication Transparency Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2592.xml",
    "summary": {
      "actionDate": "2025-04-02",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Aviation Medication Transparency Act of 2025</strong></p><p>This bill directs the Federal Aviation Administration (FAA) to compile, publish, and annually update a list of medications that may be safely prescribed to pilots and air traffic controllers for the purposes of issuing a medical certification. The list must be publicly available on the FAA website and distributed to those seeking a license and medical\u00a0certification. </p><p>Currently, the FAA does not have a list of approved medications. However, the FAA does have lists for Aviation Medical Examiners of <em>Do Not Issue</em> medications and <em>Do Not Fly</em> medications.<em></em></p>",
      "updateDate": "2026-05-05",
      "versionCode": "id119hr2592"
    },
    "title": "Aviation Medication Transparency Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-02",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Aviation Medication Transparency Act of 2025</strong></p><p>This bill directs the Federal Aviation Administration (FAA) to compile, publish, and annually update a list of medications that may be safely prescribed to pilots and air traffic controllers for the purposes of issuing a medical certification. The list must be publicly available on the FAA website and distributed to those seeking a license and medical\u00a0certification. </p><p>Currently, the FAA does not have a list of approved medications. However, the FAA does have lists for Aviation Medical Examiners of <em>Do Not Issue</em> medications and <em>Do Not Fly</em> medications.<em></em></p>",
      "updateDate": "2026-05-05",
      "versionCode": "id119hr2592"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2592ih.xml"
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
      "title": "Aviation Medication Transparency Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-08T11:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Aviation Medication Transparency Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-08T11:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Administrator of the Federal Aviation Administration to publish the list of medications that the Administrator has compiled for purposes of the medical certification of airmen, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-08T11:18:24Z"
    }
  ]
}
```
