# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1335?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1335
- Title: MSD Act
- Congress: 119
- Bill type: HR
- Bill number: 1335
- Origin chamber: House
- Introduced date: 2025-02-13
- Update date: 2026-05-30T08:05:47Z
- Update date including text: 2026-05-30T08:05:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-13 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-13 - Committee: Referred to the Subcommittee on Counterterrorism and Intelligence.
- 2025-02-13 - Committee: Referred to the Subcommittee on Emergency Management and Technology.
- Latest action: 2025-02-13: Introduced in House

## Actions

- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-13 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-13 - Committee: Referred to the Subcommittee on Counterterrorism and Intelligence.
- 2025-02-13 - Committee: Referred to the Subcommittee on Emergency Management and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1335",
    "number": "1335",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "M001217",
        "district": "23",
        "firstName": "Jared",
        "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
        "lastName": "Moskowitz",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "MSD Act",
    "type": "HR",
    "updateDate": "2026-05-30T08:05:47Z",
    "updateDateIncludingText": "2026-05-30T08:05:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-13",
      "committees": {
        "item": {
          "name": "Emergency Management and Technology Subcommittee",
          "systemCode": "hshm12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Emergency Management and Technology.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-13",
      "committees": {
        "item": {
          "name": "Counterterrorism, Law Enforcement, and Intelligence Subcommittee",
          "systemCode": "hshm05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Counterterrorism and Intelligence.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-13",
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
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-13",
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
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-13",
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
          "date": "2025-02-13T14:01:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": [
          {
            "activities": {
              "item": {
                "date": "2025-02-13T18:19:23Z",
                "name": "Referred to"
              }
            },
            "name": "Counterterrorism, Law Enforcement, and Intelligence Subcommittee",
            "systemCode": "hshm05"
          },
          {
            "activities": {
              "item": {
                "date": "2025-02-13T18:19:23Z",
                "name": "Referred to"
              }
            },
            "name": "Emergency Management and Technology Subcommittee",
            "systemCode": "hshm12"
          }
        ]
      },
      "systemCode": "hshm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-13T14:01:40Z",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "PA"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "FL"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1335ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1335\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2025 Mr. Moskowitz (for himself, Mr. Fitzpatrick , and Mrs. Cherfilus-McCormick ) introduced the following bill; which was referred to the Committee on Education and Workforce , and in addition to the Committee on Homeland Security , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo enhance the safety of elementary and secondary schools by requiring emergency response and parental notification procedures and improving the security of interior and exterior doors, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Measures for Safer School Districts Act or the MSD Act .\n#### 2. Emergency response and parental notification procedures\nTitle VIII of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 et seq. ) is amended by adding at the end the following:\nH Emergency response and parental notification procedures 8701. Emergency response and parental notification procedures (a) Policies and notification required As a condition of receiving funds under this Act, each local educational agency shall\u2014 (1) develop and implement emergency response procedures covering all students, faculty, and staff at public elementary and secondary schools under the jurisdiction of the agency; and (2) pursuant to such procedures, ensure that parents and guardians receive timely notification of covered threats and emergencies that occur on school grounds, during school transportation, or during school-sponsored activities. (b) Additional requirements The emergency response and notification procedures developed under subsection (a) shall meet the following criteria: (1) The procedures shall be developed in consultation with appropriate public safety agencies. (2) Commonly used alarm system responses for specific types of emergencies shall be implemented. (3) The procedures shall identify\u2014 (A) the primary emergency response agency that is responsible for each type of covered threat or emergency; and (B) the individuals within each school who are responsible for contacting the primary emergency response agency in the event of such a threat or emergency. (c) Covered threats and emergencies defined In this section, the term covered threats and emergencies means\u2014 (1) weapons possession or use when there is intended harm toward another person; (2) active shooter or hostage situations; (3) bomb threats; (4) murder, homicide, or manslaughter; (5) sex offenses, including rape, sexual assault, or sexual misconduct involving a student and school personnel; (6) trespassing; (7) fires; (8) natural weather emergencies, including hurricanes, tornadoes, and severe storms; (9) natural disasters; (10) exposure to harmful substances or conditions as a result of a manmade emergency; and (11) such other threats and emergencies as a local educational agency determines appropriate to address through the procedures required under subsection (a). .\n#### 3. Installation or modification of interior and exterior doors in schools\n##### (a) In general\nNot later than 90 days after the date of the enactment of this Act, the Director of the Cybersecurity and Infrastructure Security Agency (CISA) of the Department of Homeland Security, in consultation with the Secretary of Homeland Security, shall convene a rulemaking advisory committee to review and develop findings and recommendations to require the installation or modification of interior and exterior doors in any elementary or secondary school in the United States which receives Federal funding.\n##### (b) Membership\nThe Director of CISA shall chair and, in consultation with the Secretary of Homeland Security, appoint the members of the rulemaking committee under subsection (a), which shall be comprised of the Secretary of Education (or his or her designee) and at least one representative from the constituencies of\u2014\n**(1)**\nState and local law enforcement officers;\n**(2)**\nschool safety personnel or school resource officers;\n**(3)**\nschool safety advocates, which may include parents;\n**(4)**\npublic, private, or parochial school teachers or administrators;\n**(5)**\nindividuals with expertise in the area of ballistic shielding technology;\n**(6)**\nindividuals with expertise in the field of school construction, including structural engineering or architecture; and\n**(7)**\nother stakeholders or experts the Director of CISA, in consultation with the Secretary of Homeland Security, determines appropriate.\n##### (c) Considerations\nThe rulemaking advisory committee under subsection (a) shall consider the following:\n**(1)**\nRequirements for any reinforced door, including an identification or specification of appropriate technologies, mechanisms, covers, adhesives, or other qualities of such doors that may be utilized to better guarantee security within a classroom or elementary or secondary school building.\n**(2)**\nReinforced door performance standards that manufacturers and elementary or secondary schools are required to satisfy.\n**(3)**\nThe development, certification, testing, manufacturing, installation, and training relating to reinforced doors.\n**(4)**\nThe appropriate term of service or lifetime of a reinforced door.\n**(5)**\nHow requirements will ensure the effectiveness of a reinforced door in protecting against threats while not inhibiting the movement of law enforcement personnel in pursuit of a threat or the ability of students, teachers, and elementary or secondary school personnel to safely evacuate in the event of an emergency.\n**(6)**\nOther considerations the Director of CISA determines appropriate.\n##### (d) Report to Congress\nNot later than one year after the convening of the rulemaking advisory committee under subsection (a), the Director of CISA shall submit to the Committee on Homeland Security and the Committee on Education and Workforce of the House of Representatives and the Committee on Homeland Security and Governmental Affairs and the Committee on Heath, Education, Labor, and Pensions of the Senate a report based on the findings and recommendations of such committee.\n##### (e) Final rule relating to installation or modification of interior and exterior doors in schools\nNot later than six months after the date of submission of the report required under subsection (d), the Director of CISA, taking into consideration the findings and recommendations contained in such report, shall issue a final rule requiring the installation or modification of interior and exterior doors in elementary or secondary schools for the purpose of reinforcing such doors.\n##### (f) State Homeland Security Grant Program\nThis section shall be administered under the authorization of the Homeland Security Grant Program under section 2004 of the Homeland Security Act of 2002 ( 6 U.S.C. 605 ). There is authorized to be appropriated to such Program to carry out this section an additional $100,000,000 for the fiscal year in which the final rule is issued in accordance with subsection (e) and for each of the nine fiscal years thereafter. Such additional amounts may only be obligated and expended for the purpose of carrying out this section.",
      "versionDate": "2025-02-13",
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
        "actionDate": "2026-01-15",
        "text": "Referred to the Subcommittee on Oversight and Investigations."
      },
      "number": "6637",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To advance bipartisan priorities.",
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
            "name": "Advisory bodies",
            "updateDate": "2025-05-30T19:24:42Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-05-30T19:24:49Z"
          },
          {
            "name": "Educational facilities and institutions",
            "updateDate": "2025-05-30T19:24:26Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2025-05-30T19:24:20Z"
          },
          {
            "name": "Emergency communications systems",
            "updateDate": "2025-05-30T19:24:37Z"
          },
          {
            "name": "School administration",
            "updateDate": "2025-05-30T19:24:32Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-03-14T11:56:46Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
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
          "measure-id": "id119hr1335",
          "measure-number": "1335",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-13",
          "originChamber": "HOUSE",
          "update-date": "2025-07-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1335v00",
            "update-date": "2025-07-30"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Measures for Safer School Districts Act or the\u00a0MSD Act</strong></p><p>This bill requires each local educational agency (LEA), as a condition of receiving federal elementary and secondary education funds, to establish procedures for responding to school emergencies and for timely notifying parents of school emergencies. It also requires interior and exterior doors in schools to be reinforced.\u00a0</p><p>Specifically, the bill requires each LEA to (1) develop and implement emergency response procedures covering all students, faculty, and staff at public schools under the jurisdiction of the LEA; and (2) ensure that parents and guardians receive timely notification of covered threats and emergencies (e.g., active shooter situations, bomb threats, and natural disasters) that occur on school grounds, during school transportation, or during school-sponsored activities. These emergency response procedures must meet specified criteria, including by requiring\u00a0commonly used alarm system responses for specific types of emergencies.</p><p>Additionally, the bill requires the\u00a0Cybersecurity and Infrastructure Security Agency (CISA) to convene a rulemaking advisory committee to review and develop findings and recommendations to require the installation or modification of interior and exterior doors in any school that receives federal funding. Further,\u00a0CISA must (1) submit a report to Congress on the advisory committee's findings and recommendations, and (2) issue a final rule that requires the installation or modification of interior and exterior doors in schools to reinforce such doors.</p><p>The bill authorizes the use of grants under the Homeland Security Grant Program to carry out the bill's provisions.</p>"
        },
        "title": "MSD Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1335.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Measures for Safer School Districts Act or the\u00a0MSD Act</strong></p><p>This bill requires each local educational agency (LEA), as a condition of receiving federal elementary and secondary education funds, to establish procedures for responding to school emergencies and for timely notifying parents of school emergencies. It also requires interior and exterior doors in schools to be reinforced.\u00a0</p><p>Specifically, the bill requires each LEA to (1) develop and implement emergency response procedures covering all students, faculty, and staff at public schools under the jurisdiction of the LEA; and (2) ensure that parents and guardians receive timely notification of covered threats and emergencies (e.g., active shooter situations, bomb threats, and natural disasters) that occur on school grounds, during school transportation, or during school-sponsored activities. These emergency response procedures must meet specified criteria, including by requiring\u00a0commonly used alarm system responses for specific types of emergencies.</p><p>Additionally, the bill requires the\u00a0Cybersecurity and Infrastructure Security Agency (CISA) to convene a rulemaking advisory committee to review and develop findings and recommendations to require the installation or modification of interior and exterior doors in any school that receives federal funding. Further,\u00a0CISA must (1) submit a report to Congress on the advisory committee's findings and recommendations, and (2) issue a final rule that requires the installation or modification of interior and exterior doors in schools to reinforce such doors.</p><p>The bill authorizes the use of grants under the Homeland Security Grant Program to carry out the bill's provisions.</p>",
      "updateDate": "2025-07-30",
      "versionCode": "id119hr1335"
    },
    "title": "MSD Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Measures for Safer School Districts Act or the\u00a0MSD Act</strong></p><p>This bill requires each local educational agency (LEA), as a condition of receiving federal elementary and secondary education funds, to establish procedures for responding to school emergencies and for timely notifying parents of school emergencies. It also requires interior and exterior doors in schools to be reinforced.\u00a0</p><p>Specifically, the bill requires each LEA to (1) develop and implement emergency response procedures covering all students, faculty, and staff at public schools under the jurisdiction of the LEA; and (2) ensure that parents and guardians receive timely notification of covered threats and emergencies (e.g., active shooter situations, bomb threats, and natural disasters) that occur on school grounds, during school transportation, or during school-sponsored activities. These emergency response procedures must meet specified criteria, including by requiring\u00a0commonly used alarm system responses for specific types of emergencies.</p><p>Additionally, the bill requires the\u00a0Cybersecurity and Infrastructure Security Agency (CISA) to convene a rulemaking advisory committee to review and develop findings and recommendations to require the installation or modification of interior and exterior doors in any school that receives federal funding. Further,\u00a0CISA must (1) submit a report to Congress on the advisory committee's findings and recommendations, and (2) issue a final rule that requires the installation or modification of interior and exterior doors in schools to reinforce such doors.</p><p>The bill authorizes the use of grants under the Homeland Security Grant Program to carry out the bill's provisions.</p>",
      "updateDate": "2025-07-30",
      "versionCode": "id119hr1335"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1335ih.xml"
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
      "title": "MSD Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T04:23:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "MSD Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T04:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Measures for Safer School Districts Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T04:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To enhance the safety of elementary and secondary schools by requiring emergency response and parental notification procedures and improving the security of interior and exterior doors, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T04:18:37Z"
    }
  ]
}
```
