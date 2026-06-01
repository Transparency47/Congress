# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4193?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4193
- Title: Wildfire and Grid Reliability Act
- Congress: 119
- Bill type: S
- Bill number: 4193
- Origin chamber: Senate
- Introduced date: 2026-03-25
- Update date: 2026-04-09T14:07:46Z
- Update date including text: 2026-04-09T14:07:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-25: Introduced in Senate
- 2026-03-25 - IntroReferral: Introduced in Senate
- 2026-03-25 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2026-03-25: Introduced in Senate

## Actions

- 2026-03-25 - IntroReferral: Introduced in Senate
- 2026-03-25 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-25",
    "latestAction": {
      "actionDate": "2026-03-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4193",
    "number": "4193",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "W000779",
        "district": "",
        "firstName": "Ron",
        "fullName": "Sen. Wyden, Ron [D-OR]",
        "lastName": "Wyden",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Wildfire and Grid Reliability Act",
    "type": "S",
    "updateDate": "2026-04-09T14:07:46Z",
    "updateDateIncludingText": "2026-04-09T14:07:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-25",
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
      "actionDate": "2026-03-25",
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
          "date": "2026-03-25T17:21:09Z",
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
      "sponsorshipDate": "2026-03-25",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4193is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4193\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2026 Mr. Wyden (for himself and Mr. Merkley ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo require the Secretary of Energy to establish a grant program to improve the reliability of the power grid and reduce the risk of wildfires caused by power lines, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Wildfire and Grid Reliability Act .\n#### 2. Wildfire and grid reliability program\n##### (a) Definitions\nIn this section:\n**(1) Eligible entity**\nThe term eligible entity means an electric utility, including\u2014\n**(A)**\na publicly owned electric utility;\n**(B)**\na municipal electric utility;\n**(C)**\na cooperatively owned electric utility;\n**(D)**\nan investor-owned electric utility; and\n**(E)**\na Federal agency or federally owned corporation that is an electric utility (as defined in section 3 of the Federal Power Act ( 16 U.S.C. 796 )).\n**(2) Power line**\nThe term power line includes a transmission line or a distribution line, as applicable.\n**(3) Program**\nThe term program means the program established under subsection (b).\n**(4) Reliability**\nThe term reliability , with respect to the power grid, includes the ability to withstand natural disasters, such as earthquakes, ice storms, wind storms, snow storms, heat storms, and other natural disasters.\n**(5) Secretary**\nThe term Secretary means the Secretary of Energy.\n##### (b) Establishment\nNot later than 90 days after the date of enactment of this Act, the Secretary shall establish within the Office of Electricity a program under which the Secretary shall make grants to eligible entities to carry out activities that\u2014\n**(1)**\nare supplemental to existing power grid-hardening efforts of the eligible entity planned for any given year;\n**(2)**\nare designed to enhance public safety; and\n**(3)**\n**(A)**\nreduce the risk of any power lines owned or operated by the eligible entity causing a wildfire; or\n**(B)**\nincrease the reliability of the power grid.\n##### (c) Application\n**(1) In general**\nAn eligible entity desiring a grant under the program shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require.\n**(2) Requirement**\nAs a condition of receiving a grant under the program, an eligible entity shall submit to the Secretary as part of the application of the eligible entity under paragraph (1)\u2014\n**(A)**\na wildfire mitigation plan, if the eligible entity seeks a grant for purposes of implementing a project or otherwise carrying out activities to reduce wildfire risk, as described in subsection (b)(3)(A); or\n**(B)**\na report detailing past, current, and future efforts by the eligible entity to improve the reliability of the power grid if the eligible entity seeks a grant for purposes of increasing the reliability of the power grid.\n##### (d) Use of grant funds\nAn eligible entity may use a grant provided under the program\u2014\n**(1)**\nfor the undergrounding of new and existing power lines and circuits;\n**(2)**\nto harden overhead power lines with fire resistant or more resilient equipment, such as steel poles and covered wires;\n**(3)**\nto replace obsolete overhead conductors and underground cables;\n**(4)**\nto install fast-tripping protection systems;\n**(5)**\nto construct and operate 1 or more weather monitoring stations;\n**(6)**\nto install fault location equipment or early fault detection equipment;\n**(7)**\nfor the relocation of power lines to roadways;\n**(8)**\nto carry out vegetation or fuels management activities in accordance with Federal, State, and local laws (including regulations);\n**(9)**\nto install technology or equipment to mitigate hazards from or to animals and related damage to the power grid;\n**(10)**\nto install cameras, sensors, or other technology that provides real-time information about conditions;\n**(11)**\nto install technology to detect downed conductors;\n**(12)**\nfor the installation of electrical facilities necessary to sustain targeted microgrid operations, including storage for the integration of distributed energy resources into power grid operations, for the benefit of community resilience following a main power grid outage;\n**(13)**\nto harden facilities, substations, and other systems for seismic events; and\n**(14)**\nfor other, related power grid upgrades to reduce the risk of wildfire ignition or damage from natural disasters.\n##### (e) Priority\nIn making grants under the program, the Secretary shall give priority to projects that, in the determination of the Secretary, will generate the greatest community benefit in improving power grid reliability or reducing the risk of wildfire ignition from power lines or equipment relative to the cost of the project.\n##### (f) Set asides\n**(1) Wildfire set aside**\nIn making grants under the program, the Secretary shall ensure that not less than 40 percent of the total amounts made available to eligible entities under the program are made available to eligible entities that seek a grant for purposes of implementing a project or otherwise carrying out activities to reduce wildfire risk, as described in subsection (b)(3)(A).\n**(2) Small utilities set aside**\nIn making grants under the program, the Secretary shall ensure that not less than 20 percent of the amounts made available to eligible entities under the program are made available to eligible entities that sell not more than 4,000,000 megawatt-hours of electricity per year.\n##### (g) Matching requirement\n**(1) In general**\nExcept as provided in paragraph (2), as a condition of receiving a grant under the program, an eligible entity shall provide matching funds in the form of cash or an in-kind contribution in an amount equal to not less than 100 percent of the amounts made available under the grant.\n**(2) Exception for small utilities**\nWith respect to an eligible entity that sells not more than 4,000,000 megawatt-hours of electricity per year, as a condition of receiving a grant under the program, the eligible entity shall provide matching funds in the form of cash or an in-kind contribution in an amount equal to not less than 1/3 of the amounts made available under the grant.\n**(3) Existing efforts**\nOn approval by the Secretary, amounts expended by an eligible entity on power grid reliability or wildfire risk mitigation efforts during the 1-year period ending on the date on which a grant is received under the program shall count toward the matching requirement described in paragraph (1) or (2), as applicable.\n##### (h) Federal power marketing administrations\nAny amounts made available to a Federal power marketing administration pursuant to a grant under the program shall be nonreimbursable.\n##### (i) Technical assistance and support\n**(1) In general**\nUsing amounts made available to the Secretary to carry out the program, the Secretary may\u2014\n**(A)**\nprovide technical assistance to\u2014\n**(i)**\neligible entities seeking to prepare an application under subsection (c); and\n**(ii)**\neligible entities to which the Secretary has provided a grant under the program; and\n**(B)**\nprovide grants to eligible entities for the hiring or retention of individuals to provide and support, on a professional basis, assistance (including technical assistance) and informed decisionmaking in the planning, financing, and implementation of 1 or more activities described in subsection (d).\n**(2) Treatment**\nGrants under paragraph (1)(B)\u2014\n**(A)**\nshall not be counted toward a set-aside described in subsection (f); and\n**(B)**\nshall not be subject to subsection (g).\n##### (j) Biennial report\nNot later than 2 years after the date of enactment of this Act, and every 2 years thereafter, the Secretary shall submit to the Committee on Energy and Natural Resources of the Senate and the Committee on Energy and Commerce of the House of Representatives a report describing the manner in which, and the extent to which\u2014\n**(1)**\nthe reliability of the power grid has increased under the program during the period covered by the report; and\n**(2)**\nthe risk of wildfires caused by power lines has been reduced under the program during the period covered by the report.\n##### (k) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary to carry out the program $15,000,000,000 for each of fiscal years 2027 through 2036.",
      "versionDate": "2026-03-25",
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
        "updateDate": "2026-04-09T14:07:46Z"
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
      "date": "2026-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4193is.xml"
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
      "title": "Wildfire and Grid Reliability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-03T05:38:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Wildfire and Grid Reliability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-03T05:38:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Energy to establish a grant program to improve the reliability of the power grid and reduce the risk of wildfires caused by power lines, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-03T05:33:34Z"
    }
  ]
}
```
