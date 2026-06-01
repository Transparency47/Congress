# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7761?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7761
- Title: Heirs Education and Investment to Resolve Succession of Property Act
- Congress: 119
- Bill type: HR
- Bill number: 7761
- Origin chamber: House
- Introduced date: 2026-03-03
- Update date: 2026-03-19T19:42:49Z
- Update date including text: 2026-03-19T19:42:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-03: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2026-03-03: Introduced in House

## Actions

- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-03",
    "latestAction": {
      "actionDate": "2026-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7761",
    "number": "7761",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "B000490",
        "district": "2",
        "firstName": "Sanford",
        "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
        "lastName": "Bishop",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Heirs Education and Investment to Resolve Succession of Property Act",
    "type": "HR",
    "updateDate": "2026-03-19T19:42:49Z",
    "updateDateIncludingText": "2026-03-19T19:42:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-03",
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
      "actionDate": "2026-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-03",
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
          "date": "2026-03-03T17:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
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
      "bioguideId": "S001189",
      "district": "8",
      "firstName": "Austin",
      "fullName": "Rep. Scott, Austin [R-GA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "GA"
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
      "sponsorshipDate": "2026-03-03",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7761ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7761\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2026 Mr. Bishop (for himself, Mr. Austin Scott of Georgia , and Mr. Davis of North Carolina ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo reauthorize and improve the relending program to resolve ownership and succession on farmland, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Heirs Education and Investment to Resolve Succession of Property Act .\n#### 2. Reauthorization of the heirs property intermediary relending program\nSection 310I(g) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1936c(g) ) is amended by striking 2023 and inserting 2031 .\n#### 3. Cooperative agreements for heirs property resolution through direct public interest legal services\nSection 310I of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1936c ) is amended\u2014\n**(1)**\nby redesignating subsections (f) and (g) as subsections (g) and (h), respectively; and\n**(2)**\nby inserting after subsection (e) the following:\n(f) Cooperative agreements for heirs property resolution through direct public interest legal services (1) In general The Secretary shall enter into cooperative agreements with eligible entities to provide legal or accounting services to underserved heirs, at no cost to the underserved heirs, to assist in resolving issues related to ownership and succession on farmland or forest land that has multiple owners. Such a cooperative agreement must be for any of the following purposes: (A) To assist with transitioning land to agricultural production. (B) To maintain land in agricultural production. (C) To increase access to programs administered by the Secretary through the resolution of real property claims in order to allow real property owners to meet land ownership eligibility requirements for participation in a program administered by the Secretary. (2) Administration of cooperative agreements (A) Duration (i) In general A cooperative agreement under paragraph (1) shall be in effect for not more than 4 years, subject to clause (ii). (ii) Special rule The Secretary may re-enter into a cooperative agreement with the same or a different eligible entity to provide continued services for heirs if property ownership is not resolved within the initial term of the original cooperative agreement, and the entity certifies that the entity understands that the cooperative agreement is not guaranteed to be funded for more than 4 years after the commencement of the original cooperative agreement. (B) Management of performance (i) Annual reports An eligible entity must provide annual reports to the Secretary summarizing the progress made during each fiscal year towards achieving the goals of the cooperative agreement for the heirs for whom services are provided under the cooperative agreement. (ii) Information and data The Secretary may require an eligible entity to provide the Secretary with such information or data, other than personally identifiable information or data, as the Secretary deems necessary to determine that the eligible entity is making acceptable progress. (iii) Effect of failure to demonstrate success If an eligible entity providing services under such a cooperative agreement does not demonstrate success, as determined by the Secretary, in resolving or reasonably attempting to resolve the property claims of an heir, the Secretary may terminate the agreement, or elect to not enter into a new cooperative agreement with the eligible entity after the initial term of the original cooperative agreement. (C) Implementation The Secretary may utilize requests for public input or the formal rulemaking process to effectuate this subsection. At a minimum, the Secretary shall make publicly available the criteria for selecting an eligible entity to enter into an agreement to provide services, the administrative and performance requirements for cooperative agreements under this subsection, as well as codify within its internal policy its implementation process. (D) Heirs property not in farming On a limited basis, and when determined by the Secretary to meet the purposes of a program administered by the Secretary and to expand access to such a program, the Secretary may allow an eligible entity to provide services at no cost to an heir who is not an underserved heir if\u2014 (i) the land with respect to which the services are to be provided is not farmland or in agricultural production, but could be viably productive for agricultural, conservation, or forestry purposes; (ii) the heir satisfies all other requirements of the definition of underserved heir ; (iii) the heir can provide proof to substantiate that the heir is in control of the real property; and (iv) the heir certifies to the Secretary that the heir intends to apply for, and make a good faith effort to enroll the land in, a program administered by the Secretary once property claims to the land are resolved through services provided under a cooperative agreement entered into under this subsection. (3) Definitions In this subsection: (A) Eligible entity The term eligible entity means a nonprofit organization that\u2014 (i) provides legal or accounting services to an underserved heir at no cost to the underserved heir; and (ii) has demonstrated experience in resolving issues related to ownership and succession on farmland or forest land that has multiple owners. (B) Limited resource heir An heir shall be considered a limited resource heir for purposes of this subsection if\u2014 (i) the total household income of the heir is at or below the national poverty level for a family of 4, or less than 50 percent of the county median household income for the 2 immediately preceding calendar years, as determined annually using data of the Department of Commerce; or (ii) the property of the heir for which legal services are provided pursuant to a cooperative agreement entered into under this subsection is in a persistent poverty community, as determined annually on the basis of data from the Department of Commerce, or a socially vulnerable area, as designated by the Centers on Disease Control and Prevention. (C) Underserved heir The term underserved heir means an heir with an undivided ownership interest in farmland that has multiple owners, who is\u2014 (i) a limited resource heir; (ii) a member of a socially disadvantaged group (as defined in section 2501(a) of the Food, Agriculture, Conservation, and Trade Act of 1990); or (iii) a veteran (as defined in section 101(2) of title 38, United States Code). (4) Annual reports to Congress Within 1 year after the date of the enactment of this subsection, and annually thereafter, the Secretary shall prepare, make public, and submit to the Committee on Agriculture of the House of Representatives and the Committee on Agriculture, Nutrition, and Forestry of the Senate a written report on the activities carried out under this subsection in the year covered by the report. (5) Limitations on authorization of appropriations (A) In general To carry out this subsection, there is authorized to be appropriated to the Secretary $60,000,000 for each of fiscal years 2027 through 2031. (B) Limitation on use of funds for administration The Secretary may expend for administrative purposes not more than 3 percent of the amounts made available under subparagraph (A). .\n#### 4. Annual report on operations and outcomes under the relending program to resolve ownership and succession on farmland\nSection 310I(g) of the Consolidated Farm and Rural Development Act, as so redesignated by section 3 of this Act, is amended by striking Not later than 1 year after the date of enactment of this section, the Secretary shall and inserting The Secretary shall annually .\n#### 5. Reports on land access and farmland ownership data collection\nSection 12607(c) of the Agriculture Improvement Act of 2018 ( 7 U.S.C. 2204i(c) ) is amended by striking 2023 and inserting 2031 .",
      "versionDate": "2026-03-03",
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
        "updateDate": "2026-03-19T19:42:49Z"
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
      "date": "2026-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7761ih.xml"
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
      "title": "Heirs Education and Investment to Resolve Succession of Property Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-18T08:08:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Heirs Education and Investment to Resolve Succession of Property Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-18T08:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To reauthorize and improve the relending program to resolve ownership and succession on farmland, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-18T08:03:28Z"
    }
  ]
}
```
