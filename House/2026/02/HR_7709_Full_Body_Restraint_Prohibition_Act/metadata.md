# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7709?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7709
- Title: Full-Body Restraint Prohibition Act
- Congress: 119
- Bill type: HR
- Bill number: 7709
- Origin chamber: House
- Introduced date: 2026-02-25
- Update date: 2026-05-16T08:07:17Z
- Update date including text: 2026-05-16T08:07:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-25: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2026-02-26 - Committee: Referred to the Subcommittee on Oversight, Investigations, and Accountability.
- Latest action: 2026-02-25: Introduced in House

## Actions

- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2026-02-26 - Committee: Referred to the Subcommittee on Oversight, Investigations, and Accountability.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-25",
    "latestAction": {
      "actionDate": "2026-02-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7709",
    "number": "7709",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "R000617",
        "district": "3",
        "firstName": "Delia",
        "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
        "lastName": "Ramirez",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Full-Body Restraint Prohibition Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:17Z",
    "updateDateIncludingText": "2026-05-16T08:07:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-26",
      "committees": {
        "item": {
          "name": "Oversight, Investigations, and Accountability Subcommittee",
          "systemCode": "hshm09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Oversight, Investigations, and Accountability.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-25",
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
      "actionDate": "2026-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-25",
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
          "date": "2026-02-25T14:00:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-26T20:54:56Z",
              "name": "Referred to"
            }
          },
          "name": "Oversight, Investigations, and Accountability Subcommittee",
          "systemCode": "hshm09"
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "DC"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "MI"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "NY"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "CA"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "GA"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "NY"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "IL"
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
      "sponsorshipDate": "2026-02-25",
      "state": "PA"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "CA"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "NY"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "WA"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "PA"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7709ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7709\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2026 Mrs. Ramirez (for herself, Ms. Norton , Ms. Tlaib , Mr. Goldman of New York , Ms. Simon , Mr. Johnson of Georgia , Mr. Espaillat , Mr. Davis of Illinois , Ms. Lee of Pennsylvania , Ms. Lofgren , Ms. Vel\u00e1zquez , and Ms. Randall ) introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo amend the Homeland Security Act of 2002 to prohibit the Secretary of Homeland Security from obligating or expending Federal funds for the acquisition of, or utilizing, full-body restraints, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Full-Body Restraint Prohibition Act .\n#### 2. Prohibitions on the Department of Homeland Security with respect to full-body restraints\n##### (a) In general\nTitle VII of the Homeland Security Act of 2002 ( 6 U.S.C. 341 et seq. ) is amended by adding at the end the following new section:\n714. Prohibitions with respect to full-body restraints (a) In general The Secretary may not\u2014 (1) obligate or expend Federal funds for the acquisition of, or (2) utilize, a full-body restraint. (b) Saving provision The prohibition under subsection (a)(1) does not apply with respect to a contract or other similar type agreement entered into on or before the date of the enactment of this section. (c) Federal service If an officer or employee of the Department in the course of employment with the Department\u2014 (1) violates a prohibition under subsection (a), or (2) deceives Congress or departmental leadership, as described in section 454, on a matter related to such prohibition, the Secretary, through the employee discipline and adverse action programs referred to in section 704(b)(10), shall remove such officer or employee, as the case may be, from Federal service. (d) Reports (1) In general Not later than 90 days after the date of the enactment of this section and quarterly thereafter, the Secretary shall submit to the Committee on Homeland Security and the Committee on the Judiciary of the House of Representatives and the Committee on Homeland Security and Governmental Affairs and the Committee on the Judiciary of the Senate a report that includes the following: (A) Information relating to departmental compliance with the prohibitions under subsection (a). (B) An accounting of the full-body restraints, if any, in the possession of the Department. (2) Contents If the prohibition under subsection (a)(2) is violated, the applicable report under paragraph (1) shall include, to the extent practicable, the following with respect to such violation: (A) An identification of the following: (i) The individual with respect to whom personnel of the Department utilized a full-body restraint. (ii) If applicable, each field office to which such personnel are assigned or deployed, as the case may be. (B) Information relating to the following: (i) The reason for such utilization. (ii) The age, sex, race, and ethnicity of such individual. (iii) The period of time for which such restraint was so utilized. (iv) The citizenship or immigration status of such individual. (v) Whether such individual was injured in the course of being placed in such restraint. (vi) Whether subsequent to such placement such individual was injured as a result of such utilization. (vii) The component of the Department through which such utilization was carried out. (viii) The location at which, or the transportation route on which, such utilization was carried out. (ix) The language access services, if any, available to such individual immediately before and during such utilization. (C) An identification of the officer or employee of the Department who is responsible for such utilization. (D) Information relating to the following: (i) Whether such officer or employee, as the case may be, during such utilization was a doctor, nurse, or other health professional, qualified to determine whether such utilization would injure such individual. (ii) If clause (i) is answered in the affirmative, such qualifications. (e) Full-Body restraints defined In this section, the term full-body restraints means four-point and five-point restraints that immobilize an individual. .\n##### (b) Clerical amendment\nThe table of contents in section 1(b) of the Homeland Security Act of 2002 is amended by inserting after the item relating to section 713 the following new item:\nSec. 714. Prohibitions with respect to full-body restraints. .",
      "versionDate": "2026-02-25",
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
        "name": "Immigration",
        "updateDate": "2026-03-27T20:06:35Z"
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
      "date": "2026-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7709ih.xml"
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
      "title": "Full-Body Restraint Prohibition Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-21T03:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Full-Body Restraint Prohibition Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-21T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Homeland Security Act of 2002 to prohibit the Secretary of Homeland Security from obligating or expending Federal funds for the acquisition of, or utilizing, full-body restraints, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-21T03:48:24Z"
    }
  ]
}
```
