# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3976?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3976
- Title: Connect the Grid Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3976
- Origin chamber: Senate
- Introduced date: 2026-03-03
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-03: Introduced in Senate
- 2026-03-03 - IntroReferral: Introduced in Senate
- 2026-03-03 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2026-03-03: Introduced in Senate

## Actions

- 2026-03-03 - IntroReferral: Introduced in Senate
- 2026-03-03 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3976",
    "number": "3976",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Connect the Grid Act of 2026",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-03",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-03",
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
        "item": {
          "date": "2026-03-03T22:34:09Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3976is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3976\nIN THE SENATE OF THE UNITED STATES\nMarch 3, 2026 Mr. Markey (for himself and Mr. Merkley ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo interconnect the Electric Reliability Council of Texas to its neighbors, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Connect the Grid Act of 2026 .\n#### 2. Definitions\nIn this Act:\n**(1) Abandoned mine land**\nThe term abandoned mine land means land, water, or a watershed that is contaminated or scarred by extraction, beneficiation, or processing of ores or minerals (which may include phosphate, but does not include coal).\n**(2) Brownfield site**\nThe term brownfield site has the meaning given the term in section 101 of the Comprehensive Environmental Response, Compensation, and Liability Act of 1980 ( 42 U.S.C. 9601 ).\n**(3) Commission**\nThe term Commission means the Federal Energy Regulatory Commission.\n**(4) Electric Reliability Organization**\nThe term Electric Reliability Organization has the meaning given the term in section 215(a) of the Federal Power Act ( 16 U.S.C. 824o(a) ).\n**(5) Environmental justice community**\nThe term environmental justice community means a community with significant representation of communities of color, low-income communities, or Tribal and Indigenous communities that experiences, or is at risk of experiencing, higher or more adverse human health or environmental effects.\n**(6) ERCOT**\nThe term ERCOT means the Electric Reliability Council of Texas.\n**(7) Grid-enhancing technology**\nThe term grid-enhancing technology means a solution that increases the transfer capability of high-voltage transmission facilities.\n**(8) MISO**\nThe term MISO means the Midcontinent Independent System Operator transmission organization.\n**(9) National Priorities List**\nThe term National Priorities List means the National Priorities List developed by the President in accordance with section 105(a)(8)(B) of the Comprehensive Environmental Response, Compensation, and Liability Act of 1980 ( 42 U.S.C. 9605(a)(8)(B) ).\n**(10) Registered apprenticeship program**\nThe term registered apprenticeship program means an apprenticeship program registered under the Act of August 16, 1937 (commonly known as the National Apprenticeship Act ; 50 Stat. 664, chapter 663; 29 U.S.C. 50 et seq. ), that meets the standards of subpart A of part 29, and part 30, of title 29, Code of Federal Regulations (or successor regulations).\n**(11) Reliability standard**\nThe term reliability standard has the meaning given the term in section 215(a) of the Federal Power Act ( 16 U.S.C. 824o(a) ).\n**(12) SPP**\nThe term SPP means the Southwest Power Pool transmission organization.\n**(13) Total transfer capability**\nThe term total transfer capability has the meaning given the term in section 37.6(b)(1)(vi) of title 18, Code of Federal Regulations (as in effect on the date of enactment of this Act).\n**(14) Transmission facility**\nThe term transmission facility means a facility that is used for the transmission of electric energy in interstate commerce, including a transmission line.\n**(15) Transmission organization**\nThe term transmission organization has the meaning given the term in section 215(a) of the Federal Power Act ( 16 U.S.C. 824o(a) ).\n**(16) Tribal and Indigenous community**\nThe term Tribal and Indigenous community means a population of people who are members of\u2014\n**(A)**\na federally recognized Indian Tribe;\n**(B)**\na State-recognized Indian Tribe;\n**(C)**\nan Alaska Native or Native Hawaiian community or organization; or\n**(D)**\nany other community of Indigenous people located in a State.\n**(17) Tribal government**\nThe term Tribal government means the governing body of an Indian Tribe.\n**(18) Western Interconnection**\nThe term Western Interconnection means the synchronously operated electric transmission grid located in the western part of North America, including parts of Montana, Nebraska, New Mexico, South Dakota, Texas, Wyoming, and Mexico, and all of Arizona, California, Colorado, Idaho, Nevada, Oregon, Utah, Washington, and the Canadian Provinces of British Columbia and Alberta.\n#### 3. Jurisdiction with respect to ERCOT\n##### (a) Application of part II of the Federal Power Act\nSection 201(b)(2) of the Federal Power Act ( 16 U.S.C. 824(b)(2) ) is amended\u2014\n**(1)**\nin the first sentence, by striking section 201(f) and inserting subsection (f) ; and\n**(2)**\nin the second sentence\u2014\n**(A)**\nby striking 210, 211, 211A, 212, ; and\n**(B)**\nby striking an electric utility or other entity and inserting any entity that is otherwise exempt under subsection (f) .\n##### (b) Definition of public utility\nSection 201(e) of the Federal Power Act ( 16 U.S.C. 824(e) ) is amended by striking 210, 211, 211A, 212, .\n##### (c) Repeal of ERCOT Exemptions\n**(1)**\nSection 212 of the Federal Power Act ( 16 U.S.C. 824k ) is amended by striking subsection (k).\n**(2)**\nSection 216 of the Federal Power Act ( 16 U.S.C. 824p ) is amended by striking subsection (k).\n**(3)**\nSection 217 of the Federal Power Act ( 16 U.S.C. 824q ) is amended\u2014\n**(A)**\nby striking subsection (h); and\n**(B)**\nby redesignating subsections (i) through (k) as subsections (h) through (j), respectively.\n**(4)**\nSection 220 of the Federal Power Act ( 16 U.S.C. 824t ) is amended by striking subsection (f).\n##### (d) Technical conference\nNot later than 180 days after the date of enactment of this Act, the Commission shall convene a technical conference to assist entities affected by the amendments made by this section with compliance with any requirements made applicable to those entities pursuant to those amendments, including by publishing the steps necessary for such compliance.\n#### 4. Electric reliability\n##### (a) Amendments\nSection 215 of the Federal Power Act ( 16 U.S.C. 824o ) is amended\u2014\n**(1)**\nin subsection (a)(3), in the second sentence, by striking enlarge such facilities or to construct new transmission capacity or generation capacity and inserting construct new generation capacity ; and\n**(2)**\nin subsection (i)(2), by striking or transmission .\n##### (b) Reliability standard for total transfer capability\n**(1) In general**\nNot later than 30 days after the date of enactment of this Act, the Commission shall order the Electric Reliability Organization to submit to the Commission a proposed reliability standard that requires minimum total transfer capability of\u2014\n**(A)**\nbetween 4.3 and 12.6 gigawatts between the area under functional control of ERCOT and the area under functional control of SPP;\n**(B)**\nbetween 2.5 and 16.2 gigawatts between the area under functional control of ERCOT and the area under functional control of MISO; and\n**(C)**\nbetween 2.6 and 7.9 gigawatts between the area under functional control of ERCOT and the Western Interconnection.\n**(2) Contents**\nThe Commission may only approve a proposed reliability standard described in paragraph (1) if that reliability standard\u2014\n**(A)**\nrequires minimum total transfer capability as described in paragraph (1); and\n**(B)**\nrequires each of ERCOT and SPP, ERCOT and MISO, and ERCOT and 1 or more neighboring balancing authorities in the Western Interconnection (as determined by the Electric Reliability Organization) to jointly submit, not later than 1 year after the date of enactment of this Act, a plan that\u2014\n**(i)**\ndesignates 1 or more entities to site and construct new transmission facilities, or modify existing transmission facilities, to achieve the applicable minimum total transfer capability; and\n**(ii)**\nincludes a timeline for that siting and construction or modification, which timeline shall include that such siting and construction or modification be completed by January 1, 2035.\n**(3) Priority**\nAny plan for the siting and construction or modification of transmission facilities described in paragraph (2)(B) shall prioritize\u2014\n**(A)**\nthe use of grid-enhancing technologies;\n**(B)**\nthe use of existing rights-of-ways, such as highways and railroads, to site and construct new transmission facilities;\n**(C)**\nthe siting and construction of new transmission facilities on degraded land, including sites on the National Priorities List, brownfield sites, landfills, abandoned mine land, and contaminated or abandoned agricultural land;\n**(D)**\nthe siting and construction of new transmission facilities in a manner that expands access to renewable energy sources, including wind, solar, and geothermal sources;\n**(E)**\nproviding meaningful community involvement opportunities, including by conducting outreach to\u2014\n**(i)**\nenvironmental justice communities, including by conducting planning meetings, set at times and places to maximize the number of community members who can conveniently attend, with appropriate services, including translation and interpreting services and virtual attendance, in those environmental justice communities;\n**(ii)**\nTribal and Indigenous communities;\n**(iii)**\nTribal governments; and\n**(iv)**\nrelevant labor organizations; and\n**(F)**\nthe use of registered apprenticeship programs and prevailing wages, as determined by the Secretary of Labor in accordance with subchapter IV of chapter 31 of title 40, United States Code.\n**(4) Environmental review**\nAny project to site, construct, or modify transmission facilities that is conducted to comply with the reliability standard described in paragraph (1) shall be subject to the requirements of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ) and the Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. ).\n**(5) Savings provision**\nNothing in this subsection overrides or inhibits the authority of the Commission to require minimum interregional transfer between regions in a pair or grouping of regions other than a pair or grouping of regions described in subparagraph (A), (B), or (C) of paragraph (1).\n##### (c) Consideration for national interest electric transmission corridors\nIn carrying out section 216 of the Federal Power Act ( 16 U.S.C. 824p ), the Secretary of Energy shall consider designating as a national interest electric transmission corridor any area in which transmission facilities will be sited and constructed or modified pursuant to this section.\n#### 5. Increased borrowing authority under the Transmission Facilitation Program\nSection 40106(d)(2) of the Infrastructure Investment and Jobs Act ( 42 U.S.C. 18713(d)(2) ) is amended by striking $2,500,000,000 and inserting $13,500,000,000 .\n#### 6. Study and report on benefits of interconnection with Mexico\n##### (a) Definition of covered facility\nIn this section, the term covered facility means a facility for the generation, transmission, or sale of electric energy.\n##### (b) Study and report\nNot later than 1 year after the date of enactment of this Act, the Secretary of Energy shall conduct a study and submit to Congress a report on\u2014\n**(1)**\nthe reliability, climate, and cost benefits of the interconnection of covered facilities in the United States with covered facilities in Mexico; and\n**(2)**\nthe siting and construction, or modification, of covered facilities that will bring the most cumulative benefits.",
      "versionDate": "2026-03-03",
      "versionType": "Introduced in Senate"
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
        "name": "Energy",
        "updateDate": "2026-03-23T20:27:40Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3976is.xml"
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
      "title": "Connect the Grid Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T03:23:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Connect the Grid Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-19T03:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to interconnect the Electric Reliability Council of Texas to its neighbors, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-19T03:18:45Z"
    }
  ]
}
```
