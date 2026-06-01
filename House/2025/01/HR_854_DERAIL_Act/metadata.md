# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/854?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/854
- Title: DERAIL Act
- Congress: 119
- Bill type: HR
- Bill number: 854
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2025-03-25T13:11:41Z
- Update date including text: 2025-03-25T13:11:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-31: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-02-01 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.
- Latest action: 2025-01-31: Introduced in House

## Actions

- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-02-01 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-31",
    "latestAction": {
      "actionDate": "2025-01-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/854",
    "number": "854",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "D000530",
        "district": "17",
        "firstName": "Christopher",
        "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
        "lastName": "Deluzio",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "DERAIL Act",
    "type": "HR",
    "updateDate": "2025-03-25T13:11:41Z",
    "updateDateIncludingText": "2025-03-25T13:11:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-01",
      "committees": {
        "item": {
          "name": "Railroads, Pipelines, and Hazardous Materials Subcommittee",
          "systemCode": "hspw14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
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
      "actionDate": "2025-01-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-31",
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
          "date": "2025-01-31T15:09:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-01T15:44:48Z",
              "name": "Referred to"
            }
          },
          "name": "Railroads, Pipelines, and Hazardous Materials Subcommittee",
          "systemCode": "hspw14"
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
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "CA"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "TX"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "PA"
    },
    {
      "bioguideId": "B001296",
      "district": "2",
      "firstName": "Brendan",
      "fullName": "Rep. Boyle, Brendan F. [D-PA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Boyle",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "PA"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "TX"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "WI"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "TX"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "PA"
    },
    {
      "bioguideId": "S001215",
      "district": "11",
      "firstName": "Haley",
      "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Stevens",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "MI"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "IL"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "PA"
    },
    {
      "bioguideId": "R000579",
      "district": "18",
      "firstName": "Patrick",
      "fullName": "Rep. Ryan, Patrick [D-NY-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Ryan",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "NY"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "CO"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "MN"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr854ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 854\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Mr. Deluzio (for himself, Mr. Khanna , Mr. Doggett , Ms. Dean of Pennsylvania , Mr. Boyle of Pennsylvania , Mr. Green of Texas , Ms. Moore of Wisconsin , Mr. Casar , Ms. Lee of Pennsylvania , Ms. Stevens , Ms. Schakowsky , Mr. Evans of Pennsylvania , Mr. Ryan , and Ms. Pettersen ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo direct the Secretary of Transportation to issue certain regulations to define high-hazard flammable train, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Decreasing Emergency Railroad Accident Instances Locally Act or the DERAIL Act .\n#### 2. High-hazard flammable train\nNot later than 90 days after the date of enactment of this Act, the Secretary of Transportation shall issue such regulations as are necessary to amend section 171.8 of title 49, Code of Federal Regulations, to modify the definition of high-hazard flammable train to mean a single train transporting 1 or more loaded tank cars of a Class 3 flammable liquid or a Class 2 flammable gas and other materials the Secretary determines necessary for safety.\n#### 3. Reporting of material toxic by inhalation\n##### (a) In general\nChapter 209 of title 49, United States Code, is amended by adding at the end the following:\n20904. Reporting of accidents involving material toxic by inhalation Not later than 24 hours after any train derailment involving a train carrying material toxic by inhalation, the railroad carrier involved in such derailment shall report to the National Response Center, State officials, local officials, and Tribal governments all material toxic by inhalation on such train. .\n##### (b) Clerical amendment\nThe analysis for chapter 209 of title 49, United States Code, is amended by adding at the end the following:\n20904. Reporting of accidents involving material toxic by inhalation. .",
      "versionDate": "2025-01-31",
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
        "updateDate": "2025-03-04T14:21:59Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-31",
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
          "measure-id": "id119hr854",
          "measure-number": "854",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-31",
          "originChamber": "HOUSE",
          "update-date": "2025-03-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr854v00",
            "update-date": "2025-03-25"
          },
          "action-date": "2025-01-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Decreasing Emergency Railroad Accident Instances Locally Act or the DERAIL Act</strong></p><p>This bill requires the Department of Transportation (DOT) to expand the definition of a high-hazard flammable train (HHFT), thereby subjecting more trains to additional safety requirements.</p><p>Specifically, DOT must expand the definition of <em>HHFT </em>to mean a train transporting one or more loaded tank cars of a Class 3 flammable liquid (e.g., benzene residue) or a Class 2 flammable gas (e.g., vinyl chloride) and other materials DOT determines necessary for safety. Current regulations define <em>HHFT </em>as a train transporting 20 or more loaded tank cars of a Class 3 flammable liquid in a continuous block or 35 or more loaded tank cars of a Class 3 flammable liquid dispersed throughout the train.</p><p>The bill also requires railway carriers to report a train derailment that involves a train carrying material toxic by inhalation within 24 hours of the derailment to the National Response Center (NRC), state and local officials, and tribal governments. As background, the NRC is a part of the federally established National Response System. Reports to the NRC activate\u00a0the National Oil and Hazardous Substances Pollution Contingency Plan and the federal government's response capabilities.</p>"
        },
        "title": "DERAIL Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr854.xml",
    "summary": {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Decreasing Emergency Railroad Accident Instances Locally Act or the DERAIL Act</strong></p><p>This bill requires the Department of Transportation (DOT) to expand the definition of a high-hazard flammable train (HHFT), thereby subjecting more trains to additional safety requirements.</p><p>Specifically, DOT must expand the definition of <em>HHFT </em>to mean a train transporting one or more loaded tank cars of a Class 3 flammable liquid (e.g., benzene residue) or a Class 2 flammable gas (e.g., vinyl chloride) and other materials DOT determines necessary for safety. Current regulations define <em>HHFT </em>as a train transporting 20 or more loaded tank cars of a Class 3 flammable liquid in a continuous block or 35 or more loaded tank cars of a Class 3 flammable liquid dispersed throughout the train.</p><p>The bill also requires railway carriers to report a train derailment that involves a train carrying material toxic by inhalation within 24 hours of the derailment to the National Response Center (NRC), state and local officials, and tribal governments. As background, the NRC is a part of the federally established National Response System. Reports to the NRC activate\u00a0the National Oil and Hazardous Substances Pollution Contingency Plan and the federal government's response capabilities.</p>",
      "updateDate": "2025-03-25",
      "versionCode": "id119hr854"
    },
    "title": "DERAIL Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Decreasing Emergency Railroad Accident Instances Locally Act or the DERAIL Act</strong></p><p>This bill requires the Department of Transportation (DOT) to expand the definition of a high-hazard flammable train (HHFT), thereby subjecting more trains to additional safety requirements.</p><p>Specifically, DOT must expand the definition of <em>HHFT </em>to mean a train transporting one or more loaded tank cars of a Class 3 flammable liquid (e.g., benzene residue) or a Class 2 flammable gas (e.g., vinyl chloride) and other materials DOT determines necessary for safety. Current regulations define <em>HHFT </em>as a train transporting 20 or more loaded tank cars of a Class 3 flammable liquid in a continuous block or 35 or more loaded tank cars of a Class 3 flammable liquid dispersed throughout the train.</p><p>The bill also requires railway carriers to report a train derailment that involves a train carrying material toxic by inhalation within 24 hours of the derailment to the National Response Center (NRC), state and local officials, and tribal governments. As background, the NRC is a part of the federally established National Response System. Reports to the NRC activate\u00a0the National Oil and Hazardous Substances Pollution Contingency Plan and the federal government's response capabilities.</p>",
      "updateDate": "2025-03-25",
      "versionCode": "id119hr854"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr854ih.xml"
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
      "title": "DERAIL Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-28T09:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "DERAIL Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-28T09:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Decreasing Emergency Railroad Accident Instances Locally Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-28T09:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Transportation to issue certain regulations to define high-hazard flammable train, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-28T09:03:29Z"
    }
  ]
}
```
