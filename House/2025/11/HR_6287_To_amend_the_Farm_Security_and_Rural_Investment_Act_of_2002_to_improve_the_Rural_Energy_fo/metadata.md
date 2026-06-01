# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6287?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6287
- Title: REAP Modernization Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6287
- Origin chamber: House
- Introduced date: 2025-11-21
- Update date: 2026-05-16T08:07:35Z
- Update date including text: 2026-05-16T08:07:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-21: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.
- Latest action: 2025-11-21: Introduced in House

## Actions

- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-21",
    "latestAction": {
      "actionDate": "2025-11-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6287",
    "number": "6287",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "V000138",
        "district": "7",
        "firstName": "Eugene",
        "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
        "lastName": "Vindman",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "REAP Modernization Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:35Z",
    "updateDateIncludingText": "2026-05-16T08:07:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-13",
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
      "actionDate": "2025-11-21",
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
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-21",
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
          "date": "2025-11-21T14:01:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-13T20:01:01Z",
              "name": "Referred to"
            }
          },
          "name": "Commodity Markets, Digital Assets, and Rural Development Subcommittee",
          "systemCode": "hsag22"
        }
      },
      "systemCode": "hsag00",
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
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-11-21",
      "state": "CA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-01-06",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6287ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6287\nIN THE HOUSE OF REPRESENTATIVES\nNovember 21, 2025 Mr. Vindman (for himself and Mr. Valadao ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Farm Security and Rural Investment Act of 2002 to improve the Rural Energy for America Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rural Energy for America Program Modernization Act of 2025 or the REAP Modernization Act of 2025 .\n#### 2. Rural Energy for America Program\n##### (a) In general\nSection 9007 of the Farm Security and Rural Investment Act of 2002 ( 7 U.S.C. 8107 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby redesignating paragraphs (1) and (2) as subparagraphs (A) and (B), respectively, and indenting appropriately;\n**(B)**\nin the matter preceding subparagraph (A) (as so redesignated), by striking The Secretary and inserting the following:\n(1) In general The Secretary ;\n**(C)**\nin paragraph (1) (as so designated), in the matter preceding subparagraph (A) (as so redesignated), by inserting (referred to in this section as the Program ) after Program ; and\n**(D)**\nby adding at the end the following:\n(2) Climate benefits In carrying out the Program, the Secretary shall promote the reduction of greenhouse gas emissions as a result of carrying out projects funded by grants and other financial assistance under the Program. ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (D), by striking and at the end;\n**(ii)**\nby redesignating subparagraph (E) as subparagraph (G); and\n**(iii)**\nby inserting after subparagraph (D) the following:\n(E) a producer cooperative; (F) a nongovernmental organization; and ;\n**(B)**\nin paragraph (3)\u2014\n**(i)**\nin subparagraph (E), by striking and at the end;\n**(ii)**\nin subparagraph (F), by striking the period at the end and inserting ; and ; and\n**(iii)**\nby adding at the end the following:\n(G) the potential of the proposed program to reduce greenhouse gas emissions and provide other climate benefits. ; and\n**(C)**\nin paragraph (4)\u2014\n**(i)**\nin subparagraph (B), by redesignating clauses (i) and (ii) as subclauses (I) and (II), respectively, and indenting appropriately;\n**(ii)**\nby redesignating subparagraphs (A) and (B) as clauses (i) and (ii), respectively, and indenting appropriately;\n**(iii)**\nin the matter preceding clause (i) (as so redesignated), by striking A recipient and inserting the following:\n(A) In general A recipient ; and\n**(iv)**\nby adding at the end the following:\n(B) Grant options A grant awarded under paragraph (1) may be used to carry out 1 or more of the activities described in subparagraph (A). ;\n**(3)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (1)(A), by adding after and below the end the following:\nThe Secretary may, on a limited case-by-case basis, provide financial assistance described in this subparagraph to agricultural producer cooperatives and rural electric cooperatives that do not otherwise qualify for the assistance. ;\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (F), by striking and at the end;\n**(ii)**\nby redesignating subparagraph (G) as subparagraph (H); and\n**(iii)**\nby inserting after subparagraph (F) the following:\n(G) the potential of the renewable energy system to reduce greenhouse gas emissions and result in other climate benefits; and ; and\n**(C)**\nin paragraph (3)(A), by striking 25 percent and inserting 50 percent ;\n**(4)**\nby redesignating subsections (d), (e), and (f) as subsections (e), (f), and (i), respectively;\n**(5)**\nby inserting after subsection (c) the following:\n(d) Streamlined application process The Secretary shall develop a streamlined application process, including within each tier described in subsection (c)(4), under which an entity may apply for a grant under subsection (b), financial assistance under subsection (c), or a bundled application for a project with components eligible under clauses (i) and (ii) of subsection (c)(1)(A). ;\n**(6)**\nin subsection (e) (as so redesignated)\u2014\n**(A)**\nin the subsection heading, by striking Outreach and inserting Outreach, technical assistance, and education ;\n**(B)**\nby striking that adequate and inserting the following:\nthat\u2014 (1) adequate ;\n**(C)**\nin paragraph (1) (as so designated), by striking the period at the end and inserting a semicolon; and\n**(D)**\nby adding at the end the following:\n(2) technical assistance is provided to entities seeking to apply for a grant or financial assistance under the Program; and (3) outreach, technical assistance, and education is provided to recipients of grants and other financial assistance under the Program relating to integrating renewable energy projects on land shared with crops or livestock. ;\n**(7)**\nin subsection (f) (as so redesignated), in paragraph (1), by striking $20,000 and inserting $50,000 ;\n**(8)**\nby inserting after subsection (f) (as so redesignated) the following:\n(g) Study (1) Definition of dual-use energy system In this subsection, the term dual-use energy system means a system under which renewable energy production and agricultural production, including crop or animal production, occur together on the same piece of land. (2) Study The Secretary shall carry out a study on dual-use energy systems. (3) Report Not later than 2 years after the date of enactment of the REAP Modernization Act of 2025 , the Secretary shall submit to Congress, and make publicly available online, a report on the results of the study carried out under paragraph (2), which shall include a recommendation as to whether the scope of grants and other financial assistance under the Program should be expanded to cover projects that generate more energy without significantly impacting farm operations or leading to the conversion of existing farm land. (h) Energy generated In the case of a project funded by a grant or other financial assistance provided under the Program that takes place on a property on which a residence is closely associated with and shares an energy metering device with an agricultural operation or rural small business to be served by the project, there shall not be any requirement imposed relating to the quantity of energy generated by the project that must be used by the agricultural operation or rural small business. ; and\n**(9)**\nin subsection (i) (as so redesignated), by adding at the end the following:\n(4) Outreach, technical assistance, and education Of the funds made available to carry out this section for a fiscal year, the Secretary shall use not more than 8 percent to carry out subsection (e). (5) Reserve fund (A) In general There is established a reserve fund (referred to in this paragraph as the reserve fund ), into which, each fiscal year, not less than 15 percent of the funds made available under paragraphs (1) and (3) to carry out this section for that fiscal year shall be transferred. (B) Use of reserve fund After all other funds for the Program are obligated for a fiscal year, the Secretary may use amounts in the reserve fund to provide grants and other financial assistance under the Program for projects using underutilized renewable energy technologies. (C) Unused funds If there are remaining funds in the reserve fund at the end of a fiscal year, the Secretary shall use those remaining funds to provide grants and other financial assistance under the Program without regard to whether the grants or financial assistance relate to underutilized renewable energy technologies. .\n##### (b) Conforming amendments\nSection 9007 of the Farm Security and Rural Investment Act of 2002 ( 7 U.S.C. 8107 ) is amended by striking subsection (f) each place it appears and inserting subsection (i) .",
      "versionDate": "2025-11-21",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-12-19T18:10:01Z"
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
      "date": "2025-11-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6287ih.xml"
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
      "title": "REAP Modernization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-18T05:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "REAP Modernization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-18T05:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rural Energy for America Program Modernization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-18T05:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Farm Security and Rural Investment Act of 2002 to improve the Rural Energy for America Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-18T05:18:14Z"
    }
  ]
}
```
