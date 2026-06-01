# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2703?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2703
- Title: Advancing GETs Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2703
- Origin chamber: House
- Introduced date: 2025-04-08
- Update date: 2026-05-08T08:06:53Z
- Update date including text: 2026-05-08T08:06:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-08: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-04-08: Introduced in House

## Actions

- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-08",
    "latestAction": {
      "actionDate": "2025-04-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2703",
    "number": "2703",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "C001066",
        "district": "14",
        "firstName": "Kathy",
        "fullName": "Rep. Castor, Kathy [D-FL-14]",
        "lastName": "Castor",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Advancing GETs Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-08T08:06:53Z",
    "updateDateIncludingText": "2026-05-08T08:06:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-08",
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
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-08",
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
          "date": "2025-04-08T14:03:00Z",
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
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "NY"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "CA"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "IL"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "WA"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "CA"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "CA"
    },
    {
      "bioguideId": "A000148",
      "district": "4",
      "firstName": "Jake",
      "fullName": "Rep. Auchincloss, Jake [D-MA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Auchincloss",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "MA"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "IL"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "TN"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2703ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2703\nIN THE HOUSE OF REPRESENTATIVES\nApril 8, 2025 Ms. Castor of Florida (for herself, Mr. Tonko , Mr. Peters , Mr. Casten , Ms. Schrier , Mr. Mullin , and Mr. Huffman ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require the Federal Energy Regulatory Commission to establish a shared savings incentive to return a portion of the savings attributable to an investment in grid-enhancing technology to the developer of that grid-enhancing technology, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Advancing Grid-Enhancing Technologies Act of 2025 or the Advancing GETs Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Commission**\nThe term Commission means the Federal Energy Regulatory Commission.\n**(2) Grid-enhancing technology**\nThe term grid-enhancing technology means any hardware or software that\u2014\n**(A)**\nincreases the capacity, efficiency, reliability, resilience, or safety of transmission facilities and transmission technologies; and\n**(B)**\nis installed in addition to transmission facilities and transmission technologies\u2014\n**(i)**\nto give operators of the transmission facilities and transmission technologies more situational awareness and control over the electric grid;\n**(ii)**\nto make the transmission facilities and transmission technologies more efficient; or\n**(iii)**\nto increase the transfer capacity of the transmission facilities and transmission technologies.\n**(3) Secretary**\nThe term Secretary means the Secretary of Energy.\n#### 3. Shared savings incentive for grid-enhancing technologies\n##### (a) Definition of developer\nIn this section, the term developer , with respect to grid-enhancing technology, means the entity that pays to install the grid-enhancing technology.\n##### (b) Establishment of shared savings incentive\nNot later than 18 months after the date of enactment of this Act, the Commission shall promulgate a final rule to implement section 219(b)(3) of the Federal Power Act ( 16 U.S.C. 824s(b)(3) ) by providing a shared savings incentive that returns a portion of the savings attributable to an investment in grid-enhancing technology to the developer of that grid-enhancing technology, in accordance with this section.\n##### (c) Requirements\n**(1) In general**\nThe Commission shall determine the percentage of savings attributable to an investment in grid-enhancing technology that can be returned to the developer of that grid-enhancing technology pursuant to the shared savings incentive established under subsection (b), subject to the conditions that the percentage\u2014\n**(A)**\nis not less than 10 percent and not more than 25 percent;\n**(B)**\nis not determined on a per-project, per-investment, or case-by-case basis; and\n**(C)**\nis applied consistently to all investments in grid-enhancing technology eligible for the shared savings incentive, regardless of the type of grid-enhancing technology installed.\n**(2) Time period for recovery**\nThe shared savings incentive established under subsection (b) shall return a percentage, determined in accordance with paragraph (1), of the applicable savings to the developer of the applicable grid-enhancing technology over a period of 3 years.\n##### (d) Eligibility\nSubject to subsection (e), the shared savings incentive established under subsection (b) shall apply with respect to\u2014\n**(1)**\nany developer, with respect to the investment of that developer in grid-enhancing technology that is installed as described in section 2(2)(B); and\n**(2)**\nany grid-enhancing technology, including\u2014\n**(A)**\ngrid-enhancing technology that relates to new transmission facilities or transmission technologies; and\n**(B)**\ngrid-enhancing technology that relates to existing transmission facilities or transmission technologies.\n##### (e) Limitations\n**(1) Minimum savings**\n**(A) In general**\nThe shared savings incentive established under subsection (b) shall apply with respect to an investment in grid-enhancing technology only if the expected savings attributable to the investment over the 3-year period described in subsection (c)(2), as determined by the Commission, are at least 4 times the cost of the investment.\n**(B) Determination**\n**(i) In general**\nThe Commission shall determine how to quantify the cost of an investment and the expected savings attributable to an investment for purposes of subparagraph (A).\n**(ii) Costs**\nFor purposes of subparagraph (A), the cost of an investment may include any costs associated with the permitting, installation, or purchase of the applicable grid-enhancing technology.\n**(2) Already installed GETs**\nThe shared savings incentive established under subsection (b) may not be applied with respect to grid-enhancing technology that is already installed as of the date of enactment of this Act.\n**(3) Consumer protection**\nThe Commission shall determine appropriate consumer protections for the shared savings incentive established under subsection (b).\n##### (f) Evaluation and sunset of shared savings incentive\n**(1) Evaluation**\nNot earlier than 7 years, and not later than 10 years, after the shared savings incentive is established under subsection (b), the Commission shall\u2014\n**(A)**\nevaluate the necessity and efficacy of the shared savings incentive; and\n**(B)**\ndetermine whether to maintain, revise, or suspend the shared savings incentive.\n**(2) Consideration of Order No. 1920**\nIn conducting the evaluation under paragraph (1)(A), the Commission shall consider\u2014\n**(A)**\nhow the shared savings incentive aligns with the requirement that grid-enhancing technologies be considered in long-term regional transmission planning under Order No. 1920 of the Commission, entitled Building for the Future Through Electric Regional Transmission Planning and Cost Allocation (89 Fed. Reg. 49280 (June 11, 2024)) (or a successor order);\n**(B)**\nwhether and how the shared savings incentive should be revised to further align with that requirement; and\n**(C)**\nwhether, in light of that requirement, the shared savings incentive should be maintained or suspended.\n**(3) Public comment**\nIn conducting the evaluation under paragraph (1)(A), the Commission shall provide an opportunity for public comment, including by stakeholders.\n#### 4. Congestion reporting\n##### (a) Annual reports\n**(1) In general**\nBeginning on the date that is 1 year after the effective date of the rule promulgated under subsection (b), all operators of transmission facilities or transmission technologies shall submit to the Commission annual reports containing data on the costs associated with congestion management with respect to the transmission facilities or transmission technologies, including all relevant constraints.\n**(2) Requirement**\nEach annual report submitted under paragraph (1) shall identify\u2014\n**(A)**\nwith respect to each reported constraint that caused more than $500,000 in associated costs\u2014\n**(i)**\nthe cause of the constraint, including physical infrastructure and transient disruptions; and\n**(ii)**\nthe next limiting element type and its identified rating limit; and\n**(B)**\neach constraint that will be addressed by planned future upgrades to infrastructure and facilities.\n##### (b) Rulemaking\nNot later than 18 months after the date of enactment of this Act, the Commission shall promulgate a final rule establishing a universal metric and protocol for the measuring and reporting of data under subsection (a).\n##### (c) Uses of data\n**(1) Analyses**\n**(A) In general**\nThe Commission and the Secretary shall each use the data submitted under subsection (a) to conduct analyses, as the Commission or the Secretary, as applicable, determines to be appropriate.\n**(B) Coordination**\nThe Commission and the Secretary may coordinate with respect to any analyses conducted using the data submitted under subsection (a).\n**(2) Map**\nThe Commission and the Secretary, acting jointly, shall\u2014\n**(A)**\nuse the data submitted under subsection (a) to create a map of costs associated with congestion management in the transmission system; and\n**(B)**\nupdate that map not less frequently than once each year.\n##### (d) Publication of data and map\nThe Commission and the Secretary shall make the data submitted under subsection (a) and the map described in subsection (c)(2) publicly available on the websites of\u2014\n**(1)**\nthe Commission; and\n**(2)**\nthe Department of Energy.\n#### 5. Grid-enhancing technology application guide\n##### (a) Definition of developer\nIn this section, the term developer means a developer of transmission facilities or transmission technologies, including a developer of transmission facilities or transmission technologies that pays to install grid-enhancing technology with respect to those transmission facilities or transmission technologies.\n##### (b) Establishment of application guide\nNot later than 18 months after the date of enactment of this Act, the Secretary shall establish an application guide for utilities and developers seeking to implement grid-enhancing technologies.\n##### (c) Updates\nThe guide established under subsection (b) shall be reviewed and updated annually.\n##### (d) Technical assistance\n**(1) In general**\nOn request of a utility or developer using the guide established under subsection (b), the Secretary shall provide technical assistance to that utility or developer with respect to the use of grid-enhancing technologies for particular applications.\n**(2) Clearinghouse**\nIn carrying out paragraph (1), the Secretary shall establish a clearinghouse of previously completed grid-enhancing technology projects that the Secretary, utilities, and developers may use to identify issues and solutions relating to the use of grid-enhancing technologies for particular applications.\n##### (e) Authorization of appropriations\nThere are authorized to be appropriated to carry out this section, to remain available until expended\u2014\n**(1)**\n$5,000,000 for fiscal year 2025; and\n**(2)**\n$1,000,000 for each of fiscal years 2026 through 2036.",
      "versionDate": "2025-04-08",
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
        "actionDate": "2026-04-15",
        "text": "Committee on Energy and Natural Resources Subcommittee on Energy. Hearings held."
      },
      "number": "1327",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Advancing GETs Act of 2025",
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
            "name": "Advanced technology and technological innovations",
            "updateDate": "2026-04-16T14:49:51Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-04-16T14:49:51Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-16T14:49:51Z"
          },
          {
            "name": "Electric power generation and transmission",
            "updateDate": "2026-04-16T14:49:51Z"
          },
          {
            "name": "Energy efficiency and conservation",
            "updateDate": "2026-04-16T14:49:51Z"
          },
          {
            "name": "Energy prices",
            "updateDate": "2026-04-16T14:49:51Z"
          },
          {
            "name": "Energy revenues and royalties",
            "updateDate": "2026-04-16T14:49:51Z"
          },
          {
            "name": "Energy storage, supplies, demand",
            "updateDate": "2026-04-16T14:49:51Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-04-16T14:49:51Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-04-16T14:49:51Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-05-05T12:11:37Z"
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
      "date": "2025-04-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2703ih.xml"
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
      "title": "Advancing GETs Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-16T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Advancing GETs Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-16T04:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Advancing Grid-Enhancing Technologies Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-16T04:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Federal Energy Regulatory Commission to establish a shared savings incentive to return a portion of the savings attributable to an investment in grid-enhancing technology to the developer of that grid-enhancing technology, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-16T04:48:25Z"
    }
  ]
}
```
