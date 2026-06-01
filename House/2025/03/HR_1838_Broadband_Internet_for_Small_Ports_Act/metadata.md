# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1838?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1838
- Title: Broadband Internet for Small Ports Act
- Congress: 119
- Bill type: HR
- Bill number: 1838
- Origin chamber: House
- Introduced date: 2025-03-04
- Update date: 2025-04-01T08:06:13Z
- Update date including text: 2025-04-01T08:06:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-04: Introduced in House
- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-04 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-28 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.
- Latest action: 2025-03-04: Introduced in House

## Actions

- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-04 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-28 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-04",
    "latestAction": {
      "actionDate": "2025-03-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1838",
    "number": "1838",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "P000610",
        "district": "",
        "firstName": "Stacey",
        "fullName": "Del. Plaskett, Stacey E. [D-VI-At Large]",
        "lastName": "Plaskett",
        "party": "D",
        "state": "VI"
      }
    ],
    "title": "Broadband Internet for Small Ports Act",
    "type": "HR",
    "updateDate": "2025-04-01T08:06:13Z",
    "updateDateIncludingText": "2025-04-01T08:06:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-28",
      "committees": {
        "item": {
          "name": "Commodity Markets, Digital Assets, and Rural Development Subcommittee",
          "systemCode": "hsag22"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-04",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-04",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-04",
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
          "date": "2025-03-04T15:04:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-28T20:48:57Z",
              "name": "Referred to"
            }
          },
          "name": "Commodity Markets, Digital Assets, and Rural Development Subcommittee",
          "systemCode": "hsag22"
        }
      },
      "systemCode": "hsag00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-04T15:04:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1838ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1838\nIN THE HOUSE OF REPRESENTATIVES\nMarch 4, 2025 Ms. Plaskett (for herself and Mr. Moore of Alabama ) introduced the following bill; which was referred to the Committee on Agriculture , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Rural Electrification Act of 1936 to improve access to broadband telecommunications services in rural areas, including by encouraging the provision of broadband loans and grants to increase broadband service in rural ports, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Broadband Internet for Small Ports Act .\n#### 2. Access to broadband telecommunications services in rural areas\nSection 601 of the Rural Electrification Act of 1936 ( 7 U.S.C. 950bb ) is amended\u2014\n**(1)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (A)\u2014\n**(I)**\nin clause (i)\u2014\n**(aa)**\nby striking of at least\u2014 and inserting a semicolon; and\n**(bb)**\nby striking subclauses (I) and (II);\n**(II)**\nin clause (iii), by striking and at the end;\n**(III)**\nin clause (iv), by striking the period at the end and inserting ; and ; and\n**(IV)**\nby adding at the end the following:\n(v) give priority to applications for projects to provide rapid and expanded deployment of fixed and mobile broadband on cropland and ranchland within a service territory for use in various applications of precision agriculture. ;\n**(ii)**\nin subparagraph (B)\u2014\n**(I)**\nin clause (i)\u2014\n**(aa)**\nin subclause (III), by inserting or after the semicolon;\n**(bb)**\nin subclause (IV), by striking or and inserting and ; and\n**(cc)**\nby striking subclause (V); and\n**(II)**\nin clause (ii)\u2014\n**(aa)**\nin the matter preceding subclause (I), by striking 2 and inserting 1 ;\n**(bb)**\nin subclause (IV), by inserting and after the semicolon;\n**(cc)**\nin subclause (V), by striking ; and and inserting a period at the end; and\n**(dd)**\nby striking subclause (VI); and\n**(iii)**\nby adding at the end the following:\n(C) Ports in rural areas priority (i) Definition of port In this subparagraph, the term port means\u2014 (I) any port on the navigable waters of the United States, including territories; (II) any harbor, marine terminal, or other shore side facility used principally for the movement of goods on inland waters; and (III) any port formed in accordance with applicable State or territory law. (ii) Priority In addition to the priority given under subparagraph (B), the Secretary shall give equal priority to an application for a project that would increase the availability of broadband service in a port in a rural area. (D) Identification of unserved communities (i) In general In the case of an application given the highest priority under subparagraph (A)(i), the Secretary shall confirm that each unserved rural community identified in the application is eligible for funding by\u2014 (I) conferring with and obtaining data from the Chair of the Federal Communications Commission and the Administrator of the National Telecommunications and Information Administration with respect to the service area proposed in the application; (II) reviewing any other source that is relevant to service data validation, as determined by the Secretary; and (III) performing site-specific testing to verify the unavailability of any residential broadband service in the unserved rural community. (ii) Adjustments Not less often than once every 2 years, the Secretary shall review, and may adjust through notice published in the Federal Register, the unserved communities identified under clause (i). ; and\n**(B)**\nin paragraph (3), by striking subparagraphs (C) and (D) and inserting the following:\n(C) Maximum Except as provided in subparagraph (D), the amount of any grant made under this section shall not exceed 50 percent of the development costs of the project for which the grant is provided. (D) Secretarial authority to adjust The Secretary may make grants of up to 75 percent of the development costs of the project for which the grant is provided to an eligible entity if the Secretary determines that the project serves\u2014 (i) an area of rural households described in paragraph (2)(A)(ii); and (ii) a rural community described in any of subclauses (I) through (IV) of paragraph (2)(B)(i). ;\n**(2)**\nin subsection (d)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (B), by striking subsection (j) and inserting subsection (l) ; and\n**(ii)**\nby adding at the end the following:\n(C) Relation to universal service high-cost support The Secretary shall communicate with the Federal Communications Commission to ensure that any grants, loans, or loan guarantees made under this section provide a level of service that is not less than the level of service provided through universal service high-cost support (as defined in section 54.5 of title 47, Code of Federal Regulations, or any successor regulation) provided by the Commission. ;\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (A)\u2014\n**(I)**\nin clause (i), by striking 50 and inserting 90 ; and\n**(II)**\nin clause (ii), by striking 3 and inserting 2 ; and\n**(C)**\nby adding at the end the following:\n(6) Application process The Secretary shall provide to an applicant of a grant, loan, or loan guarantee under this section feedback and decisions on funding in a timely manner. ;\n**(3)**\nby redesignating subsections (j) and (k) as subsections (l) and (m), respectively;\n**(4)**\nby inserting after subsection (i) the following:\n(j) Broadband buildout data As a condition of receiving a grant, loan, or loan guarantee under this section, a recipient of assistance shall provide to the Secretary complete, reliable, and precise geolocation information that indicates the location of new broadband service that is being provided or upgraded within the service territory supported by the grant, loan, or loan guarantee not later than 30 days after the earlier of\u2014 (1) the date of completion of any project milestone established by the Secretary; or (2) the date of completion of the project. (k) Environmental reviews The Secretary may obligate, but not disperse, funds under this Act before the completion of otherwise required environmental, historical, or other types of reviews if the Secretary determines that a subsequent site-specific review shall be adequate and easily accomplished for the location of towers, poles, or other broadband facilities in the service area of the borrower without compromising the project or the required reviews. ; and\n**(5)**\nin subsection (l)(2)(A) (as so redesignated)\u2014\n**(A)**\nin clause (i), by striking and at the end;\n**(B)**\nin clause (ii), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(iii) set aside at least 1 percent to be used for\u2014 (I) conducting oversight under this section; and (II) implementing accountability measures and related activities authorized under this section. .",
      "versionDate": "2025-03-04",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-03-19T15:05:46Z"
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
      "date": "2025-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1838ih.xml"
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
      "title": "Broadband Internet for Small Ports Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-19T09:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Broadband Internet for Small Ports Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-19T09:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Rural Electrification Act of 1936 to improve access to broadband telecommunications services in rural areas, including by encouraging the provision of broadband loans and grants to increase broadband service in rural ports, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-19T09:48:28Z"
    }
  ]
}
```
