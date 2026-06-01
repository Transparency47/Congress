# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/107?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/107
- Title: Lumbee Fairness Act
- Congress: 119
- Bill type: S
- Bill number: 107
- Origin chamber: Senate
- Introduced date: 2025-01-16
- Update date: 2026-03-21T11:03:25Z
- Update date including text: 2026-03-21T11:03:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in Senate
- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on Indian Affairs.
- 2025-11-05 - Committee: Committee on Indian Affairs. Hearings held. Hearings printed: S.Hrg. 119-275.
- Latest action: 2025-01-16: Introduced in Senate

## Actions

- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on Indian Affairs.
- 2025-11-05 - Committee: Committee on Indian Affairs. Hearings held. Hearings printed: S.Hrg. 119-275.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/107",
    "number": "107",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "T000476",
        "district": "",
        "firstName": "Thomas",
        "fullName": "Sen. Tillis, Thomas [R-NC]",
        "lastName": "Tillis",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Lumbee Fairness Act",
    "type": "S",
    "updateDate": "2026-03-21T11:03:25Z",
    "updateDateIncludingText": "2026-03-21T11:03:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-05",
      "committees": {
        "item": {
          "name": "Indian Affairs Committee",
          "systemCode": "slia00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Indian Affairs. Hearings held. Hearings printed: S.Hrg. 119-275.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Indian Affairs Committee",
          "systemCode": "slia00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Indian Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
        "item": [
          {
            "date": "2025-11-05T21:44:34Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-11-05T21:44:34Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-01-16T17:33:27Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Indian Affairs Committee",
      "systemCode": "slia00",
      "type": "Other"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "NC"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "VA"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "VA"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-01-24",
      "state": "NH"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "NH"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "WV"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "SC"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "OK"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "NJ"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "CT"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "MD"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "DE"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CT"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "DE"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "MA"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "HI"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "False",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "WI"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "HI"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "MD"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-10-07",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s107is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 107\nIN THE SENATE OF THE UNITED STATES\nJanuary 16, 2025 Mr. Tillis (for himself and Mr. Budd ) introduced the following bill; which was read twice and referred to the Committee on Indian Affairs\nA BILL\nTo amend the Lumbee Act of 1956.\n#### 1. Short title\nThis Act may be cited as the Lumbee Fairness Act .\n#### 2. Federal recognition\nThe Act of June 7, 1956 (70 Stat. 254, chapter 375), is amended\u2014\n**(1)**\nby striking section 2;\n**(2)**\nin the first sentence of the first section, by striking That the Indians and inserting the following:\n3. Designation of Lumbee Indians The Indians ;\n**(3)**\nin the preamble\u2014\n**(A)**\nby inserting before the first undesignated clause the following:\n1. Findings Congress finds that\u2014 ;\n**(B)**\nby designating the undesignated clauses as paragraphs (1) through (4), respectively, and indenting appropriately;\n**(C)**\nby striking Whereas each place it appears;\n**(D)**\nby striking and after the semicolon at the end of each of paragraphs (1) and (2) (as so designated); and\n**(E)**\nin paragraph (4) (as so designated), by striking : Now, therefore, and inserting a period;\n**(4)**\nby moving the enacting clause so as to appear before section 1 (as so designated);\n**(5)**\nby striking the last sentence of section 3 (as designated by paragraph (2));\n**(6)**\nby inserting before section 3 (as designated by paragraph (2)) the following:\n2. Definitions In this Act: (1) Secretary The term Secretary means the Secretary of the Interior. (2) Tribe The term Tribe means the Lumbee Tribe of North Carolina or the Lumbee Indians of North Carolina. ; and\n**(7)**\nby adding at the end the following:\n4. Federal recognition (a) In general Federal recognition is extended to the Tribe (as designated as petitioner number 65 by the Office of Federal Acknowledgment). (b) Applicability of laws All laws and regulations of the United States of general application to Indians and Indian tribes shall apply to the Tribe and its members. (c) Petition for acknowledgment Notwithstanding section 3, any group of Indians in Robeson and adjoining counties, North Carolina, whose members are not enrolled in the Tribe (as determined under section 5(d)) may petition under part 83 of title 25 of the Code of Federal Regulations for acknowledgment of tribal existence. 5. Eligibility for Federal services (a) In general The Tribe and its members shall be eligible for all services and benefits provided by the Federal Government to federally recognized Indian tribes. (b) Service area For the purpose of the delivery of Federal services and benefits described in subsection (a), those members of the Tribe residing in Robeson, Cumberland, Hoke, and Scotland counties in North Carolina shall be deemed to be residing on or near an Indian reservation. (c) Determination of needs On verification by the Secretary of a tribal roll under subsection (d), the Secretary and the Secretary of Health and Human Services shall\u2014 (1) develop, in consultation with the Tribe, a determination of needs to provide the services for which members of the Tribe are eligible; and (2) after the tribal roll is verified, each submit to Congress a written statement of those needs. (d) Tribal roll (1) In general For purpose of the delivery of Federal services and benefits described in subsection (a), the tribal roll in effect on the date of enactment of this section shall, subject to verification by the Secretary, define the service population of the Tribe. (2) Verification limitation and deadline The verification by the Secretary under paragraph (1) shall\u2014 (A) be limited to confirming documentary proof of compliance with the membership criteria set out in the constitution of the Tribe adopted on November 16, 2001; and (B) be completed not later than 2 years after the submission of a digitized roll with supporting documentary proof by the Tribe to the Secretary. 6. Authorization to take land into trust (a) In general Notwithstanding any other provision of law, the Secretary is hereby authorized to take land into trust for the benefit of the Tribe. (b) Treatment of certain land An application to take into trust land located within Robeson County, North Carolina, under this section shall be treated by the Secretary as an on reservation trust acquisition under part 151 of title 25, Code of Federal Regulations (or a successor regulation). 7. Jurisdiction of State of North Carolina (a) In general With respect to land located within the State of North Carolina that is owned by, or held in trust by the United States for the benefit of, the Tribe, or any dependent Indian community of the Tribe, the State of North Carolina shall exercise jurisdiction over\u2014 (1) all criminal offenses that are committed; and (2) all civil actions that arise. (b) Transfer of jurisdiction (1) In general Subject to paragraph (2), the Secretary may accept on behalf of the United States, after consulting with the Attorney General of the United States, any transfer by the State of North Carolina to the United States of any portion of the jurisdiction of the State of North Carolina described in subsection (a) over Indian country occupied by the Tribe pursuant to an agreement between the Tribe and the State of North Carolina. (2) Restriction A transfer of jurisdiction described in paragraph (1) may not take effect until 2 years after the effective date of the agreement described in that paragraph. (c) Effect Nothing in this section affects the application of section 109 of the Indian Child Welfare Act of 1978 ( 25 U.S.C. 1919 ). .",
      "versionDate": "2025-01-16",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-01-16",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "474",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Lumbee Fairness Act",
      "type": "HR"
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
            "updateDate": "2025-04-14T17:13:53Z"
          },
          {
            "name": "Indian lands and resources rights",
            "updateDate": "2025-04-14T17:13:53Z"
          },
          {
            "name": "North Carolina",
            "updateDate": "2025-04-14T17:13:53Z"
          }
        ]
      },
      "policyArea": {
        "name": "Native Americans",
        "updateDate": "2025-04-09T20:22:12Z"
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
    "originChamber": "Senate",
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
          "measure-id": "id119s107",
          "measure-number": "107",
          "measure-type": "s",
          "orig-publish-date": "2025-01-16",
          "originChamber": "SENATE",
          "update-date": "2025-04-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s107v00",
            "update-date": "2025-04-10"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><b>Lumbee Fairness Act</b></p> <p>This bill extends federal recognition to the Lumbee Tribe of North Carolina and makes its members eligible for the services and benefits provided to members of federally recognized tribes. </p> <p>Members of the tribe residing in Robeson, Cumberland, Hoke, and Scotland Counties in North Carolina are deemed to be within the delivery area for such services.</p> <p>The Department of the Interior and the Department of Health and Human Services must develop, in consultation with the tribe, a determination of needs to provide the services for which members of the tribe are eligible.</p> <p>Interior may take land into trust for the benefit of the tribe.</p> <p>Finally, North Carolina must exercise jurisdiction over all criminal offenses committed, and all civil actions that arise, on North Carolina lands owned by, or held in trust for, the Lumbee Tribe or any dependent Indian community of the tribe unless jurisdiction is transferred to the United States pursuant to an agreement between the tribe and the state.</p>"
        },
        "title": "Lumbee Fairness Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s107.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Lumbee Fairness Act</b></p> <p>This bill extends federal recognition to the Lumbee Tribe of North Carolina and makes its members eligible for the services and benefits provided to members of federally recognized tribes. </p> <p>Members of the tribe residing in Robeson, Cumberland, Hoke, and Scotland Counties in North Carolina are deemed to be within the delivery area for such services.</p> <p>The Department of the Interior and the Department of Health and Human Services must develop, in consultation with the tribe, a determination of needs to provide the services for which members of the tribe are eligible.</p> <p>Interior may take land into trust for the benefit of the tribe.</p> <p>Finally, North Carolina must exercise jurisdiction over all criminal offenses committed, and all civil actions that arise, on North Carolina lands owned by, or held in trust for, the Lumbee Tribe or any dependent Indian community of the tribe unless jurisdiction is transferred to the United States pursuant to an agreement between the tribe and the state.</p>",
      "updateDate": "2025-04-10",
      "versionCode": "id119s107"
    },
    "title": "Lumbee Fairness Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Lumbee Fairness Act</b></p> <p>This bill extends federal recognition to the Lumbee Tribe of North Carolina and makes its members eligible for the services and benefits provided to members of federally recognized tribes. </p> <p>Members of the tribe residing in Robeson, Cumberland, Hoke, and Scotland Counties in North Carolina are deemed to be within the delivery area for such services.</p> <p>The Department of the Interior and the Department of Health and Human Services must develop, in consultation with the tribe, a determination of needs to provide the services for which members of the tribe are eligible.</p> <p>Interior may take land into trust for the benefit of the tribe.</p> <p>Finally, North Carolina must exercise jurisdiction over all criminal offenses committed, and all civil actions that arise, on North Carolina lands owned by, or held in trust for, the Lumbee Tribe or any dependent Indian community of the tribe unless jurisdiction is transferred to the United States pursuant to an agreement between the tribe and the state.</p>",
      "updateDate": "2025-04-10",
      "versionCode": "id119s107"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s107is.xml"
        }
      ],
      "type": "Introduced in Senate"
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
      "updateDate": "2026-03-21T11:03:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Lumbee Fairness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-19T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Lumbee Act of 1956.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-19T03:18:25Z"
    }
  ]
}
```
