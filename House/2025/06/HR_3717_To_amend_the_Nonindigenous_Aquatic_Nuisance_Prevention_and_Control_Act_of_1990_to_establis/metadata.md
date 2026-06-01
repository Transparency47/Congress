# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3717?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3717
- Title: Golden Mussel Eradication and Control Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3717
- Origin chamber: House
- Introduced date: 2025-06-04
- Update date: 2026-03-13T08:05:31Z
- Update date including text: 2026-03-13T08:05:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-04: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-04 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-06-04: Introduced in House

## Actions

- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-04 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-04",
    "latestAction": {
      "actionDate": "2025-06-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3717",
    "number": "3717",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "H001090",
        "district": "9",
        "firstName": "Josh",
        "fullName": "Rep. Harder, Josh [D-CA-9]",
        "lastName": "Harder",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Golden Mussel Eradication and Control Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-13T08:05:31Z",
    "updateDateIncludingText": "2026-03-13T08:05:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-04",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-04",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-04",
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
          "date": "2025-06-04T14:02:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-06-04T14:02:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
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
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "CA"
    },
    {
      "bioguideId": "M001163",
      "district": "7",
      "firstName": "Doris",
      "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Matsui",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "CA"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "CA"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "CA"
    },
    {
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "CA"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3717ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3717\nIN THE HOUSE OF REPRESENTATIVES\nJune 4, 2025 Mr. Harder of California (for himself, Mr. Garamendi , Ms. Matsui , Mr. Thompson of California , Mr. DeSaulnier , and Mr. Gray ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on Natural Resources , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Nonindigenous Aquatic Nuisance Prevention and Control Act of 1990 to establish a demonstration program with respect to the golden mussel.\n#### 1. Short title\nThis Act may be cited as the Golden Mussel Eradication and Control Act of 2025 .\n#### 2. Golden mussel demonstration program\nSection 1202 of the Nonindigenous Aquatic Nuisance Prevention and Control Act of 1990 ( 16 U.S.C. 4722 ) is amended\u2014\n**(1)**\nby redesignating subsections (j) and (k) as subsections (k) and (l), respectively; and\n**(2)**\nby inserting after subsection (i) the following:\n(j) Golden mussel demonstration program (1) Demonstration program (A) In general The Task Force, in partnership with State and local entities, port authorities, industry partners, institutions of higher education, and local nonprofit organizations, shall develop a demonstration program of prevention, monitoring, control, eradication, education, and research with respect to the golden mussel, including\u2014 (i) research and development regarding\u2014 (I) the biology; (II) the environmental tolerances; (III) the effect on\u2014 (aa) fisheries; (bb) water quality; and (cc) other ecosystem components; and (IV) the efficacy of control mechanisms and technologies; (ii) tracking dispersal and establishment of an early warning system to alert likely areas of future infestations; (iii) development of control and eradication methods and plans, including\u2014 (I) in and around\u2014 (aa) derelict vessels; (bb) public infrastructure; (cc) fish screens; and (dd) waterways; and (II) hull inspections; and (iv) provision of technical assistance to regional, State and local entities to carry out this subsection, as applicable. (B) Implementation area The demonstration program shall be implemented in the Sacramento-San Joaquin Delta and any other waters of the United States the Task Force determines are infested, or likely to become infested, by the golden mussel. (C) Availability of certain information The Task Force shall collect and make available to State and local entities and port authorities, through direct reports, publications, and other means necessary, information relating to control and eradication methods and plans developed under the demonstration program. (D) Control and eradication guidelines Not later than 1 year after the date of the enactment of this subsection, the Task Force shall develop guidelines to control the spread of and eradicate the golden mussel, including through the establishment of watercraft inspection stations. (2) Response and containment research grant program (A) In general The Task Force shall establish a grant program to award amounts, on a competitive basis, to State and local entities, institutions of higher education, nonprofit organizations, and industry partners to carry out projects that\u2014 (i) identify effective technologies and mechanisms to control and remove golden mussels from\u2014 (I) water intakes; (II) conveyance infrastructure; (III) fish screens; (IV) derelict vessels; (V) boat hulls; (VI) waterways; or (VII) other areas where the golden mussel may be found; or (ii) provide an understanding of the biology of the golden mussel and effective containment science with respect to the golden mussel. (B) Technology transfer In carrying out the grant program, the Task Force may enter into an agreement with a State or local entity, port authority, industry partner, or any other appropriate entity for the use or sale of any new technology developed under the grant program to expedite the control and eradication of golden mussels. (3) Coordination (A) In general The demonstration program shall provide guidance to other Federal agencies, States, port authorities for all United States ports of entry, local government agencies, and regional and other entities with the necessary expertise to participate in control and eradication methods and plans developed pursuant to the demonstration program. (B) Delegation The Task Force may delegate responsibility for implementing all or a portion of a control or eradication method or plan developed pursuant to the demonstration program to an entity described in subparagraph (A) if the Task Force determines\u2014 (i) such entity has sufficient authority or jurisdiction and expertise; and (ii) it will be more efficient or effective to delegate such responsibility than to retain such responsibility. (4) Authorization of appropriations There are authorized to be appropriated to the Task Force to carry out this section $15,000,000 for each of fiscal years 2026 through 2030. (5) Definitions In this subsection: (A) Demonstration program The term demonstration program means the demonstration program developed under paragraph (1)(A). (B) Grant program The term grant program means the grant program established under paragraph (2)(A). (C) Institution of higher education The term institution of higher education has the meaning given the term in section 101(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) ). .",
      "versionDate": "2025-06-04",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-07-14T18:18:03Z"
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
      "date": "2025-06-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3717ih.xml"
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
      "title": "Golden Mussel Eradication and Control Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-11T03:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Golden Mussel Eradication and Control Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-11T03:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Nonindigenous Aquatic Nuisance Prevention and Control Act of 1990 to establish a demonstration program with respect to the golden mussel.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-11T03:48:45Z"
    }
  ]
}
```
