# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/474?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/474
- Title: Lumbee Fairness Act
- Congress: 119
- Bill type: HR
- Bill number: 474
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2026-02-04T04:26:27Z
- Update date including text: 2026-02-04T04:26:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/474",
    "number": "474",
    "originChamber": "House",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "R000603",
        "district": "7",
        "firstName": "David",
        "fullName": "Rep. Rouzer, David [R-NC-7]",
        "lastName": "Rouzer",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Lumbee Fairness Act",
    "type": "HR",
    "updateDate": "2026-02-04T04:26:27Z",
    "updateDateIncludingText": "2026-02-04T04:26:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T14:01:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "NC"
    },
    {
      "bioguideId": "H001067",
      "district": "9",
      "firstName": "Richard",
      "fullName": "Rep. Hudson, Richard [R-NC-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Hudson",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "NC"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "NC"
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
      "sponsorshipDate": "2025-01-16",
      "state": "NC"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "NC"
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
      "sponsorshipDate": "2025-01-16",
      "state": "NC"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison [R-NC-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "NC"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "NC"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "CO"
    },
    {
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "NC"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-07-25",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr474ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 474\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Mr. Rouzer (for himself, Mr. Harris of North Carolina , Mr. Hudson , Mrs. Foushee , Mr. Murphy , Ms. Ross , Mr. Davis of North Carolina , Mr. McDowell , and Mr. Moore of North Carolina ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Lumbee Act of 1956.\n#### 1. Short title\nThis Act may be cited as the Lumbee Fairness Act .\n#### 2. Federal recognition\nThe Act of June 7, 1956 (70 Stat. 254, chapter 375), is amended\u2014\n**(1)**\nby striking section 2;\n**(2)**\nin the first sentence of the first section, by striking That the Indians and inserting the following:\n3. Designation of Lumbee Indians The Indians\u2014 ;\n**(3)**\nin the preamble\u2014\n**(A)**\nby inserting before the first undesignated clause the following:\n1. Findings Congress finds that\u2014 ;\n**(B)**\nby designating the undesignated clauses as paragraphs (1) through (4), respectively, and indenting appropriately;\n**(C)**\nby striking Whereas each place it appears;\n**(D)**\nby striking and after the semicolon at the end of each of paragraphs (1) and (2) (as so designated); and\n**(E)**\nin paragraph (4) (as so designated), by striking : Now, therefore, and inserting a period;\n**(4)**\nby moving the enacting clause so as to appear before section 1 (as so designated);\n**(5)**\nby striking the last sentence of section 3 (as designated by paragraph (2));\n**(6)**\nby inserting before section 3 (as designated by paragraph (2)) the following:\n2. Definitions In this Act: (1) Secretary The term Secretary means the Secretary of the Interior. (2) Tribe The term Tribe means the Lumbee Tribe of North Carolina or the Lumbee Indians of North Carolina. ; and\n**(7)**\nby adding at the end the following:\n4. Federal recognition (a) In general Federal recognition is extended to the Tribe (as designated as petitioner number 65 by the Office of Federal Acknowledgment). (b) Applicability of laws All laws and regulations of the United States of general application to Indians and Indian tribes shall apply to the Tribe and its members. (c) Petition for acknowledgment Notwithstanding section 3, any group of Indians in Robeson and adjoining counties, North Carolina, whose members are not enrolled in the Tribe (as determined under section 5(d)) may petition under part 83 of title 25 of the Code of Federal Regulations for acknowledgment of tribal existence. 5. Eligibility for Federal services (a) In general The Tribe and its members shall be eligible for all services and benefits provided by the Federal Government to federally recognized Indian tribes. (b) Service area For the purpose of the delivery of Federal services and benefits described in subsection (a), those members of the Tribe residing in Robeson, Cumberland, Hoke, and Scotland counties in North Carolina shall be deemed to be residing on or near an Indian reservation. (c) Determination of needs On verification by the Secretary of a tribal roll under subsection (d), the Secretary and the Secretary of Health and Human Services shall\u2014 (1) develop, in consultation with the Tribe, a determination of needs to provide the services for which members of the Tribe are eligible; and (2) after the tribal roll is verified, each submit to Congress a written statement of those needs. (d) Tribal roll (1) In general For purpose of the delivery of Federal services and benefits described in subsection (a), the tribal roll in effect on the date of enactment of this section shall, subject to verification by the Secretary, define the service population of the Tribe. (2) Verification limitation and deadline The verification by the Secretary under paragraph (1) shall\u2014 (A) be limited to confirming documentary proof of compliance with the membership criteria set out in the constitution of the Tribe adopted on November 16, 2001; and (B) be completed not later than 2 years after the submission of a digitized roll with supporting documentary proof by the Tribe to the Secretary. 6. Authorization to take land into trust (a) In general Notwithstanding any other provision of law, the Secretary is hereby authorized to take land into trust for the benefit of the Tribe. (b) Treatment of certain land An application to take into trust land located within Robeson County, North Carolina, under this section shall be treated by the Secretary as an on reservation trust acquisition under part 151 of title 25, Code of Federal Regulations (or a successor regulation). 7. Jurisdiction of State of North Carolina (a) In general With respect to land located within the State of North Carolina that is owned by, or held in trust by the United States for the benefit of, the Tribe, or any dependent Indian community of the Tribe, the State of North Carolina shall exercise jurisdiction over\u2014 (1) all criminal offenses that are committed; and (2) all civil actions that arise. (b) Transfer of jurisdiction (1) In general Subject to paragraph (2), the Secretary may accept on behalf of the United States, after consulting with the Attorney General of the United States, any transfer by the State of North Carolina to the United States of any portion of the jurisdiction of the State of North Carolina described in subsection (a) over Indian country occupied by the Tribe pursuant to an agreement between the Tribe and the State of North Carolina. (2) Restriction A transfer of jurisdiction described in paragraph (1) may not take effect until 2 years after the effective date of the agreement described in that paragraph. (c) Effect Nothing in this section affects the application of section 109 of the Indian Child Welfare Act of 1978 ( 25 U.S.C. 1919 ). .",
      "versionDate": "2025-01-16",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-11-05",
        "text": "Committee on Indian Affairs. Hearings held."
      },
      "number": "107",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Lumbee Fairness Act",
      "type": "S"
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
            "name": "Federal-Indian relations",
            "updateDate": "2025-04-14T17:14:10Z"
          },
          {
            "name": "Indian lands and resources rights",
            "updateDate": "2025-04-14T17:14:10Z"
          },
          {
            "name": "North Carolina",
            "updateDate": "2025-04-14T17:14:10Z"
          }
        ]
      },
      "policyArea": {
        "name": "Native Americans",
        "updateDate": "2025-04-09T20:15:07Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119hr474",
          "measure-number": "474",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-04-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr474v00",
            "update-date": "2025-04-10"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Lumbee Fairness Act</b></p> <p>This bill extends federal recognition to the Lumbee Tribe of North Carolina and makes its members eligible for the services and benefits provided to members of federally recognized tribes. </p> <p>Members of the tribe residing in Robeson, Cumberland, Hoke, and Scotland Counties in North Carolina are deemed to be within the delivery area for such services.</p> <p>The Department of the Interior and the Department of Health and Human Services must develop, in consultation with the tribe, a determination of needs to provide the services for which members of the tribe are eligible.</p> <p>Interior may take land into trust for the benefit of the tribe.</p> <p>Finally, North Carolina must exercise jurisdiction over all criminal offenses committed, and all civil actions that arise, on North Carolina lands owned by, or held in trust for, the Lumbee Tribe or any dependent Indian community of the tribe unless jurisdiction is transferred to the United States pursuant to an agreement between the tribe and the state.</p>"
        },
        "title": "Lumbee Fairness Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr474.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Lumbee Fairness Act</b></p> <p>This bill extends federal recognition to the Lumbee Tribe of North Carolina and makes its members eligible for the services and benefits provided to members of federally recognized tribes. </p> <p>Members of the tribe residing in Robeson, Cumberland, Hoke, and Scotland Counties in North Carolina are deemed to be within the delivery area for such services.</p> <p>The Department of the Interior and the Department of Health and Human Services must develop, in consultation with the tribe, a determination of needs to provide the services for which members of the tribe are eligible.</p> <p>Interior may take land into trust for the benefit of the tribe.</p> <p>Finally, North Carolina must exercise jurisdiction over all criminal offenses committed, and all civil actions that arise, on North Carolina lands owned by, or held in trust for, the Lumbee Tribe or any dependent Indian community of the tribe unless jurisdiction is transferred to the United States pursuant to an agreement between the tribe and the state.</p>",
      "updateDate": "2025-04-10",
      "versionCode": "id119hr474"
    },
    "title": "Lumbee Fairness Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Lumbee Fairness Act</b></p> <p>This bill extends federal recognition to the Lumbee Tribe of North Carolina and makes its members eligible for the services and benefits provided to members of federally recognized tribes. </p> <p>Members of the tribe residing in Robeson, Cumberland, Hoke, and Scotland Counties in North Carolina are deemed to be within the delivery area for such services.</p> <p>The Department of the Interior and the Department of Health and Human Services must develop, in consultation with the tribe, a determination of needs to provide the services for which members of the tribe are eligible.</p> <p>Interior may take land into trust for the benefit of the tribe.</p> <p>Finally, North Carolina must exercise jurisdiction over all criminal offenses committed, and all civil actions that arise, on North Carolina lands owned by, or held in trust for, the Lumbee Tribe or any dependent Indian community of the tribe unless jurisdiction is transferred to the United States pursuant to an agreement between the tribe and the state.</p>",
      "updateDate": "2025-04-10",
      "versionCode": "id119hr474"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr474ih.xml"
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
      "title": "Lumbee Fairness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-12T10:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Lumbee Fairness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-12T10:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Lumbee Act of 1956.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-12T10:48:16Z"
    }
  ]
}
```
